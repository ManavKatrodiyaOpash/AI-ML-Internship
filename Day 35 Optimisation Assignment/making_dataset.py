import numpy as np
import pandas as pd

np.random.seed(42)

n_rows = 10000

data = {
    "LotArea": np.random.randint(2000, 20000, n_rows),
    "OverallQual": np.random.randint(1, 10, n_rows),
    "OverallCond": np.random.randint(1, 10, n_rows),
    "YearBuilt": np.random.randint(1950, 2022, n_rows),
    "TotalBsmtSF": np.random.randint(0, 3000, n_rows),
    "GrLivArea": np.random.randint(500, 4000, n_rows),
    "GarageCars": np.random.randint(0, 4, n_rows),
    "GarageArea": np.random.randint(0, 1000, n_rows),

    "Neighborhood": np.random.choice(
        ["NAmes", "CollgCr", "OldTown", "Edwards", "Somerst"], n_rows
    ),
    "HouseStyle": np.random.choice(
        ["1Story", "2Story", "1.5Fin", "SLvl"], n_rows
    ),
    "RoofStyle": np.random.choice(
        ["Gable", "Hip", "Flat"], n_rows
    ),
    "Exterior": np.random.choice(
        ["VinylSd", "HdBoard", "MetalSd", "Wd Sdng"], n_rows
    ),
    "Heating": np.random.choice(
        ["GasA", "GasW", "Grav"], n_rows
    ),
    "SaleCondition": np.random.choice(
        ["Normal", "Abnorml", "Partial"], n_rows
    )
}

df = pd.DataFrame(data)

# Create target with noise
df["SalePrice"] = (
    df["OverallQual"] * 20000 +
    df["GrLivArea"] * 50 +
    df["GarageCars"] * 15000 +
    np.random.normal(0, 20000, n_rows)
).astype(int)

# Introduce missing values (important for pipeline practice)
for col in ["LotArea", "GarageArea", "TotalBsmtSF", "Neighborhood"]:
    df.loc[df.sample(frac=0.05).index, col] = np.nan

df.to_csv("synthetic_ames_housing.csv", index=False)