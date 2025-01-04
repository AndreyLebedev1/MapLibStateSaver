import os
from datetime import datetime as dt

import numpy as np
import sklearn

import xml.etree.ElementTree as ET
from sklearn.cluster import KMeans


class KMeansStateSaver:
    def __init__(self, kMeans : sklearn.cluster._kmeans.KMeans):
        self.kMeans_ = kMeans

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
        
        centroids = kmeans.cluster_centers_
        root = ET.Element("KMeansCentroids")

        for i, centroid in enumerate(centroids):
            centroid_element = ET.SubElement(root, "Centroid", id=str(i))
            for j, value in enumerate(centroid):
                coord_element = ET.SubElement(centroid_element, "Coordinate", index=str(j))
                coord_element.text = str(value)

        if not filename:
            filename = path + '//' + dt.now().strftime("%d/%m/%Y %H:%M:%S")
        else:
            filename = path + '//' + filename

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)

