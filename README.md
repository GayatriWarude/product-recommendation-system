# Product Recommendation System

## Overview
This project is a Machine Learning-based Product Recommendation System developed using clustering algorithms. The system recommends similar products based on product ratings and popularity. It includes Exploratory Data Analysis (EDA), model comparison, and deployment using Streamlit.

## Features
- Product recommendation based on clustering
- Interactive Streamlit web application
- Product search and selection
- Rating and popularity filtering
- Cluster labeling for better interpretation
- Real-time recommendation display

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn

## Machine Learning Models Used
- KMeans Clustering
- Hierarchical Clustering
- DBSCAN

| Model        | Silhouette Score | Verdict      |
| ------------ | ---------------- | ------------ |
| KMeans       | 0.6478           | Selected     |
| Hierarchical | 0.6572           | Good         |
| DBSCAN       | 0.8880           | Not Suitable |

## Final Model Selection
KMeans was selected as the final model because it produced balanced and meaningful clusters while also being scalable and easy to interpret for recommendation tasks.

## Project Workflow
- Data Loading and Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Clustering Model Building
- Model Evaluation and Comparison
- Recommendation Function Development
- Streamlit Deployment

## Deployment
The project was deployed using Streamlit to create an interactive user interface where users can:
- Select products
- View product details
- Get similar product recommendations

## How to Run the Project

### 1. Clone the Repository
https://github.com/GayatriWarude/product-recommendation-system.git

### 2. Open Project Folder
cd product-recommendation-system

### 3. Install Required Libraries
pip install -r requirements.txt

### 4. Run the Streamlit Application
streamlit run app.py

## Future Improvements
- Add collaborative filtering
- Add product images and names
- Improve recommendation accuracy
- Deploy on cloud platforms

## Author
Gayatri Warude
  
