import pandas as pd
import matplotlib.pyplot as plt

# Read in the CSV file
df = pd.read_csv('obesity.csv')

# Filter the data by selected characteristics
selected_df = df.loc[df['Characteristic'].isin(['Total', 'Sex', 'Race/Ethnicity'])]

# Generate the scatter plot
selected_df.plot(kind='scatter', x='Data_Value', y='Sample_Size', alpha=0.5)
plt.xlabel('Percent with Obesity')
plt.ylabel('Sample Size')
plt.title('Obesity Among Children and Adolescents Aged 2-19 Years\nby Sample Size')
plt.show()
