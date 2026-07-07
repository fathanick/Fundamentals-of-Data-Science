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
