# Drink-Machine
Esta es la simulación del funcionamiento de una maquina dispensadora de bebidas y golosinas.
Soy un aprendiz de Python e implemento lo que voy aprendiendo en cosas que se me ocurren.

Una maquina de bebida y golosinas tiene los productos almacenados e identificados con una clave que a su vez tienen un valor.
Esto es lo que represento en el diciionario de mi codigo, una clave y un valor.

Para poder acceder a esos elementos de alguna manera de la misma forma que al presionar el codigo
que representa un producto en una maquina de verdad y  la maquina lo expulsa, en el codigo se expulsa el valor de la clave seleccionada.

Tambien tenemos en el codigo la variable credito que representa el momento que el usuario introduce dinero en la maquina, este dinero sera
almacenado en la variable credito.

Una vez guardado el valor de credito, el usuario procede a marcar la clave que representa un producto, que luego en nuestro codigo
usamos con el metodo get para acceder a su valor y asi poder comparar el valor del producto con el saldo abonada en credito y devolverle
al usuario su producto o dado el caso que el valor del producto sea superior al credito, se le indica al usuario que no es suficiente, esto
sucedera mientras se cumpla la condicion de que credito sea menor al valor del producto.

Si el valor de credito es mayor o igual al valor del producto o clave que selecciono el usuario, el programa simula entregar el producto
haciendo comparaciones de credito y valor del producto para indicarle el cambio que corresponda.
