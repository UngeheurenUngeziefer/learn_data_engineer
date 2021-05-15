import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

numpy_array = np.load('Data_Engineer\Exoplanets.eu Analytics' + \
                                    '\exoplanets_data.npy', allow_pickle=True)
df = pd.DataFrame.from_records(numpy_array)

pd.set_option('display.max_columns', None)
df.head()

columns = ['granule_uid', 'mass', 'semi_major_axis']

mass_sma_df = df[['mass', 'semi_major_axis']]
mass_sma_df.dropna()

x = mass_sma_df['mass']
y = mass_sma_df['semi_major_axis']
s = mass_sma_df['mass']

plt.xlabel('Mass')
plt.ylabel('Semi Major Axis')

# plt.scatter(x, y, s=s)
# plt.show()

from time import time
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def bench_k_means(kmeans, name, data, labels):
    """Benchmark to evaluate the KMeans initialization methods.
    Parameters
    ----------
    kmeans : KMeans instance
        A :class:`~sklearn.cluster.KMeans` instance with the initialization
        already set.
    name : str
        Name given to the strategy. It will be used to show the results in a
        table.
    data : ndarray of shape (n_samples, n_features)
        The data to cluster.
    labels : ndarray of shape (n_samples,)
        The labels used to compute the clustering metrics which requires some
        supervision.
    """
    t0 = time()
    estimator = make_pipeline(StandardScaler(), kmeans).fit(data)
    fit_time = time() - t0
    results = [name, fit_time, estimator[-1].inertia_]

    # Define the metrics which require only the true labels and estimator
    # labels
    clustering_metrics = [
        metrics.homogeneity_score,
        metrics.completeness_score,
        metrics.v_measure_score,
        metrics.adjusted_rand_score,
        metrics.adjusted_mutual_info_score,
    ]
    results += [m(labels, estimator[-1].labels_) for m in clustering_metrics]

    # The silhouette score requires the full dataset
    results += [
        metrics.silhouette_score(data, estimator[-1].labels_,
                                 metric="euclidean", sample_size=300,)
    ]

    # Show the results
    formatter_result = ("{:9s}\t{:.3f}s\t{:.0f}\t{:.3f}\t{:.3f}"
                        "\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}")
    print(formatter_result.format(*results))


from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

print(82 * '_')
print('init\t\ttime\tinertia\thomo\tcompl\tv-meas\tARI\tAMI\tsilhouette')

kmeans = KMeans(init="k-means++", n_clusters=3, n_init=4,
                random_state=0)
                
bench_k_means(kmeans=kmeans, name="k-means++", data=mass_sma_df, label='1')

kmeans = KMeans(init="random", n_clusters=3, n_init=4, random_state=0)
bench_k_means(kmeans=kmeans, name="random", data=mass_sma_df, label='1')

pca = PCA(n_components=3).fit(mass_sma_df)
kmeans = KMeans(init=pca.components_, n_clusters=3, n_init=1)
bench_k_means(kmeans=kmeans, name="PCA-based", data=mass_sma_df, label='1')

print(82 * '_')