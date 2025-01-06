# Outlier Analysis Theory
- *Collective anomalies*: Set of sequence of data points, typically representing unusual events. 
- *Output of Outlier detection algorithms*:
  - Score: measure "outlierness" of a data point. 
  - Binary label: whether the data point is an outlier or not (typically depending on the score). 
- *Noise*: Anomalies need to be distinguished from process/system noise. 
  - Noise can be seen as *weak outliers*, while Anomalies can be seen as *strong outliers*. 
  - Separation should be quantified based on the specific application. 
- *Contextual Outliers*: Entities in a graph which are normally not connected together may show anomalous connections with each other. 

## Data Models
- Outlier detection algorithms create a data model of the normal patterns in the data, to compute outlier scores on the basis of deviations from these patterns:
  - *Generative models*: Such as gaussian-mixture models. 
  - *Linear models*: Determine distance from the best-fit (least squares) plane. Also included is dimensionality reduction: PCA. 
  - *Proximity-based models*: Model outliers as points which are isolated from the remaining data: Isolation forests, KMeans clustering, KNN (calculating distance of each point from its centroid). 
- Data models make assumptions on the normal behavior of the data. 
  - Hence satisfying data model assumptions is very important for the model chosen. 