"""
Exercise 3

We want to ensure that each variable contributes equally to the kNN classifier,
 so we will need to scale the data by subtracting the mean of each column and 
 dividing each column by its standard deviation. Then, we will use principal 
 components to take a linear snapshot of the data from several different angles, 
 with each snapshot ordered by how well it aligns with variation in the data. 
 
 In this exercise, we will scale the numeric data and extract the first two 
 principal components
 
 """
 
from sklearn import preprocessing
scaled_data = preprocessing.scale(numeric_data)
numeric_data = pd.DataFrame(scaled_data)

from  sklearn import decomposition
pca = decomposition.PCA(numeric_data)
#Last line is wrong
#principal_components = preprocessing.LabelEncoder.fit_transform(numeric_data.iloc[:,0:2])