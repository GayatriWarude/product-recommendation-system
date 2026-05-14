import streamlit as st
import pandas as pd

# Load data
product_features = pd.read_csv('product_features.csv')

# 🔥 ADD THIS LINE
popularity_threshold = product_features['rating_count'].quantile(0.75)

# Existing block
cluster_summary = product_features.groupby('km_cluster')[['avg_rating','rating_count']].mean()

cluster_labels = {}

for cluster in cluster_summary.index:
    rating = cluster_summary.loc[cluster, 'avg_rating']
    count = cluster_summary.loc[cluster, 'rating_count']
    
    if rating >= 4.0 and count >= popularity_threshold:
        cluster_labels[cluster] = 'Top Rated & Popular'
    elif rating >= 4.0:
        cluster_labels[cluster] = 'Highly Rated'
    elif count >= popularity_threshold:
        cluster_labels[cluster] = 'Popular'
    else:
        cluster_labels[cluster] = 'Low Performing'

product_features['cluster_label'] = product_features['km_cluster'].map(cluster_labels)

# Recommendation function
def recommend_similar_products(product_id, top_n=5):
    if product_id not in product_features['productid'].values:
        return None

    cluster_id = product_features[
        product_features['productid'] == product_id
    ]['km_cluster'].values[0]

    similar_products = product_features[
        product_features['km_cluster'] == cluster_id
    ]

    similar_products = similar_products[
        similar_products['productid'] != product_id
    ]

    similar_products = similar_products.sort_values(
        by=['rating_count', 'avg_rating'],
        ascending=False
    )

    return similar_products[['productid', 'avg_rating', 'rating_count', 'cluster_label']].head(top_n)
    
# UI
st.title("🛒 Product Recommendation System")
st.markdown("### 🎯 Get similar products based on ratings & popularity")

# 🔥 ADD HERE 👇
min_rating_val = float(product_features['avg_rating'].min())
max_rating_val = float(product_features['avg_rating'].max())

min_count_val = int(product_features['rating_count'].min())
max_count_val = int(product_features['rating_count'].max())

min_rating = st.slider(
    "Minimum Rating",
    min_rating_val,
    max_rating_val,
    float(product_features['avg_rating'].mean())
)

min_count = st.slider(
    "Minimum Rating Count",
    min_count_val,
    max_count_val,
    int(product_features['rating_count'].mean())
)

top_n = st.slider(
    "Select number of recommendations",
    1, 20, 5
)

# Convert to string
product_features['productid'] = product_features['productid'].astype(str)

product_ids = sorted(product_features['productid'].unique())

selected_product = st.selectbox(
    "🔍 search and select product",
    product_ids
)


# ✅ Keep selected product after click

    
if selected_product:
    st.info(f"📌 Selected Product: {selected_product}")
    
if selected_product:
    selected_data = product_features[
        product_features['productid'] == selected_product
    ]
else:
    selected_data = pd.DataFrame()
    
st.write("### 📦 Selected Product Details")
# ✅ Safe display (no crash)
if not selected_data.empty:
    col1, col2, col3 = st.columns(3)

    col1.metric("⭐ Rating", selected_data['avg_rating'].values[0])
    col2.metric("🔥 Rating Count", selected_data['rating_count'].values[0])
    col3.metric("🏷️ Cluster Label", selected_data['cluster_label'].values[0])

# Button
if selected_product:
    result = recommend_similar_products(selected_product, top_n)

    if result is not None:

        # Apply filters
        result = result[
            (result['avg_rating'] >= min_rating) &
            (result['rating_count'] >= min_count)
        ]

        st.success(f"✨ Showing products similar to {selected_product}")

        if not result.empty:
            st.dataframe(result)
        else:
            st.warning("⚠️ No products match your selected filters. Try lowering the filters.")
    else:
        st.write("Product not found!")