# Evaluación de Redes Informáticas — Clave de Respuestas

**Uso exclusivo del docente**  
Redes Informáticas · UTU · 2026

---

> **Fuentes:** Modelos OSI y TCP/IP · Capa 4 — Transporte · Capa 5 — Sesión · Protocolo IP

---

## Sección 1 — Modelos OSI y TCP/IP

| N° | Pregunta | Respuesta correcta | Opción |
|----|----------|--------------------|--------|
| 01 | ¿Cuántas capas tiene el modelo OSI? | **7 capas** | C |
| 02 | ¿Cuántas capas tiene el modelo TCP/IP? | **4 capas** | C |
| 03 | ¿Cuál fue el objetivo principal del modelo OSI impulsado por la ISO? | **Definir un modelo de referencia estándar para comunicación entre sistemas de distintos fabricantes** | B |
| 04 | ¿A qué capas del modelo OSI corresponde la capa "Acceso a la Red" de TCP/IP? | **Capa 1 (Física) y Capa 2 (Enlace de datos)** | B |
| 05 | ¿En qué capa del modelo OSI trabaja el router? | **Capa 3 — Red** | C |

### Justificaciones — Sección 1

**01** — El modelo OSI (Open Systems Interconnection) tiene 7 capas: (1) Física, (2) Enlace de datos, (3) Red, (4) Transporte, (5) Sesión, (6) Presentación y (7) Aplicación.

**02** — El modelo TCP/IP tiene 4 capas: Acceso a la Red, Internet, Transporte y Aplicación. Es más compacto que el OSI y es la base real de Internet.

**03** — La ISO impulsó el modelo OSI a fines de los años 70 para resolver el caos de protocolos propietarios incompatibles. Su objetivo no fue definir protocolos específicos sino describir qué función debía cumplir cada capa.

**04** — La capa "Acceso a la Red" de TCP/IP agrupa las funciones de las capas 1 y 2 del modelo OSI (transmisión de bits y comunicación en la LAN). La capa "Internet" de TCP/IP corresponde a la capa 3 de OSI.

**05** — El router opera en capa 3 (Red): analiza la dirección IP de destino, consulta su tabla de enrutamiento y decide por qué interfaz reenviar el paquete. El hub trabaja en capa 1 y el switch en capa 2.

---

## Sección 2 — Capa de Transporte (Capa 4) y Capa de Sesión (Capa 5)

| N° | Pregunta | Respuesta correcta | Opción |
|----|----------|--------------------|--------|
| 06 | ¿Cuál es la PDU de la capa de Transporte? | **Segmento (o datagrama en UDP)** | D |
| 07 | ¿Qué diferencia principal existe entre TCP y UDP? | **TCP garantiza entrega confiable, orden y control de flujo; UDP no garantiza entrega ni orden** | B |
| 08 | ¿Cuántos pasos tiene el three-way handshake de TCP y cuáles son? | **3 pasos: SYN → SYN-ACK → ACK** | B |
| 09 | ¿Cuál es la función principal de la capa de Sesión (capa 5)? | **Gestionar el ciclo de vida de conversaciones entre aplicaciones: apertura, mantenimiento, sincronización y cierre** | C |
| 10 | ¿Qué función cumple la capa de Presentación (capa 6)? | **Traducir formatos, codificar, comprimir y cifrar datos para que sistemas distintos los entiendan** | C |

### Justificaciones — Sección 2

**06** — Cada capa tiene su PDU: Bit (capa 1), Trama (capa 2), Paquete (capa 3), **Segmento** (capa 4 TCP) o **Datagrama** (capa 4 UDP), y Datos (capas 5–7).

**07** — TCP establece conexión, confirma recepción con ACK, retransmite datos perdidos y controla el flujo. UDP simplemente envía sin confirmar — es más rápido y se prefiere para streaming, DNS, videollamadas y juegos en línea.

**08** — El three-way handshake tiene exactamente 3 pasos: (1) el cliente envía **SYN** para iniciar, (2) el servidor responde **SYN-ACK** aceptando, (3) el cliente confirma con **ACK**. Recién entonces empieza la transferencia de datos.

**09** — La capa 5 (Sesión) gestiona el ciclo completo de una conversación: **apertura** (negocia parámetros e identidades), **mantenimiento** (mantiene el canal activo con tokens), **sincronización** (puntos de recuperación) y **cierre controlado**. Ejemplo: una sesión SSH o SMB.

**10** — La capa 6 (Presentación) adapta el formato de los datos: traduce entre formatos (ASCII, Unicode), aplica compresión y gestiona cifrado/descifrado (TLS en análisis didáctico). Permite que sistemas con distintas representaciones internas se entiendan.

---

## Sección 3 — Protocolo IP y Subredes

| N° | Pregunta | Respuesta correcta | Opción |
|----|----------|--------------------|--------|
| 11 | ¿Cuántos bits tiene una dirección IPv4? | **32 bits** | B |
| 12 | ¿Cuántos hosts utilizables tiene una red `/26`? | **62 hosts utilizables** | C |
| 13 | ¿Cuál rango corresponde a IP privadas RFC1918? | **172.16.0.0 – 172.31.255.255** | B |
| 14 | ¿Qué es el "gateway" en una red IP? | **El router que permite que una red local se comunique con otras redes** | B |
| 15 | ¿Cuántos bits tiene una dirección IPv6 y por qué fue necesario? | **128 bits — representados en hexadecimal, con espacio prácticamente ilimitado** | C |

### Justificaciones — Sección 3

**11** — IPv4 = 32 bits = 4 octetos × 8 bits. Permite ≈ 4.294 millones de direcciones (2³² = 4.294.967.296). Por el agotamiento de ese espacio se desarrolló IPv6.

**12** — Con `/26` quedan 6 bits para hosts: 2⁶ = 64 direcciones totales. Se restan 2 (dirección de red y broadcast): **64 − 2 = 62 hosts utilizables**. Máscara en decimal: 255.255.255.192.

**13** — Los tres rangos privados RFC1918 son:
- `10.0.0.0/8` → 10.0.0.0 – 10.255.255.255
- `172.16.0.0/12` → **172.16.0.0 – 172.31.255.255** ✓
- `192.168.0.0/16` → 192.168.0.0 – 192.168.255.255

Ninguno es enrutable directamente en Internet sin NAT.

**14** — El gateway es el router que actúa como "puerta de salida" de la red local. Sin un gateway correctamente configurado, un dispositivo solo puede comunicarse dentro de su propia red local. Ejemplo típico: 192.168.1.1.

**15** — IPv6 tiene 128 bits (vs. 32 de IPv4), representados en 8 grupos de 4 dígitos hexadecimales separados por `:`. Ejemplo: `2001:0db8:85a3::8a2e:0370:7334`. Ofrece 2¹²⁸ ≈ 3,4 × 10³⁸ direcciones.

---

## Sección 4 — Protocolos, Puertos y Seguridad

| N° | Pregunta | Respuesta correcta | Opción |
|----|----------|--------------------|--------|
| 16 | ¿Qué puerto usa HTTPS y qué protocolo lo protege? | **Puerto 443 — protegido con TLS** | D |
| 17 | ¿Qué significa la secuencia DORA en DHCP? | **Discover, Offer, Request, Acknowledge** | B |
| 18 | ¿Qué ataque satura la tabla MAC del switch? | **MAC Flooding** | C |
| 19 | ¿Cuál NO es un protocolo de enrutamiento dinámico? | **FTP (File Transfer Protocol)** | D |
| 20 | ¿Qué indica el campo "Window Size" en la cabecera TCP? | **La cantidad de datos que el receptor puede aceptar sin confirmación (control de flujo)** | C |

### Justificaciones — Sección 4

**16** — HTTPS opera en el **puerto 443/TCP** y agrega **TLS (Transport Layer Security)** sobre HTTP. En una captura de Wireshark se puede ver el handshake TCP y la negociación TLS, pero el contenido de la aplicación viaja cifrado. HTTP sin cifrado usa el puerto 80.

**17** — La secuencia DORA describe los 4 mensajes DHCP:
1. **Discover** — el cliente busca servidores DHCP por broadcast (UDP 68→67)
2. **Offer** — el servidor ofrece una IP y parámetros de red
3. **Request** — el cliente solicita usar la IP ofrecida
4. **Acknowledge** — el servidor confirma la concesión

**18** — El **MAC Flooding** inunda la tabla CAM del switch con miles de direcciones MAC falsas. Al saturarse, el switch no puede identificar destinos y reenvía tráfico a todos los puertos (comportamiento de hub), permitiendo al atacante capturarlo. Contramedida: **Port Security**.

**19** — **FTP** es un protocolo de transferencia de archivos de la capa de aplicación (puerto 20/21 TCP). Los protocolos de enrutamiento dinámico son: **OSPF**, **BGP** (enrutamiento global de Internet entre proveedores), **RIP** y **EIGRP**.

**20** — El campo **Window Size** (16 bits en la cabecera TCP) implementa el **control de flujo**: indica cuántos bytes puede recibir el receptor sin necesidad de enviar un ACK de confirmación. Si la ventana es pequeña, el emisor debe esperar antes de continuar enviando datos.

---

## Tabla resumen de respuestas

| N° | Sec | Opción | N° | Sec | Opción |
|----|-----|--------|----|-----|--------|
| 01 | 1   | **C**  | 11 | 3   | **B**  |
| 02 | 1   | **C**  | 12 | 3   | **C**  |
| 03 | 1   | **B**  | 13 | 3   | **B**  |
| 04 | 1   | **B**  | 14 | 3   | **B**  |
| 05 | 1   | **C**  | 15 | 3   | **C**  |
| 06 | 2   | **D**  | 16 | 4   | **D**  |
| 07 | 2   | **B**  | 17 | 4   | **B**  |
| 08 | 2   | **B**  | 18 | 4   | **C**  |
| 09 | 2   | **C**  | 19 | 4   | **D**  |
| 10 | 2   | **C**  | 20 | 4   | **C**  |

---

## Criterio de evaluación sugerido

| Puntaje | Porcentaje | Calificación |
|---------|------------|--------------|
| 18 – 20 | 90 – 100 % | Muy Bueno / Sobresaliente |
| 14 – 17 | 70 – 89 %  | Bueno |
| 10 – 13 | 50 – 69 %  | Regular / Suficiente |
| 0 – 9   | 0 – 49 %   | Insuficiente |

*Cada pregunta vale 1 punto. Puntaje total: 20 puntos.*
