## INTRODUCCIÓN A LOS EQUIPOS E INSTRUMENTOS DEL LABORATORIO 
Se muestra lo desarrollado en el laboratorio para conocer y manipular los equipos e instrumentos electrónicos básicos, además reconoce y verifica las características de medición eléctrica con el multímetro.

### Indice:

* [Materiales](#materiales)
* [Uso del multímetro y Fuente de alimentación](#uso-del-multímetro-y-fuente-de-alimentación)
   * [Promedio de errores absoluto y relativo](#promedio-de-errores-absoluto-y-relativo)
* [Uso del Generador de Señales y Osciloscopio](#uso-del-generador-de-señales) 
  * [Valores ajustados de la grafica](#valores-ajustados-de-la-grafica) 
  * [Valores medidos de la señal de entrada en un periodo](#valores-medidos-de-la-señal-de-entrada-en-un-periodo)


## Materiales
   * Fuente de alimentación regulable (HY3005BC )
   * Multímetro Digital (UT139C)
   * Generador de Señales (AFG1022)
   * Osciloscopio Digital (TBS 1000C Series)
   * Cable BNC Male-Male 
   * Par de cables cocodrilos
   * Punta de osciloscopio con conector BNC (Male)


## Uso del multímetro y Fuente de alimentación


### Promedio de errores absoluto y relativo:
<div style="text-align:center;">
	<table border="1" style="margin: 0 auto;">
		<tr>
            <td>N°</td>
			<td>Valor Real</td>
			<td>Valor medio</td>
            <td>Error Absoluto</td>
            <td>Error relativo</td>
		</tr>
		<tr>
			<td>1</td>
			<td>5.00 V</td>
            <td>5.00 V</td>
            <td>0.00 V</td>
            <td>0%</td>
		</tr>
		<tr>
			<td>2</td>
			<td>6.00 V</td>
            <td>5.99 V</td>
            <td>0.01 V</td>
            <td>0.16% - 0.0016</td>
		</tr>
		<tr>
			<td>3</td>
			<td>7.00 V</td>
            <td>6.98 V<d>
            <td>0.02 V</td>
            <td>0.286% - 0.00286</td>
		</tr>
        <tr>
			<td>4</td>
			<td>8.00 V</td>
            <td>7.98 V</td>
            <td>0.01 V</td>
            <td>0.125% - 0.00125</td>
		</tr>
        <tr>
			<td>5</td>
			<td>9.00 V</td>
            <td>8.98 V</td>
            <td>0.02 V</td>
            <td>0.2% - 0.002</td>
		</tr>
        <tr>
			<td>6</td>
			<td>10.00 V</td>
            <td>9.98 V</td>
            <td>0.02 V</td>
            <td>0.2% - 0.002</td>
		</tr>
        <tr>
			<td>7</td>
			<td>11.00 V</td>
            <td>10.98 V</td>
            <td>0.02 V</td>
            <td>0.18% - 0.0018</td>
		</tr>
        <tr>
			<td>8</td>
			<td>12.00 V</td>
            <td>11.98 V</td>
            <td>0.02 V</td>
            <td>0.16% - 0.0016 </td>
		</tr>
        <tr>
			<td>9</td>
			<td>13.00 V</td>
            <td>12.98 V</td>
            <td>0.02 V</td>
            <td>0.154% - 0.00154</td>
		</tr>
        <tr>
			<td>10</td>
			<td>14.00 V</td>
            <td>13.97 V</td>
            <td>0.03 V</td>
            <td>0.214% - 0.002143</td>
		</tr>
        <tr>
			<td colspan="3">Promedio</td>
			<td> 0.017 V</td>
            <td>0.1679% </td>
		</tr>      
	</table>
    </div>

## Uso del Generador de Señales y Osciloscopio

En este experimento la consigna era modificar los parámetros de posición horizontal, vertical y disparo para ajustar la visualización de la señal sinusoidal en el osciloscopio, la cual es obtenida mediante el generador de señales.

Función de los instrumentos usados en esta sesión:

- Generador de señales: Emite señales eléctricas de frecuencias y amplitudes específicas, esencial para probar, calibrar y experimentar con dispositivos electrónicos.

- Osciloscopio digital: Muestra visualmente la forma de onda de señales, permitiendo a los técnicos analizar la amplitud, frecuencia y otros parámetros, con capacidades avanzadas de procesamiento y almacenamiento de datos

Primero conectamos mediante un cable BNC a ambos dispositivos en el canal 1, posteriormente ajustamos el generador de señales en los siguientes parámetros:

 - Frecuencia: 10khz
 - Amplitud: 2,5V
 - Offset: 0V

![Descripción de la imagen](https://github.com/Dooncito/fundamentos-de-dise-o/blob/bf121f668855a956393db675a95042635661d115/Imagenes/img%20lab/Imagen%20de%20WhatsApp%202024-01-12%20a%20las%2017.00.42_4287fac1.jpg)

### Valores ajustados de la grafica

Se ajustaron los siguientes valores para sincronizar el voltaje en el osciloscopio:
- Escala de división vertical: 665V
- Amplitud máxima: 2.5kV
- Amplitud mínima: 0V
- Tiempo: 20μs
- Tasa de muestreo: 62,5MS/s
- Tiempo de registro: 20k ptos

Valores encontrados post-ajustes:
- Frecuencia: 10kHZ
- Voltaje pico: 1,01kV
- Variación de amplitud: 2,5kV

Al final nó se lograron obtener los valores solicitados, debido a que el valor de la escala de división vertical fue ajustado erroneamente en 665V.

### Valores medidos de la señal de entrada en un periodo 
