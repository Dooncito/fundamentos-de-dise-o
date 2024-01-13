## INTRODUCCIÓN A LOS EQUIPOS E INSTRUMENTOS DEL LABORATORIO 
Se muestra lo desarrollado en el laboratorio para conocer y manipular los equipos e instrumentos electrónicos básicos, además reconoce y verifica las características de medición eléctrica con el multímetro.

### Indice:

* [Materiales](#materiales)
* [Uso del multímetro y Fuente de alimentación](#uso-del-multímetro-y-fuente-de-alimentación)
   * [Promedio de errores absoluto y relativo](#promedio-de-errores-absoluto-y-relativo)
   * [Fotos de los datos](#fotos-de-todos-los-datos)
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
Para poder obtener nuestra recopilación de datos, comenzamos teniendo a nuestra disposición la Fuente de alimentación y un multímetro, además como implemento adicional unos par de cables cocodrilos. 
Empezamos conectando a la corriente la Fuente de alimentación y encendiéndola; con el multímetro colocamos sus cable correspondiente en tierra y voltaje, además lo ponemos en la opción voltaje(AC-DC). 
Ahora con la fuente de alimentación, nos está pidiendo configurarlo a 5V y 1A, entonces tenemos que regular el voltaje y la corriente con las medidas indicadas. Para continuar, con la ayuda de los cables de cocodrilos lo unimos con los cables del multímetro y el otro extremo lo colamos en las salidas(-/+) de la fuente. 
Ya teniendo todo encendido y conectado, al presionar el botón Output que habilita la tensión de salida mostrándonos en el multímetro su valor medido. Para concluir, hicimos 10 mediciones desde el voltaje 5V hasta 14V para después calcular sus error absoluto y error relativo del multímetro .

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
		    
### Fotos de todos los datos

| <!-- -->      | <!-- -->        | 
|:-------------:|:---------------:|
|![Dato1](https://github.com/Dooncito/fundamentos-de-dise-o/blob/703f38db74b7585dd59aa5495e9ef399025d9ff2/Imagenes/img%20lab/Imagen%20de%20WhatsApp%202024-01-12%20a%20las%2015.08.02_085b0f56.jpg)       |  ![dato2](https://github.com/Dooncito/fundamentos-de-dise-o/blob/703f38db74b7585dd59aa5495e9ef399025d9ff2/Imagenes/img%20lab/Imagen%20de%20WhatsApp%202024-01-12%20a%20las%2015.08.01_77c8b35a.jpg)   |
| Dato#1 5V       | Dato#2 6V       | 
|![Dato3](https://github.com/Dooncito/fundamentos-de-dise-o/blob/0045c4cc9771b9c136ec8f0d969115dec8c548cd/Imagenes/img%20lab/Imagen%20de%20WhatsApp%202024-01-12%20a%20las%2015.08.01_9f1547ca.jpg)       |  ![dato4](https://github.com/Dooncito/fundamentos-de-dise-o/blob/0045c4cc9771b9c136ec8f0d969115dec8c548cd/Imagenes/img%20lab/Imagen%20de%20WhatsApp%202024-01-12%20a%20las%2015.07.51_6c178c32.jpg)   |
| Dato#3 7V       | Dato#4 8V       | 
|![Dato5](https://github.com/Dooncito/fundamentos-de-dise-o/blob/a9c7ba4ec8b01229b20789a3b9dd1299347f49f6/Imagenes/img%20lab/Imagen%20de%20WhatsApp%202024-01-12%20a%20las%2015.07.44_c568c30e.jpg)       |  ![dato6](https://github.com/Dooncito/fundamentos-de-dise-o/blob/a9c7ba4ec8b01229b20789a3b9dd1299347f49f6/Imagenes/img%20lab/Imagen%20de%20WhatsApp%202024-01-12%20a%20las%2015.07.36_8357af24.jpg)   |
| Dato#5 9V       | Dato#6 10V       | 
|![Dato7](https://github.com/Dooncito/fundamentos-de-dise-o/blob/a9c7ba4ec8b01229b20789a3b9dd1299347f49f6/Imagenes/img%20lab/Imagen%20de%20WhatsApp%202024-01-12%20a%20las%2015.07.36_2623ec21.jpg)      |  ![dato8](https://github.com/Dooncito/fundamentos-de-dise-o/blob/a9c7ba4ec8b01229b20789a3b9dd1299347f49f6/Imagenes/img%20lab/Imagen%20de%20WhatsApp%202024-01-12%20a%20las%2015.07.36_1ca4a2c4.jpg)   |
| Dato#7 11V       | Dato#8 12V       | 
|![Dato9](https://github.com/Dooncito/fundamentos-de-dise-o/blob/a9c7ba4ec8b01229b20789a3b9dd1299347f49f6/Imagenes/img%20lab/Imagen%20de%20WhatsApp%202024-01-12%20a%20las%2015.07.35_3694b7b8.jpg)       |  ![dato10](https://github.com/Dooncito/fundamentos-de-dise-o/blob/a9c7ba4ec8b01229b20789a3b9dd1299347f49f6/Imagenes/img%20lab/Imagen%20de%20WhatsApp%202024-01-12%20a%20las%2015.08.03_abec248e.jpg)   |
| Dato#9 13V       | Dato#10 14V       | 	    


## Uso del Generador de Señales y Osciloscopio
En este procedimiento nos pide ajustar los valores para visualizar la grafica deseada. Conctando el generador de Señales con el Osciloscopio, los dos estanfo en el cañal 1 conectados por un cable BNC(Male-Male). Controlando la posicion vertical, la horizontal y el disparo.Así mismo, visualizando la señal sinusoida, haciendo uso los cursores y monstrar en el Osciloscopio las mediciones del Amplitud y Periodo que nos da la señal.  


### Valores ajustados de la grafica

### Valores medidos de la señal de entrada en un periodo 
