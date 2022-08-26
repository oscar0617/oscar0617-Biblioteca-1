# Libreria #1 Números complejos:

_En esta libreria encontraremos las siguientes operaciones en los números complejos:_
1. Suma.
2. Producto.
3. Resta.
4. División.
5. Módulo.
6. Conjugado.
7. Conversiones entre representaciones polares y cartesianas.
8. La fase de un número complejo.
### Pre-requisitos
_Para poder correr nuestra libreria necesitaremos un iDLE cualquiera de python._\
_Podemos instalar pyhton desde su sitio oficial totalmente gratis._

### Ejemplos
_A continuación encontraremos el ejemplo de la función suma para los numeros complejos:_
```
def sumaComplejos(numero1, numero2):    
    res = ()
    sumaReal = numero1[0] + numero2[0]
    sumaImaginaria = numero1[1] + numero2[1]
    res = (sumaReal, sumaImaginaria)
    return (res)
```
_¿Cómo podemos verificar estos resultados?_
_Sencillo, debemos recordar que la suma de números complejos es directa, es decir, sumamos la parte real de cada número y su parte compleja o imaginaria._ \
_En la siguientes lineas de codigo podemos observar ese algoritmo:_
```
sumaReal = numero1[0] + numero2[0]
sumaImaginaria = numero1[1] + numero2[1]
```
_Posteriormente, estas dos variables (*sumaReal* y *sumaImaginaria*) se almacenan en una tupla nombrada *res*._
### Pruebas en codigo
_Al finalizar el codigo podemos encontrar estas lineas de codigo:_
```
prettyprinting(sumaComplejos(c1, c2))
prettyprinting(restaComplejos(c1, c2))
prettyprinting(multiplicacionComplejos(c1, c2))
prettyprinting(divisionComplejos(c1, c2))
prettyprinting(moduloComplejo(c1))
prettyprinting(conjugadoComplejo(c1))
prettyPrintingPolar(rectangular_polar(c1))
prettyprinting(polar_rectangular(c1))
prettyPrintingPolar(faseComplejo(c1))
```
_Estas lineas prueban una a una cada función con un uno o dos numeros complejos, dependiendo la función a probar._
_A continuacion veremos que nos imprimen estas lineas de codigo con las variables ```c1, c2 = (1,-1), (1,0) ```:_
```
2-1i
0-1i
1-1i
1.0-1.0i
1.414
1+1i
1.41,-0.79θ
0.54-0.84i
-0.7854 θ
```
## ¿Como lo construimos?
* [Pycharm](https://www.jetbrains.com/es-es/pycharm/) - El framework web usado

## Autor
* **Oscar Lesmes** - *Libreria completa* - [GitHub](https://github.com/villanuevand)

