import pandas as pd
import matplotlib.pyplot as plt

# Read in the CSV file
df = pd.read_csv('obesity.csv')

# Filter the data by selected characteristics
selected_df = df.loc[df['Characteristic'].isin(['Total', 'Sex', 'Race/Ethnicity'])]

# Sum the values by characteristic
summed_df = selected_df.groupby('Characteristic').sum()

# Generate a pie chart
summed_df.plot(kind='pie', y='Data_Value', legend=False)
plt.ylabel('')
plt.title('Obesity Among Children and Adolescents\nAged 2-19 Years by Selected Characteristics')
plt.show()
