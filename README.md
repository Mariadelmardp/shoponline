# Proyecto ShopOnline (Isla de Sabores)

## Descripción general

ShopOnline es un proyecto de análisis de datos enfocado en un e-commerce de productos canarios gourmet llamado "Isla de Sabores". El objetivo principal es transformar datos de ventas, clientes y marketing en insights accionables mediante visualizaciones interactivas y métricas clave que ayuden a la toma de decisiones.

## Objetivos del proyecto

- Analizar la rentabilidad por producto y categoría
- Identificar patrones de comportamiento de clientes
- Evaluar la eficacia de campañas de marketing
- Desarrollar indicadores clave para monitorizar el rendimiento del negocio
- Presentar los hallazgos mediante dashboards interactivos

## Estructura del proyecto

```
ShopOnline/
│
├── data/                  # Datos utilizados para el análisis
│   ├── sales_data.csv     # Datos de transacciones de ventas
│   ├── clients_data.csv   # Información de clientes
│   ├── traffic_data.csv   # Datos de tráfico web
│   ├── campaigns_data.csv # Información de campañas de marketing
│   ├── inventory_data.csv # Datos de inventario
│   └── satisfaction_data.csv # Reseñas y satisfacción de clientes
│
├── src/                   # Código fuente del proyecto
│   ├── creacion_data.ipynb # Notebook para generación de datos sintéticos
│   └── eda.ipynb     # Notebook con análisis exploratorio
│
├── docs/                  # Documentación del proyecto
│   ├── data_dictionary.md # Descripción de los campos de datos
│   └── insights.md        # Hallazgos principales del análisis
│
├── dashboards/            # Archivos de Power BI
│   └── shoponline.pbix    # Dashboard principal del proyecto
│
├── env_shoponli/          # Entorno virtual Python para el proyecto
│
└── README.md              # Este archivo
```

## Tecnologías utilizadas

- **Python**: Para la generación de datos, limpieza y análisis exploratorio
- **Pandas y NumPy**: Para manipulación y análisis de datos
- **Faker**: Para generación de datos sintéticos realistas
- **Jupyter Notebooks**: Para documentación y exploración interactiva
- **Git/GitHub**: Para control de versiones y colaboración
- **Power BI**: Para la creación de dashboards interactivos

## Datasets

Para este proyecto se utilizaron datasets sintéticos generados con Python y la biblioteca Faker, que incluyen:

1. **Sales Data (200 registros)**: Transacciones de venta con fecha, producto, cantidad, precio y total.
2. **Clients Data (100 registros)**: Perfiles de clientes con datos demográficos, ubicación y patrones de compra.
3. **Traffic Data (150 registros)**: Información sobre visitas a la web, incluyendo página de entrada, duración y dispositivo.
4. **Campaigns Data (50 registros)**: Detalles de campañas de marketing con presupuesto, impresiones, clics y conversiones.
5. **Inventory Data (10 registros)**: Catálogo de productos con información de stock, precios, márgenes y proveedores.
6. **Satisfaction Data (100 registros)**: Reseñas de clientes con calificaciones y comentarios sobre productos.

La generación sintética de datos permitió:

- Crear un ecosistema de datos completo y coherente
- Simular patrones realistas de comportamiento de clientes y ventas
- Incorporar variabilidad controlada para probar hipótesis
- Trabajar con un volumen de datos adecuado para análisis en Power BI
- Evitar preocupaciones de privacidad al trabajar con datos no reales

## Dashboard principal

El dashboard está estructurado en tres páginas principales:

### 1. Análisis de ventas y rentabilidad

- KPIs: Ventas totales, margen de beneficio, tasa de repetición, valor medio del pedido
- Margen bruto y porcentual por producto
- Visualización de margen vs volumen de ventas
- Ranking de productos por popularidad
- Índice de potencial de producto
- Tendencia de ventas mensuales

### 2. Análisis de cliente y comportamiento

- KPIs: Clientes por mes, número total de clientes, LTV, NPS
- Distribución de dispositivos utilizados para compras
- Frecuencia de compra
- Distribución de clientes por ubicación y edad
- Calificación de productos
- Distribución por género

### 3. Campañas y adquisición

- KPIs: CAC, ROI promedio, CTR, tasa de conversión
- Distribución del ROI por tipo de campaña
- Coste por conversión según tipo de campaña
- Comparación de duración de campañas
- Tasa de rebote por página de aterrizaje
- Rendimiento mensual de campañas

## Hallazgos principales

- El Vino Tinto Canario y el Queso Majorero son los productos más vendidos, representando aproximadamente el 33% de las ventas totales.
- Solo el 32% de los clientes realizan compras repetidas, lo que indica una oportunidad de mejora en estrategias de fidelización.
- El 60% de las ventas provienen de Madrid, Barcelona y Canarias.
- Existe una correlación significativa entre la compra de Mojo Picón y Vino Tinto Canario.
- Los dispositivos móviles representan aproximadamente el 35% del tráfico, pero tienen una tasa de conversión menor que los desktops.
- El Email Marketing muestra el mejor ROI entre los canales de marketing utilizados.

## Métricas clave desarrolladas

- **Índice de Potencial de Producto**: Combina crecimiento mensual y margen bruto para identificar productos con mayor potencial.
- **Tasa de repetición de compra**: Porcentaje de clientes que realizan más de una compra.
- **Valor medio del pedido**: Promedio de gasto por transacción.
- **CAC (Coste de Adquisición de Cliente)**: Inversión necesaria para adquirir un nuevo cliente.
- **LTV (Valor del Tiempo de Vida del Cliente)**: Valor estimado que un cliente generará durante su relación con la tienda.

## Próximos pasos

- Implementar un sistema de alertas para productos con stock bajo y alto potencial
- Desarrollar un modelo predictivo para estimar ventas futuras
- Crear segmentos de clientes más detallados para campañas personalizadas
- Integrar datos de redes sociales para análisis de sentimiento
- Optimizar la estrategia de marketing basada en los canales con mejor ROI

## Instalación y configuración

1. Clonar el repositorio

```bash
git clone https://github.com/[usuario]/shoponline.git
cd shoponline
```

2. Crear y activar entorno virtual (el proyecto ya incluye uno llamado env_shoponline)

```bash
# Para crear un nuevo entorno (opcional, si no usas el existente)
python -m venv env_shoponline

# Para activar el entorno existente
# En Windows:
env_shoponline\Scripts\activate
# En macOS/Linux:
source env_shoponline/bin/activate
```

3. Instalar dependencias

```bash
pip install -r requirements.txt
```

4. Ejecutar notebooks (opcional)

```bash
jupyter notebook src/creacion_data.ipynb
# o
jupyter notebook src/eda.ipynb
```

5. Abrir el dashboard en Power BI

```
dashboards/shoponline.pbix
```

## Contacto

Para más información sobre este proyecto o colaboraciones, puedes contactarme a través de:

- LinkedIn: [Tu perfil de LinkedIn]
- Email: mariadelmardp@hotmail.com
- GitHub: [Tu perfil de GitHub]

---

Desarrollado como parte del Porfolio en Data Analytics de Insight Creativo (marca personal)
