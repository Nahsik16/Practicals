import random
def initcentroids(data, k):
    return random.sample(data, k)

def assign_clusters(data, centroids):
    clusters = {}
    for x in data:
        closest_centroid = min(centroids, key=lambda c: abs(x - c))
        if closest_centroid not in clusters:
            clusters[closest_centroid] = []
        clusters[closest_centroid].append(x)
    return clusters

def update_centroids(clusters):
    new_centroids = []
    for _, point in clusters.items():
        new_centroids.append(sum(point) / len(point))
    return new_centroids

def kmeans(data, k, max_iters=100):
    centroids = initcentroids(data, k)
    for i in range(max_iters):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(clusters)
        if centroids == new_centroids:
            print(f"Converged at {i+1}th iteration")
            break
        centroids = new_centroids
    return centroids, clusters

data = [1, 2, 3, 10, 11, 12, 20, 21, 22]
k = 3

centroids, clusters = kmeans(data, k)
print("Final Centroids:", centroids)
print("Clusters:", clusters)