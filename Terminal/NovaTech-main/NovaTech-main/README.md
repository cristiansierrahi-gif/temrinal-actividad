# Misión por equipos: Rescate en NovaTech

Guía para coders. Léanla completa en equipo antes de escribir el primer comando.

## La historia

El desarrollador de NovaTech renunció sin avisar. Dejó el servidor hecho un desastre y un cliente esperando su sitio web. Nadie sabe quién es el cliente ni qué pidió.

Antes de irse, el desarrollador escondió pistas en el servidor. Su equipo tiene que encontrarlas, descubrir el pedido, rescatar los archivos y entregar el proyecto organizado. **Solo con la terminal.**

## Antes de empezar

### 1. Abran una terminal Bash

| Sistema | Qué abrir |
| --- | --- |
| Linux | La aplicación **Terminal** |
| macOS | La aplicación **Terminal** (búsquenla con Cmd + Espacio) |
| Windows | **Git Bash** (viene con Git). Si usan WSL, abran **Ubuntu** |

Escriban `pwd` y presionen Enter. Si aparece una ruta como `/home/usuario` o `/c/Users/usuario`, están listos.

### 2. Descarguen los dos scripts

En el gist que les compartió el facilitador hay dos archivos además de esta guía:

- `preparar_mision.sh`: crea el escenario de la misión.
- `verificar.sh`: revisa su trabajo y les dice cuántos puntos llevan.

Para descargarlos, usen el botón **Download ZIP** del gist o, en cada archivo, el botón **Raw** y luego Ctrl + S (Cmd + S en Mac). Guárdenlos en la carpeta **Descargas** (Downloads).

Si descargaron el ZIP, descomprímanlo y busquen los dos archivos `.sh` dentro de la carpeta que se crea.

### 3. Lleven los scripts a su carpeta personal

Este es su primer comando real. Desde la terminal:

```bash
cd ~/Downloads
ls
```

Deben ver `preparar_mision.sh` y `verificar.sh`. Muévanlos a su carpeta personal:

```bash
mv preparar_mision.sh verificar.sh ~
cd ~
ls
```

Si descomprimieron un ZIP, primero entren a la carpeta descomprimida con `cd` y luego hagan el `mv`.

### 4. Creen el escenario

Desde su carpeta personal, **una sola vez**:

```bash
bash preparar_mision.sh
```

Debe aparecer el mensaje `Escenario listo`. Se creó una carpeta llamada `novatech`. Ahí empieza todo.

> Si aparece `Ya existe la carpeta novatech`, es porque ya lo ejecutaron antes. No lo vuelvan a correr: avísenle al facilitador.

### 5. Verifiquen su avance cuando quieran

Desde cualquier carpeta pueden ejecutar:

```bash
bash ~/verificar.sh
```

El verificador muestra 14 chequeos. `[OK]` significa que está bien y `[--]` que falta algo. No les dice cómo resolverlo. Pueden ejecutarlo cuantas veces quieran.

## El equipo

Trabajan en un solo computador por equipo. Si tienen otro, úsenlo solo para consultar esta guía y las diapositivas.

| Rol | Qué hace |
| --- | --- |
| **Piloto** | Es el único que toca el teclado. Escribe los comandos que el equipo decide. |
| **Navegante** | Lee la misión en voz alta y dicta los pasos con palabras, nunca el comando exacto. |
| **Auditor** | Antes de cada `rm` o `mv`, pide un `pwd` y un `ls` para confirmar dónde están. Puede frenar al piloto. |
| **Escriba** | Lleva la bitácora: le dicta al piloto qué escribir en `bitacora.txt`. |

Los roles **rotan al terminar cada misión**. Con 3 integrantes, el navegante también es escriba. Con 5, hay dos auditores.

## Reglas

1. Prohibido el explorador de archivos, el mouse y los editores de texto. Solo terminal.
2. Todos deben ser pilotos al menos una vez.
3. Si borran algo por error, solo pueden recuperarlo desde su respaldo (Misión 3).
4. Pueden pedir dos pistas al facilitador. Cada una cuesta 1 punto.
5. No compartan respuestas con otros equipos.

## Cómo escribir en la bitácora

La bitácora es un archivo de texto donde anotan todo lo que descubren. Se escribe con `echo`:

```bash
echo "Equipo Los Pingüinos: Ana, Luis, Sara" >> bitacora.txt
```

- `>>` **agrega** una línea al final del archivo. Úsenlo siempre.
- `>` **borra todo** el contenido y escribe solo la línea nueva. Cuidado.

Para ver la bitácora: `cat bitacora.txt`.

## Misiones

Hagan las misiones en orden. Cada una desbloquea la siguiente.

### Misión 1 — Reconocimiento

Antes de tocar nada, exploren el servidor y anoten lo que encuentran.

1. Entren a la carpeta `novatech` y lean `LEEME.txt`.
2. Creen `bitacora.txt` dentro de `novatech`. La primera línea es el nombre del equipo y sus integrantes.
3. Respondan en la bitácora, una línea por respuesta:
   1. ¿Cuál es la ruta absoluta de la carpeta `novatech`?
   2. ¿Cuántas carpetas hay directamente dentro de `novatech`?
   3. ¿Cuántos archivos `.tmp` hay en `servidor_viejo`?
   4. ¿Qué dice el archivo `notas_dev.txt`?
4. Muéstrenle la bitácora al facilitador con `cat`.

**Rotación de roles.**

### Misión 2 — Tras las pistas

El desarrollador escondió una cadena de pistas que lleva al pedido del cliente.

1. Encuentren la primera pista en `servidor_viejo`. No aparece con un `ls` normal.
2. Sigan cada pista hasta el mensaje del cliente. Cuidado: hay pistas falsas.
3. Anoten en la bitácora:
   1. El nombre del cliente.
   2. La ruta absoluta del archivo donde encontraron el pedido.
   3. La palabra clave.
4. Escriban en la bitácora los requisitos del cliente con sus propias palabras. Los van a necesitar en las misiones 4 y 5.

**Rotación de roles.**

### Misión 3 — Respaldo

Un buen equipo de rescate nunca toca nada sin respaldo.

1. Hagan una copia completa de `servidor_viejo` llamada `respaldo_servidor`, dentro de `novatech`.
2. Comprueben que el respaldo incluye la pista oculta.
3. El auditor explica al equipo por qué la copia de una carpeta necesita una opción especial y qué pasaría sin ella. Anótenlo en la bitácora.

Desde aquí, si borran algo por error, lo recuperan copiándolo desde `respaldo_servidor`.

**Rotación de roles.**

### Misión 4 — Construir el proyecto

Con los requisitos de la Misión 2, armen la estructura que pidió el cliente.

1. Creen la carpeta del proyecto con el nombre exacto que pidió el cliente.
2. Creen todas las subcarpetas que piden los requisitos. Reto opcional: háganlo con el menor número de comandos posible.
3. Muevan cada archivo de `servidor_viejo` a su carpeta correcta. No copien: muevan.
4. Renombren los archivos que el cliente quiere con otro nombre.
5. Creen la página nueva que pidió el cliente.
6. Revisen el resultado con `ls -la` en cada carpeta.

**Rotación de roles.**

### Misión 5 — Limpieza y entrega

1. Eliminen todos los archivos `.tmp`, los `.log` y la carpeta `copia_vieja`.
2. Revisen que `servidor_viejo` quedó vacío, incluidos los archivos ocultos. Si queda algo útil, muévanlo; si no, eliminen la carpeta completa.
3. Creen `README.md` dentro del proyecto con el nombre del equipo, el nombre del cliente y una línea por cada integrante.
4. Creen el `.gitignore` que pidió el cliente.
5. Ejecuten `bash ~/verificar.sh` y corrijan hasta lograr **14 de 14**.
6. Llamen al facilitador y muéstrenle el verificador y la bitácora completa.

**Rotación de roles.**

### Misión 6 — Contraataque

Ahora su equipo diseña un reto para otro equipo y resuelve el que le toque.

1. En su carpeta personal, creen una carpeta llamada `reto_` seguida del nombre del equipo (por ejemplo, `reto_pinguinos`).
2. Dentro, construyan un laberinto que cumpla todo esto:
   - Al menos 3 niveles de carpetas.
   - Al menos 4 pistas encadenadas, escritas con `echo`.
   - Al menos 2 pistas ocultas.
   - Al menos 2 pistas falsas.
   - Un archivo largo con el mensaje importante al final.
   - Un tesoro final con una palabra clave inventada por el equipo.
3. Creen `INICIO.txt` en la raíz del reto con la primera instrucción.
4. El facilitador les dirá a qué computador moverse.
5. Resuelvan el reto que encuentren y escriban la palabra clave en un archivo `resuelto.txt` dentro de ese reto, con el nombre de su equipo.
6. Vuelvan a su computador y revisen si su reto fue resuelto.

## Puntuación

| Componente | Puntos |
| --- | --- |
| Verificador (`verificar.sh`) | 14 |
| Bitácora completa y correcta (misiones 1 a 3) | 6 |
| Su reto de la Misión 6 cumple las 6 condiciones | 6 |
| Resolver el reto de otro equipo | 3 |
| Todos fueron pilotos | 1 |
| Cada pista pedida al facilitador | −1 |

Máximo: **30 puntos**. En caso de empate, gana el equipo que llegó primero a 14 de 14 en el verificador.

## Comandos que van a necesitar

| Comando | Qué hace |
| --- | --- |
| `pwd` | Muestra la ubicación actual |
| `ls -l` | Lista detallada (tamaño, fecha, tipo) |
| `ls -a` | Incluye archivos ocultos (los que empiezan con punto) |
| `cd carpeta` | Entra en una carpeta (`cd ..` sube un nivel, `cd ~` va a la carpeta personal) |
| `clear` | Limpia la terminal |
| `touch archivo` | Crea un archivo vacío |
| `mkdir carpeta` | Crea una carpeta (`mkdir -p a/b/c` crea toda la ruta) |
| `cp origen destino` | Copia un archivo |
| `cp -r carpeta destino` | Copia una carpeta completa |
| `mv origen destino` | Mueve o renombra |
| `rm archivo` | Elimina un archivo (no hay papelera) |
| `rm -r carpeta` | Elimina una carpeta completa (no hay papelera) |
| `cat archivo` | Muestra todo el contenido de un archivo |
| `echo "texto" >> archivo` | Agrega una línea al final de un archivo |

**Trucos:** la tecla **Tab** autocompleta nombres. La **flecha arriba** repite comandos anteriores. El asterisco agrupa archivos: `*.txt` significa "todos los archivos que terminan en .txt".

## Si algo falla

| Mensaje | Qué significa | Qué hacer |
| --- | --- | --- |
| `No such file or directory` | El archivo o carpeta no está donde están parados | `pwd` y `ls` para ubicarse |
| `cp: -r not specified; omitting directory` | Intentaron copiar una carpeta sin `-r` | Agreguen `-r` |
| `rm: cannot remove 'x': Is a directory` | Intentaron borrar una carpeta sin `-r` | Revisen con el auditor y agreguen `-r` |
| `bash: preparar_mision.sh: No such file...` | El script no está en la carpeta actual | `cd ~` y `ls`; repitan el paso 3 |
| `Ya existe la carpeta novatech` | El escenario ya estaba creado | No lo ejecuten de nuevo; avisen al facilitador |
| La terminal no responde y no vuelve el `$` | Un comando quedó esperando | Presionen Ctrl + C |

¡Mucha suerte, equipo de rescate!
