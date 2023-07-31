# Snippet 1: Introduction to Multivariate Analysis
pairs(df) # Scatter plot matrix
correlation_matrix <- cor(df) # Correlation matrix

# Snippet 2: Principal Component Analysis (PCA)
pca <- prcomp(df, scale. = TRUE)
pca_result <- pca$x

# Snippet 3: Cluster Analysis
library(cluster)
kmeans_result <- kmeans(df, centers=3)

# Snippet 4: Discriminant Analysis
library(MASS)
lda_result <- lda(y ~ X1 + X2 + X3, data=df)
