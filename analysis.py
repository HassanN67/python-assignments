# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

print("Task 1: Dataset Exploration")
print("=" * 50)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())
print("\n")

# Explore dataset structure
print("Dataset information:")
print(df.info())
print("\n")

print("Dataset shape:", df.shape)
print("\n")

# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())
print("\n")

# Since there are no missing values in this dataset, we don't need to clean
print("No missing values found - dataset is clean!")
print("\n" + "=" * 50 + "\n")

# Task 2: Basic Data Analysis
print("Task 2: Basic Data Analysis")
print("=" * 50)

# Basic statistics
print("Basic statistics for numerical columns:")
print(df.describe())
print("\n")

# Group by species and compute means
print("Mean values for each measurement by species:")
species_means = df.groupby('species').mean()
print(species_means)
print("\n")

# Additional analysis - find maximum values by species
print("Maximum values by species:")
species_max = df.groupby('species').max()
print(species_max)
print("\n")

# Interesting findings
print("Interesting Findings:")
print("- Setosa has the smallest measurements across all features")
print("- Virginica has the largest measurements across all features")
print("- Versicolor falls in between setosa and virginica")
print("- Sepal width shows the least variation between species")
print("\n" + "=" * 50 + "\n")

# Task 3: Data Visualization
print("Task 3: Data Visualization")
print("=" * 50)

# Set up the plotting style
plt.style.use('seaborn-v0_8')
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 1. Line chart - Trends in measurements across species (using index as pseudo-time)
plt.subplot(2, 2, 1)
for species in df['species'].unique():
    species_data = df[df['species'] == species]
    plt.plot(species_data.index[:30], species_data['sepal length (cm)'][:30], 
             label=species, marker='o', markersize=3)
plt.title('Sepal Length Trends (First 30 Samples)')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.grid(True, alpha=0.3)

# 2. Bar chart - Average measurements by species
plt.subplot(2, 2, 2)
features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
x_pos = range(len(features))
width = 0.25

for i, species in enumerate(df['species'].unique()):
    species_data = df[df['species'] == species]
    means = species_data[features].mean()
    plt.bar([p + i * width for p in x_pos], means, width=width, label=species, alpha=0.8)

plt.title('Average Measurements by Species')
plt.xlabel('Measurement Type')
plt.ylabel('Average Value (cm)')
plt.xticks([p + width for p in x_pos], features, rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)

# 3. Histogram - Distribution of sepal length
plt.subplot(2, 2, 3)
plt.hist(df['sepal length (cm)'], bins=15, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)

# 4. Scatter plot - Sepal length vs Petal length
plt.subplot(2, 2, 4)
colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
for species in df['species'].unique():
    species_data = df[df['species'] == species]
    plt.scatter(species_data['sepal length (cm)'], 
                species_data['petal length (cm)'], 
                label=species, alpha=0.7, c=colors[species])

plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Additional visualizations for better understanding
print("Additional Visualizations:")
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Box plot for species comparison
plt.subplot(1, 2, 1)
df.boxplot(column=['sepal length (cm)', 'sepal width (cm)', 
                   'petal length (cm)', 'petal width (cm)'], by='species')
plt.title('Measurement Distribution by Species')
plt.suptitle('')  # Remove automatic title
plt.xticks(rotation=45)

# Correlation heatmap
plt.subplot(1, 2, 2)
numeric_df = df.drop('species', axis=1)
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap of Measurements')

plt.tight_layout()
plt.show()

# Final observations
print("\nFinal Observations:")
print("1. Clear separation between species, especially in petal measurements")
print("2. Strong positive correlation between petal length and petal width")
print("3. Setosa is distinctly different from the other two species")
print("4. Versicolor and virginica show some overlap but are generally separable")
print("5. The dataset is well-balanced with 50 samples per species")

# Save the cleaned dataset (optional)
df.to_csv('cleaned_iris_dataset.csv', index=False)
print("\nCleaned dataset saved as 'cleaned_iris_dataset.csv'")