Análisis de Ventas — Vesper (tienda de ropa online)

Este es un análisis exploratorio de 18 meses de ventas de una tienda de ropa online, con el objetivo de identificar qué productos, talles y regiones impulsan el negocio, y detectar qué factores explican los picos y valles de ingresos mes a mes.

Contexto:
Vesper es una tienda de ropa online (remeras, baby tees, buzos, accesorios) que vende a través de Tiendanube y despacha por correo a todo el país. Este análisis nace de una necesidad real del negocio: entender qué está funcionando y qué se puede mejorar, más allá de la intuición.

Fuente de datos:
Exportaciones de ventas de Tiendanube, marzo 2025 – septiembre 2026 (213 ventas, 299 líneas de producto). Los datos personales de compradores (nombre, DNI, teléfono, email, dirección) fueron removidos en la limpieza antes de este análisis, el dataset público de este repositorio no contiene información identificable de clientes.

Preguntas de negocio:
¿Cómo evolucionaron las ventas de productos mes a mes? ¿Hay evidencia de estacionalidad?
¿Qué categorías y diseños puntuales generan más ingresos y unidades vendidas?
¿De qué provincias/ciudades son los clientes y cómo se distribuyen las ventas?
¿Qué talles rotan más?
¿Qué diferencias hay entre Buenos Aires/CABA y el resto del país?
¿Cuál es el ticket promedio y cómo se compone?

Metodología y stack:
Limpieza y procesamiento: Python (pandas)
Análisis exploratorio: Python (pandas, matplotlib, seaborn)
Dashboard interactivo: Power BI

Decisiones de limpieza destacadas:
El export de Tiendanube trae los datos del pedido (fecha, total, envío) solo en la primera línea de cada venta cuando hay varios productos, se completan hacia abajo agrupando por número de venta.
El nombre del producto no identifica el diseño de forma confiable (mismo diseño escrito distinto según el pedido). Se usó el SKU para agrupar variantes del mismo diseño bajo una sola etiqueta limpia.
El talle se extrae del nombre del producto (no viene en un campo propio), lo cual generó un hallazgo de calidad de datos.

Insights clave:
Categorías: Remera y Baby Tee concentran el 67,1% de las ventas netas de productos. Remera lidera en facturación, mientras Baby Tee lidera en unidades vendidas.
2. Diseño: al agrupar variantes por diseño base, Jeff es el diseño con mayor facturación.
3. Geografía: Buenos Aires/CABA concentran la mayor parte de los pedidos y ventas. Fuera de Buenos Aires/CABA se observan 1,52 unidades por pedido vs. 1,39, una diferencia de aproximadamente 9,4%. El análisis por provincia no muestra evidencia descriptiva suficiente para atribuir las diferencias de ventas al costo de envío.
4. Talles:Remera tiene 100% de cobertura de talle y Baby Tee 42,7% después de complementar talles explícitos presentes en algunos nombres de producto. La cobertura incompleta de Baby Tee limita la confiabilidad de cualquier conclusión sobre rotación por talle.
5. Ticket: el ticket promedio total es de 28.867, compuesto por 24.845 de subtotal de productos, -1.092 de descuentos y 5.114 de envío.
6. Datos temporales: julio de 2026 y febrero de 2026 son los meses de mayores ventas netas del período, septiembre de 2026 es parcial y no se utiliza para comparar meses completos. Con la cobertura disponible no alcanza para afirmar una estacionalidad anual consolidada.


<img width="1208" height="671" alt="dashboard" src="https://github.com/user-attachments/assets/72664693-498d-4d02-91ce-26b89227f7f6" />


Autor:
(Tomas Martin — https://www.linkedin.com/in/tomas-martin-4877a2227/ — martintomasnahuel@gmail.com)
