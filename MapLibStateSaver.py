import os
import sklearn
import xml.etree.ElementTree as ET
from datetime import datetime as dt


class KMeansStateSaver:
    def __init__(self, kMeans : sklearn.cluster._kmeans.KMeans):
        self.kMeans_ = kMeans

    def save_state(self, path: str, filename: str = r''):
        try:
            if not path:
                states_dir = './states'
                if not os.path.exists(states_dir):
                    os.mkdir(states_dir)
            if not os.path.exists(path):
                os.mkdir(path)
        except Exception as e:
            print(f"Ошибка при сохранении состояния в директорию {path}: {e}")
        
        centroids = self.kMeans_.cluster_centers_
        root = ET.Element("KMeansCentroids")

        for i, centroid in enumerate(centroids):
            centroid_element = ET.SubElement(root, "Centroid", id=str(i))
            for j, value in enumerate(centroid):
                coord_element = ET.SubElement(centroid_element, "Coordinate", index=str(j))
                coord_element.text = str(value)

        if not filename:
            filename = path + '/kMeans ' + dt.now().strftime("%Y_%m_%d__%H_%M_%S") + '.xml'
        else:
            filename = path + '/' + filename

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)


class PCAStateSaver:
    def __init__(self, pca : sklearn.decomposition._pca):
        self.pca_ = pca

    def save_state(self, path: str, filename: str = r''):
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
            filename = path + '/pca ' + dt.now().strftime("%Y_%m_%d__%H_%M_%S") + '.xml'
        else:
            filename = path + '/' + filename

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)


class EMClassifierStateSaver:
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
        
        root = ET.Element("ElasticMapClassifier")
        #TODO take saving EM classifier info: coords of map into 3d PC space with their classes marks

        if not filename:
            filename = path + '//' + dt.now().strftime("%d/%m/%Y %H:%M:%S")
        else:
            filename = path + '//' + filename

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)


class SOMClassifierStateSaver:
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
        
        root = ET.Element("SomClassifier")
        #TODO take saving SOM classifier info: coords of map into som space with their classes marks

        if not filename:
            filename = path + '//' + dt.now().strftime("%d/%m/%Y %H:%M:%S")
        else:
            filename = path + '//' + filename

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
