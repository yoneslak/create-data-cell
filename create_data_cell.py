import pandas as pd
import numpy as np

# Step 1: Define parameters for synthetic data
num_samples = 1000  # Number of synthetic cells
gene_expression_range = (0, 100)  # Range for gene expression levels
stimulus_levels = ['low', 'medium', 'high']  # Possible stimulus levels
morphology_features = ['round', 'elongated', 'irregular']  # Morphological types

# Step 2: Generate synthetic data
# Generate random gene expression data
gene_expression_data = np.random.uniform(gene_expression_range[0], gene_expression_range[1], num_samples)

# Generate random stimulus levels
stimulus_data = np.random.choice(stimulus_levels, num_samples)

# Generate random morphology features
morphology_data = np.random.choice(morphology_features, num_samples)

# Step 3: Create a DataFrame
synthetic_data = pd.DataFrame({
    'Gene_Expression': gene_expression_data,
    'Stimulus_Level': stimulus_data,
    'Morphology': morphology_data
})

# Step 4: Analyze the synthetic data
# Group by stimulus level and calculate mean gene expression
mean_expression_by_stimulus = synthetic_data.groupby('Stimulus_Level')['Gene_Expression'].mean()

# Print the results
print("Mean Gene Expression by Stimulus Level:")
print(mean_expression_by_stimulus)

# Additional analysis: Count of each morphology type
morphology_counts = synthetic_data['Morphology'].value_counts()
print("\nCount of Each Morphology Type:")
print(morphology_counts)

# Additional analysis: Summary statistics of gene expression
summary_statistics = synthetic_data['Gene_Expression'].describe()
print("\nSummary Statistics of Gene Expression:")
print(summary_statistics)