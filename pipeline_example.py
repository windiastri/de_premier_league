import pandas as pd
from demo_v1 import apply_discount

# 1. Extract data from source CSV
data_extracted = pd.read_csv('source_playstation_games.csv')


# 2. Transform data: Apply discount to game price
data_extracted['price'] = data_extracted.apply(apply_discount, axis=1)

# 3. Load transformed data to another CSV file
data_extracted.to_csv('target_playstation_games.csv', index=False)