import sys
import pandas as pd

# 1. Capturamos argumentos
print("arguments", sys.argv)
day = sys.argv[1]

# 2. Operación simple con Pandas
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(f"Running pipeline for day {day}")
print(df.head())

# 3. Guardar resultado
df.to_parquet(f"output_day_{day}.parquet")