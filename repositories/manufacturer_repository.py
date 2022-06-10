from db.run_sql import run_sql
from models.manufacturer import Manufacturer

def delete_all(): 
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

#def delete(id): 

def save(manufacturer): 
    sql = "INSERT INTO manufacturers (name) VALUES (%s) RETURNING id"
    values = [manufacturer.name]
    sql_results = run_sql(sql, values)
    id = sql_results[0]['id']
    manufacturer.id = id 

def select_all(): 
    manufacturers = []
    sql = "SELECT * FROM manufacturers"
    sql_results = run_sql(sql)

    for result in sql_results:
        manufacturer = Manufacturer(result['name'], result['id'])
        manufacturers.append(manufacturer)
    
    return manufacturers

#def select(id):

#def update
