import pdb 

from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manu_repo

manufacturer1 = Manufacturer("BMW")
manu_repo.save(manufacturer1)

results = manu_repo.select_all()
for result in results: 
    print(result)

pdb.set_trace()