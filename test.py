import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных из файла CSV
df = pd.read_csv('data\football_data.csv')

# Фильтрация данных по дате
start_date = '2021-01-01'
end_date = '2021-12-31'
mask = (df['date'] >= start_date) & (df['date'] <= end_date)
df_filtered = df.loc[mask]

# Группировка данных по командам
df_grouped = df_filtered.groupby(['team']).agg({
    'wins': np.sum,
    'draws': np.sum,
    'losses': np.sum,
    'goals_for': np.sum,
    'goals_against': np.sum,
    'points': np.sum
}).reset_index()

# Вычисление среднего количества голов, забитых и пропущенных за матч
df_grouped['avg_goals_for'] = df_grouped['goals_for'] / (df_grouped['wins'] + df_grouped['draws'] + df_grouped['losses'])
df_grouped['avg_goals_against'] = df_grouped['goals_against'] / (df_grouped['wins'] + df_grouped['draws'] + df_grouped['losses'])

# Сортировка данных по количеству набранных очков
df_sorted = df_grouped.sort_values(by=['points'], ascending=False)

# Построение диаграммы рассеяния среднего количества голов, забитых и пропущенных за матч
fig, ax = plt.subplots()
ax.scatter(df_sorted['avg_goals_for'], df_sorted['avg_goals_against'])
for i, txt in enumerate(df_sorted['team']):
    ax.annotate(txt, (df_sorted['avg_goals_for'][i], df_sorted['avg_goals_against'][i]))
plt.xlabel('Среднее количество забитых голов за матч')
plt.ylabel('Среднее количество пропущенных голов за матч')
plt.title('Среднее количество забитых и пропущенных голов за матч по командам')
plt.show()