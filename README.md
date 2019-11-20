# Banco Central de la República Argentina

Esta libreria hace más facil la obtencion de informacion de las variables macroeconomicas publicadas por el BCRA.

## Metodos

* ```BCRA.monetary_base(timeframe)``` : Base Monetaria - Promedio acumulado del mes (MM de $)
* ```BCRA.fx_reserves(timeframe)``` : Reservas Internacionales del BCRA (MM de USD)
* ```BCRA.monthly_inflation``` : Inflación mensual (variación en %)

## Timeframe

El ```(timeframe)``` es definido usando ```Y``` para años, ```W``` para semanas y ```M``` para meses.

* Ejemplo :
1. ```BCRA.monetary_base('1 Y')``` : Debera traer el historico de la base monetaria del ultimo año.
2. ```BCRA.monetary_base('1 M')``` : Debera traer el historico de la base monetaria del ultimo mes.
3. ```BCRA.monetary_base('1 W')``` : Debera traer el historico de la base monetaria de la ultima semana.


### Disclaimer

Este software y el autor del mismo no tienen ninguna relacion con el Banco Central de la República Argentina, el autor limita su responsabilidad a publicar dicho software para uso de terceros sin ningun fin comercial, si debido a alguna actualizacion en las politicas del BCRA este software violara algunos de los terminos de dicha entidad por favor notificar al autor para hacer las modificaciones necesarias o remover por completo este repositorio.

### Licencia MIT

Se concede permiso por la presente, libre de cargos, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software"), a utilizar el Software sin restricción, incluyendo sin limitación los derechos a usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar, y/o vender copias del Software, y a permitir a las personas a las que se les proporcione el Software a hacer lo mismo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "COMO ESTÁ", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A GARANTÍAS DE COMERCIALIZACIÓN, IDONEIDAD PARA UN PROPÓSITO PARTICULAR E INCUMPLIMIENTO. EN NINGÚN CASO LOS AUTORES O PROPIETARIOS DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O CUALQUIER OTRO MOTIVO, DERIVADAS DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O SU USO U OTRO TIPO DE ACCIONES EN EL SOFTWARE.