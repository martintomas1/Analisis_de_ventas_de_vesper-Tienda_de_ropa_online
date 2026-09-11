Análisis de Ventas — Vesper (tienda de ropa online)

Este es un análisis exploratorio de 18 meses de ventas de una tienda de ropa online, con el objetivo de identificar qué productos, talles y regiones impulsan el negocio, y detectar qué factores explican los picos y valles de ingresos mes a mes.

Contexto:
Vesper es una tienda de ropa online (remeras, baby tees, buzos, accesorios) que vende a través de Tiendanube y despacha por correo a todo el país. Este análisis nace de una necesidad real del negocio: entender qué está funcionando y qué se puede mejorar, más allá de la intuición.

Fuente de datos:
Exportaciones de ventas de Tiendanube, marzo 2025 – septiembre 2026 (213 ventas, 299 líneas de producto). Los datos personales de compradores (nombre, DNI, teléfono, email, dirección) fueron removidos en la limpieza antes de este análisis, el dataset público de este repositorio no contiene información identificable de clientes.

Preguntas de negocio:
¿Qué categorías y diseños puntuales generan más ingresos?
¿Cómo evolucionan los ingresos mes a mes? ¿Hay estacionalidad, y a qué se debe?
¿De qué provincias son los clientes, y cómo influye el costo de envío?
¿Qué talles rotan más, y qué tan confiable es ese dato?

Metodología y stack:
Limpieza y procesamiento: Python (pandas)
Análisis exploratorio: Python (pandas, matplotlib, seaborn)
Dashboard interactivo: Power BI

Decisiones de limpieza destacadas:
El export de Tiendanube trae los datos del pedido (fecha, total, envío) solo en la primera línea de cada venta cuando hay varios productos, se completan hacia abajo agrupando por número de venta.
El nombre del producto no identifica el diseño de forma confiable (mismo diseño escrito distinto según el pedido). Se usó el SKU para agrupar variantes del mismo diseño bajo una sola etiqueta limpia.
El talle se extrae del nombre del producto (no viene en un campo propio), lo cual generó un hallazgo de calidad de datos.

Insights clave:
1. Remera y Baby Tee concentran el 67% de los ingresos. De $4.774.368 en ventas confirmadas, Remera ($1.885.991) y Baby Tee (1.316.230) representan la mayoría. El diseño "Jeff" es el más fuerte del catálogo, vendido en ambos formatos, tanto Baby Tee como remera. Recomendación: priorizar stock y variantes nuevas en estas dos categorías antes de diversificar el catálogo.
3. Los pedidos de afuera de Buenos Aires compran en promedio el doble de unidades por pedido, probablemente para amortizar el costo y tiempo de envío. La concentración geográfica en sí parece responder más a alcance de marca que a costo o poder adquisitivo. Recomendación: cruzar este dato con analítica de redes sociales (de dónde vienen los seguidores).
4. Calidad de datos: el talle se cargó de forma pareja en Remera, pero no en Baby Tee. Remera tiene talle identificable en el 99% de sus ventas, Baby Tee, solo en el 38%. Esto no es una limitación técnica sino una inconsistencia puntual al cargar productos Baby Tee. Recomendación: cargar el talle de Baby Tee con el mismo criterio que ya se usa en Remera, para poder gestionar stock por talle con confianza.

Para el dashboard: abrir dashboard_vesper.pbix en Power BI Desktop y actualizar el origen de datos si es necesario.


<img width="1208" height="671" alt="dashboard" src="https://github.com/user-attachments/assets/72664693-498d-4d02-91ce-26b89227f7f6" />


Autor:
(Tomas Martin — https://www.linkedin.com/in/tomas-martin-4877a2227/ — martintomasnahuel@gmail.com)
