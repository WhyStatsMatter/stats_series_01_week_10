# Snippet 1: Introduction to Multivariate Analysis
import seaborn as sns

sns.pairplot(df) # Scatter plot matrix
correlation_matrix = df.corr() # Correlation matrix

# Snippet 2: Principal Component Analysis (PCA)
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca_result = pca.fit_transform(df)

# Snippet 3: Cluster Analysis
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3).fit(df)
clusters = kmeans.labels_

# Snippet 4: Discriminant Analysis
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

lda = LinearDiscriminantAnalysis()
lda_result = lda.fit(X, y).transform(X)
