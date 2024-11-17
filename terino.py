from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd


data = pd.DataFrame({"query": ["IA", "Machine Learning", "Big Data", "IA no Brasil"]})


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["query"])


kmeans = KMeans(n_clusters=2, random_state=0)
data["cluster"] = kmeans.fit_predict(X)

print(data)
