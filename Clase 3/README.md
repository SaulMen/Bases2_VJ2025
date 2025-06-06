## Clase 3

## RESPALDO Y RECUPERACIÓN
_____

## **INDICE**
- [**Backup Compelto**](#backup-completo)
- [**Restauración Backup Completo**](#restauracion-backup-completo)
- [**Backup Incremental**](#backup-incremental)
______

A continuación se le presentan los comandos utilizados para la creación de backup completos e incrementales desde la terminal y cómo realizarlo paso a paso

### Backup Completo
Una vez creada nuestra base de datos con registros, funciones o procedimientos en sus tablas procedemos a realizar una copia de seguridad por medio del siguiente comando:

```bash
mysqldump -u usuario -p nombre_de_la_BBDD > archivo_salida.sql
```
>Nota: Luego de dar ENTER nos pedirá que ingresemos nuestra contraseña y se generará el archivo.

### Restauración Backup Completo
Una vez creado nuestro archivo de restauración podemos restaurar nuestra base de datos en caso de algún problema ocasiondo en nuestra base de datos que ocasiona su respectiva perdida.

Sin embargo al generar nuestro archivo de `backup_completo.sql` este se guarda con la codificación `UTF-16` y al ejecutar el comando para restaurar tendremos problemas con la incopatibilidad de caracteres, por lo que tenemos dos opciones para cambiar la codificación:

1. La primera es utilizando VSCode en la parte inferior derecha y seleccionar el encoding `UTF-8 With BOM`

2. La segunda opción es ubicarnos en la carpeta del archivo y cambiar su encoding desde la terminal con el siguiente comando:

```bash
Get-Content archivo-utf-16.sql -Encoding Unicode | Set-Content -Encoding UTF8 nuevo-archivo-utf-8.sql
```

Una vez cambiado el encoding del archivo procedemos a restaurar la base de datos por medio del siguiente comando:

```bash
mysql -u tu_usuario -p ejemplo2 < backup_completo.sql
```
>Nota: La ejecución de este comando debe de realizarse desde el CMD y no en PowerShell.
_____

### Backup Incremental
Una vez creada nuestra base de datos con registros, funciones o procedimientos en sus tablas procedemos a realizar una copia de seguridad por medio del siguiente comando:

```bash
mysqldump -u usuario -p nombre_de_la_BBDD > archivo_salida.sql
```
>Nota: Luego de dar ENTER nos pedirá que ingresemos nuestra contraseña y se generará el archivo.


Sin embargo, en MySQL debemos de crear las backups incremental por medio de BIN-LOGS. Por lo tanto, para activar esta opción y que nos permita acceder a los LOGS debemos de hacer lo siguiente:

1. Ir a nuestro archivo my.ini, ubicado por lo general en `C:\ProgramData\MySQL\MySQL Server 8.0\my.ini`, dentro de este archivo verificamos para las siguientes lineas no estén comentadas:
```bash
    log-bin="USUARIO-bin"

    server-id=1
```

2. Luego en la terminal ingresamos el siguiente comando para liberar cualquier bloqueo de tablas que la sesión actual de MySQL tenga:
```bash
mysql -u root -p -e "UNLOCK TABLES;"
``` 

3. Luego ingresamos este comando para mostrar una lista de los archivos de registro binario (binary logs o binlogs) que el servidor MySQL ha generado:
```bash
mysql -u root -p -e "SHOW BINARY LOGS;"
``` 
Identificamos el nombre del último archivo binario y su ubicación, por lo regular está dentro de la carpeta `Data` donde se encuentra el archivo `my.ini`. Entonces al ingresar a la carpeta al final podemos encontrar los BIN-LOGS. 

4. Una vez encontrado el archivo guardamos la ubicación, por lo regular similar a este: 
```bash
"C:/ProgramData/MySQL/MySQL Server 8.0/Data/Usuario-bin.000xxx"
```

5. Luego ejecutamos este comando:
```bash
mysql -u root -p -e "FLUSH TABLES WITH READ LOCK; SHOW MASTER STATUS;"
```
Este comando nos dará el nombre del último BIN-LOG con los datos modificados y su posición exacta del BIN-LOG, esta posición será nuestra `posición inicial` para la creación del backup incremental.

6. Por lo tanto podemos seguir añadiendo registros, funciones o procedimientos en nuestra base de datos. Una vez tengas más información dentro de nuestra base de datos procedemos a ejecutar nuevamente el siguiente comando:
```bash
mysql -u root -p -e "FLUSH TABLES WITH READ LOCK; SHOW MASTER STATUS;"
```
Está vez para conocer la nueva posición de nuestro BIN-LOG, la cual será nuestra posición final.

Por lo tanto tenemos lo siguiente:
- La ubicación de nuestro BIN-LOG
- La posición inicial
- La posición final

Por lo que podemos crear nuestro archivo backup incremental 2, con el siguiente comando:
```bash
mysqlbinlog --start-position=xxx --stop-position=xxx "ubicacion_del_archivo-BIN-LOG.xxx" > backup_incremental.sql
```
>Nota: Para crear más backups incremental, se repite el proceso. Lo necesario es conocer las dos posiciones de nuestro BIN-LOG

### Restauración Backup Incremental
Una vez creado nuestro archivo de restauración podemos restaurar nuestra base de datos incrementalmente en caso de algún problema ocasiondo en nuestra base de datos que ocasiona su respectiva perdida.

Sin embargo al generar nuestros archivos incrementales se guardan con la codificación `UTF-16` por lo que debemos guardarlos con la codificación `UTF-8 With BOM` por lo que se repite el proceso explicado anteriormente.

Una vez cambiado el encoding del archivo procedemos a restaurar la base de datos por medio del siguiente comando:

```bash
mysql -u tu_usuario -p ejemplo2 < incremental1.sql
```

Luego nuestro siguiente archivo de recuperación y así sucesivamente:
```bash
mysql -u tu_usuario -p ejemplo2 < incremental2.sql
```
>Nota: La ejecución de este comando debe de realizarse desde el CMD y no en PowerShell.


