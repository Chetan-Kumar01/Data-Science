import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load and cache data
@st.cache_data
def load_data():
    iris = load_iris()
    data = pd.DataFrame(iris.data, columns=iris.feature_names)
    data['target'] = iris.target
    return data, iris.target_names

# Step 1: Load the data
data, target_names = load_data()

# Step 2: Train the model
model = RandomForestClassifier()
model.fit(data.iloc[:, :-1], data['target'])

# Step 3: Sidebar UI
st.sidebar.title("🌸 Iris Flower Classifier")

sepal_length = st.sidebar.slider(
    "Sepal Length (cm)",
    float(data['sepal length (cm)'].min()),
    float(data['sepal length (cm)'].max()),
    float(data['sepal length (cm)'].mean())
)
sepal_width = st.sidebar.slider(
    "Sepal Width (cm)",
    float(data['sepal width (cm)'].min()),
    float(data['sepal width (cm)'].max()),
    float(data['sepal width (cm)'].mean())
)
petal_length = st.sidebar.slider(
    "Petal Length (cm)",
    float(data['petal length (cm)'].min()),
    float(data['petal length (cm)'].max()),
    float(data['petal length (cm)'].mean())
)
petal_width = st.sidebar.slider(
    "Petal Width (cm)",
    float(data['petal width (cm)'].min()),
    float(data['petal width (cm)'].max()),
    float(data['petal width (cm)'].mean())
)

# Step 4: Prepare input data
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# Step 5: Make prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

# Step 6: Display output on main page
st.header("🔍 Prediction Result")
st.write("Based on the values you selected:")

st.write(f"- **Sepal Length:** {sepal_length} cm")
st.write(f"- **Sepal Width:** {sepal_width} cm")
st.write(f"- **Petal Length:** {petal_length} cm")
st.write(f"- **Petal Width:** {petal_width} cm")

st.success(f"🌼 Predicted Species: **{predicted_species.capitalize()}**")
