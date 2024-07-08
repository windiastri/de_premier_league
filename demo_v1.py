import pandas as pd


# Create the sample data
data = {
    'gamer_name': ['Aaron Stark', 'Sophia Turner', 'Michael White', 'Linda Green'],
    'game_title': ['Final Fantasy XVI', 'God of War: Ragnarok', 'The Last of Us Part III', 'Ratchet & Clank: Rift Apart'],
    'purchase_date': ['2023-01-15', '2023-01-18', '2021-12-25', '2023-01-19'],
    'price': [59.99, 69.99, 49.99, 59.99]
}


# Convert data dictionary to a DataFrame
df = pd.DataFrame(data)

# print(df)


# # Save this data to a CSV file, representing our source data
df.to_csv('source_playstation_games.csv', index=False)

# Define a function to apply discount based on purchase date
def apply_discount(row):
    if row['purchase_date'] <= '2022-12-31':
        return row['price'] * 0.9  
    return row['price']