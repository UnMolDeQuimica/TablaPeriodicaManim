# TablaPeriodicaManim
Tabla periodica creada con Manim usada para facilitar el crear videos.


## Base de datos Elementos.csv

La base de datos Elementos.csv incluye amplia información de cada elemento, como número atómico, su masa atómica, su símbolo y mucho más. 

De momento solo estos datos son utilizados, pero en el futuro se espera poder ampliar la clase para añadir nuevos datos. 

## Clase Elemento

En el archivo elemento.py está la clase Elemento. Esta sirve para contruir un marco en el que se introduce cierta información similar a las celdas que constituyen una tabla periódica. 

De manera básica, el marco incluye el número atómico, la masa atómica y el símbolo del elemento. En futuras versiones se añadirá la posibilidad de incluir otros datos como número de protones, número de neutrones, número de electrones, valencias, etc.

Esta clase hereda de VGroup y se define en base a los siguientes parámetros:

- numero: El número atómico del elemento.
- masa: Masa atómica del elemento. Se toma directamente del número atómico. Queda pendiente hacer que esta selección se haga de manera opcional de tal manera que pueda introducir el valor que uno quiera manteniendo la posibilidad de que se elija automáticamente.
- simbolo: Símbolo del elemento. Pendiente igual que la masa.
- nombre: Nombre del elemento. Pendiente igual que la masa.
- color: Color del contorno del marco.
- opacidad: Opacidad del relleno del marco
- relleno: Color del relleno del marco. Se puede hacer uso de un gradiente de color.
- color_texto: Color del texto. Esto incluye el símbolo, el número y la masa. 
- gradiente: Número de "pasos" a usar en el gradiente. El valor que viene por defecto es aceptable en la mayoría de casos. 

## Clase TablaPeriodica

En el archivo Tabla.py se hace uso de la clase Elemento para poder crear todos los elementos por grupos de la tabla periódica y luego organizarlos por bloques (s, p, d y f)

Estos bloques, a su vez se organizan para poder crear la tabla periódica como clase heredada de VGroup. 

Posteriormente se reescala y se centra para poder tenerla visible. 

Al final del archivo se incluye un ejemplo haciendo uso de la clase Tabla y la clase Elemento para hacer destacar un elemento en concreto: el Iridio. 

Por el momento, y dado el gran número de elementos, el tiempo que tarda en renderizarse la tabla periódica es muy elevado, por lo que queda pendiente encontrar donde se puede hacer más eficiente.

## Modelo de Bohr. 

En el archivo Modelo_Bohr.py se hace uso de la clase Elemento para construir una simplificación del modelo de Bohr y con ello una animación. Su función es ejemplificar la utilidad de la clase Elemento. 

El código es algo viejo y creado cuando era un completo novato, así que puede mejorar mucho a fin de simplificar la creación de la animación con menos código. 

Además, quizá sería interesante hacer uso de la clase Sphere en la clase ThreeDScene para que los protones, neutrones y electrones tengan más forma de esfera que de punto. 

## Futuras actualizaciones.

En el futuro espero poder crear las siguientes ampliaciones: 

- [ ] Soporte para celdas unidad a fin de crear redes tridimensionales de manera sencilla. Quizá ver como otros paquetes de python gestionan esto pueda ser de ayuda.
- [ ] Soporte para creación de diagramas como diagramas de energía de reacción y similares. La clase graph puede ser muy útil.
- [ ] Soporte para la creación de moléculas en tres dimensiones. Actualmente no existe ningun paquete para manim capaz de simplificar esta tarea. Lo más parecido es chanim, que hace uso de chemfig para poder crear diagramas en 2 dimensiones, pero poder crear las estructuras tridimensionales y modificarlas desde el propio manim puede ser muy práctico. 
- [ ] Simplificación del sistema de la estructuración de la tabla periódica. Este sistema es dificultoso y costoso a nivel computacional. Además, no permite cambiar el tamaño de los marcos sin destruir la estructura de la tabla periódica. Encontrar una forma automatizar esta organización será útil para crear distintos diagramas.
- [ ] Simplificación de la selección de un único elemento en la tabla periódica. Quizá el uso de índices o un diccionario ayude a modificar un único elemento sin necesidad de crear una copia. 
