# <p align = "center"> 🖼Estado del arte🖌 </p>
Realizar una investigación de artículos científicos provenientes de fuentes verificadas que presenten resultados experimentales basados en hechos conocidos o nuevos conocimientos. Además, llevar a cabo la búsqueda de equipos o dispositivos existentes en el mercado y patentes que cumplan funciones relacionadas con la problemática. Para concluir, la elaboración de una tabla que contenga los requerimientos funcionales y no funcionales, para solucionar el problema.  
### Contenido:
1. [Contexto Científico](#contexto-científico🧪)

   1.1 [Artículo #1](#artículo-1-indoor-air-quality-monitoring-systems-based-on-internet-of-things-a-systematic-review-sistemas-de-monitoreo-de-la-calidad-del-aire-interior-basados-​​en-internet-de-las-cosas-una-revisión-sistemática)

   1.2 [Artículo #2](#artículo-2-continuous-monitoring-of-indoor-environmental-quality-using-an-arduino-based-data-acquisition-system)

   1.3 [Artículo #3](#artículo-3-a-systematic-review-and-meta-analysis-of-field-studies-of-portable-air-cleaners-performance-user-behavior-and-by-product-emissions)

   1.4 [Artículo #4](#articulo-4-long-term-exposure-to-pm-and-all-cause-and-cause-specific-mortality-a-systematic-review-and-meta-analysisexposición-a-largo-plazo-a-pm-y-mortalidad-por-todas-las-causas-y-por-causas-específicas-una-revisión-sistemática-y-un-metanálisis)
3. [Contexto Comercial](#contexto-comercial-💻)   
    
    2.1 [Equipos o Dispositivos en el mercado](#dispositivos-en-el-mercado-o-equipos)
    
    2.1 [Patentes](#patentes)
4. [Tabla de Requerimiento](#requerimientos)
5. [Bibliografía](#bibliografía)

## CONTEXTO CIENTÍFICO🧪

### Artículo 1. Indoor Air Quality Monitoring Systems Based on Internet of Things: A Systematic Review                                         (Sistemas de monitoreo de la calidad del aire interior basados ​​en Internet de las cosas: una revisión sistemática)  

El siguiente artículo es una revisión sistemática que proporciona información del estado actual de los sistemas de monitoreo de la calidad del aire interior (IAQ) basados en LOT y su principal objetivo es, mediante la información de estudios realizados en diversos países, el proporcionar una visión general del campo de monitoreo de la calidad del aire interior y de paso resaltar las dificultades técnicas de la actualidad para futuras investigaciones. 

<p align="center"><strong>Figura 1:</strong></p>
<p align="center">
  <img src="https://github.com/Dooncito/fundamentos-de-dise-o/assets/156021864/ed595feb-14ff-4eb0-9b71-bb6c57cfbee5" width="500" style="margin: auto;">
</p>

#### Resultados

De los 40 estudios realizados, la temperatura, la humedad, el CO 2 , el CO, las PM 10 , las PM 2,5 y los VOC son los parámetros de IAQ monitoreados más comúnmente. Donde 26 utilizaron 33 tipos de sensores dedicados para la detección de IAQ.
El sensor más utilizado fueron los censores de la serie MQ, utilizados para la detección de de múltiples tipos de gases, sin embargo, la principal desventaja de la serie MQ es que requieren una calibración de campo, además de que las especificaciones de precisión no están detalladas en las hojas de datos del fabricante
Solo dos estudios utilizaron placas de sensores todo en uno, cuya ventaja es que pueden medir múltiples parámetros con sondas de sensor precalibradas incorporadas, sin embargo, su elevado costo limita bastante su accesibilidad y son inadecuados para la implementación en tiempo real.
Arduino Uno y Raspberry Pi fueron los microprocesadores(MCU) más utilizados como puertas de enlace para sus monitoreos.
26 estudios prefieren almacenar sus datos de IAQ en servidores de la nube debido a su fácil accesos a las actualizaciones desde cualquier lugar y momento, convirtiéndola así en la fuente de almacenamiento de datos con mayor comodidad y uso.
Los métodos de consulta de datos preferidos son mediante app móviles y páginas webs.
Las fuentes de energía preferidas para ejecutar monitoreos de IAQ fueron las fuentes de alimentación, seguido del uso de baterías externas. Las células solares también fueron utilizadas como fuentes de energía para monitoreos de IAQ, mas solo se implementaron en dos estudios.

**Referencia: https://www.mdpi.com/1660-4601/17/14/4942**

### Artículo 2. Continuous monitoring of indoor environmental quality using an Arduino-based data acquisition system
Describe el desarrollo de un sistema de monitoreo de calidad del aire que es a la vez asequible y portátil, basado en la plataforma Arduino. Este sistema utiliza un sensor fotoacústico para medir las concentraciones de PM2.5 y PM10 en el aire. Tiene una batería recargable y una unidad de almacenamiento,es un dispositivo autónomo que puede ser llevado a cualquier lugar. El sistema fue probado en un laboratorio y se ha demostrado que es capaz de medir las concentraciones de PM2.5 y PM10 con una precisión del 95%. Tiene un bajo costo, por lo tanto es accesible para muchos usuarios, es una herramienta prometedora para el monitoreo de calidad del aire en interiores.

<p align="center"><strong>Figura 2:</strong></p>
<p align="center">
  <img src="https://github.com/Dooncito/fundamentos-de-dise-o/blob/main/Imagenes/img3/metaFun.jpg" width="500" style="margin: auto;">
</p>

**Referencia: https://www.sciencedirect.com/science/article/abs/pii/S2352710218301025**

### Artículo 3. A systematic review and meta-analysis of field studies of portable air cleaners: Performance, user behavior, and by-product emissions
El artículo aborda la eficacia de los purificadores de aire portátiles (PAC) en la reducción de la contaminación del aire en espacios interiores. Estos dispositivos emplean diversos métodos, como filtros u otras tecnologías, para eliminar contaminantes como partículas finas, gases y elementos biológicos del aire.

Se llevaron a cabo estudios en varias partes del mundo, con un enfoque particular en América del Norte, Asia y Europa. Los resultados de esta revisión indican que los PAC pueden ser eficaces para disminuir la contaminación del aire en entornos cerrados. Sin embargo, la eficiencia varía dependiendo del tipo de contaminante, la tecnología de limpieza utilizada y el comportamiento del usuario.

Se observa que los PAC son más efectivos para reducir las partículas finas en comparación con los contaminantes gaseosos o biológicos. Entre las tecnologías de limpieza más eficaces para las partículas finas se encuentran los filtros HEPA y los filtros de carbón activado. Poseen el potencial de mejorar la calidad del aire en ambientes interiores. No obstante, se destaca la necesidad de realizar más investigaciones para comprender a fondo su eficacia y seguridad.

<p align="center"><strong>Figura 3:</strong></p>
<p align="center">
  <img src="https://github.com/Dooncito/fundamentos-de-dise-o/blob/main/Imagenes/img3/metaFun2.jpg" width="500" style="margin: auto;">
</p>

<p align="center"><strong>Figura 4:</strong></p>
<p align="center">
  <img src="https://github.com/Dooncito/fundamentos-de-dise-o/blob/main/Imagenes/img3/imgMeta.jpg" width="500" style="margin: auto;">
</p>

**Referencia: https://www.sciencedirect.com/science/article/abs/pii/S0048969723074156**

### Articulo 4. Long-term exposure to PM and all-cause and cause-specific mortality: A systematic review and meta-analysis(Exposición a largo plazo a PM y mortalidad por todas las causas y por causas específicas: una revisión sistemática y un metanálisis)

En base a la revisión sistemática, se evidencia que las partículas PM2.5 representan un riesgo significativo para la salud, con asociaciones claras a mayor mortalidad por diversas causas, incluyendo enfermedades cardiovasculares, respiratorias y cáncer de pulmón. Los riesgos relativos combinados revelan un aumento de 1,08 en la mortalidad por causas naturales por cada incremento de 10 µg/m3 de PM2.5, y 1,04 por cada 10 µg/m3 de PM10.

A pesar de un aumento sustancial en la base de evidencia, la escasez de estudios en países de ingresos bajos y medianos destaca la necesidad de más investigación. Las asociaciones persistentes con PM2.5, incluso por debajo de los niveles actuales de exposición recomendados por la OMS, subrayan la importancia crítica de abordar la contaminación del aire para salvaguardar la salud pública.
<p align="center"><strong>Figura 5:</strong></p>
<p align="center">
  <img src="https://github.com/Dooncito/fundamentos-de-dise-o/assets/156021864/62a045ea-9e9c-4ad5-9936-046653ea3dc7" width="500" style="margin: auto;">
</p>


**Referencia: https://pubmed.ncbi.nlm.nih.gov/32703584/**

## CONTEXTO COMERCIAL 💻
### **Dispositivos en el mercado o equipos:**
#### Producto #1:
### <p align="center">Medidor de CO2 PCE-AQD 50-ICA</p>
**Finalidad:** Mide temperatura, humedad, presión atmosférica, CO2
<p align="center"><strong>Figura 6:</strong></p>
<p align="center">
  <img src="https://github.com/Dooncito/fundamentos-de-dise-o/blob/b9b25c8712343dd760b5010f12b208be1002879d/Imagenes/img_comercial_y_cienti/mercado1.jpg" width="300" style="margin: auto;">
</p>

**Descripción:** El medidor de CO2 integra diferentes sensores. Entre ellos está un sensor que mide el dióxido de carbono hasta 40 000 ppm, un sensor de temperatura para un rango entre 0 y +50 ºC, un sensor que mide la humedad del aire entre 0 y 100 % H.r. Gracias a los diferentes sensores que integra el medidor de CO2 puede usarlo en múltiples aplicaciones. Puede visualizar los valores en la pantalla digital del medidor de CO2. Además, incluye una valoración Bien / Regular / Mal de la concentración de CO2 del aire. La pantalla digital de bajo consumo permite aumentar la autonomía del acumulador del medidor de CO2.

**Enlace:** [Aqui](https://www.pce-instruments.com/peru/instrumento-medida/medidor/medidor-de-co2-pce-instruments-medidor-de-co2-pce-aqd-50-ica-incl.-certificado-calibraci%C3%B3n-det_6080851.htm?_list=kat&_listpos=2)  
#### Producto #2:
### <p align="center">Extractor De Humo 550w Para Maquina Cnc Laser Co2 De Corte</p>
**Finalidad:** Eliminar o capturar los humos y partículas generados
<p align="center"><strong>Figura 7:</strong></p>
<p align="center">
  <img src="https://github.com/Dooncito/fundamentos-de-dise-o/blob/dc18e8ffbf06b6b6356ff15c65d55858bcf8a4d1/Imagenes/img_comercial_y_cienti/product2.jpg" width="250" style="margin: auto;">
</p>

**Descripción:** Extractor de humo de 550W para máquinas CNC LASER de tubo CO2 industriales,  ventilador que utiliza tiro negativo para atraer humos y partículas de polvo a un sistema de filtración contenido. Este proceso elimina las partículas peligrosas del aire. Los filtros que utiliza la unidad de extracción tienen un sensor que le informará cuando sea necesario cambiarlos.

**Enlace:** [Aqui](https://articulo.mercadolibre.com.pe/MPE-613414503-extractor-de-humo-550w-para-maquina-cnc-laser-co2-de-corte-_JM#position=7&search_layout=stack&type=item&tracking_id=36806d49-40f4-4ef6-88d3-3cbdf239d971)  
#### Producto #3:
### <p align="center">Sensor detector de monóxido de carbono GK</p>
**Finalidad:** Electroquímico que mide el monóxido de carbono.
<p align="center"><strong>Figura 8:</strong></p>
<p align="center">
  <img src="https://github.com/Dooncito/fundamentos-de-dise-o/blob/dc18e8ffbf06b6b6356ff15c65d55858bcf8a4d1/Imagenes/img_comercial_y_cienti/product3.jpg" width="400" style="margin: auto;">
</p>

**Descripción:** El detector doméstico de monóxido de carbono (CO) es un detector de excelentes prestaciones y reducido tamaño, dada su construcción con materiales de gran resistencia brinda excelentes características de desempeño para la detección doméstica de monóxido de carbono. Cuando la lectura indicada por el sensor se encuentre en el umbral de alarma, el detector de gas ubicado en la parte frontal del instrumento, genera destellos para que puedan ser advertidos desde por el usuario y en la parte frontal del equipo se activará en el momento en el que la concentración de monóxido alcance o supere las 100 PPM. 

**Enlace:** [Aqui](https://www.valiometro.pe/sensor-detector-de-monoxido-de-carbono-gk) 

#### Producto #4:
### <p align="center">Medidor de partículas PCE-AQD 20</p>
**Finalidad:** Medición de temperatura, humedad del aire, CO2, PM2,5 y presión atmosférica.
<p align="center"><strong>Figura 9:</strong></p>
<p align="center">
  <img src="https://github.com/Dooncito/fundamentos-de-dise-o/blob/dc18e8ffbf06b6b6356ff15c65d55858bcf8a4d1/Imagenes/img_comercial_y_cienti/product4.jpg" width="300" style="margin: auto;">
</p>

**Descripción:** El medidor de partículas es un instrumento de medición ideal para controlar la calidad del aire en puestos de trabajo. El medidor de partículas es ideal para protocolar de forma continua la temperatura y humedad del aire, el CO2, las partículas PM 2,5 y la presión atmosférica. Todos estos parámetros sirven al encargado de salud y seguridad para conocer la calidad del aire. Los valores medidos con el medidor de partículas se guardan en una tarjeta de memoria SD. El formato del fichero es xls lo que le permite leer los valores directamente con el programa Excel sin la necesidad de pasar a través de un software. Los valores se visualizan en la gran pantalla retroiluminada.

**Enlace:** [Aqui](https://www.pce-instruments.com/peru/instrumento-medida/medidor/medidor-de-particulas-pce-instruments-medidor-de-part%C3%ADculas-pce-aqd-20-det_5909905.htm?_list=kat&_listpos=9)

### **Patentes:** 
#### Patente #1:
### <p align="center">_Dispositivo de aspiración y purificación de humos con función de recuperación de calor residua_</p>
**Fecha de publicación:** 2022-06-21

**Número de publicaciones:** CN216790309U

**Inventores:** TANG JIE; NI DAMANDO; LIU ZONGLING

<p align="center"><strong>Figura 10:</strong></p>
<p align="center">
  <img src="https://github.com/Dooncito/fundamentos-de-dise-o/blob/120f9ca0a7d9455328a6638fb018465983668eeb/Imagenes/img_comercial_y_cienti/protos1.jpg" width="500" style="margin: auto;">
</p>

**Descripción:** El dispositivo es un sistema de aspiración y purificación de humos para cocinas, con recuperación de calor residual. Con una carcasa en forma de L y mecanismo de intercambio de calor, recicla el calor del humo durante la purificación. La estructura incluye placas, tira guía, y un mecanismo de intercambio con aletas y tubos de absorción. Este diseño garantiza eficiencia al aprovechar el calor residual durante la aspiración y purificación de humos de cocina.(Tang J., 2022)

**Referencia:** TANG, J.; DAMING, N.; ZONGLING, L.(2022)Smoke suction and purification device with waste heat recovery function for kitchen. CN216790309U. Recuperado de https://worldwide.espacenet.com/patent/search/family/082010151/publication/CN216790309U?q=pn%3DCN216790309U

#### Patente #2:
### <p align="center">_Sistema de precipitación electrostática para captura de materia partícula en equipos de conbustión domésticos_</p>
**Fecha de publicación:** 2020-01-02

**Número de publicaciones:** WO2020000115A1

**Inventores:** SOTO ESPINACE, Ricardo; BURBOA VILLARROEL, Eduardo; SOTO VERA, Esteban

<p align="center"><strong>Figura 11:</strong></p>
<p align="center">
  <img src="https://github.com/Dooncito/fundamentos-de-dise-o/blob/120f9ca0a7d9455328a6638fb018465983668eeb/Imagenes/img_comercial_y_cienti/protos2.png" width="500" style="margin: auto;">
</p>

**Descripción:** La invención es un sistema de precipitación electrostática para capturar material particulado en equipos de combustión como estufas y calderas de biomasa. Incluye un tubo metálico, una caja de componentes eléctricos, una puerta con sensores de apertura y cierre, un electrodo removible y un conjunto eléctrico externo. La característica distintiva es la seguridad con sensores que apagan la fuente de alto voltaje al abrir la puerta, evitando descargas eléctricas. La amplitud de voltaje necesario para reducir el material particulado varía de 17kV a 38kV, con un valor máximo operativo de aproximadamente 28kV.(Soto E., 2020)

**Referencia:** SOTO ESPINACE, R.; BURBOA VILLARROEL, E.; SOTO VERA, E.(2020)ELECTROSTATIC PRECIPITATION SYSTEM FOR CAPTURING PARTICULATE MATTER IN HOME COMBUSTION EQUIPMENT. WO2020000115A1. Recuperado de https://worldwide.espacenet.com/patent/search/family/065529042/publication/WO2020000115A1?q=pn%3DWO2020000115A1

#### Patente #3:
### <p align="center">_Dispositivo de humo y circuito de detección de humo_</p>
**Fecha de publicación:** 2021-06-01

**Número de publicaciones:** US11024141B2

**Inventor:** Eric V.Gonzales

<p align="center"><strong>Figura 12:</strong></p>
<p align="center">
  <img src="https://github.com/Dooncito/fundamentos-de-dise-o/blob/120f9ca0a7d9455328a6638fb018465983668eeb/Imagenes/img_comercial_y_cienti/protos3.png" width="500" style="margin: auto;">
</p>

**Descripción:** Un procedimiento para supervisar una ubicación llevado a cabo por uno o más procesadores incluye la recepción de señales provenientes de un sensor de humo. Posteriormente, se identifican una o más características distintivas a partir de las señales recibidas. Luego, se establece una ventana de tiempo basándose en al menos una de las características identificadas. Se caracterizan uno o más tipos de incendio dentro de la ventana de tiempo determinada utilizando las características identificadas. Además, se determinan de manera dinámica uno o más niveles de alarma según la caracterización de los tipos de fuego. Se evalúa al menos una característica dentro de la ventana de tiempo utilizando los niveles de alarma establecidos y, si se detecta una condición de alarma, se emite una señal de alarma.(Gonzales, 2021)

**Referencia:** Gonzales, E.(2021)  Smoke device and smoke detection circuit. US11024141B2. Recuperado de https://patentimages.storage.googleapis.com/c1/45/a8/021df7692b10cf/US11024141.pdf
### Patente #4:
### <p align="center">_Ventilador de escape de humo electrónico de protección del medio ambiente y aparato de absorción de electrones de humo_</p>
**Fecha de publicación:** 2008-11-12

**Número de publicaciones:** CN100431711C

**Inventores:** TAO XIANFANG

<p align="center"><strong>Figura 13:</strong></p>
<p align="center">
  <img src="https://github.com/Dooncito/fundamentos-de-dise-o/blob/120f9ca0a7d9455328a6638fb018465983668eeb/Imagenes/img_comercial_y_cienti/protos4.png" width="500" style="margin: auto;">
</p>

**Descripción:** La tecnología absorbe el polvo utilizando electricidad estática para ionizar y cargar las partículas de humo, luego utiliza un fuerte campo eléctrico para desviar y absorber las partículas de humo cargadas para generar iones de oxígeno negativos,que contribuyen a refrescar y esterilizar el aire.
Utiliza un fuerte campo eléctrico generado por un alto voltaje para ionizar las partículas de humo o la mezcla en el humo para cargarlo, y luego usa la misma electricidad para repelerse entre sí. El principio de atracción mutua, reciclarlo. Una vez recuperados los vapores de aceite, el gas descargado por la campana extractora electrónica respetuosa con el medio ambiente apenas contiene vapores de aceite u otras impurezas, y todo es aire puro, lo que equivale a filtrar el aire contaminado. (XIANFANG. ,2008)


**Referencia:** XIANFANG, T. (2008) Environmental protection electronic smoke exhaust ventilator and smoke electron absorption apparatus. CN100431711C. Recuperado de https://worldwide.espacenet.com/patent/search?q=pn%3DCN100431711C


## REQUERIMIENTOS 

![img](https://github.com/Dooncito/fundamentos-de-dise-o/blob/main/Imagenes/NoFuncionales.jpg)

![img](https://github.com/Dooncito/fundamentos-de-dise-o/blob/main/Imagenes/Funcionales.jpg)


## Bibliografía
Chen, J., & Hoek, G. (2020). Long-term exposure to PM and all-cause and cause-specific mortality: A systematic review and meta-analysis. Environment international. Recuperado de https://doi.org/10.1016/j.envint.2020.105974

Ebrahimifakhar, A., Poursadegh, M., Hu, Y., Yuill, D. P., & Luo, Y. (2024). A systematic review and meta-analysis of field studies of portable air cleaners: Performance, user behavior, and by-product emissions. Science of The Total Environment. Recuperado de https://doi.org/10.1016/j.scitotenv.2023.168786

Gonzales, E. (2021). Smoke device and smoke detection circuit. US11024141B2. Recuperado de https://patentimages.storage.googleapis.com/c1/45/a8/021df7692b10cf/US11024141.pdf

Karami, M., McMorrow, G. V., & Wang, L. (2018). Continuous monitoring of indoor environmental quality using an Arduino-based data acquisition system. Journal of Building Engineering. Recuperado de https://doi.org/10.1016/j.jobe.2018.05.014

Li, C., Zhang, K., Dai, Z., Ma, Z., & Liu, X. (2020). Investigation of the Impact of Land-Use Distribution on PM2.5 in Weifang: Seasonal Variations. International Journal of Environmental Research and Public Health. Recuperado de https://doi.org/10.3390/ijerph17145135

SOTO ESPINACE, R.; BURBOA VILLARROEL, E.; SOTO VERA, E. (2020). Electrostatic precipitation system for capturing particulate matter in home combustion equipment. WO2020000115A1. Recuperado de https://worldwide.espacenet.com/patent/search/family/065529042/publication/WO2020000115A1?q=pn%3DWO2020000115A1

TANG, J.; DAMING, N.; ZONGLING, L. (2022). Smoke suction and purification device with waste heat recovery function for kitchen. CN216790309U. Recuperado de https://worldwide.espacenet.com/patent/search/family/082010151/publication/CN216790309U?q=pn%3DCN216790309U

XIANFANG, T. (2008). Environmental protection electronic smoke exhaust ventilator and smoke electron absorption apparatus. CN100431711C. Recuperado de https://worldwide.espacenet.com/patent/search?q=pn%3DCN100431711C
