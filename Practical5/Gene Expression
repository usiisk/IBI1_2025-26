print("=" * 50)
print("1. Gene Expression Analysis")
print("=" * 50)

# Create dictionary with initial genes
gene_expression = {
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}

# Print the initial dictionary
print("Initial dictionary:", gene_expression)

# Add gene MYC
gene_expression["MYC"] = 11.6
print("After adding MYC:", gene_expression)

# Bar chart of expression values
plt.figure(figsize=(8, 5))
genes = list(gene_expression.keys())
values = list(gene_expression.values())
plt.bar(genes, values, color='skyblue')
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.title("Gene Expression Levels")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Gene of interest (change this variable to test different genes)
gene_of_interest = "BRCA1"  # <- Modify this gene name to test error handling

if gene_of_interest in gene_expression:
    print(f"Expression value of {gene_of_interest}: {gene_expression[gene_of_interest]}")
else:
    print(f"Error: Gene '{gene_of_interest}' not found in the dataset.")

# Calculate average expression
average_expression = sum(gene_expression.values()) / len(gene_expression)
print(f"Average gene expression level: {average_expression:.2f}")
