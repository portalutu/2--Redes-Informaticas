#!/usr/bin/env python3
"""
Genera un archivo PCAP de ejemplo para prácticas de análisis de red.
Modifica el bloque NET al principio del archivo para adaptar la práctica.
"""

import struct
import random
import socket
import time
import os

random.seed(42)

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN DE RED — modifica estos valores para adaptar la práctica
# ═══════════════════════════════════════════════════════════════════════════════

NET = {
    # Parámetros de la red
    'mask':      '255.255.255.0',
    'broadcast': '192.168.1.255',

    # Infraestructura
    'gateway': {'ip': '192.168.1.1',  'mac': 'c0:a8:01:01:00:01', 'name': 'gateway'},
    'dns':     {'ip': '192.168.1.2',  'mac': 'c0:a8:01:02:00:02', 'name': 'dns-srv'},
    'nas':     {'ip': '192.168.1.10', 'mac': 'c0:a8:01:0a:00:0a', 'name': 'nas-01'},

    # Terminales Windows (50 % de los equipos)
    'windows_hosts': [
        {'ip': '192.168.1.101', 'mac': '00:50:56:aa:01:01', 'name': 'WIN-PC01'},
        {'ip': '192.168.1.102', 'mac': '00:50:56:aa:01:02', 'name': 'WIN-PC02'},
        {'ip': '192.168.1.103', 'mac': '08:00:27:bb:01:03', 'name': 'WIN-PC03'},
        {'ip': '192.168.1.104', 'mac': '08:00:27:bb:01:04', 'name': 'WIN-PC04'},
        {'ip': '192.168.1.105', 'mac': 'b8:ac:6f:cc:01:05', 'name': 'WIN-PC05'},
    ],

    # Terminales Linux (50 % de los equipos)
    'linux_hosts': [
        {'ip': '192.168.1.111', 'mac': '00:0c:29:dd:02:01', 'name': 'linux-ws01'},
        {'ip': '192.168.1.112', 'mac': '00:0c:29:dd:02:02', 'name': 'linux-ws02'},
        {'ip': '192.168.1.113', 'mac': '52:54:00:ee:02:03', 'name': 'linux-ws03'},
        {'ip': '192.168.1.114', 'mac': '52:54:00:ee:02:04', 'name': 'linux-ws04'},
        {'ip': '192.168.1.115', 'mac': 'de:ad:be:ef:02:05', 'name': 'linux-ws05'},
    ],

    # Dominios que aparecerán en consultas DNS
    'domains': [
        'utu.edu.uy', 'google.com', 'microsoft.com',
        'github.com', 'ubuntu.com', 'nas-01.local', 'gateway.local',
    ],

    # Archivo de salida y cantidad de paquetes
    'output_file':  '1000_practica_red_192_168_1.pcap',
    'packet_count': 1000,
}

# ═══════════════════════════════════════════════════════════════════════════════
# Variables derivadas — no hace falta modificar nada debajo de esta línea
# ═══════════════════════════════════════════════════════════════════════════════

GW        = NET['gateway']
DNS_SRV   = NET['dns']
NAS       = NET['nas']
WIN_HOSTS = [dict(h, os='windows') for h in NET['windows_hosts']]
LIN_HOSTS = [dict(h, os='linux')   for h in NET['linux_hosts']]
ALL_HOSTS = WIN_HOSTS + LIN_HOSTS
DOMAINS   = NET['domains']

WIN_UA = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
]
LIN_UA = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/123.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
]

WEB_PATHS = ['/', '/index.html', '/login', '/api/v1/status', '/static/app.js',
             '/favicon.ico', '/robots.txt', '/images/logo.png']

# ─── Helpers PCAP ────────────────────────────────────────────────────────────

def pcap_global_header():
    # magic, ver_major, ver_minor, thiszone, sigfigs, snaplen, network(Ethernet=1)
    return struct.pack('<IHHiIII', 0xa1b2c3d4, 2, 4, 0, 0, 65535, 1)

def pcap_pkt_header(ts_sec, ts_usec, cap_len):
    return struct.pack('<IIII', ts_sec, ts_usec, cap_len, cap_len)

# ─── Checksum ────────────────────────────────────────────────────────────────

def cksum(data: bytes) -> int:
    if len(data) % 2:
        data += b'\x00'
    s = sum(struct.unpack_from(f'>{len(data)//2}H', data))
    while s >> 16:
        s = (s & 0xffff) + (s >> 16)
    return (~s) & 0xffff

# ─── Conversiones ────────────────────────────────────────────────────────────

def mb(mac: str) -> bytes:
    return bytes(int(x, 16) for x in mac.split(':'))

def ib(ip: str) -> bytes:
    return socket.inet_aton(ip)

# ─── Constructores de capas ───────────────────────────────────────────────────

def eth(dst: str, src: str, etype: int, payload: bytes) -> bytes:
    return mb(dst) + mb(src) + struct.pack('>H', etype) + payload

def ipv4(src: str, dst: str, proto: int, payload: bytes, ttl: int = 64) -> bytes:
    ident = random.randint(1, 65535)
    tot = 20 + len(payload)
    hdr = struct.pack('>BBHHHBB', 0x45, 0, tot, ident, 0x4000, ttl, proto) \
        + b'\x00\x00' + ib(src) + ib(dst)
    cs = cksum(hdr)
    return hdr[:10] + struct.pack('>H', cs) + hdr[12:] + payload

def udp(src_ip: str, dst_ip: str, sport: int, dport: int, payload: bytes) -> bytes:
    ln = 8 + len(payload)
    pseudo = ib(src_ip) + ib(dst_ip) + struct.pack('>BBH', 0, 17, ln)
    hdr = struct.pack('>HHHH', sport, dport, ln, 0)
    cs = cksum(pseudo + hdr + payload)
    return struct.pack('>HHHH', sport, dport, ln, cs) + payload

def tcp(src_ip: str, dst_ip: str, sport: int, dport: int,
        seq: int, ack: int, flags: int, payload: bytes, win: int = 65535) -> bytes:
    hdr = struct.pack('>HHIIHHHH', sport, dport, seq, ack, (5 << 12) | flags, win, 0, 0)
    ln = 20 + len(payload)
    pseudo = ib(src_ip) + ib(dst_ip) + struct.pack('>BBH', 0, 6, ln)
    cs = cksum(pseudo + hdr + payload)
    return hdr[:16] + struct.pack('>H', cs) + hdr[18:] + payload

# ─── ARP ─────────────────────────────────────────────────────────────────────

def arp_req(sender_mac, sender_ip, target_ip) -> bytes:
    payload = struct.pack('>HHBBH', 1, 0x0800, 6, 4, 1) \
        + mb(sender_mac) + ib(sender_ip) \
        + b'\x00'*6 + ib(target_ip)
    return eth('ff:ff:ff:ff:ff:ff', sender_mac, 0x0806, payload)

def arp_reply(sender_mac, sender_ip, target_mac, target_ip) -> bytes:
    payload = struct.pack('>HHBBH', 1, 0x0800, 6, 4, 2) \
        + mb(sender_mac) + ib(sender_ip) \
        + mb(target_mac) + ib(target_ip)
    return eth(target_mac, sender_mac, 0x0806, payload)

# ─── DNS ─────────────────────────────────────────────────────────────────────

def dns_name(name: str) -> bytes:
    out = b''
    for part in name.split('.'):
        enc = part.encode()
        out += bytes([len(enc)]) + enc
    return out + b'\x00'

def dns_query(txid: int, name: str, qtype: int = 1) -> bytes:
    hdr = struct.pack('>HHHHHH', txid, 0x0100, 1, 0, 0, 0)
    return hdr + dns_name(name) + struct.pack('>HH', qtype, 1)

def dns_response(txid: int, name: str, ip: str, qtype: int = 1) -> bytes:
    hdr = struct.pack('>HHHHHH', txid, 0x8180, 1, 1, 0, 0)
    question = dns_name(name) + struct.pack('>HH', qtype, 1)
    rdata = ib(ip) if qtype == 1 else b''
    answer = dns_name(name) + struct.pack('>HHIH', qtype, 1, 300, len(rdata)) + rdata
    return hdr + question + answer

def dns_nxdomain(txid: int, name: str) -> bytes:
    hdr = struct.pack('>HHHHHH', txid, 0x8183, 1, 0, 0, 0)
    return hdr + dns_name(name) + struct.pack('>HH', 1, 1)

# ─── ICMP ────────────────────────────────────────────────────────────────────

def icmp_echo(type_: int, id_: int, seq: int) -> bytes:
    payload = b'UTU2026' * 4
    hdr = struct.pack('>BBHHH', type_, 0, 0, id_, seq)
    cs = cksum(hdr + payload)
    return struct.pack('>BBHHH', type_, 0, cs, id_, seq) + payload

# ─── DHCP ────────────────────────────────────────────────────────────────────

def dhcp_discover(client_mac: str, xid: int) -> bytes:
    bootp = struct.pack('>BBBBIHH4s4s4s4s',
        1, 1, 6, 0, xid, 0, 0,
        b'\x00'*4, b'\x00'*4, b'\x00'*4, b'\x00'*4
    )
    bootp += mb(client_mac) + b'\x00'*10 + b'\x00'*192
    bootp += b'\x63\x82\x53\x63'   # magic cookie
    bootp += b'\x35\x01\x01'        # DHCP Discover
    bootp += b'\xff'                # End
    return bootp

def dhcp_offer(client_mac: str, offered_ip: str, xid: int) -> bytes:
    gw_ip  = NET['gateway']['ip']
    dns_ip = NET['dns']['ip']
    mask   = NET['mask']
    bootp = struct.pack('>BBBBIHH4s4s4s4s',
        2, 1, 6, 0, xid, 0, 0,
        ib(offered_ip), b'\x00'*4, ib(gw_ip), b'\x00'*4
    )
    bootp += mb(client_mac) + b'\x00'*10 + b'\x00'*192
    bootp += b'\x63\x82\x53\x63'
    bootp += b'\x35\x01\x02'                              # DHCP Offer
    bootp += b'\x01\x04' + ib(mask)                      # Subnet mask
    bootp += b'\x03\x04' + ib(gw_ip)                     # Router
    bootp += b'\x06\x04' + ib(dns_ip)                    # DNS
    bootp += b'\x33\x04' + struct.pack('>I', 86400)      # Lease time
    bootp += b'\xff'
    return bootp

# ─── HTTP ────────────────────────────────────────────────────────────────────

def http_get(host: str, path: str, ua: str) -> bytes:
    return (f"GET {path} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {ua}\r\n"
            f"Accept: text/html\r\nConnection: keep-alive\r\n\r\n").encode()

def http_200(body: str = "<html><body>OK</body></html>") -> bytes:
    return (f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n"
            f"Content-Length: {len(body)}\r\nServer: nginx/1.24\r\n\r\n{body}").encode()

def http_404() -> bytes:
    body = "<html><body>404 Not Found</body></html>"
    return (f"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n"
            f"Content-Length: {len(body)}\r\nServer: nginx/1.24\r\n\r\n{body}").encode()

# ─── SMB (simplificado) ──────────────────────────────────────────────────────

def smb_negotiate() -> bytes:
    return (b'\xfeSMB'                  # SMB2 magic
            + struct.pack('<H', 64)     # StructureSize
            + b'\x00' * 60)

def smb_session_setup() -> bytes:
    return (b'\xfeSMB'
            + struct.pack('<H', 64)
            + b'\x01' + b'\x00' * 59)

# ─── NFS (RPC simplificado) ──────────────────────────────────────────────────

def nfs_null_call(xid: int) -> bytes:
    return struct.pack('>IIIIII', xid, 0, 2, 100003, 3, 0) + b'\x00'*8

def nfs_null_reply(xid: int) -> bytes:
    return struct.pack('>IIIII', xid, 1, 0, 0, 0)

# ─── SSH (handshake simplificado) ────────────────────────────────────────────

def ssh_banner(is_server: bool = False) -> bytes:
    if is_server:
        return b'SSH-2.0-OpenSSH_9.6\r\n'
    return b'SSH-2.0-OpenSSH_9.3p2 Ubuntu-1ubuntu3\r\n'

# ─── mDNS ────────────────────────────────────────────────────────────────────

def mdns_query(name: str) -> bytes:
    hdr = struct.pack('>HHHHHH', 0, 0, 1, 0, 0, 0)
    return hdr + dns_name(name) + struct.pack('>HH', 1, 1)

# ─── NetBIOS Name Query ───────────────────────────────────────────────────────

def netbios_name_query(name: str) -> bytes:
    txid = random.randint(1, 65535)
    encoded = name.upper().ljust(15) + '\x00'
    nb_encoded = b''
    for ch in encoded:
        n = ord(ch)
        nb_encoded += bytes([0x41 + (n >> 4), 0x41 + (n & 0x0f)])
    nb_name = bytes([32]) + nb_encoded + b'\x00'
    hdr = struct.pack('>HHHHHH', txid, 0x0110, 1, 0, 0, 0)
    return hdr + nb_name + struct.pack('>HHI', 0x0020, 0x0001, 0)

# ─── Acumulador de paquetes ───────────────────────────────────────────────────

pkts   = []
cur_ts = int(time.time()) - 7200   # 2 horas atrás
cur_us = 0

def add_pkt(frame: bytes):
    global cur_ts, cur_us
    cur_us += random.randint(800, 120_000)
    if cur_us >= 1_000_000:
        cur_ts += cur_us // 1_000_000
        cur_us  = cur_us  % 1_000_000
    pkts.append(pcap_pkt_header(cur_ts, cur_us, len(frame)) + frame)

def rport() -> int:
    return random.randint(49152, 65535)

# ─── Generadores de tráfico ───────────────────────────────────────────────────

def gen_arp(n=40):
    """ARP requests y replies entre todos los hosts."""
    pairs = [(h, t) for h in ALL_HOSTS for t in [GW, DNS_SRV, NAS] + ALL_HOSTS if h != t]
    random.shuffle(pairs)
    for sender, target in pairs[:n//2]:
        add_pkt(arp_req(sender['mac'], sender['ip'], target['ip']))
        add_pkt(arp_reply(target['mac'], target['ip'], sender['mac'], sender['ip']))
        if len(pkts) >= n * 2:
            break

def gen_dhcp(n=24):
    """DHCP Discover/Offer/Request/ACK para todos los hosts."""
    for h in ALL_HOSTS[:n//4]:
        xid  = random.randint(0x10000000, 0xFFFFFFFF)
        bcast_ip  = '255.255.255.255'
        bcast_mac = 'ff:ff:ff:ff:ff:ff'

        disc = dhcp_discover(h['mac'], xid)
        add_pkt(eth(bcast_mac, h['mac'], 0x0800,
                    ipv4(h['ip'], bcast_ip, 17, udp(h['ip'], bcast_ip, 68, 67, disc))))
        offer = dhcp_offer(h['mac'], h['ip'], xid)
        add_pkt(eth(h['mac'], GW['mac'], 0x0800,
                    ipv4(GW['ip'], h['ip'], 17, udp(GW['ip'], h['ip'], 67, 68, offer))))
        req = dhcp_discover(h['mac'], xid)
        req = req[:240+3] + b'\x03' + req[240+4:]   # tipo → Request
        add_pkt(eth(bcast_mac, h['mac'], 0x0800,
                    ipv4(h['ip'], bcast_ip, 17, udp(h['ip'], bcast_ip, 68, 67, req))))
        add_pkt(eth(h['mac'], GW['mac'], 0x0800,
                    ipv4(GW['ip'], h['ip'], 17, udp(GW['ip'], h['ip'], 67, 68, offer))))

def gen_dns(n=80):
    """Consultas DNS hacia el servidor interno."""
    done = 0
    while done < n:
        host   = random.choice(ALL_HOSTS)
        domain = random.choice(DOMAINS)
        txid   = random.randint(1, 65535)
        sport  = rport()

        q = dns_query(txid, domain)
        add_pkt(eth(DNS_SRV['mac'], host['mac'], 0x0800,
                    ipv4(host['ip'], DNS_SRV['ip'], 17,
                         udp(host['ip'], DNS_SRV['ip'], sport, 53, q))))
        done += 1

        if random.random() < 0.8:
            fake_ip = f'93.184.{random.randint(1,254)}.{random.randint(1,254)}'
            r = dns_response(txid, domain, fake_ip)
        else:
            r = dns_nxdomain(txid, domain)
        add_pkt(eth(host['mac'], DNS_SRV['mac'], 0x0800,
                    ipv4(DNS_SRV['ip'], host['ip'], 17,
                         udp(DNS_SRV['ip'], host['ip'], 53, sport, r))))
        done += 1

def gen_icmp(n=40):
    """Pings entre hosts y hacia la infraestructura."""
    done = 0
    while done < n:
        src = random.choice(ALL_HOSTS)
        dst = random.choice([GW, DNS_SRV, NAS] + ALL_HOSTS)
        if src == dst:
            continue
        icmp_id  = random.randint(1, 65535)
        icmp_seq = random.randint(1, 10)
        add_pkt(eth(dst['mac'], src['mac'], 0x0800,
                    ipv4(src['ip'], dst['ip'], 1, icmp_echo(8, icmp_id, icmp_seq))))
        done += 1
        add_pkt(eth(src['mac'], dst['mac'], 0x0800,
                    ipv4(dst['ip'], src['ip'], 1, icmp_echo(0, icmp_id, icmp_seq))))
        done += 1

def gen_http(n=100):
    """Tráfico HTTP (three-way handshake + GET + respuesta)."""
    F = {'SYN': 0x002, 'SYN_ACK': 0x012, 'ACK': 0x010, 'PSH_ACK': 0x018}
    done = 0
    while done < n:
        host    = random.choice(ALL_HOSTS)
        ua      = random.choice(WIN_UA if host['os'] == 'windows' else LIN_UA)
        domain  = random.choice(DOMAINS)
        path    = random.choice(WEB_PATHS)
        sport   = rport()
        dport   = 80
        dst_ip  = GW['ip']
        dst_mac = GW['mac']
        seq_c   = random.randint(1_000_000, 9_000_000)
        seq_s   = random.randint(1_000_000, 9_000_000)

        add_pkt(eth(dst_mac, host['mac'], 0x0800,
                    ipv4(host['ip'], dst_ip, 6,
                         tcp(host['ip'], dst_ip, sport, dport, seq_c, 0, F['SYN'], b''))))
        done += 1
        add_pkt(eth(host['mac'], dst_mac, 0x0800,
                    ipv4(dst_ip, host['ip'], 6,
                         tcp(dst_ip, host['ip'], dport, sport, seq_s, seq_c+1, F['SYN_ACK'], b''))))
        done += 1
        add_pkt(eth(dst_mac, host['mac'], 0x0800,
                    ipv4(host['ip'], dst_ip, 6,
                         tcp(host['ip'], dst_ip, sport, dport, seq_c+1, seq_s+1, F['ACK'], b''))))
        done += 1
        get_pl = http_get(domain, path, ua)
        add_pkt(eth(dst_mac, host['mac'], 0x0800,
                    ipv4(host['ip'], dst_ip, 6,
                         tcp(host['ip'], dst_ip, sport, dport, seq_c+1, seq_s+1, F['PSH_ACK'], get_pl))))
        done += 1
        resp = http_200() if random.random() < 0.85 else http_404()
        add_pkt(eth(host['mac'], dst_mac, 0x0800,
                    ipv4(dst_ip, host['ip'], 6,
                         tcp(dst_ip, host['ip'], dport, sport, seq_s+1,
                             seq_c+1+len(get_pl), F['PSH_ACK'], resp))))
        done += 1

def gen_smb(n=60):
    """Tráfico SMB2 (puerto 445) desde Windows hacia el NAS."""
    F = {'SYN': 0x002, 'SYN_ACK': 0x012, 'PSH_ACK': 0x018}
    done = 0
    while done < n:
        host  = random.choice(WIN_HOSTS)
        sport = rport()
        seq_c = random.randint(1_000_000, 9_000_000)
        seq_s = random.randint(1_000_000, 9_000_000)

        add_pkt(eth(NAS['mac'], host['mac'], 0x0800,
                    ipv4(host['ip'], NAS['ip'], 6,
                         tcp(host['ip'], NAS['ip'], sport, 445, seq_c, 0, F['SYN'], b''))))
        done += 1
        add_pkt(eth(host['mac'], NAS['mac'], 0x0800,
                    ipv4(NAS['ip'], host['ip'], 6,
                         tcp(NAS['ip'], host['ip'], 445, sport, seq_s, seq_c+1, F['SYN_ACK'], b''))))
        done += 1
        neg = smb_negotiate()
        add_pkt(eth(NAS['mac'], host['mac'], 0x0800,
                    ipv4(host['ip'], NAS['ip'], 6,
                         tcp(host['ip'], NAS['ip'], sport, 445, seq_c+1, seq_s+1, F['PSH_ACK'], neg))))
        done += 1
        sess = smb_session_setup()
        add_pkt(eth(host['mac'], NAS['mac'], 0x0800,
                    ipv4(NAS['ip'], host['ip'], 6,
                         tcp(NAS['ip'], host['ip'], 445, sport, seq_s+1,
                             seq_c+1+len(neg), F['PSH_ACK'], sess))))
        done += 1

def gen_nfs(n=40):
    """Tráfico NFS (UDP 2049) desde Linux hacia el NAS."""
    done = 0
    while done < n:
        host = random.choice(LIN_HOSTS)
        xid  = random.randint(1, 0xFFFFFFFF)
        add_pkt(eth(NAS['mac'], host['mac'], 0x0800,
                    ipv4(host['ip'], NAS['ip'], 17,
                         udp(host['ip'], NAS['ip'], rport(), 2049, nfs_null_call(xid)))))
        done += 1
        add_pkt(eth(host['mac'], NAS['mac'], 0x0800,
                    ipv4(NAS['ip'], host['ip'], 17,
                         udp(NAS['ip'], host['ip'], 2049, rport(), nfs_null_reply(xid)))))
        done += 1

def gen_ssh(n=60):
    """Conexiones SSH (TCP 22) desde Linux hacia gateway y NAS."""
    F = {'SYN': 0x002, 'SYN_ACK': 0x012, 'PSH_ACK': 0x018}
    done = 0
    while done < n:
        host   = random.choice(LIN_HOSTS)
        target = random.choice([GW, NAS])
        sport  = rport()
        seq_c  = random.randint(1_000_000, 9_000_000)
        seq_s  = random.randint(1_000_000, 9_000_000)

        add_pkt(eth(target['mac'], host['mac'], 0x0800,
                    ipv4(host['ip'], target['ip'], 6,
                         tcp(host['ip'], target['ip'], sport, 22, seq_c, 0, F['SYN'], b''))))
        done += 1
        add_pkt(eth(host['mac'], target['mac'], 0x0800,
                    ipv4(target['ip'], host['ip'], 6,
                         tcp(target['ip'], host['ip'], 22, sport, seq_s, seq_c+1, F['SYN_ACK'], b''))))
        done += 1
        srv_banner = ssh_banner(is_server=True)
        cli_banner = ssh_banner(is_server=False)
        add_pkt(eth(host['mac'], target['mac'], 0x0800,
                    ipv4(target['ip'], host['ip'], 6,
                         tcp(target['ip'], host['ip'], 22, sport, seq_s+1, seq_c+1, F['PSH_ACK'], srv_banner))))
        done += 1
        add_pkt(eth(target['mac'], host['mac'], 0x0800,
                    ipv4(host['ip'], target['ip'], 6,
                         tcp(host['ip'], target['ip'], sport, 22, seq_c+1,
                             seq_s+1+len(srv_banner), F['PSH_ACK'], cli_banner))))
        done += 1

def gen_netbios(n=30):
    """NetBIOS Name Query (UDP 137) broadcast desde Windows."""
    bcast = NET['broadcast']
    done  = 0
    while done < n:
        host  = random.choice(WIN_HOSTS)
        query = netbios_name_query(random.choice([h['name'] for h in WIN_HOSTS + [GW]]))
        add_pkt(eth('ff:ff:ff:ff:ff:ff', host['mac'], 0x0800,
                    ipv4(host['ip'], bcast, 17, udp(host['ip'], bcast, 137, 137, query))))
        done += 1

def gen_mdns(n=30):
    """mDNS (UDP 5353) multicast desde Linux."""
    MDNS_IP  = '224.0.0.251'
    MDNS_MAC = '01:00:5e:00:00:fb'
    done = 0
    while done < n:
        host = random.choice(LIN_HOSTS)
        add_pkt(eth(MDNS_MAC, host['mac'], 0x0800,
                    ipv4(host['ip'], MDNS_IP, 17,
                         udp(host['ip'], MDNS_IP, 5353, 5353,
                             mdns_query(host['name'] + '.local')))))
        done += 1

def gen_fill(target: int):
    """FIN-ACK adicionales hasta completar el total de paquetes."""
    F = {'FIN_ACK': 0x011}
    while len(pkts) < target:
        src = random.choice(ALL_HOSTS)
        dst = random.choice([GW, NAS] + ALL_HOSTS)
        if src == dst:
            continue
        sport = rport()
        seq   = random.randint(1_000_000, 9_000_000)
        ack   = random.randint(1_000_000, 9_000_000)
        add_pkt(eth(dst['mac'], src['mac'], 0x0800,
                    ipv4(src['ip'], dst['ip'], 6,
                         tcp(src['ip'], dst['ip'], sport, 80, seq, ack, F['FIN_ACK'], b''))))

# ─── Parser de paquetes → texto plano ────────────────────────────────────────

def _dns_name_from(data: bytes, offset: int) -> str:
    """Decodifica un nombre DNS (sin soporte de punteros comprimidos)."""
    parts = []
    while offset < len(data):
        ln = data[offset]
        if ln == 0:
            break
        if ln & 0xc0:   # puntero de compresión — no lo seguimos
            break
        offset += 1
        parts.append(data[offset:offset + ln].decode('utf-8', errors='replace'))
        offset += ln
    return '.'.join(parts)

def _tcp_flags_str(raw_flags: int) -> str:
    names = ((0x002, 'SYN'), (0x010, 'ACK'), (0x008, 'PSH'),
             (0x001, 'FIN'), (0x004, 'RST'), (0x020, 'URG'))
    return ', '.join(name for bit, name in names if raw_flags & bit) or '—'

def _parse_frame(frame: bytes, pkt_num: int, ts_sec: int, ts_usec: int) -> dict:
    """Analiza una trama Ethernet y devuelve un dict con los campos principales."""
    r = dict(num=pkt_num, ts=ts_sec + ts_usec / 1_000_000,
             src='', dst='', proto='DATA', length=len(frame), info='')

    if len(frame) < 14:
        return r

    dst_mac = ':'.join(f'{b:02x}' for b in frame[0:6])
    src_mac = ':'.join(f'{b:02x}' for b in frame[6:12])
    etype   = struct.unpack_from('>H', frame, 12)[0]

    # ── ARP ──────────────────────────────────────────────────────────────────
    if etype == 0x0806:
        r['proto'] = 'ARP'
        r['src']   = src_mac
        r['dst']   = dst_mac
        if len(frame) >= 42:
            op        = struct.unpack_from('>H', frame, 20)[0]
            sender_ip = socket.inet_ntoa(frame[28:32])
            target_ip = socket.inet_ntoa(frame[38:42])
            r['info'] = (f'Who has {target_ip}?  Tell {sender_ip}'
                         if op == 1 else f'{sender_ip} is at {src_mac}')
        return r

    if etype != 0x0800:
        r['proto'] = f'ETH 0x{etype:04x}'
        r['src']   = src_mac
        r['dst']   = dst_mac
        return r

    # ── IPv4 ─────────────────────────────────────────────────────────────────
    ihl    = (frame[14] & 0x0f) * 4
    proto  = frame[23]
    ttl    = frame[22]
    src_ip = socket.inet_ntoa(frame[26:30])
    dst_ip = socket.inet_ntoa(frame[30:34])
    r['src'] = src_ip
    r['dst'] = dst_ip
    ip_pl = frame[14 + ihl:]   # payload IP

    # ── ICMP ─────────────────────────────────────────────────────────────────
    if proto == 1:
        r['proto'] = 'ICMP'
        if len(ip_pl) >= 8:
            t    = ip_pl[0]
            id_  = struct.unpack_from('>H', ip_pl, 4)[0]
            seq  = struct.unpack_from('>H', ip_pl, 6)[0]
            kind = 'request' if t == 8 else 'reply  '
            r['info'] = (f'Echo (ping) {kind}  '
                         f'id=0x{id_:04x}, seq={seq}, ttl={ttl}')
        return r

    # ── UDP ──────────────────────────────────────────────────────────────────
    if proto == 17:
        if len(ip_pl) < 8:
            return r
        sport  = struct.unpack_from('>H', ip_pl, 0)[0]
        dport  = struct.unpack_from('>H', ip_pl, 2)[0]
        udp_pl = ip_pl[8:]
        ports  = {sport, dport}

        # DNS
        if 53 in ports:
            r['proto'] = 'DNS'
            if len(udp_pl) >= 12:
                txid   = struct.unpack_from('>H', udp_pl, 0)[0]
                flags  = struct.unpack_from('>H', udp_pl, 2)[0]
                is_rsp = bool(flags & 0x8000)
                rcode  = flags & 0x000f
                name   = _dns_name_from(udp_pl, 12)
                if is_rsp:
                    tag = 'No such name' if rcode == 3 else 'A (respuesta)'
                    r['info'] = f'Standard query response 0x{txid:04x}  {tag}  {name}'
                else:
                    r['info'] = f'Standard query 0x{txid:04x}  A {name}'
            return r

        # DHCP
        if ports & {67, 68}:
            r['proto'] = 'DHCP'
            if len(udp_pl) >= 241:
                xid  = struct.unpack_from('>I', udp_pl, 4)[0]
                opts = udp_pl[240:]   # las opciones empiezan en offset 240 (tras el magic cookie)
                i = 0
                mtype = 0
                while i < len(opts) - 1:
                    code = opts[i]
                    if code == 0xff:
                        break
                    if code == 0:
                        i += 1
                        continue
                    ln = opts[i + 1] if i + 1 < len(opts) else 0
                    if code == 53 and i + 2 < len(opts):
                        mtype = opts[i + 2]
                    i += 2 + ln
                labels = {1: 'Discover', 2: 'Offer', 3: 'Request', 5: 'ACK'}
                r['info'] = (f'DHCP {labels.get(mtype, f"Type {mtype}")}  '
                             f'Transaction ID 0x{xid:08x}')
            return r

        # NetBIOS NS
        if 137 in ports:
            r['proto'] = 'NBNS'
            r['info'] = f'Name service query  {src_ip} → {dst_ip}'
            return r

        # mDNS
        if 5353 in ports:
            r['proto'] = 'MDNS'
            name = _dns_name_from(udp_pl, 12) if len(udp_pl) >= 13 else ''
            r['info'] = f'Standard query  {name}'
            return r

        # NFS / RPC
        if 2049 in ports:
            r['proto'] = 'NFS'
            direction  = 'Call' if dport == 2049 else 'Reply'
            r['info']  = f'RPC {direction}  NFS NULL procedure'
            return r

        r['proto'] = 'UDP'
        r['info']  = f'{sport} → {dport}  Len={len(udp_pl)}'
        return r

    # ── TCP ──────────────────────────────────────────────────────────────────
    if proto == 6:
        if len(ip_pl) < 20:
            return r
        sport      = struct.unpack_from('>H', ip_pl, 0)[0]
        dport      = struct.unpack_from('>H', ip_pl, 2)[0]
        seq        = struct.unpack_from('>I', ip_pl, 4)[0]
        ack        = struct.unpack_from('>I', ip_pl, 8)[0]
        hdr_word   = struct.unpack_from('>H', ip_pl, 12)[0]
        raw_flags  = hdr_word & 0x1ff
        data_off   = (hdr_word >> 12) * 4
        tcp_pl     = ip_pl[data_off:]
        fstr       = _tcp_flags_str(raw_flags)
        ports      = {sport, dport}

        # HTTP
        if 80 in ports:
            if tcp_pl.startswith(b'GET ') or tcp_pl.startswith(b'POST '):
                r['proto'] = 'HTTP'
                r['info']  = tcp_pl.split(b'\r\n')[0].decode('utf-8', errors='replace')
                return r
            if tcp_pl.startswith(b'HTTP/'):
                r['proto'] = 'HTTP'
                r['info']  = tcp_pl.split(b'\r\n')[0].decode('utf-8', errors='replace')
                return r

        # SMB2
        if 445 in ports:
            r['proto'] = 'SMB2'
            if tcp_pl.startswith(b'\xfeSMB') and len(tcp_pl) > 16:
                cmd   = tcp_pl[16]
                cmds  = {0: 'Negotiate', 1: 'Session Setup'}
                label = cmds.get(cmd, 'Command')
                side  = 'Request' if dport == 445 else 'Response'
                r['info'] = f'SMB2 {label} {side}'
            else:
                r['info'] = f'{sport} → {dport}  [{fstr}]  Seq={seq}  Ack={ack}'
            return r

        # SSH
        if 22 in ports:
            r['proto'] = 'SSH'
            if tcp_pl.startswith(b'SSH-'):
                banner = tcp_pl.split(b'\r\n')[0].decode('utf-8', errors='replace')
                r['info'] = f'{"Servidor" if sport == 22 else "Cliente"}: {banner}'
            else:
                r['info'] = f'{sport} → {dport}  [{fstr}]  Seq={seq}  Ack={ack}'
            return r

        r['proto'] = 'TCP'
        r['info']  = (f'{sport} → {dport}  [{fstr}]  '
                      f'Seq={seq}  Ack={ack}  Len={len(tcp_pl)}')
        return r

    r['info'] = f'Protocolo IP {proto}'
    return r


def write_txt(out_file: str, final_pkts: list, base_ts: int):
    """Genera un archivo de texto con el mismo contenido que el PCAP."""
    txt_file = os.path.splitext(out_file)[0] + '.txt'
    cap_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(base_ts))

    rows = []
    for i, raw in enumerate(final_pkts, start=1):
        # raw = pcap_pkt_header (16 bytes) + frame
        ts_sec  = struct.unpack_from('<I', raw, 0)[0]
        ts_usec = struct.unpack_from('<I', raw, 4)[0]
        frame   = raw[16:]
        rows.append(_parse_frame(frame, i, ts_sec, ts_usec))

    t0 = rows[0]['ts'] if rows else 0

    with open(txt_file, 'w', encoding='utf-8') as f:

        # ── Encabezado ───────────────────────────────────────────────────────
        sep = '=' * 100
        f.write(f'{sep}\n')
        f.write(f'  CAPTURA DE RED — {os.path.basename(out_file)}\n')
        f.write(f'  Fecha/hora de inicio : {cap_time}\n')
        f.write(f'  Total de paquetes    : {len(final_pkts)}\n')
        f.write(f'  Red analizada        : {NET["broadcast"].rsplit(".", 1)[0]}.0/{NET["mask"]}\n')
        f.write(f'{sep}\n\n')

        # ── Tabla de paquetes ─────────────────────────────────────────────────
        HDR = (f'{"No.":>5}  {"Tiempo (s)":>12}  '
               f'{"Origen":<22}  {"Destino":<22}  '
               f'{"Proto":<8}  {"Long.":>5}  Información')
        f.write(HDR + '\n')
        f.write('-' * 100 + '\n')

        for r in rows:
            rel = r['ts'] - t0
            line = (f'{r["num"]:>5}  {rel:>12.6f}  '
                    f'{r["src"]:<22}  {r["dst"]:<22}  '
                    f'{r["proto"]:<8}  {r["length"]:>5}  {r["info"]}')
            f.write(line + '\n')

        # ── Referencia de hosts ───────────────────────────────────────────────
        f.write(f'\n{sep}\n')
        f.write('  REFERENCIA DE HOSTS\n')
        f.write(f'{sep}\n')
        f.write(f'  {"IP":<18} {"MAC":<20} {"Nombre":<14} Sistema operativo\n')
        f.write('  ' + '-' * 70 + '\n')

        infra = [
            (NET['gateway'], 'Infraestructura (router)'),
            (NET['dns'],     'Infraestructura (DNS)'),
            (NET['nas'],     'Infraestructura (NAS)'),
        ]
        for h, label in infra:
            f.write(f'  {h["ip"]:<18} {h["mac"]:<20} {h["name"]:<14} {label}\n')

        f.write('  ' + '-' * 70 + '\n')
        for h in NET['windows_hosts']:
            f.write(f'  {h["ip"]:<18} {h["mac"]:<20} {h["name"]:<14} Windows\n')

        f.write('  ' + '-' * 70 + '\n')
        for h in NET['linux_hosts']:
            f.write(f'  {h["ip"]:<18} {h["mac"]:<20} {h["name"]:<14} Linux\n')

        # ── Glosario de protocolos ────────────────────────────────────────────
        f.write(f'\n{sep}\n')
        f.write('  GLOSARIO DE PROTOCOLOS\n')
        f.write(f'{sep}\n')
        glosario = [
            ('ARP',   'Address Resolution Protocol    — resuelve IP → MAC en la red local'),
            ('DHCP',  'Dynamic Host Configuration     — asignación automática de IPs'),
            ('DNS',   'Domain Name System (UDP 53)    — resuelve nombres → IPs'),
            ('ICMP',  'Internet Control Message       — diagnóstico (ping, errores)'),
            ('HTTP',  'HyperText Transfer Protocol    — navegación web (TCP 80)'),
            ('SMB2',  'Server Message Block v2        — acceso a archivos Windows (TCP 445)'),
            ('NFS',   'Network File System (UDP 2049) — acceso a archivos Linux'),
            ('SSH',   'Secure Shell (TCP 22)          — terminal remota cifrada'),
            ('NBNS',  'NetBIOS Name Service (UDP 137) — resolución de nombres Windows'),
            ('MDNS',  'Multicast DNS (UDP 5353)       — resolución local Linux/macOS'),
        ]
        for proto, desc in glosario:
            f.write(f'  {proto:<8} {desc}\n')

        f.write(f'\n{sep}\n')
        f.write('  Archivo generado automáticamente con generar_pcap.py — UTU 2026\n')
        f.write(f'{sep}\n')

    return txt_file


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    TARGET   = NET['packet_count']
    out_dir  = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(out_dir, NET['output_file'])

    print(f"Generando tráfico de red ({TARGET} paquetes)...")

    gen_arp(40)
    gen_dhcp(24)
    gen_dns(80)
    gen_icmp(40)
    gen_http(100)
    gen_smb(60)
    gen_nfs(40)
    gen_ssh(60)
    gen_netbios(30)
    gen_mdns(30)
    gen_fill(TARGET)

    final_pkts = pkts[:TARGET]

    with open(out_file, 'wb') as f:
        f.write(pcap_global_header())
        for p in final_pkts:
            f.write(p)

    txt_file = write_txt(out_file, final_pkts, cur_ts - 7200)

    pcap_kb = os.path.getsize(out_file) / 1024
    txt_kb  = os.path.getsize(txt_file)  / 1024
    print(f"PCAP generado    : {out_file}  ({pcap_kb:.1f} KB)")
    print(f"TXT  generado    : {txt_file}  ({txt_kb:.1f} KB)")
    print(f"Paquetes         : {len(final_pkts)}")
    print()
    print("Distribución de tráfico:")
    print("  ARP            : ~40 paquetes")
    print("  DHCP           : ~24 paquetes")
    print("  DNS  (UDP  53) : ~80 paquetes")
    print("  ICMP           : ~40 paquetes")
    print("  HTTP (TCP  80) : ~100 paquetes")
    print("  SMB  (TCP 445) : ~60 paquetes  [Windows → NAS]")
    print("  NFS  (UDP 2049): ~40 paquetes  [Linux → NAS]")
    print("  SSH  (TCP  22) : ~60 paquetes  [Linux]")
    print("  NetBIOS (137)  : ~30 paquetes  [Windows broadcast]")
    print("  mDNS  (5353)   : ~30 paquetes  [Linux multicast]")
    print()
    print("Hosts en la captura:")
    print(f"  {NET['gateway']['ip']:15s} — Gateway (router)")
    print(f"  {NET['dns']['ip']:15s} — Servidor DNS interno")
    print(f"  {NET['nas']['ip']:15s} — NAS")
    for h in NET['windows_hosts']:
        print(f"  {h['ip']:15s} — {h['name']} (Windows)")
    for h in NET['linux_hosts']:
        print(f"  {h['ip']:15s} — {h['name']} (Linux)")

if __name__ == '__main__':
    main()
