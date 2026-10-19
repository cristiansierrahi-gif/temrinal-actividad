-Diferencia entre una ruta absoluta y una relativa utilizando dos carpetas que acabas de crear.
 La ruta absoluta se emplea desde la carpeta raiz escribiendo toda la ubicacion donde se va a crear, modificar o borrar un archivo, mientras que la relativa se deebe estar dentro de ella para poder ejecutar la actividad deseada

-.control_interno no aparece en el listado normal y cómo manejar nombres que contienen espacios.
 El archivo se convierte en oculto por el punto que tiene antes del nombre, lo que impide su visualizacion con un ls normal. Los espacion se sustitullen por un guion abajo para indicicar que continua

-explica cuándo utilizarías > y cuándo >>.
 Se usa > cuando se va a escribir por primera vez el contenido de un archivo o se quiere remplazar la informacion del mismo mientras que cuando usamos >> agrega informacion a la ultima linea del archivo sin tener que modificar el contenido del archivo.

-demuestra que mover un archivo cambia su ubicación y conserva su contenido.
 Cuando se mueven archivos con la herramienta mv, se traslada la informacion que lleve dentro de la carpeta ya que esta agrupa todo lo que tenga adentro.

-explica cómo el mismo comando permite mover y renombrar archivos.
 Mv permite colocar renombrar un archivo y moverlo con la opcion de indicar la ruta a la que se va a enviar el archivo y colocando un nuevo nombre. Cuando solo se desea mover a una carpeta sin cambiar el nombre es indispensable colocar bien la ruta, porque en caso de no encontrar el nombre de la carpeta pasara a llamarse asi.

-explica la diferencia entre copiar un archivo y copiar una carpeta que contiene otras carpetas.
 La diferencia radica en que el el archivo actualiza su informacion al momento de hacer una copia a otra ya existente, mientras que con una carpeta se crea una nueva con el nombre asi ese mismo contenido ya exista

-explica por qué rmdir pudo eliminar una carpeta vacía, pero falló cuando contenía archivos.
 rmdir solo puede eliminar carpetas que no tengan contenido, si se desea eliminar carpetas con archivos se debe usar rm -r


