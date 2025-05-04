# Diccionario de Datos - Proyecto ShopOnline

Este documento describe en detalle cada uno de los datasets utilizados en el proyecto ShopOnline, incluyendo la estructura, campos y valores posibles de cada conjunto de datos.

## 1. Datos de Ventas (`sales_data.csv`)

Dataset con información sobre transacciones de venta realizadas en la tienda online.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| Fecha | Date | Fecha en que se realizó la venta (YYYY-MM-DD) |
| Producto | String | Nombre del producto vendido |
| Cantidad | Integer | Número de unidades vendidas en la transacción |
| Precio Unitario | Float | Precio por unidad en euros, puede incluir descuentos |
| Total Venta | Float | Importe total de la venta (Cantidad × Precio Unitario) |

**Notas adicionales:**
- El dataset incluye 200 registros
- Aproximadamente un 15% de las ventas tienen descuentos aplicados
- Las fechas abarcan todo el año 2024
- Los precios son consistentes con los datos del inventario

## 2. Datos de Clientes (`clients_data.csv`)

Dataset con perfiles de clientes registrados en la plataforma.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID Cliente | Integer | Identificador único del cliente |
| Nombre | String | Nombre completo del cliente |
| Edad | Integer | Edad del cliente |
| Género | String | Género del cliente (M/F) |
| Ubicación | String | Ciudad de residencia del cliente |
| Frecuencia de compra | String | Categorización del cliente según su actividad de compra |
| Fecha de registro | Date | Fecha en que el cliente se registró en la plataforma |
| Fuente de adquisición | String | Canal a través del cual el cliente llegó a la tienda |

**Valores posibles:**
- **Frecuencia de compra**: "Una compra" (45%), "Ocasional" (30%), "Recurrente" (18%), "VIP" (7%)
- **Fuente de adquisición**: "Búsqueda orgánica", "Redes sociales", "Recomendación", "Publicidad pagada", "Email marketing", "Evento gastronómico"
- **Ubicación**: Incluye principales ciudades españolas y canarias, con distribución ponderada (mayor concentración en Madrid, Barcelona y ciudades canarias)

**Notas adicionales:**
- El dataset incluye 100 perfiles de clientes
- La distribución de edad está ponderada para representar el mercado objetivo (concentración mayor entre 35-54 años)
- El ratio de género es aproximadamente 48% hombres, 52% mujeres

## 3. Datos de Tráfico Web (`traffic_data.csv`)

Dataset con información sobre visitas a la tienda online.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| Fecha | Date | Fecha de la visita |
| Página de Aterrizaje | String | Página donde el usuario comenzó su visita |
| Duración (min) | Float | Duración de la visita en minutos |
| Tasa de Rebote | Float | Porcentaje de visitas que abandonaron sin interactuar (0-100) |
| Fuente | String | Origen del tráfico |
| Dispositivo | String | Tipo de dispositivo utilizado por el visitante |

**Valores posibles:**
- **Página de Aterrizaje**: "Página de Inicio" y páginas de producto individuales
- **Fuente**: "Orgánico", "Pagado", "Redes Sociales", "Email", "Directo", "Referidos"
- **Dispositivo**: "Móvil", "Desktop", "Tablet"

**Notas adicionales:**
- El dataset incluye 150 registros de tráfico
- Los parámetros de duración y tasa de rebote varían según fuente y dispositivo (ej: menores duraciones en móvil)
- La página de inicio recibe aproximadamente un 35% del tráfico total

## 4. Datos de Campañas (`campaigns_data.csv`)

Dataset con información sobre campañas de marketing realizadas.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| Campaña ID | Integer | Identificador único de la campaña |
| Tipo de Campaña | String | Categoría de la campaña |
| Fecha Inicio | Date | Fecha de inicio de la campaña |
| Fecha Fin | Date | Fecha de finalización de la campaña |
| Presupuesto | Float | Inversión realizada en la campaña (euros) |
| Impressions | Integer | Número de veces que se mostró la campaña |
| Clics | Integer | Número de clics recibidos |
| Conversiones | Integer | Número de ventas conseguidas |
| ROI | Float | Retorno de inversión calculado |

**Valores posibles:**
- **Tipo de Campaña**: "Anuncios en Google", "Email Marketing", "Redes Sociales"

**Notas adicionales:**
- El dataset incluye 50 campañas
- La duración varía según el tipo (Email: 1-7 días, Redes: 1-14 días, Google: 7-30 días)
- Las tasas de conversión están ajustadas a valores realistas por canal (Email: 5-15%, Redes: 2-8%, Google: 3-10%)

## 5. Datos de Inventario (`inventory_data.csv`)

Dataset con información sobre los productos disponibles en la tienda.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID Producto | Integer | Identificador único del producto |
| Nombre | String | Nombre del producto |
| SKU | String | Código único de stock (Stock Keeping Unit) |
| Categoría | String | Categoría del producto |
| Proveedor | String | Empresa proveedora del producto |
| Stock Inicial | Integer | Cantidad inicial en inventario |
| Stock Actual | Integer | Cantidad disponible actualmente |
| Stock Mínimo | Integer | Nivel mínimo recomendado de stock |
| Stock Máximo | Integer | Nivel máximo recomendado de stock |
| Costo Unitario | Float | Costo de adquisición por unidad (euros) |
| Precio Venta | Float | Precio de venta al público (euros) |
| Margen (%) | Float | Porcentaje de margen de beneficio |
| Estado Stock | String | Estado actual del nivel de inventario |
| Vida Útil (días) | Integer | Tiempo recomendado de vida del producto |

**Valores posibles:**
- **Categoría**: "Lácteos y quesos", "Aceites y condimentos", "Bebidas", "Dulces y mermeladas", "Cereales y harinas", "Productos frescos"
- **Estado Stock**: "Agotado", "Bajo", "Disponible"

**Notas adicionales:**
- El dataset incluye 10 productos canarios
- Los márgenes oscilan entre 63% y 78%
- El SKU está formado por un código de categoría, un número secuencial y las primeras letras del producto

## 6. Datos de Satisfacción del Cliente (`satisfaction_data.csv`)

Dataset con información sobre reseñas y valoraciones de clientes.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID Cliente | Integer | Identificador del cliente que realizó la reseña |
| Producto | String | Producto evaluado |
| Calificación | Integer | Puntuación otorgada (1-5 estrellas) |
| Comentarios | String | Texto de la reseña |
| Fecha Review | Date | Fecha en que se publicó la reseña |
| Comprador Verificado | Boolean | Indica si el cliente realmente compró el producto |
| Respuesta Vendedor | String | Respuesta del vendedor a la reseña (si existe) |
| Compartido en Redes | Boolean | Indica si la reseña fue compartida en redes sociales |

**Notas adicionales:**
- El dataset incluye 100 reseñas
- Cada producto tiene un perfil de satisfacción particular (media y desviación típica)
- El 90% de las reseñas son de compradores verificados
- Aproximadamente el 80% de las reseñas de 3 o menos estrellas reciben respuesta
- Los comentarios están generados desde plantillas específicas con aspectos positivos y negativos para cada producto
