import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:/users/siddhika/Downloads/menu.csv")
data.head(2)

data.shape

plt.figure(figsize=(10, 4), dpi=100)
menu_category = data.Category.value_counts()
menu_category.plot.bar(color=['red', 'pink', 'pink', 'pink', 'pink',
                              'pink', 'pink', 'pink', 'pink'])
plt.title("Number of Menu Items for each Food Category")
plt.ylabel("Count")
plt.xlabel("Menu Category")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 4), dpi=100)

correlation = data['Calories'].corr(data['Calories from Fat'])
plt.scatter(data.Calories, data['Calories from Fat'], color='black')
plt.text(500, 450, 'r = {}'.format(round(correlation, 2)))
plt.xlabel("Calories")
plt.ylabel("Calories from Fat")
plt.title("Relationship between Calories and Calories from Fat")
plt.show()

data.groupby('Category')['Trans Fat'].mean()
data['saturated_cholesterol'] = data['Saturated Fat']/data['Cholesterol']*100
saturated_cholesterol = data.groupby('Category')
['saturated_cholesterol'].mean().dropna().nlargest(5)

plt.figure(figsize=(10, 4), dpi=100)
saturated_cholesterol.sort_values(ascending=False).plot.bar(color='orange')
plt.title("Top 5 food categories with the highest % Saturated Fat")
plt.ylabel("Percentage")
plt.xlabel("Menu Category")
plt.xticks(rotation=45)
plt.show()
coffee_tea = data[data.Category == 'Coffee & Tea']
coffee_tea.groupby('Item')
['saturated_cholesterol'].mean().sort_values(ascending=False)


shakes = data[data.Category == 'Smoothies & Shakes']
shakes.groupby('Item')['saturated_cholesterol'].mean().sort_values()

beef_pork = data[data.Category == 'Beef & Pork']
beef_pork.groupby('Item')['saturated_cholesterol'].mean().sort_values()

salads = data[data.Category == 'Salads']
salads.groupby('Item')['saturated_cholesterol'].mean().sort_values()

chicken_fish = data[data.Category == 'Chicken & Fish']
chicken_fish.groupby('Item')['saturated_cholesterol'].mean().sort_values()

data.groupby('Category')['Carbohydrates (% Daily Value)'].mean()

plt.figure(figsize=(10, 4), dpi=100)
plt.scatter(data['Total Fat (% Daily Value)'],
            data['Carbohydrates (% Daily Value)'], color='k')
correlation = data
['Total Fat (% Daily Value)'].corr(data['Carbohydrates (% Daily Value)'])
plt.text(125, 20, 'r = {}'.format(round(correlation, 2)))
plt.xlabel("% Total Fat")
plt.ylabel("% Total Carbohydrate")
plt.title("Relationship between % Total Fat and % Total Carbohydrate")
plt.show()

data.groupby('Category')['Vitamin A (% Daily Value)'].mean()

data.groupby('Category')['Vitamin C (% Daily Value)'].mean()

beverage = data[data.Category == 'Beverages']
beverage.groupby('Item')['Vitamin C (% Daily Value)'].mean().sort_values()

iron = data.groupby('Category')['Iron (% Daily Value)'].mean()
calcium = data.groupby('Category')['Calcium (% Daily Value)'].mean()

plt.figure(figsize=(10, 4), dpi=100)

category = iron.index
Iron = iron.values
Calcium = calcium.values

X_axis = np.arange(len(category))

plt.bar(X_axis-0.2, Iron, 0.4, label='Iron', color='pink')
plt.bar(X_axis+0.2, Calcium, 0.4, label='Calcium', color='black')


plt.xticks(X_axis, category)
plt.xlabel("Menu Categories")
plt.title("Distribution of Iron and Calcium in McDonald's Foods")
plt.xticks(rotation=45)
plt.legend()
plt.show()
