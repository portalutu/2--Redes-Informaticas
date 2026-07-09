# Redes de Computadoras — 2° EMT

Repositorio de materiales para la materia **Redes de Computadoras**, nivel 2° EMT – Tecnologías de la Información, UTU 2026.

## 🌐 Sitio web del curso

Todo el contenido de este repositorio está organizado y navegable desde **[index.html](index.html)**, un portal que centraliza el acceso a la teoría, las prácticas, las herramientas y las evaluaciones. Si el repositorio tiene GitHub Pages habilitado, el portal queda disponible también en la URL pública del sitio.

---

## Estructura del repositorio

```text
2--Redes-Informaticas/
├── index.html         # Portal de acceso a todos los materiales del curso
├── Teorico/            # Documentos y presentaciones teóricas
├── Practicas/          # Capturas de red para practicar análisis de tráfico
├── Herramientas/        # Simuladores interactivos y scripts generadores de PCAP
├── Eval/               # Actividades de evaluación (con subcarpeta Hechas/ de resueltas)
├── Proyecto/           # Proyecto final integrador
└── Documentos/         # Documentación adicional del curso
```

---

## Teórico

### Documento principal

| Archivo | Descripción |
| ------- | ----------- |
| [Modelos_OSI_TCPIP.md](Teorico/Modelos_OSI_TCPIP.md) | Documento completo sobre modelos OSI y TCP/IP: historia, capas, protocolos, direccionamiento IP, subnetting y comparativa entre modelos |
| [Redes-Protocolos.pdf](Teorico/Redes-Protocolos.pdf) | Presentación introductoria del curso |

### Presentaciones interactivas (HTML)

| Archivo | Contenido |
| ------- | --------- |
| [capa_4_osi_presentacion_interactiva_v_4_completa.html](Teorico/capa_4_osi_presentacion_interactiva_v_4_completa.html) | Capa 4 OSI – Transporte (TCP/UDP, puertos, segmentación) |
| [capa_5_osi_sesion_interactiva.html](Teorico/capa_5_osi_sesion_interactiva.html) | Capa 5 OSI – Sesión |
| [capa_6_osi_presentacion_interactiva.html](Teorico/capa_6_osi_presentacion_interactiva.html) | Capa 6 OSI – Presentación (formatos, cifrado, compresión) |
| [capa_7_osi_aplicacion_interactiva.html](Teorico/capa_7_osi_aplicacion_interactiva.html) | Capa 7 OSI – Aplicación (HTTP, DNS, DHCP, SMTP) |
| [protocolo_ip.html](Teorico/protocolo_ip.html) | Protocolo IP interactivo |
| [protocolo_ip_explicacion.html](Teorico/protocolo_ip_explicacion.html) | Explicación del protocolo IP |
| [viaje_paquete_ip.html](Teorico/viaje_paquete_ip.html) | Visualización del recorrido de un paquete IP por la red |
| [pcap_wireshark.html](Teorico/pcap_wireshark.html) | Introducción a archivos PCAP y Wireshark |

### Contenidos cubiertos en el teórico

#### Modelos de referencia

- Contexto histórico: ARPANET, la necesidad de estandarización
- Problemas de las redes antes de OSI y TCP/IP
- Modelo OSI: 7 capas (Física, Enlace, Red, Transporte, Sesión, Presentación, Aplicación)
- Modelo TCP/IP: 4 capas (Acceso a la red, Internet, Transporte, Aplicación)
- Comparativa OSI vs. TCP/IP

#### Capa Física (1)

- Medios de transmisión: UTP, fibra óptica, Wi-Fi, satélite
- Tabla de distancias máximas por medio
- Control de colisiones (CSMA/CD)
- Seguridad física

#### Capa de Enlace de Datos (2)

- Tramas Ethernet
- Direcciones MAC y subcapas LLC/MAC
- Switches y dominios de colisión
- VLANs (IEEE 802.1Q), puertos access y trunk
- Ataques: MAC flooding, ARP spoofing, VLAN hopping
- Protecciones: Port Security, DHCP Snooping, DAI

#### Capa de Red (3)

- Protocolo IP (IPv4 e IPv6)
- Direccionamiento: privado (RFC1918) y público
- Máscaras de subred y notación CIDR
- Subnetting paso a paso con ejemplos binarios
- Enrutamiento estático y dinámico (RIP, OSPF, BGP)
- Routers y tablas de enrutamiento
- NAT y su función en redes domésticas y empresariales

#### Capa de Transporte (4)

- TCP vs. UDP: diferencias y casos de uso
- Puertos y multiplexación de aplicaciones
- Segmentación y control de flujo

#### Capas 5, 6 y 7

- Sesión, Presentación y Aplicación
- Protocolos: HTTP/S, DNS, DHCP, SMTP, FTP, SSH, Telnet

---

## Prácticas

### Capturas de red para análisis

| Archivos | Descripción |
| -------- | ----------- |
| [800_practica_red_192_168_1.pcap](Practicas/800_practica_red_192_168_1.pcap) / [.txt](Practicas/800_practica_red_192_168_1.txt) | Captura de 800 paquetes en la red 192.168.1.0/24 |
| [1000_practica_red_192_168_1.pcap](Practicas/1000_practica_red_192_168_1.pcap) / [.txt](Practicas/1000_practica_red_192_168_1.txt) | Captura de 1000 paquetes en la red 192.168.1.0/24 |

Los archivos `.pcap` pueden abrirse con **Wireshark**. Los archivos `.txt` contienen la descripción del tráfico capturado.

---

## Herramientas del curso

| Archivo | Descripción |
| ------- | ----------- |
| [terminal_simulador.html](Herramientas/terminal_simulador.html) | Simulador interactivo de terminal para practicar captura de red en el navegador |
| [wireshark_simulador.html](Herramientas/wireshark_simulador.html) | Simulador interactivo de Wireshark en el navegador |
| [generar_pcap.py](Herramientas/generar_pcap.py) / [.sh](Herramientas/generar_pcap.sh) | Scripts para generar archivos de captura PCAP de práctica |
| [terminal_simulador.py](Herramientas/terminal_simulador.py) / [.sh](Herramientas/terminal_simulador.sh) | Versiones script del simulador de terminal |

---

## Evaluaciones

| Archivo | Descripción |
| ------- | ----------- |
| [actividad_analisis_trafico.html](Eval/actividad_analisis_trafico.html) | Actividad guiada de análisis de tráfico con preguntas y ejercicios |
| [500_practica_red_192_168_1.pcap](Eval/500_practica_red_192_168_1.pcap) / [.txt](Eval/500_practica_red_192_168_1.txt) | Captura de 500 paquetes en la red 192.168.1.0/24 para la evaluación |
| [Hechas/evaluacion_redes_informaticas.html](Eval/Hechas/evaluacion_redes_informaticas.html) | Evaluación de Redes Informáticas ya realizada |
| [Hechas/evaluacion_redes_respuestas.md](Eval/Hechas/evaluacion_redes_respuestas.md) | Respuestas correspondientes a la evaluación resuelta |

---

## Proyecto Final

[Idea del Proyecto Final](Proyecto/idea_proyecto.md)

Proyecto integrador de diseño e implementación de una red para una institución real o simulada.

### Escenarios disponibles

**Escenario A — Liceo:** sala de informática (30 PC), laboratorio (15 PC), administración (10 PC), biblioteca (5 PC), WiFi estudiantes y docentes, servidor local.

**Escenario B — Empresa:** área administrativa (10 equipos), área de desarrollo (20 equipos), sala de reuniones (WiFi), área de servidores, red para visitantes.

### Requisitos del proyecto

1. Diagrama de red (Packet Tracer, draw.io o diagrams.net)
2. Topología elegida y justificación
3. Plan de direccionamiento IP con subredes por sector
4. Dispositivos de red y su función
5. Servicios de red (DHCP, DNS, servidor de archivos, web interno)
6. Medidas de seguridad básica
7. Simulación funcional en Packet Tracer

### Entregables

- Documento técnico (5–10 páginas)
- Diagrama de red (archivo digital)
- Simulación Packet Tracer (archivo `.pkt`)
- Presentación oral (10 minutos por equipo)

### Rúbrica

| Criterio | Puntaje |
| -------- | ------- |
| Diseño de red | 25 |
| Direccionamiento IP | 20 |
| Simulación Packet Tracer | 25 |
| Documentación técnica | 15 |
| Presentación oral | 15 |
| **Total** | **100** |

---

## Herramientas utilizadas en el curso

- **Wireshark** — análisis de capturas de tráfico de red
- **Cisco Packet Tracer** — simulación de redes
- **draw.io / diagrams.net** — diagramas de red
- **Python** — generación de capturas PCAP para prácticas
