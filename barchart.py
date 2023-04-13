import pandas as pd
import matplotlib.pyplot as plt

# Read in the CSV file
df = pd.read_csv('obesity.csv')

# Filter the data by selected characteristics
selected_df = df.loc[df['Characteristic'].isin(['Total', 'Sex', 'Race/Ethnicity'])]

# Sum the values by characteristic and gender
summed_df = selected_df.groupby(['Characteristic', 'Gender']).sum()

# Reset the index to make Gender a column instead of an index
summed_df = summed_df.reset_index()

# Generate a bar chart for each characteristic
for characteristic in selected_df['Characteristic'].unique():
    # Filter the summed data for the current characteristic
    plot_df = summed_df.loc[summed_df['Characteristic'] == characteristic]

    # Generate the bar chart
    plot_df.plot(kind='bar', x='Gender', y='Data_Value', legend=False)
    plt.xlabel('')
    plt.ylabel('Percent')
    plt.title(f'Obesity Among Children and Adolescents Aged 2-19 Years\nby {characteristic}')
    plt.show()
