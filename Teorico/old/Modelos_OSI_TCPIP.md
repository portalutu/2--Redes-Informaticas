# Modelos OSI y TCP/IP

## 1. Introducción

Hoy en día estamos acostumbrados a abrir páginas web, enviar correos, mensajes, compartir información,  hacer videollamadas o usamos apps en el celular en forma totalmente "transparente", pero por detrás de todas estas acciones ocurren muchos procesos de comunicación entre equipos de todo tipo. Para que esa comunicación funcione, **absolutamente** **todos** los dispositivos involucrados **deben seguir reglas comunes**.

Esas reglas son denominados estándares y protocolos, y surgieron de años de cuidadosa planificación, estandarización e innovación. Antes de la estandarización de los modelos **OSI** y **TCP/IP**, el mundo de las redes estaba fragmentado: cada fabricante podía trabajar con tecnologías, protocolos y formatos propios, lo que dificultaba enormemente la interoperabilidad.

Esta situación es el resultado de una evolución tecnológica que comenzó varias décadas antes del surgimiento de las redes modernas.

**1.1 Contexto histótico**

**1945** – El científico **Vannevar Bush** publica el artículo *"As We May Think"*, donde imagina sistemas de información interconectados capaces de compartir conocimiento. Aunque no describe redes de computadoras como las actuales, introduce la idea de sistemas de información conectados.

**Finales de los años 1940 y 1950** – Las primeras computadoras electrónicas aparecen en laboratorios militares y universidades. Estas máquinas funcionaban de manera aislada y no existían redes que permitieran compartir información entre ellas.

**Década de 1960** – El crecimiento del uso de computadoras genera la necesidad de conectar sistemas para compartir recursos. Surgen investigaciones sobre **conmutación de paquetes**, un concepto clave desarrollado por **Paul Baran**, **Donald Davies** y **Leonard Kleinrock**. Este enfoque permite dividir la información en pequeños paquetes que pueden viajar por diferentes rutas dentro de una red.

**1969** – Se crea **ARPANET**, considerada la primera red de computadoras de gran escala. Fue financiada por la agencia ARPA del Departamento de Defensa de Estados Unidos. Inicialmente conectaba universidades y centros de investigación, demostrando que era posible interconectar sistemas informáticos a distancia.

**Principios de los años 1970** – Comienzan a aparecer muchas redes diferentes, cada una con tecnologías y protocolos propios. Algunos ejemplos incluyen **ARPANET**, **SNA de IBM**, **DECnet de Digital Equipment Corporation** y otras arquitecturas propietarias. Estas redes funcionaban bien internamente, pero no podían comunicarse entre sí.

**1973 – 1974** – **Vinton Cerf** y **Robert Kahn** desarrollan el concepto de **internetworking**, que propone una arquitectura capaz de conectar redes distintas. De esta investigación surgen los primeros diseños del protocolo **TCP**, que más tarde evolucionaría hacia la familia **TCP/IP**.

**Finales de los años 1970** – La proliferación de redes incompatibles genera un problema global de interoperabilidad. Diferentes organizaciones comienzan a trabajar en estándares que permitan que sistemas de distintos fabricantes puedan comunicarse.

**1977 – 1978** – La **ISO (International Organization for Standardization)** inicia el desarrollo de un modelo conceptual para organizar las funciones de comunicación en redes. Este trabajo daría origen al **modelo OSI (Open Systems Interconnection)**.

Este contexto histórico explica por qué fue necesario crear modelos de referencia. La industria necesitaba una forma estructurada de definir cómo debían comunicarse los sistemas, lo que finalmente llevó al desarrollo del modelo OSI y a la consolidación de la arquitectura TCP/IP.


---


## 2. Los problemas de las redes antes del establecimiento de TCP/IP y OSI

Antes de que existieran modelos de referencia claros y conjuntos de protocolos ampliamente aceptados, las redes tenían varios problemas importantes.

### 2.1 Falta de compatibilidad entre fabricantes

Cada fabricante diseñaba sus propios sistemas de comunicación. Esto significaba que equipos de marcas distintas muchas veces no podían comunicarse entre sí o requerían adaptaciones complejas.

**Ejemplo práctico:** una empresa podía tener computadoras, terminales y equipos de red de diferentes proveedores, pero no lograr que todos intercambiaran datos correctamente.

### 2.2 Protocolos cerrados y propietarios

Muchas soluciones de red eran propietarias. Eso implicaba dependencia del fabricante, poca flexibilidad y altos costos de expansión o mantenimiento.

### 2.3 Ausencia de una estructura común para diseñar redes

No existía un modelo universal que organizara las funciones de la comunicación en capas. Como consecuencia, diagnosticar fallas, diseñar nuevas soluciones o enseñar redes era mucho más difícil.

### 2.4 Dificultad para interconectar redes diferentes

Había redes con distintos tamaños de paquetes, métodos de transmisión, velocidades, medios físicos y formatos de direccionamiento. Integrarlas entre sí era un desafío técnico importante.

### 2.5 Problemas para escalar

A medida que las redes crecían, se necesitaban soluciones que permitieran conectar muchos sistemas de forma ordenada y mantenible. Los enfoques cerrados y aislados no escalaban bien.

### 2.6 Complejidad para detectar errores

Cuando una comunicación fallaba, no estaba claro si el problema era del medio físico, del direccionamiento, del control de errores, de la aplicación o del formato de los datos. Hacía falta una forma de separar responsabilidades.

### 2.7 Necesidad de estandarización

La industria necesitaba un lenguaje común para que diferentes tecnologías pudieran convivir. De esa necesidad nacieron los modelos de referencia y la estandarización por capas.

---

## 3. Historia del modelo OSI

El modelo **OSI** significa **Open Systems Interconnection** o **Interconexión de Sistemas Abiertos**.

Fue impulsado por la **ISO** con el objetivo de crear un modelo de referencia estándar que permitiera la comunicación entre sistemas de distintos fabricantes. Su desarrollo comenzó a fines de la década de 1970 y quedó formalizado en los primeros años de la década de 1980.

### 3.1 ¿Por qué surgió?

Surgió como respuesta al desorden existente en el mundo de las redes. Había demasiados protocolos y arquitecturas incompatibles, y era necesario un marco común para organizar la comunicación de datos.

### 3.2 Objetivo principal

El objetivo del modelo OSI no fue definir exactamente qué protocolo debía usar cada red, sino **describir qué función debía cumplir cada capa** dentro del proceso de comunicación.

### 3.3 Importancia histórica

Aunque en la práctica el modelo TCP/IP terminó imponiéndose en Internet, el modelo OSI se volvió fundamental para:

* estudiar redes,
* diseñar arquitecturas de comunicación,
* diagnosticar problemas,
* y entender la separación de funciones en una red.

En la enseñanza técnica sigue siendo una herramienta central porque ordena el conocimiento de manera clara y precisa.

---

## 4. El modelo OSI

El modelo OSI divide el proceso de comunicación en **7 capas**. Cada capa cumple una función específica y se apoya en la capa inferior.

La idea central es simple:

* cada capa resuelve un tipo de problema,
* ofrece servicios a la capa superior,
* y trabaja de forma coordinada con el resto.

### 4.1 Las 7 capas del modelo OSI

1. **Física**
2. **Enlace de datos**
3. **Red**
4. **Transporte**
5. **Sesión**
6. **Presentación**
7. **Aplicación**

---

## 5. Las 7 capas del modelo OSI, detalladas

## Capa 1. Física

### Función

Se encarga de la transmisión **física** de bits a través del medio.

### Qué define

* cables,
* conectores,
* señales eléctricas, ópticas o de radio,
* niveles de voltaje,
* sincronización básica,
* velocidad de transmisión.

### Unidad de datos

**Bit**

### Ejemplos

* cable UTP,
* fibra óptica,
* conectores RJ45,
* hubs,
* repetidores,
* estándares físicos de Ethernet.

### Relación con la subcapa MAC

Aunque el modelo OSI separa claramente la **capa física (1)** de la **capa de enlace de datos (2)**, en muchas explicaciones prácticas de redes Ethernet ambas trabajan muy estrechamente.

Dentro de la **capa 2 (Enlace de datos)** existe una división en **dos subcapas**:

* **LLC (Logical Link Control)**
* **MAC (Media Access Control)**

La **subcapa MAC** es especialmente importante porque:

* controla **cómo los dispositivos acceden al medio físico**,
* gestiona las **direcciones MAC**, que identifican de forma única cada interfaz de red,
* determina **cuándo un dispositivo puede transmitir datos** para evitar colisiones.

En tecnologías como **Ethernet y Wi‑Fi**, la subcapa MAC trabaja en conjunto con la capa física para permitir que los bits transmitidos por el cable o el aire puedan organizarse correctamente en **tramas**.

### Ejemplo práctico

Si conectamos dos PCs mediante cable de red:

1. La **capa física** envía los bits por el cable.
2. La **subcapa MAC** identifica el dispositivo destino mediante su **dirección MAC**.
3. La **trama Ethernet** llega al equipo correcto dentro de la red local.

---

### Distancias máximas según el medio de transmisión

Los distintos **medios físicos de transmisión** tienen limitaciones técnicas relacionadas con la potencia de señal, interferencias, atenuación y tecnología utilizada. Estas limitaciones determinan la **distancia máxima aproximada** que puede recorrer una señal sin necesidad de repetidores o regeneradores.

| Medio de transmisión           | Tipo        | Distancia típica máxima                | Observaciones                                                    |
| ------------------------------ | ----------- | -------------------------------------- | ---------------------------------------------------------------- |
| **NFC**                        | Inalámbrico | 10 cm                                  | Usado para pagos móviles y tarjetas de proximidad                |
| **Bluetooth**                  | Inalámbrico | 10 m (Clase 2) / hasta 100 m (Clase 1) | Dispositivos personales como auriculares, teclados o IoT         |
| **Zigbee**                     | Inalámbrico | 10 – 100 m                             | Muy usado en domótica y sensores IoT                             |
| **Wi‑Fi**                      | Inalámbrico | 30 – 100 m                             | Depende de obstáculos, interferencias y estándar (802.11n/ac/ax) |
| **UTP (Ethernet)**             | Alámbrico   | 100 m                                  | Distancia estándar para redes Ethernet sobre par trenzado        |
| **STP**                        | Alámbrico   | 100 m                                  | Par trenzado blindado para entornos con interferencias           |
| **FTP (Foiled Twisted Pair)**  | Alámbrico   | 100 m                                  | Variante con blindaje adicional contra interferencias            |
| **Coaxial (Ethernet antiguo)** | Alámbrico   | 185 – 500 m                            | Utilizado en Ethernet 10BASE2 y 10BASE5                          |
| **Fibra óptica multimodo**     | Alámbrico   | 300 m – 2 km                           | Usada en redes LAN, campus y centros de datos                    |
| **Radio microondas terrestre** | Inalámbrico | 5 – 50 km                              | Enlaces punto a punto entre antenas con línea de vista           |
| **Fibra óptica monomodo**      | Alámbrico   | 10 – 80 km o más                       | Utilizada en redes de telecomunicaciones de larga distancia      |
| **Línea T1**                   | Alámbrico   | ~1 km entre repetidores                | Enlaces digitales de 1.544 Mbps utilizados en telecomunicaciones |
| **Línea T2**                   | Alámbrico   | ~1 km entre repetidores                | Capacidad aproximada de 6.312 Mbps                               |
| **Línea T3**                   | Alámbrico   | Hasta ~45 km con regeneradores         | Enlace de alta capacidad (44.736 Mbps) utilizado por operadores  |
| **Fibra óptica submarina**     | Alámbrico   | Cientos a miles de km                  | Backbone internacional de Internet                               |
| **Enlace satelital (GEO)**     | Satelital   | 35,786 km hasta el satélite            | Comunicación global con alta latencia                            |
| **Enlace satelital (LEO)**     | Satelital   | 500 – 2,000 km hasta el satélite       | Usado por constelaciones modernas como Starlink                  |

Estas distancias pueden variar dependiendo de:

* la calidad del cableado,
* interferencias ambientales,
* equipos utilizados (switches, repetidores, amplificadores),
* estándares tecnológicos específicos.

Cuando la distancia necesaria supera los límites del medio físico, se utilizan dispositivos como **repetidores, switches, regeneradores ópticos o enlaces intermedios**.

---

### Limitaciones de la capa 1

La **capa física** es la base de toda comunicación en red, pero tiene varias limitaciones importantes:

* Solo transporta **bits**, no interpreta direcciones, paquetes ni protocolos.
* No puede identificar **qué dispositivo envía o recibe información**.
* No tiene mecanismos propios de **control de errores complejos**.
* No puede decidir rutas ni gestionar tráfico.
* Está limitada por las **características físicas del medio**.

Entre las limitaciones más comunes se encuentran:

* **distancia máxima del cable** (por ejemplo, 100 metros en Ethernet UTP),
* **atenuación de señal**,
* **interferencia electromagnética**,
* **ruido eléctrico**,
* limitaciones de **velocidad del medio**.

Por estas razones, la capa física depende de las capas superiores para organizar y controlar la comunicación.

---

### Control de colisiones en el medio físico

Aunque el control lógico de colisiones pertenece principalmente a la **subcapa MAC (capa 2)**, el fenómeno de la colisión ocurre en el **medio físico**, cuando dos dispositivos transmiten señales eléctricas o de radio al mismo tiempo.

En redes antiguas donde muchos equipos compartían el mismo cable o segmento (por ejemplo redes Ethernet con **hub**), podían producirse colisiones físicas.

Cuando esto ocurría:

* las señales se superponían,
* los bits se corrompían,
* los dispositivos debían retransmitir los datos.

El mecanismo utilizado para manejar estas situaciones fue **CSMA/CD**, donde:

1. el dispositivo escucha el medio físico,
2. transmite solo si el canal está libre,
3. detecta colisiones en el cable,
4. espera un tiempo aleatorio antes de retransmitir.

Con la introducción de **switches y enlaces full‑duplex**, las colisiones prácticamente desaparecieron en redes modernas.

---

### Seguridad en capa 1

La seguridad en la capa física se relaciona con el **acceso físico al medio de transmisión**. Si un atacante obtiene acceso al cableado o a los dispositivos físicos de red, puede comprometer la seguridad del sistema.

### Amenazas comunes

**1. Intercepción física del cableado**

Un atacante puede conectar un dispositivo al cable de red para capturar tráfico.

**2. Dispositivos de escucha (taps de red)**

Existen dispositivos que pueden insertarse en un cable para copiar todo el tráfico que circula por él.

**3. Sabotaje físico**

Cortar cables, desconectar equipos o interferir con el medio de transmisión puede provocar caídas completas de red.

**4. Interferencia electromagnética intencional**

En algunos casos se pueden generar interferencias para degradar la comunicación inalámbrica.

---

### Medidas de protección en capa 1

Las medidas de seguridad en esta capa suelen ser **físicas u organizativas**:

* control de acceso a salas de servidores,
* racks cerrados con llave,
* canalización protegida del cableado,
* monitoreo físico de la infraestructura,
* segmentación del cableado estructurado,
* uso de fibra óptica en enlaces críticos.

La fibra óptica tiene ventajas de seguridad porque:

* es más difícil de interceptar sin cortar el cable,
* no emite señales electromagnéticas detectables externamente.

---

### Problemas típicos

* cable dañado,
* conector flojo,
* interferencia electromagnética,
* puerto sin señal,
* velocidad o dúplex mal negociados,
* atenuación o pérdida de señal en el medio.

---

## Capa 2. Enlace de datos

### Función

Se encarga de la comunicación confiable entre dispositivos que están en el **mismo enlace o red local**. Su objetivo principal es tomar los bits que provienen de la capa física y organizarlos en estructuras llamadas **tramas**, permitiendo que los dispositivos de la misma red puedan identificarse y comunicarse correctamente.

La capa de enlace es fundamental en redes locales porque controla cómo se transmite la información dentro de un mismo segmento de red.

### Qué hace

* organiza los bits en **tramas**,
* usa direcciones físicas (**MAC**),
* detecta errores locales,
* controla el acceso al medio,
* administra la comunicación dentro de una red local.

### Unidad de datos

**Trama**

### Subcapas de la capa de enlace

La capa de enlace de datos se divide en dos subcapas:

**1. LLC (Logical Link Control)**

Se encarga de la comunicación lógica entre dispositivos y de la identificación de los protocolos de capa superior que utilizan la red.

**2. MAC (Media Access Control)**

Controla el acceso al medio físico y utiliza las **direcciones MAC** para identificar los dispositivos dentro de una red local.

### Ejemplos

* Ethernet,
* direcciones MAC,
* switches,
* VLAN,
* PPP,
* Wi‑Fi (802.11).

### Ejemplo práctico

Cuando una PC envía datos a otra PC dentro de la misma LAN, la capa de enlace utiliza la **dirección MAC del destino** para encapsular los datos en una **trama Ethernet** y enviarla por la red local.

Un switch recibe esa trama y analiza la dirección MAC de destino para decidir **por qué puerto debe reenviarla**.

---

### VLAN (Virtual LAN)

Las VLAN (Virtual Local Area Network) son una tecnología de capa 2 que permite dividir una red física en varias redes lógicas independientes.

En una red tradicional sin VLAN, todos los dispositivos conectados a un mismo switch pertenecen al mismo dominio de broadcast, es decir, todos reciben ciertos tipos de tráfico de red.

Las VLAN permiten segmentar la red, de forma que dispositivos conectados al mismo switch puedan pertenecer a redes diferentes, como si estuvieran conectados a switches distintos.

¿Para qué se utilizan las VLAN?

Las VLAN se utilizan principalmente para:

mejorar la organización de la red, separando departamentos o áreas,

reducir el tráfico de broadcast,

aumentar la seguridad, evitando que todos los dispositivos estén en la misma red,

facilitar la administración de redes grandes.

Ejemplo práctico

Supongamos una empresa con tres departamentos:

Administración

Docencia

Invitados

Aunque todos los equipos estén conectados al mismo switch, se pueden crear:

VLAN 10 → Administración

VLAN 20 → Docencia

VLAN 30 → Invitados

Cada VLAN funciona como si fuera una red separada.

Los equipos dentro de la misma VLAN pueden comunicarse directamente en capa 2, mientras que la comunicación entre VLANs requiere un router o switch de capa 3.

VLAN tagging (IEEE 802.1Q)

Para que varios switches puedan transportar tráfico de múltiples VLANs entre ellos, se utiliza el estándar IEEE 802.1Q, que agrega una etiqueta dentro de la trama Ethernet.

Esta etiqueta indica a qué VLAN pertenece el tráfico.

Existen dos tipos principales de puertos en los switches:

Puerto Access

pertenece a una sola VLAN

conecta dispositivos finales como PCs, impresoras o cámaras

Puerto Trunk

transporta tráfico de múltiples VLANs

se utiliza para interconectar switches o dispositivos de red

Beneficios de las VLAN

mejor segmentación de la red

mayor seguridad

reducción de dominios de broadcast

mejor organización de la infraestructura de red

Las VLAN son una de las tecnologías más importantes de la capa 2, y forman la base de muchas arquitecturas modernas de redes empresariales.

---

### Limitaciones de la capa 2

La capa de enlace de datos funciona únicamente dentro de una **misma red local o dominio de broadcast**. Esto implica varias limitaciones:

* No puede enrutar datos entre redes distintas.
* No utiliza direcciones lógicas globales como IP.
* Su alcance está limitado al segmento de red.
* Las tramas no están diseñadas para viajar por Internet.

Por esta razón, cuando un dispositivo necesita comunicarse con otro que está en **otra red**, es necesario que intervenga la **capa 3 (red)** mediante un **router**.

---

### Control de colisiones

En las primeras redes Ethernet, varios dispositivos compartían el mismo medio físico (por ejemplo, un cable coaxial o un hub). Esto generaba la posibilidad de que **dos equipos transmitieran al mismo tiempo**, provocando una **colisión**.

Para resolver este problema se diseñaron mecanismos de control de acceso al medio.

### CSMA/CD

Uno de los métodos más conocidos es **CSMA/CD (Carrier Sense Multiple Access with Collision Detection)**.

Este mecanismo funciona de la siguiente forma:

1. Un dispositivo escucha el medio antes de transmitir.
2. Si el medio está libre, comienza la transmisión.
3. Si dos dispositivos transmiten al mismo tiempo, ocurre una colisión.
4. Los dispositivos detectan la colisión.
5. Cada uno espera un tiempo aleatorio antes de volver a intentar transmitir.

Este sistema fue muy común en redes Ethernet con **hubs**.

### Evolución con switches

Las redes modernas utilizan **switches**, lo que permite crear enlaces dedicados entre dispositivos. Gracias a esto:

* se reducen o eliminan las colisiones,
* cada enlace puede trabajar en **full duplex**,
* el rendimiento de la red mejora significativamente.

---

### Seguridad en capa 2

Aunque muchas personas asocian la seguridad de redes con firewalls o sistemas de capa 3 y 4, existen varios problemas de seguridad que ocurren directamente en la **capa de enlace de datos**.

#### Ataques comunes en capa 2

**1. MAC flooding**

Un atacante envía grandes cantidades de direcciones MAC falsas a un switch para llenar su tabla de direcciones. Cuando la tabla se satura, el switch comienza a comportarse como un hub y envía tráfico a todos los puertos, permitiendo que el atacante capture información.

**2. ARP spoofing (o ARP poisoning)**

El atacante envía respuestas ARP falsas para asociar su dirección MAC con la dirección IP de otro dispositivo, como un router. Esto le permite interceptar el tráfico de la red.

**3. VLAN hopping**

Técnica que intenta enviar tráfico entre VLANs sin pasar por un router o firewall, aprovechando configuraciones incorrectas en switches.

---

### Mecanismos de protección en capa 2

Los switches modernos incluyen varias herramientas para mejorar la seguridad en esta capa.

**Port Security**

Permite limitar cuántas direcciones MAC pueden conectarse a un puerto específico del switch.

**DHCP Snooping**

Permite identificar servidores DHCP legítimos y bloquear servidores DHCP falsos dentro de la red.

**Dynamic ARP Inspection (DAI)**

Evita ataques de ARP spoofing verificando que las respuestas ARP coincidan con la información conocida de la red.

**Segmentación mediante VLAN**

Permite separar dispositivos en redes lógicas independientes, reduciendo el alcance de ataques dentro de una LAN.

---

### Problemas típicos

* conflicto de VLAN o dirección MAC,
* dirección MAC no aprendida,
* errores de trama,
* loops de red (tormentas de broadcast),
* fallas en switching.

---



### Función

Permite que los datos viajen entre **redes diferentes**.

### Qué hace

* usa direcciones lógicas,
* selecciona rutas,
* permite el enrutamiento,
* fragmenta paquetes si es necesario.

### Unidad de datos

**Paquete**

### Ejemplos

* IP,
* routers,
* subredes,
* ICMP,
* direccionamiento IPv4 e IPv6.

### Ejemplo práctico

Cuando un estudiante abre una web alojada en otro país, los paquetes salen de su red local y atraviesan varios routers gracias a la capa de red.

### Problemas típicos

* IP mal configurada,
* puerta de enlace incorrecta,
* subred equivocada,
* ruta inexistente.

---

## Capa 3. Red

### Función

Permite que los datos viajen entre **redes diferentes**. La capa de red es responsable del **direccionamiento lógico** y del **enrutamiento**, es decir, de determinar por qué camino deben viajar los paquetes para llegar desde el origen hasta el destino.

Mientras que la capa 2 funciona dentro de una red local, la capa 3 permite **interconectar múltiples redes**, formando lo que conocemos como **internetworking** (redes de redes).

### Qué hace

* usa direcciones lógicas (IP),
* determina rutas entre redes,
* permite el **enrutamiento de paquetes**,
* fragmenta paquetes cuando es necesario,
* interconecta redes locales distintas.

### Unidad de datos

**Paquete**

### Ejemplos

* IP,
* routers,
* subredes,
* ICMP,
* direccionamiento IPv4 e IPv6.

### Dispositivos de la capa 3

El dispositivo más representativo de esta capa es el **router**.

Otros dispositivos que pueden trabajar en esta capa son:

* routers
* switches de capa 3
* firewalls
* gateways

#### Funcionamiento básico de un router

Un **router** es un dispositivo que conecta **dos o más redes diferentes** y decide por dónde deben enviarse los paquetes.

El funcionamiento general de un router es el siguiente:

1. recibe un paquete desde una red
2. analiza la **dirección IP de destino**
3. consulta su **tabla de enrutamiento**
4. decide por qué interfaz debe reenviar el paquete
5. envía el paquete hacia la siguiente red

Cada router mantiene una **tabla de rutas**, que indica qué redes conoce y cuál es el mejor camino para alcanzarlas.

### Ejemplo práctico

Cuando un estudiante abre una web alojada en otro país:

1. el paquete sale de la red local
2. llega al **router del hogar o del liceo**
3. ese router lo envía al proveedor de Internet
4. atraviesa múltiples routers en Internet
5. finalmente llega al servidor de destino

---

### Enrutamiento

El **enrutamiento** es el proceso mediante el cual los routers determinan la mejor ruta para enviar paquetes entre redes.

Existen dos formas principales de configurar el enrutamiento.

#### Enrutamiento estático

En el **enrutamiento estático**, las rutas se configuran manualmente por un administrador de red.

El administrador indica explícitamente:

* qué red existe
* cuál es el router siguiente (next hop)

Ventajas:

* simple de implementar
* consume pocos recursos
* predecible

Desventajas:

* difícil de mantener en redes grandes
* no se adapta automáticamente a fallas de red

Ejemplo conceptual de ruta estática:

"Para llegar a la red 192.168.2.0, enviar el tráfico al router 192.168.1.1"

---

### Enrutamiento dinámico

En el **enrutamiento dinámico**, los routers utilizan **protocolos de enrutamiento** que intercambian información automáticamente sobre las redes disponibles.

Esto permite que los routers:

* descubran nuevas redes
* aprendan rutas automáticamente
* se adapten a cambios o fallas en la red

Protocolos comunes de enrutamiento dinámico:

* **RIP (Routing Information Protocol)**
* **OSPF (Open Shortest Path First)**
* **EIGRP**
* **BGP (Border Gateway Protocol)**

El protocolo **BGP** es especialmente importante porque se utiliza para el **enrutamiento global de Internet** entre proveedores de servicio.

---

### Ámbito público y privado de las redes

Las direcciones IP pueden pertenecer a dos ámbitos principales:

#### Direcciones IP privadas

Las **IP privadas** se utilizan dentro de redes internas (hogares, empresas, liceos) y **no son accesibles directamente desde Internet**.

Rangos privados definidos por RFC1918:

* 10.0.0.0 – 10.255.255.255
* 172.16.0.0 – 172.31.255.255
* 192.168.0.0 – 192.168.255.255

Estas direcciones se utilizan dentro de redes locales y normalmente se conectan a Internet mediante **NAT (Network Address Translation)**.

#### Direcciones IP públicas

Las **IP públicas** son direcciones únicas en Internet y permiten que un dispositivo sea accesible desde otras redes del mundo.

Estas direcciones son asignadas por organizaciones de registro de Internet como:

* **IANA**
* **RIRs (Regional Internet Registries)**

Ejemplos de RIR:

* ARIN
* RIPE
* LACNIC
* APNIC

Los proveedores de Internet asignan direcciones públicas a routers o servicios conectados a Internet.

---

### Problemas típicos

* IP mal configurada
* puerta de enlace incorrecta
* subred equivocada
* ruta inexistente
* tabla de enrutamiento incorrecta

---

### El protocolo IP y el direccionamiento de red

El **Protocolo IP (Internet Protocol)** es el protocolo principal de la **capa 3 del modelo OSI** y de la **capa Internet del modelo TCP/IP**. Su función principal es permitir que los paquetes viajen desde un origen hasta un destino a través de múltiples redes interconectadas.

El protocolo IP se encarga de:

* identificar dispositivos mediante **direcciones IP**,
* encapsular datos en **paquetes**,
* permitir que los routers puedan decidir cómo reenviar esos paquetes.

A diferencia de TCP, el protocolo IP es **no orientado a conexión**, lo que significa que los paquetes pueden viajar por rutas diferentes dentro de la red.

---

### Direccionamiento IPv4

El estándar más conocido de direccionamiento es **IPv4 (Internet Protocol version 4)**.

Una dirección IPv4 tiene **32 bits**, divididos en **4 octetos de 8 bits**.

Ejemplo:

```
192.168.1.10
```

Cada octeto puede tener valores entre **0 y 255**.

Esto permite aproximadamente:

**4.294.967.296 direcciones posibles**.

Debido al crecimiento de Internet, este espacio de direcciones comenzó a agotarse, lo que llevó al desarrollo de **IPv6**.

---

### Direccionamiento IPv6

**IPv6 (Internet Protocol version 6)** fue diseñado para reemplazar gradualmente a IPv4.

Características principales:

* direcciones de **128 bits**
* representadas en **hexadecimal**
* separadas por dos puntos

Ejemplo:

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

Ventajas de IPv6:

* espacio de direcciones prácticamente ilimitado
* mejor soporte para redes modernas
* simplificación de ciertos procesos de enrutamiento
* eliminación de la necesidad de NAT en muchos casos

---

### Máscara de subred

Una **máscara de subred** permite dividir una red IP en **subredes más pequeñas**.

La máscara indica qué parte de la dirección IP corresponde a:

* **la red**
* **los hosts (dispositivos)**

Ejemplo:

```
IP: 192.168.1.10
Máscara: 255.255.255.0
```

Esto significa que:

* **192.168.1** identifica la red
* **.10** identifica el dispositivo dentro de esa red

La máscara también puede representarse en **notación CIDR**:

```
192.168.1.10/24
```

El número **/24** indica que los primeros **24 bits** corresponden a la red.

---

### Cálculo de subredes

La división de redes en subredes permite organizar mejor las infraestructuras y reducir el tráfico innecesario.

Ejemplo simple:

Red original:

```
192.168.1.0/24
```

Esta red tiene:

* 256 direcciones totales
* 254 hosts utilizables

Si dividimos la red en dos subredes:

```
192.168.1.0/25
192.168.1.128/25
```

Cada subred tendrá:

* 128 direcciones totales
* 126 hosts utilizables

Otro ejemplo:

Red:

```
10.0.0.0/24
```

Subredes posibles usando /26:

```
10.0.0.0/26
10.0.0.64/26
10.0.0.128/26
10.0.0.192/26
```

Cada subred tendrá **62 hosts utilizables**.

---

### Comprendiendo el subnetting con matemáticas binarias

Las direcciones IPv4 están compuestas por **32 bits**. Estos bits se dividen entre:

* bits de **red**
* bits de **host**

Cada octeto tiene 8 bits:

```
192.168.1.10
```

En binario sería aproximadamente:

```
11000000.10101000.00000001.00001010
```

### Máscara de subred en binario

Ejemplo de máscara:

```
255.255.255.0
```

En binario:

```
11111111.11111111.11111111.00000000
```

Esto significa:

* los **primeros 24 bits** identifican la red
* los **últimos 8 bits** identifican los hosts

Por eso se escribe como:

```
/24
```

---

### Ejemplo de extensión de máscara

Red original:

```
192.168.1.0/24
```

Máscara en binario:

```
11111111.11111111.11111111.00000000
```

Si "tomamos" un bit de la parte de host para crear subredes:

```
11111111.11111111.11111111.10000000
```

Esto corresponde a la máscara:

```
255.255.255.128
```

Notación CIDR:

```
/25
```

Esto genera **2 subredes**.

Subred 1:

```
192.168.1.0 – 192.168.1.127
```

Subred 2:

```
192.168.1.128 – 192.168.1.255
```

Hosts utilizables por subred:

```
2^7 − 2 = 126
```

Se restan dos direcciones porque:

* una es la **dirección de red**
* otra es la **dirección de broadcast**

---

### Ejemplo con /26 explicado paso a paso

Máscara /26 en binario:

```
11111111.11111111.11111111.11000000
```

En decimal:

```
255.255.255.192
```

Bits para hosts:

```
6 bits
```

Hosts posibles:

```
2^6 − 2 = 62 hosts
```

Saltos entre subredes:

```
256 − 192 = 64
```

Subredes resultantes:

```
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
```

Visualización:

| Subred           | Primer host   | Último host   | Broadcast     |
| ---------------- | ------------- | ------------- | ------------- |
| 192.168.1.0/26   | 192.168.1.1   | 192.168.1.62  | 192.168.1.63  |
| 192.168.1.64/26  | 192.168.1.65  | 192.168.1.126 | 192.168.1.127 |
| 192.168.1.128/26 | 192.168.1.129 | 192.168.1.190 | 192.168.1.191 |
| 192.168.1.192/26 | 192.168.1.193 | 192.168.1.254 | 192.168.1.255 |

---

### Método rápido para calcular subredes

1. Identificar la máscara original.
2. Determinar cuántos bits se "piden prestados" para crear subredes.
3. Calcular el número de subredes:

```
2^n
```

4. Calcular hosts por subred:

```
2^h − 2
```

5. Calcular el salto entre subredes.

Este método permite diseñar redes con mayor organización y eficiencia.

---

### Conceptos importantes del direccionamiento IP

#### Dirección de red

Identifica la red completa.

Ejemplo:

```
192.168.1.0
```

#### Dirección de broadcast

Se utiliza para enviar tráfico a **todos los dispositivos de una red**.

Ejemplo:

```
192.168.1.255
```

#### Gateway

El **gateway** es el router que permite que una red local se comunique con otras redes.

Ejemplo típico:

```
192.168.1.1
```

---

### Rol del protocolo IP en Internet

El protocolo IP actúa como el **sistema de direccionamiento global de Internet**.

Gracias a IP:

* cada dispositivo puede ser identificado
* los routers pueden reenviar paquetes
* es posible conectar millones de redes diferentes

En otras palabras, **IP es el mecanismo que permite que Internet funcione como una red global de redes**.

Comprender el funcionamiento del direccionamiento IP es fundamental para entender temas posteriores como:

* subnetting avanzado
* routing
* NAT
* diseño de redes
* seguridad de red

## Capa 4. Transporte

### Función

Se encarga del transporte de datos **extremo a extremo** entre aplicaciones.

### Qué hace

* segmenta los datos,
* controla el flujo,
* maneja puertos,
* puede ofrecer entrega confiable,
* puede reordenar y verificar información.

### Unidad de datos

**Segmento** (o datagrama, según el protocolo)

### Ejemplos

* TCP,
* UDP,
* puertos como 80, 443, 53, 25.

### Ejemplo práctico

Cuando descargamos un archivo, TCP se encarga de que los datos lleguen completos y en orden.

### Problemas típicos

* puertos bloqueados,
* pérdida de segmentos,
* latencia,
* retransmisiones excesivas.

---

## Capa 5. Sesión

### Función

Administra el establecimiento, mantenimiento y cierre de sesiones de comunicación entre aplicaciones.

### Qué hace

* abre sesiones,
* mantiene el diálogo,
* coordina quién transmite y cuándo,
* puede gestionar puntos de recuperación.

### Ejemplos

* sesiones entre aplicaciones cliente-servidor,
* mecanismos de control de diálogo,
* algunas funciones presentes en protocolos de acceso remoto o comunicación persistente.

### Ejemplo práctico

En una videollamada o en una sesión remota, esta capa representa la idea de mantener la conversación activa entre dos extremos.

### Observación didáctica

En redes actuales, muchas de estas funciones no aparecen separadas de forma visible como en OSI, sino integradas en otros protocolos o aplicaciones.

---

## Capa 6. Presentación

### Función

Se ocupa del **formato de los datos** para que los sistemas puedan entenderlos.

### Qué hace

* traducción de formatos,
* codificación,
* compresión,
* cifrado y descifrado.

### Ejemplos

* ASCII y Unicode,
* JPEG,
* MPEG,
* compresión,
* cifrado TLS/SSL en ciertos análisis didácticos.

### Ejemplo práctico

Si un sistema guarda texto en un formato y otro lo recibe en otro entorno, esta capa representa la adaptación necesaria para que ambos entiendan la información.

---

## Capa 7. Aplicación

### Función

Es la capa más cercana al usuario. Ofrece servicios de red a las aplicaciones.

### Qué hace

* permite acceso a servicios de red,
* define reglas para aplicaciones de usuario,
* interactúa con software como navegadores, clientes de correo o herramientas de transferencia.

### Ejemplos

* HTTP,
* HTTPS,
* FTP,
* SMTP,
* DNS,
* DHCP,
* Telnet,
* SNMP.

### Ejemplo práctico

Cuando un navegador solicita una página web, trabaja con protocolos de la capa de aplicación.

### Problemas típicos

* servicio web caído,
* DNS que no resuelve,
* error de autenticación,
* configuración incorrecta del servidor.

---

## 6. Tabla resumen de las capas OSI

| Capa | Nombre       | Función principal                    | Ejemplo típico              |
| ---- | ------------ | ------------------------------------ | --------------------------- |
| 7    | Aplicación   | Servicios de red para el usuario     | HTTP, FTP, SMTP             |
| 6    | Presentación | Formato, cifrado, compresión         | UTF-8, JPEG, cifrado        |
| 5    | Sesión       | Apertura y mantenimiento de sesiones | Sesiones de comunicación    |
| 4    | Transporte   | Entrega extremo a extremo            | TCP, UDP                    |
| 3    | Red          | Direccionamiento y enrutamiento      | IP, routers                 |
| 2    | Enlace       | Tramas y comunicación local          | Ethernet, MAC, switches     |
| 1    | Física       | Transmisión de bits en el medio      | Cableado, conectores, señal |

---

## 7. Historia de TCP/IP

El modelo **TCP/IP** nació como una solución práctica para interconectar redes diferentes.

### 7.1 Contexto histórico

En los años 70, surgió la necesidad de conectar redes distintas, como ARPANET, redes de radio y redes satelitales. El problema era que cada una tenía interfaces, tamaños de paquetes, convenciones y velocidades diferentes.

### 7.2 Cerf y Kahn

**Vinton Cerf** y **Robert Kahn** lideraron el diseño de una arquitectura abierta de interconexión. La idea clave era que redes muy distintas pudieran comunicarse entre sí sin necesidad de que todas fueran iguales internamente.

### 7.3 Evolución

* Se desarrolló durante la década de 1970.
* Fue probado en escenarios reales entre redes heterogéneas.
* En 1983 ARPANET completó su transición a TCP/IP.
* Con el tiempo, TCP/IP se convirtió en la base técnica de Internet.

### 7.4 Por qué triunfó

TCP/IP se consolidó porque resolvía un problema real de ingeniería: **hacer funcionar la interconexión entre redes distintas**, de forma práctica, robusta y escalable.

---

## 8. El modelo TCP/IP

El modelo TCP/IP organiza la comunicación de red en **4 capas**.

### 8.1 Sus 4 capas

1. **Acceso a la red**
2. **Internet**
3. **Transporte**
4. **Aplicación**

A diferencia de OSI, este modelo no separa en capas independientes las funciones de sesión y presentación. En la práctica, esas responsabilidades suelen integrarse dentro de la capa de aplicación o en los propios protocolos y programas.

---

## 9. Las 4 capas del modelo TCP/IP, detalladas

## Capa 1. Acceso a la red

### Función

Agrupa lo relacionado con el acceso físico y lógico al medio de transmisión.

### Qué hace

* transmite tramas en la red local,
* interactúa con la tarjeta de red,
* define cómo se envían los datos por el medio,
* depende de la tecnología utilizada.

### Equivalencia aproximada en OSI

Corresponde, de forma aproximada, a las capas **Física** y **Enlace de datos** del modelo OSI.

### Ejemplos

* Ethernet,
* Wi-Fi,
* MAC,
* switches,
* controladores de red.

### Ejemplo práctico

Cuando una notebook se conecta por Wi-Fi al router de la casa, la comunicación inicial con el medio ocurre en esta capa.

---

## Capa 2. Internet

### Función

Se encarga del direccionamiento lógico y del envío de paquetes entre redes.

### Qué hace

* define direcciones IP,
* enruta paquetes,
* permite que los datos pasen por múltiples redes,
* trabaja con datagramas.

### Equivalencia aproximada en OSI

Corresponde a la **capa de Red** de OSI.

### Ejemplos

* IPv4,
* IPv6,
* ICMP,
* enrutamiento.

### Ejemplo práctico

Cuando un paquete sale de la red del liceo y llega a un servidor externo en Internet, esta capa hace posible ese recorrido.

---

## Capa 3. Transporte

### Función

Ofrece comunicación entre procesos de extremo a extremo.

### Qué hace

* usa puertos,
* segmenta datos,
* puede brindar confiabilidad,
* maneja control de errores y flujo,
* permite multiplexar varias aplicaciones.

### Equivalencia aproximada en OSI

Corresponde a la **capa de Transporte** de OSI.

### Ejemplos

* TCP,
* UDP.

### Ejemplo práctico

* **TCP**: navegación web, transferencia de archivos, correo.
* **UDP**: streaming, DNS, videollamadas, juegos en línea.

### Diferencia práctica

* **TCP** prioriza confiabilidad.
* **UDP** prioriza rapidez y menor sobrecarga.

---

## Capa 4. Aplicación

### Función

Reúne los protocolos que utilizan directamente las aplicaciones del usuario.

### Qué hace

* ofrece servicios de red a programas,
* incorpora funciones de formato, sesión y presentación cuando hace falta,
* permite la interacción final con el usuario.

### Equivalencia aproximada en OSI

Agrupa de forma aproximada las capas **Aplicación, Presentación y Sesión** del modelo OSI.

### Ejemplos

* HTTP/HTTPS,
* DNS,
* SMTP,
* POP3,
* IMAP,
* FTP,
* DHCP,
* SSH.

### Ejemplo práctico

Cuando una persona usa un navegador para entrar a un sitio web, los protocolos visibles para la aplicación trabajan aquí.

---

## 10. Tabla comparativa entre OSI y TCP/IP

| Aspecto                 | Modelo OSI                                                        | Modelo TCP/IP                                            |
| ----------------------- | ----------------------------------------------------------------- | -------------------------------------------------------- |
| Cantidad de capas       | 7 capas                                                           | 4 capas                                                  |
| Origen                  | Modelo de referencia impulsado por ISO                            | Arquitectura práctica surgida del desarrollo de Internet |
| Finalidad inicial       | Estandarizar funciones de comunicación entre sistemas abiertos    | Resolver la interconexión real entre redes heterogéneas  |
| Enfoque                 | Más conceptual y didáctico                                        | Más práctico e implementado                              |
| Uso actual              | Muy usado para enseñanza, diseño y diagnóstico                    | Base real de Internet y redes actuales                   |
| Capa de aplicación      | Solo capa 7                                                       | Reúne funciones de aplicación, presentación y sesión     |
| Capas inferiores        | Física y enlace separadas                                         | Se combinan en acceso a la red                           |
| Estandarización         | Modelo formal de referencia                                       | Basado en RFC y evolución de protocolos                  |
| Separación de funciones | Muy detallada                                                     | Más compacta                                             |
| Implementación real     | No se implementa como pila exacta en la mayoría de redes modernas | Sí, es la base operativa de Internet                     |

---

## 11. Correspondencia aproximada entre capas OSI y TCP/IP

| OSI             | TCP/IP          |
| --------------- | --------------- |
| Aplicación      | Aplicación      |
| Presentación    | Aplicación      |
| Sesión          | Aplicación      |
| Transporte      | Transporte      |
| Red             | Internet        |
| Enlace de datos | Acceso a la red |
| Física          | Acceso a la red |

---

## 12. Ejemplo completo de comunicación usando ambos modelos

Supongamos que un estudiante abre el navegador y entra a una página web.

### Mirándolo con OSI

* **Capa 7 Aplicación:** el navegador usa HTTP/HTTPS.
* **Capa 6 Presentación:** los datos pueden cifrarse y codificarse.
* **Capa 5 Sesión:** se mantiene la sesión entre cliente y servidor.
* **Capa 4 Transporte:** TCP divide y controla los segmentos.
* **Capa 3 Red:** IP enruta los paquetes.
* **Capa 2 Enlace:** Ethernet o Wi-Fi arma las tramas.
* **Capa 1 Física:** los bits viajan por cable o aire.

### Mirándolo con TCP/IP

* **Aplicación:** HTTP/HTTPS.
* **Transporte:** TCP.
* **Internet:** IP.
* **Acceso a la red:** Ethernet o Wi-Fi.

Este ejemplo muestra que ambos modelos describen el mismo proceso, pero con distinto nivel de detalle.

---

## 13. Ventajas didácticas del modelo OSI

Aunque TCP/IP es el que realmente domina las redes modernas, el modelo OSI sigue siendo muy útil porque:

* ordena mejor las funciones,
* facilita explicar dónde ocurre una falla,
* permite enseñar redes paso a paso,
* y ayuda a relacionar hardware, software y protocolos.

**Ejemplo didáctico:**

* si el cable está roto, pensamos en capa 1;
* si falla la MAC o el switch, pensamos en capa 2;
* si hay una IP mal configurada, pensamos en capa 3;
* si el puerto está cerrado, pensamos en capa 4;
* si la web no responde, pensamos en capa 7.

---

## 14. Conclusión

Los modelos **OSI** y **TCP/IP** fueron respuestas a una necesidad histórica: lograr que sistemas y redes diferentes pudieran comunicarse de manera ordenada y eficiente.

El modelo **OSI** aportó una estructura teórica clara de **7 capas**, ideal para comprender, enseñar y diagnosticar redes.

El modelo **TCP/IP**, en cambio, surgió como una solución práctica y se convirtió en la base real de Internet, con una estructura más compacta de **4 capas**.

Comprender ambos modelos es fundamental para cualquier estudiante de redes, porque permite:

* entender cómo viajan los datos,
* identificar fallas con mayor precisión,
* relacionar protocolos con funciones concretas,
* y construir una base sólida para temas posteriores como direccionamiento IP, switching, routing, servicios de red y seguridad.

---

## 15. Glosario básico

* **Protocolo:** conjunto de reglas que permite la comunicación entre dispositivos.
* **Interoperabilidad:** capacidad de sistemas diferentes para trabajar juntos.
* **Encapsulamiento:** proceso por el cual cada capa agrega información de control a los datos.
* **MAC:** dirección física de una interfaz de red.
* **IP:** dirección lógica usada para identificar equipos entre redes.
* **Segmento:** unidad de datos de transporte.
* **Paquete:** unidad de datos de red.
* **Trama:** unidad de datos de enlace.
* **Bit:** unidad mínima de información.

---
