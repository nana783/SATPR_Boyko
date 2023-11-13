import pandas as pd
import numpy as np

# Введемо дані
data = {
    'candidate': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'K1': [85, 60, 30, 75, 40],
    'K2': [30, 20, 12, 24, 15],
    'K3': [22, 10, 5, 13, 7],
    'K4': [0.65, 0.6, 0.45, 0.7, 0.55],
    'K5': [6, 7, 5, 8, 7],
    'Weight': [7, 5, 6, 8, 6]
}

df = pd.DataFrame(data)

# Нормалізуємо оцінки за кожним критерієм
for col in ['K1', 'K2', 'K3', 'K4', 'K5']:
    if col == 'K2':  # Мінімізуємо К2
        df[col] = (df[col].max() - df[col]) / (df[col].max() - df[col].min())
    else:   #Максимізуємо всі інші
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

# Розраховуємо функцію корисності для кожного кандидата
df['Usefulness function'] = (
    df['K1'] * df['Weight'][0] +
    df['K2'] * df['Weight'][1] +
    df['K3'] * df['Weight'][2] +
    df['K4'] * df['Weight'][3] +
    df['K5'] * df['Weight'][4]
)

# Знайдемо альтернативу з максимальною функцією корисності
bestAlternative = df.loc[df['Usefulness function'].idxmax(), 'candidate']
print(f"Best candidate: {bestAlternative}")

# Виводимо функції корисності
for index, row in df.iterrows():
    print(f"Usefulness function for {row['candidate']}: {row['Usefulness function']}")
