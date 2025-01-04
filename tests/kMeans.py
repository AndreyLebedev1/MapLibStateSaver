import os
import sys
import sklearn
import xml.etree.ElementTree as ET
import numpy as np

sys.path.append(r'./')

from datetime import datetime as dt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from MapLibStateSaver import KMeansStateSaver


class PCAStateSaver:
    def __init__(self, pca : sklearn.decomposition._pca):
        self.pca_ = pca

    def save_state(self, path: str, filename: str):
        try:
            if not path:
                states_dir = './states'
                if not os.path.exists(states_dir):
                    os.mkdir(states_dir)
            if not os.path.exists(path):
                os.mkdir(path)
        except Exception as e:
            print(f"Ошибка при сохранении состояния в директорию {path}: {e}")
        
        root = ET.Element("PCA")

        n_components = ET.SubElement(root, "NumberOfComponents")
        n_components.text = str(self.pca_.n_components)

        components = ET.SubElement(root, "Components")
        components.text = str(self.pca_.components_.tolist())

        singular_values = ET.SubElement(root, "SingularValues")
        singular_values.text = str(self.pca_.singular_values_.tolist())

        if not filename:
            filename = path + '//' + dt.now().strftime("%d/%m/%Y %H:%M:%S")
        else:
            filename = path + '//' + filename

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)



# import time

