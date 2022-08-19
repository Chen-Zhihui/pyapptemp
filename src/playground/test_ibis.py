import os
import pathlib
import ibis
dir(ibis)

pare = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))

db = ibis.sqlite.connect(os.path.normpath(pare / "geography.db" ))
print(db.list_tables())
countries = db.table("countries")
asian_countries = countries.filter(countries.continent == "AS")
density_in_asia = asian_countries.population.sum() / asian_countries.area_km2.sum()
density_in_asia.execute()
print(density_in_asia)
density_in_asia.plot()