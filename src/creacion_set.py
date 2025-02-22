import pandas as pd
import random
from faker import Faker

# Generación de datos ficticios
fake = Faker()

# Función para generar ventas
def generate_sales(num_records):
    products = ["Queso Majorero", "Aceite de Oliva", "Vino Tinto Canario", "Dulce de Membrillo", "Gofio"]
    sales_data = []
    
    for _ in range(num_records):
        product = random.choice(products)
        quantity = random.randint(1, 5)
        price = random.uniform(10, 30)  # Precio entre 10 y 30 €
        total_sale = round(quantity * price, 2)
        sale_date = fake.date_this_year()
        
        sales_data.append([sale_date, product, quantity, round(price, 2), total_sale])
    
    return pd.DataFrame(sales_data, columns=["Fecha", "Producto", "Cantidad", "Precio Unitario", "Total Venta"])

# Función para generar clientes
def generate_clients(num_records):
    clients_data = []
    
    for _ in range(num_records):
        client_id = random.randint(1, num_records +1)
        name = fake.name()
        age = random.randint(18, 65)
        gender = random.choice(["M", "F"])
        location = fake.city()
        purchase_freq = random.choice(["Ocasional", "Recurrente", "VIP"])
        
        clients_data.append([client_id, name, age, gender, location, purchase_freq])
    
    return pd.DataFrame(clients_data, columns=["ID Cliente", "Nombre", "Edad", "Género", "Ubicación", "Frecuencia de compra"])

# Función para generar tráfico web
def generate_traffic(num_records):
    traffic_data = []
    
    for _ in range(num_records):
        visit_date = fake.date_this_year()
        landing_page = random.choice(["Página de Inicio", "Queso Majorero", "Aceite de Oliva", "Vino Tinto Canario"])
        visit_duration = random.randint(1, 10)  # Duración en minutos
        bounce_rate = random.uniform(30, 80)  # Tasa de rebote entre 30 y 80%
        source = random.choice(["Orgánico", "Pagado", "Redes Sociales", "Referidos"])
        device = random.choice(["Móvil", "Desktop", "Tablet"])
        
        traffic_data.append([visit_date, landing_page, visit_duration, round(bounce_rate, 2), source, device])
    
    return pd.DataFrame(traffic_data, columns=["Fecha", "Página de Aterrizaje", "Duración (min)", "Tasa de Rebote", "Fuente", "Dispositivo"])

# Función para generar campañas
def generate_campaigns(num_records):
    campaigns_data = []
    
    for _ in range(num_records):
        campaign_id = random.randint(1, num_records)
        campaign_type = random.choice(["Anuncios en Google", "Email Marketing", "Redes Sociales"])
        start_date = fake.date_this_year()
        end_date = fake.date_this_year()
        budget = random.uniform(500, 2000)  # Presupuesto entre 500 y 2000 €
        impressions = random.randint(10000, 50000)
        clicks = random.randint(500, 3000)
        conversions = random.randint(50, 500)
        roi = round(random.uniform(1.5, 4.5), 2)
        
        campaigns_data.append([campaign_id, campaign_type, start_date, end_date, round(budget, 2), impressions, clicks, conversions, roi])
    
    return pd.DataFrame(campaigns_data, columns=["Campaña ID", "Fecha Inicio", "Fecha Fin", "Tipo de Campaña", "Presupuesto", "Impressions", "Clics", "Conversiones", "ROI"])

# Función para generar inventario
def generate_inventory(num_records):
    products = ["Queso Majorero", "Aceite de Oliva", "Vino Tinto Canario", "Dulce de Membrillo", "Gofio"]
    inventory_data = []
    
    for _ in range(num_records):
        product_id = random.randint(1, num_records)
        product = random.choice(products)
        initial_stock = random.randint(50, 150)  # Stock inicial entre 50 y 150 unidades
        current_stock = random.randint(0, initial_stock)
        out_of_stock = "Sí" if current_stock == 0 else "No"
        
        inventory_data.append([product_id, product, initial_stock, current_stock, out_of_stock])
    
    return pd.DataFrame(inventory_data, columns=["ID Producto", "Nombre", "Stock Inicial", "Stock Actual", "Productos Agotados"])

# Función para generar satisfacción del cliente
def generate_customer_satisfaction(num_records):
    satisfaction_data = []
    
    for _ in range(num_records):
        client_id = random.randint(1, num_records)
        product = random.choice(["Queso Majorero", "Aceite de Oliva", "Vino Tinto Canario", "Dulce de Membrillo", "Gofio"])
        rating = random.randint(1, 5)  # Puntuación de 1 a 5
        comments = fake.sentence(nb_words=6)
        
        satisfaction_data.append([client_id, product, rating, comments])
    
    return pd.DataFrame(satisfaction_data, columns=["ID Cliente", "Producto", "Calificación", "Comentarios"])

# Generación de los registros
sales_df = generate_sales(200)
clients_df = generate_clients(100)
traffic_df = generate_traffic(150)
campaigns_df = generate_campaigns(50)
inventory_df = generate_inventory(10)
satisfaction_df = generate_customer_satisfaction(100)

# Guardar los archivos CSV
sales_file = '../data/sales_data.csv'
clients_file = '../data/clients_data.csv'
traffic_file = '../data/traffic_data.csv'
campaigns_file = '../data/campaigns_data.csv'
inventory_file = '../data/inventory_data.csv'
satisfaction_file = '../data/satisfaction_data.csv'

sales_df.to_csv(sales_file, index=False)
clients_df.to_csv(clients_file, index=False)
traffic_df.to_csv(traffic_file, index=False)
campaigns_df.to_csv(campaigns_file, index=False)
inventory_df.to_csv(inventory_file, index=False)
satisfaction_df.to_csv(satisfaction_file, index=False)