import yaml
import plotly
import psycopg2

cn_std_colors_hex = ['7F8DA8', '121F24', 'F5C59F', 'D64D2B', 'BD412D']
cn_std_colors_rgb = ['rgb(127, 141, 168)', 'rgb(18, 31, 36)', 'rgb(245, 197, 15)',
                     'rgb(214, 77, 43)', 'rgb(189, 65, 45)']

def connect_sqlalchemy_GC():
    """
    Create SQLalchemy connection with PostgreSQL database
    :return: SQLalchemy connection
    """
    
    with open('config.yml', 'r') as f:
        config = yaml.load(f.read())
    
    server = config['servers']['pgAdminGC']
    
    host = server['host']
    database = server['database']
    user = server['user']
    password = server['password']

    from sqlalchemy import create_engine
    url = 'postgresql://{}:{}@{}/{}'
    url = url.format(user, password, host, database)
    return create_engine(url)

