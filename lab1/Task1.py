import pandas as pd
import numpy as np

# Введемо дані
data = {
    'Lavyer': ['A1', 'A2', 'A3', 'A4'],
    'K1': [3, 8, 4, 9],
    'K2': [7, 3, 8, 6],
    'K3': [2, 6, 3, 5],
    'K4': [9, 7, 5, 4],
    'Weight': [8, 9, 6, 7]
}

df = pd.DataFrame(data)

# Розраховуємо функцію корисності для кожного адвоката
# Формула для обчислення функції корисності
df['Usefulness function'] = (
    df['K1'] * df['Weight'][0] + 
    df['K2'] * df['Weight'][1] + 
    df['K3'] * df['Weight'][2] + 
    df['K4'] * df['Weight'][3]
)

# Знайдемо альтернативу з максимальною функцією корисності
bestLawyer = df.loc[df['Usefulness function'].idxmax(), 'Lawyer']
print(f"Best Lawyer: {bestLawyer}")
