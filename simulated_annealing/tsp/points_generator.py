import numpy as np


europe_capitals = {
        "Berlin": (52.5200, 13.4050),
        "Paris": (48.8566, 2.3522),
        "London": (51.5074, -0.1278),
        "Barcelona": (41.3851, 2.1734),        
        "Vienna": (48.2082, 16.3738),
        "Amsterdam": (52.3676, 4.9041),
        "Kopenhagen": (55.6761, 12.5683),
        "Zagreb": (45.8150, 15.9819),
        "Tallinn": (59.4370, 24.7536),   
        "Rome": (41.9028, 12.4964),
        "Madrid": (40.4168, -3.7038),
        "Warsaw": (52.2297, 21.0122),
        "Stockholm": (59.3293, 18.0686),
        "Lisbon": (38.7223, -9.1393),
        "Prague": (50.0755, 14.4378),
        "Bukarest": (44.4268, 26.1025),
        "Athens": (37.9838, 23.7275),
        "Budapest": (47.4979, 19.0402),
        "Dublin": (53.3498, -6.2603),
        "Helsinki": (60.1695, 24.9354),
        "Brussels": (50.8503, 4.3517),
        "Luxembourg": (49.8153, 6.1296),
        "Oslo": (59.9139, 10.7522), 
        "Moscow": (55.7558, 37.6176),
        "Belgrade": (44.7866, 20.4489),
    }

max_lat = max([coord[0] for coord in europe_capitals.values()])
min_lat = min([coord[0] for coord in europe_capitals.values()])
max_lon = max([coord[1] for coord in europe_capitals.values()])
min_lon = min([coord[1] for coord in europe_capitals.values()])

def generate_europe_capitals():
    

    normalized_coords = np.zeros((len(europe_capitals), 2))  # NumPy array to store normalized coordinates

    for i, (capital, coords) in enumerate(europe_capitals.items()):
        lat = (coords[0] - min_lat) / (max_lat - min_lat)
        lon = (coords[1] - min_lon) / (max_lon - min_lon)
        normalized_coords[i] = [lat, lon]

    return np.array(normalized_coords),europe_capitals














def generate_uniform(n):
    return np.random.rand(n,2)


def generate_normal(n):
    means = [[0, 0], [5, 5], [10, 10], [15, 15]]
    covs = [[[1, 0], [0, 1]], [[1, 0.5], [0.5, 1]], [[1, -0.5], [-0.5, 1]], [[1, 0], [0, 1]]]
    points = []
    for i in range(4):
        points.append(np.random.multivariate_normal(means[i],covs[i], n // 4))
    return np.vstack(points)


def generate_one_cluster(center, n_points, spread=1.5):
    x = np.random.normal(center[0], spread, size=n_points)
    y = np.random.normal(center[1], spread, size=n_points)
    return np.column_stack((x, y))


def generate_clusters(n_points_per_cluster):  
    cluster1 = generate_one_cluster((-10, -10), n_points_per_cluster)
    cluster2 = generate_one_cluster((0, -10), n_points_per_cluster)
    cluster3 = generate_one_cluster((10, -10), n_points_per_cluster)
    cluster4 = generate_one_cluster((10, 0), n_points_per_cluster)
    cluster5 = generate_one_cluster((10, 10), n_points_per_cluster)
    cluster6 = generate_one_cluster((-15,-10 ), n_points_per_cluster)
    cluster7 = generate_one_cluster((-5, 15), n_points_per_cluster)
    cluster8 = generate_one_cluster((-15, 15), n_points_per_cluster)
    cluster9 = generate_one_cluster((-15, 0), n_points_per_cluster)

    points = np.vstack((cluster1, cluster2, cluster3,cluster4, cluster5, cluster6,cluster7, cluster8, cluster9))
    np.random.shuffle(points)
    return points