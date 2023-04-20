import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors

# Sample alumni and job data
alumni_data = pd.DataFrame({
    'alum_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'skills': ['python, java, sql', 'python, c++, html', 'java, sql, html'],
    'job_preferences': ['Python Developer', 'Java Developer', 'SQL Analyst'],
    'rating': [[1, 5], [2, 4], [3, 4]]
})

jobs_data = pd.DataFrame({
    'job_id': [1, 2, 3, 4, 5],
    'job_title': ['Python Developer', 'Java Developer', 'Web Designer', 'SQL Analyst', 'UI/UX Designer'],
    'requirements': ['python, sql', 'java, c++, sql', 'html, css', 'sql', 'html, css, javascript']
})

# Content-based filtering
# Create a CountVectorizer object to convert skill strings into feature vectors
vectorizer = CountVectorizer()

# Convert skill strings into feature vectors for alumni and jobs
alumni_vectors = vectorizer.fit_transform(alumni_data['skills']).toarray()
jobs_vectors = vectorizer.transform(jobs_data['requirements']).toarray()

# Compute cosine similarities between alumni and job feature vectors
cosine_similarities = cosine_similarity(alumni_vectors, jobs_vectors)

# Collaborative filtering
# Create a user-item matrix where rows represent alumni and columns represent jobs
user_item_matrix = pd.pivot_table(data=alumni_data, index='alum_id', columns='job_preferences', values='rating')

# Train a k-nearest neighbors model on the user-item matrix
model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
model_knn.fit(user_item_matrix)

# Create a dictionary of alumni profiles
alumni_data_dict = alumni_data.set_index('alum_id').T.to_dict()

# Create a list of recommended jobs for each alumni profile
job_recommendations = []
for i in range(cosine_similarities.shape[0]):
    # Content-based filtering
    sorted_indices = cosine_similarities[i].argsort()[::-1]
    top_jobs = jobs_data.iloc[sorted_indices]['job_title'].tolist()
    content_based_jobs = [job for job in top_jobs if job in alumni_data_dict[i+1]['job_preferences']]
    
    # Collaborative filtering
    _, indices = model_knn.kneighbors(user_item_matrix.loc[i+1].values.reshape(1,-1), n_neighbors=3)
    collab_based_jobs = [user_item_matrix.columns[j] for j in indices.flatten()]
    
    # Hybrid filtering
    recommended_jobs = list(set(content_based_jobs + collab_based_jobs))
    job_recommendations.append(recommended_jobs)

# Add job
