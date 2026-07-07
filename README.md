# Fundamentals of Data Science

This repository contains hands-on course materials for learning data science with Python. The content is organized as Jupyter notebooks that can be opened locally or in Google Colab, with examples covering Python basics, probability, statistics, visualization, classification, dimensionality reduction, and clustering.

The materials are suitable for beginner undergraduate learners who already know basic programming concepts and want to practice data science workflows through code.

## Course Content

| # | Module | Notebooks | Main topics |
|---|--------|-----------|-------------|
| 1 | [Introduction to Python for Data Science](./Introduction%20to%20Python%20for%20Data%20Science) | 2 | Google Colab, NumPy, Pandas, Matplotlib, exploratory data analysis, probability, distributions, descriptive statistics |
| 2 | [Random Variables](./Random%20Variables) | 2 | Discrete random variables, PMF, continuous random variables, PDF, CDF, and probability calculation |
| 3 | [Statistics](./Statistics) | 1 | Mean, median, and mode from grouped frequency tables |
| 4 | [Data Visualization](./Data%20Visualization) | 4 | Tables, bar charts, grouped bars, scatter plots, maps, Python visualization tools, and insight generation |
| 5 | [Dimensionality Reduction](./Dimensionality%20reduction) | 3 | PCA, t-SNE, image-based dimensionality reduction, and feature reduction workflows |
| 6 | [Logistic Regression](./Logistic%20Regression) | 1 | Diabetes prediction, train-test split, model training, and classification evaluation |
| 7 | [Naive Bayes](./Naive%20Bayes) | 2 | Spam classification, text vectorization, and Playing Golf classification |
| 8 | [Decision Tree](./Decision%20Tree) | 1 | Dataset creation, preprocessing, decision tree training, and prediction |
| 9 | [K-Means](./K-Means) | 1 | Mall customer segmentation and K-Means clustering |
| 10 | [DBSCAN Clustering](./DBSCAN%20Clustering) | 1 | Mall customer clustering with density-based clustering |
| 11 | [Hierarchical Clustering](./Hierarchical%20Clustering) | 1 | Mall customer clustering with hierarchical clustering |

## Notebook List

### Introduction and Foundations

- [`Introduction to Python for Data Science/01_intro_python_datascience.ipynb`](./Introduction%20to%20Python%20for%20Data%20Science/01_intro_python_datascience.ipynb)
- [`Introduction to Python for Data Science/02_probability_statistics.ipynb`](./Introduction%20to%20Python%20for%20Data%20Science/02_probability_statistics.ipynb)
- [`Random Variables/01_Discrete_RV_Tutorial_PMF.ipynb`](./Random%20Variables/01_Discrete_RV_Tutorial_PMF.ipynb)
- [`Random Variables/02_Continuous_RV_Tutorial_PDF_CDF.ipynb`](./Random%20Variables/02_Continuous_RV_Tutorial_PDF_CDF.ipynb)
- [`Statistics/03_Mean_Median_Mode_Grouped_Data.ipynb`](./Statistics/03_Mean_Median_Mode_Grouped_Data.ipynb)

### Data Visualization

- [`Data Visualization/Data_visualization_with_Python.ipynb`](./Data%20Visualization/Data_visualization_with_Python.ipynb)
- [`Data Visualization/03_Data_Visualization_Tutorial_with_Maps_and_Graphs.ipynb`](./Data%20Visualization/03_Data_Visualization_Tutorial_with_Maps_and_Graphs.ipynb)
- [`Data Visualization/04_Data_Visualization_Tutorial.ipynb`](./Data%20Visualization/04_Data_Visualization_Tutorial.ipynb)
- [`Data Visualization/05_Finding_Insights_from_Data_Tutorial.ipynb`](./Data%20Visualization/05_Finding_Insights_from_Data_Tutorial.ipynb)

### Machine Learning

- [`Dimensionality reduction/Dimensionality_reduction_using_PCA.ipynb`](./Dimensionality%20reduction/Dimensionality_reduction_using_PCA.ipynb)
- [`Dimensionality reduction/Dimensionality_reduction_using_PCA_(2).ipynb`](./Dimensionality%20reduction/Dimensionality_reduction_using_PCA_%282%29.ipynb)
- [`Dimensionality reduction/Dimensionality_reduction_image_t_sne.ipynb`](./Dimensionality%20reduction/Dimensionality_reduction_image_t_sne.ipynb)
- [`Logistic Regression/logistic_regression_diabetes_prediction.ipynb`](./Logistic%20Regression/logistic_regression_diabetes_prediction.ipynb)
- [`Naive Bayes/01_Spam_Classification_Naive_Bayes.ipynb`](./Naive%20Bayes/01_Spam_Classification_Naive_Bayes.ipynb)
- [`Naive Bayes/02_Playing_Golf_Naive_Bayes.ipynb`](./Naive%20Bayes/02_Playing_Golf_Naive_Bayes.ipynb)
- [`Decision Tree/Decision_Tree.ipynb`](./Decision%20Tree/Decision_Tree.ipynb)
- [`K-Means/K_Means_Clustering_Tutorial.ipynb`](./K-Means/K_Means_Clustering_Tutorial.ipynb)
- [`DBSCAN Clustering/DBSCAN_mall_customer.ipynb`](./DBSCAN%20Clustering/DBSCAN_mall_customer.ipynb)
- [`Hierarchical Clustering/Hierarchical_clustering_mall_customer.ipynb`](./Hierarchical%20Clustering/Hierarchical_clustering_mall_customer.ipynb)

## Datasets

The repository includes small datasets used in the tutorials:

- [`Data Visualization/supermarket_sales.csv`](./Data%20Visualization/supermarket_sales.csv)
- [`Data Visualization/tips.csv`](./Data%20Visualization/tips.csv)
- [`Dataset/PlayingGolfData.xlsx`](./Dataset/PlayingGolfData.xlsx)
- [`Dataset/caesarian.csv.arff`](./Dataset/caesarian.csv.arff)

Some notebooks also load public datasets directly through Python libraries or external sources.

## How to Use

1. Open a notebook directly on GitHub and use its Colab badge when available.
2. Or clone the repository:

   ```bash
   git clone https://github.com/fathanick/Fundamentals-of-Data-Science.git
   cd Fundamentals-of-Data-Science
   ```

3. Open the notebooks in Google Colab, Jupyter Notebook, JupyterLab, or VS Code.
4. Run the cells in order and follow the exercises inside each notebook.

## Recommended Tools

- Python 3.x
- Google Colab or Jupyter Notebook
- Common Python data science libraries: NumPy, Pandas, Matplotlib, Seaborn, SciPy, and scikit-learn

## Repository Structure

```text
Fundamentals-of-Data-Science/
├── DBSCAN Clustering/
├── Data Visualization/
├── Dataset/
├── Decision Tree/
├── Dimensionality reduction/
├── Hierarchical Clustering/
├── Introduction to Python for Data Science/
├── K-Means/
├── Logistic Regression/
├── Naive Bayes/
├── Random Variables/
├── Statistics/
└── README.md
```
