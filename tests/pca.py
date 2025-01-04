import sys
sys.path.append(r'./')

import numpy as np
from sklearn.decomposition import PCA
from MapLibStateSaver import PCAStateSaver


if __name__ == "__main__":
    X = np.random.rand(100, 10)
    pca = PCA(n_components=2).fit(X)

    pca_state_saver = PCAStateSaver(pca)
    pca_state_saver.save_state(
        path=r'./states',
        filename='pca_example.xml'
    )
