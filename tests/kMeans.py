import sys
sys.path.append(r'./')

import numpy as np
from sklearn.cluster import KMeans
from MapLibStateSaver import KMeansStateSaver


if __name__ == "__main__":
    X = np.random.rand(100, 10)
    kmeans = KMeans(n_clusters=5, random_state=0, n_init="auto").fit(X)

    kmeans_state_saver = KMeansStateSaver(kMeans=kmeans)
    kmeans_state_saver.save_state(
        path=r'./states',
        filename='kmeans_example.xml'
    )
