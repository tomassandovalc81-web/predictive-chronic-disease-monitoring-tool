import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report
)
import warnings
warnings.filterwarnings('ignore')

# Set page configuration
st.set_page_config(
    page_title="Chronic Disease Risk Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom styling
st.markdown("""
<style>
    [data-testid="stMetricValue"] {
        font-size: 30px;
    }
    .prediction-high-risk {
        background-color: #ffcccc;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff6b6b;
    }
    .prediction-low-risk {
        background-color: #ccffcc;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #51cf66;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("🏥 Predictive Chronic Disease Monitoring Tool")
st.markdown("""
This tool uses machine learning to predict the risk of chronic diseases like Diabetes and Heart Disease.
It helps identify high-risk individuals early for better prevention and management.
""")

# Initialize session state
if 'model' not in st.session_state:
    st.session_state.model = None
if 'dt_model' not in st.session_state:
    st.session_state.dt_model = None
if 'data' not in st.session_state:
    st.session_state.data = None

# Create sample dataset
def load_sample_data():
    data = pd.DataFrame({
        'Age': [25, 45, 35, 50, 23, 40, 60, 48, 33, 52, 29, 55, 30, 65, 28, 58, 42, 38, 51, 47],
        'BMI': [22, 30, 28, 35, 20, 31, 33, 29, 27, 34, 24, 36, 25, 32, 23, 37, 26, 29, 30, 31],
        'Glucose': [90, 150, 130, 180, 85, 160, 170, 140, 120, 175, 95, 185, 100, 190, 92, 188, 145, 125, 165, 155],
        'Exercise_Hours': [7, 3, 5, 2, 8, 4, 1, 3, 6, 2, 7, 1, 6, 0, 8, 1, 4, 5, 3, 2],
        'Family_History': [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
        'Blood_Pressure': [120, 140, 130, 150, 115, 145, 160, 135, 125, 155, 118, 165, 122, 170, 116, 175, 148, 128, 158, 152],
        'Cholesterol': [180, 220, 200, 240, 175, 230, 250, 210, 190, 245, 185, 255, 195, 260, 182, 258, 215, 198, 235, 225],
        'Risk': [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1]
    })
    return data

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", 
    ["📊 Data Explorer", "🤖 Model Training", "🔮 Risk Prediction", "📈 Model Performance"])

# PAGE 1: DATA EXPLORER
if page == "📊 Data Explorer":
    st.header("📊 Data Explorer")
    
    # Load data
    if st.session_state.data is None:
        st.session_state.data = load_sample_data()
    
    data = st.session_state.data
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Samples", len(data))
    with col2:
        st.metric("High Risk (1)", (data['Risk'] == 1).sum())
    with col3:
        st.metric("Low Risk (0)", (data['Risk'] == 0).sum())
    
    st.subheader("Dataset Overview")
    st.dataframe(data, use_container_width=True)
    
    st.subheader("Statistical Summary")
    st.dataframe(data.describe(), use_container_width=True)
    
    # Visualizations
    st.subheader("Data Visualizations")
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.scatter(data, x='Glucose', y='BMI', color='Risk', 
                        title='Glucose vs BMI by Risk Level',
                        labels={'Risk': 'Risk Level'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.histogram(data, x='Age', color='Risk', 
                          title='Age Distribution by Risk Level',
                          labels={'Risk': 'Risk Level'})
        st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        fig = px.scatter(data, x='Blood_Pressure', y='Cholesterol', color='Risk',
                        title='Blood Pressure vs Cholesterol',
                        labels={'Risk': 'Risk Level'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.box(data, y='Exercise_Hours', color='Risk',
                    title='Exercise Hours by Risk Level',
                    labels={'Risk': 'Risk Level'})
        st.plotly_chart(fig, use_container_width=True)

# PAGE 2: MODEL TRAINING
elif page == "🤖 Model Training":
    st.header("🤖 Model Training")
    
    if st.session_state.data is None:
        st.session_state.data = load_sample_data()
    
    data = st.session_state.data
    
    st.write("Click the button below to train the models on the sample data.")
    
    if st.button("🚀 Train Models", use_container_width=True):
        with st.spinner("Training models..."):
            # Prepare data
            X = data[['Age', 'BMI', 'Glucose', 'Exercise_Hours', 'Family_History', 'Blood_Pressure', 'Cholesterol']]
            y = data['Risk']
            
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.25, random_state=42
            )
            
            # Logistic Regression
            lr_model = LogisticRegression(max_iter=1000)
            lr_model.fit(X_train, y_train)
            st.session_state.model = lr_model
            
            # Decision Tree with Grid Search
            dt_model = DecisionTreeClassifier(random_state=42)
            param_grid = {
                'max_depth': [3, 5, 7, 10],
                'min_samples_leaf': [1, 5, 10],
                'criterion': ['gini', 'entropy']
            }
            
            grid_search = GridSearchCV(dt_model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
            grid_search.fit(X_train, y_train)
            st.session_state.dt_model = grid_search.best_estimator_
            
            st.success("✅ Models trained successfully!")
            
            # Display training metrics
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Logistic Regression")
                lr_acc = accuracy_score(y_test, lr_model.predict(X_test))
                st.metric("Accuracy", f"{lr_acc:.3f}")
            
            with col2:
                st.subheader("Decision Tree (Best)")
                dt_acc = accuracy_score(y_test, st.session_state.dt_model.predict(X_test))
                st.metric("Accuracy", f"{dt_acc:.3f}")
                st.caption(f"Best params: {grid_search.best_params_}")

# PAGE 3: RISK PREDICTION
elif page == "🔮 Risk Prediction":
    st.header("🔮 Risk Prediction")
    
    if st.session_state.dt_model is None:
        st.warning("⚠️ Models not trained yet. Please go to 'Model Training' page first.")
    else:
        st.write("Enter patient health metrics to predict chronic disease risk:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.slider("Age", min_value=18, max_value=100, value=50)
            bmi = st.slider("BMI", min_value=10.0, max_value=50.0, value=28.0, step=0.5)
            glucose = st.slider("Glucose (mg/dL)", min_value=70, max_value=300, value=130)
        
        with col2:
            exercise = st.slider("Exercise Hours/Week", min_value=0, max_value=20, value=3)
            family_history = st.selectbox("Family History of Disease", [0, 1])
            blood_pressure = st.slider("Blood Pressure (mmHg)", min_value=80, max_value=200, value=130)
        
        cholesterol = st.slider("Cholesterol (mg/dL)", min_value=100, max_value=400, value=200)
        
        if st.button("🔍 Predict Risk", use_container_width=True):
            sample = [[age, bmi, glucose, exercise, family_history, blood_pressure, cholesterol]]
            
            # Get predictions from both models
            dt_pred = int(st.session_state.dt_model.predict(sample)[0])
            dt_prob = float(st.session_state.dt_model.predict_proba(sample)[0][1])
            
            if st.session_state.model:
                lr_pred = int(st.session_state.model.predict(sample)[0])
                lr_prob = float(st.session_state.model.predict_proba(sample)[0][1])
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Decision Tree Prediction")
                if dt_pred == 1:
                    st.markdown("""
                    <div class="prediction-high-risk">
                        <h3>⚠️ Higher Risk</h3>
                        <p><strong>Probability:</strong> {:.1%}</p>
                    </div>
                    """.format(dt_prob), unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="prediction-low-risk">
                        <h3>✅ Lower Risk</h3>
                        <p><strong>Probability:</strong> {:.1%}</p>
                    </div>
                    """.format(1 - dt_prob), unsafe_allow_html=True)
            
            with col2:
                st.subheader("Logistic Regression Prediction")
                if st.session_state.model:
                    if lr_pred == 1:
                        st.markdown("""
                        <div class="prediction-high-risk">
                            <h3>⚠️ Higher Risk</h3>
                            <p><strong>Probability:</strong> {:.1%}</p>
                        </div>
                        """.format(lr_prob), unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div class="prediction-low-risk">
                            <h3>✅ Lower Risk</h3>
                            <p><strong>Probability:</strong> {:.1%}</p>
                        </div>
                        """.format(1 - lr_prob), unsafe_allow_html=True)

# PAGE 4: MODEL PERFORMANCE
elif page == "📈 Model Performance":
    st.header("📈 Model Performance")
    
    if st.session_state.data is None:
        st.session_state.data = load_sample_data()
    
    data = st.session_state.data
    
    if st.session_state.dt_model is None:
        st.warning("⚠️ Models not trained yet. Please go to 'Model Training' page first.")
    else:
        # Prepare test data
        X = data[['Age', 'BMI', 'Glucose', 'Exercise_Hours', 'Family_History', 'Blood_Pressure', 'Cholesterol']]
        y = data['Risk']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
        
        # Decision Tree metrics
        dt_preds = st.session_state.dt_model.predict(X_test)
        dt_proba = st.session_state.dt_model.predict_proba(X_test)[:, 1]
        
        st.subheader("Decision Tree Model - Performance Metrics")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Accuracy", f"{accuracy_score(y_test, dt_preds):.3f}")
        with col2:
            st.metric("Precision", f"{precision_score(y_test, dt_preds, zero_division=0):.3f}")
        with col3:
            st.metric("Recall", f"{recall_score(y_test, dt_preds, zero_division=0):.3f}")
        with col4:
            st.metric("F1-Score", f"{f1_score(y_test, dt_preds, zero_division=0):.3f}")
        
        # Confusion Matrix
        cm = confusion_matrix(y_test, dt_preds)
        fig = px.imshow(cm, labels=dict(x="Predicted", y="Actual"),
                       x=['Low Risk', 'High Risk'],
                       y=['Low Risk', 'High Risk'],
                       color_continuous_scale='Blues',
                       title='Confusion Matrix')
        st.plotly_chart(fig, use_container_width=True)
        
        # Feature Importance
        st.subheader("Feature Importance")
        feature_importance = pd.DataFrame({
            'Feature': X.columns,
            'Importance': st.session_state.dt_model.feature_importances_
        }).sort_values('Importance', ascending=False)
        
        fig = px.bar(feature_importance, x='Importance', y='Feature', orientation='h',
                    title='Feature Importance in Decision Tree')
        st.plotly_chart(fig, use_container_width=True)
        
        # Classification Report
        st.subheader("Detailed Classification Report")
        report = classification_report(y_test, dt_preds, zero_division=0, output_dict=True)
        report_df = pd.DataFrame(report).transpose()
        st.dataframe(report_df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🏥 Predictive Chronic Disease Monitoring Tool | Created to improve early detection of chronic diseases</p>
    <p>Designed for Puerto Rico community health initiatives</p>
</div>
""", unsafe_allow_html=True)
