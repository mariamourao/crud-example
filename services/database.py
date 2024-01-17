import psycopg2


# Substitua as informações abaixo com os detalhes do seu banco de dados PostgreSQL
host = 'localhost'  # ou o endereço IP do seu servidor PostgreSQL
database = 'postgres'  # ou o nome do seu banco de dados
user = 'postgres'
password = 'special'

# Conectando ao PostgreSQL
conn = psycopg2.connect(host=host, database=database, user=user, password=password)
cursor = conn.cursor()


