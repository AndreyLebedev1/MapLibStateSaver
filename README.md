# MapLibStateSaver Library

StateSaver — это библиотека для сохранения состояния различных моделей машинного обучения, таких как KMeans и PCA. Библиотека позволяет сохранять состояние моделей в формате XML, что упрощает их последующее использование и анализ.

## Установка

Для установки необходимых зависимостей выполните следующую команду:

`pip install -r requirements.txt`

## Использование
### Импорт библиотек
```python
from MapLibStateSaver import KMeansStateSaver, PCAStateSaver
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np
```

### Главный метод с примером использования
```python
if __name__ == "__main__":
    X = np.random.rand(100, 10) # Генерация случайных данных
    kmeans = KMeans(n_clusters=5, random_state=0, n_init="auto").fit(X)
    kmeans_state_saver = KMeansStateSaver(kMeans=kmeans)
    kmeans_state_saver.save_state(
        path=r'./states',
        filename='kmeans_example.xml'
    )
    pca = PCA(n_components=2).fit(X)
    pca_state_saver = PCAStateSaver(pca)
    pca_state_saver.save_state(
        path=r'./states',
        filename='pca_example.xml'
    )
```

## Структура сохраненных файлов XML

Состояние каждой модели сохраняется в формате XML с соответствующими элементами:

- **KMeans**
  - `Centroid`: координаты центроидов кластеров.
  
- **PCA**
  - `NumberOfComponents`: количество компонент.
  - `Components`: матрица компонент.
  - `SingularValues`: сингулярные значения.

## Тестирование

В папке `tests` находятся файлы тестирования, которые проверяют функциональность библиотеки. Вы можете запустить тесты, чтобы убедиться в корректности работы сохранения состояния моделей.