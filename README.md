# 🏥 Predictive Chronic Disease Monitoring Tool

## Project Overview

A machine learning-powered web application designed to predict the risk of chronic diseases such as Diabetes and Heart Disease. This tool helps healthcare professionals and individuals identify high-risk patients early, enabling better prevention strategies and improved health outcomes.

### Problem Statement

In Puerto Rico, chronic diseases represent a significant public health challenge:
- **Diabetes** affects approximately 15–17% of adults
- **Heart Disease** accounts for around 20% of deaths
- Many cases are diagnosed late, leading to preventable complications

### Solution

This tool uses machine learning algorithms to analyze patient health metrics and predict disease risk, supporting:
- **Early Detection**: Identify at-risk individuals before symptoms develop
- **Better Prevention**: Enable timely interventions and lifestyle changes
- **Improved Management**: Support healthcare decision-making
- **Community Health**: Reduce chronic disease burden in Puerto Rico

## Features

### 📊 Data Explorer
- View and analyze the training dataset
- Statistical summaries and distributions
- Interactive visualizations (Glucose vs BMI, Age distribution, etc.)
- Risk level breakdowns

### 🤖 Model Training
- Automated training of multiple ML models:
  - Logistic Regression
  - Decision Tree Classifier (with hyperparameter tuning)
- Model performance comparison
- Grid search optimization for best parameters

### 🔮 Risk Prediction
- Interactive input form for patient health metrics:
  - Age, BMI, Glucose levels
  - Exercise hours, Family history
  - Blood pressure, Cholesterol
- Real-time risk predictions from multiple models
- Risk probability indicators
- Visual risk level indicators (High/Low)

### 📈 Model Performance
- Comprehensive evaluation metrics:
  - Accuracy, Precision, Recall, F1-Score
- Confusion matrix visualization
- Feature importance analysis
- Detailed classification reports

## Installation

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tomassandovalc81-web/predictive-chronic-disease-monitoring-tool.git
   cd predictive-chronic-disease-monitoring-tool
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run Locally

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Deployment on Streamlit Cloud

1. **Push to GitHub** (ensure the repository is public)
2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**
3. **Sign in with GitHub**
4. **Click "New app"**
5. **Select**:
   - Repository: `predictive-chronic-disease-monitoring-tool`
   - Branch: `main`
   - File: `app.py`
6. **Click Deploy**

**Important**: Ensure `requirements.txt` is in the root directory with compatible versions.

## Requirements

The app uses modern, compatible versions to work with Python 3.12+:

```
streamlit>=1.32.0
pandas>=2.1.0
scikit-learn>=1.3.0
numpy>=1.26.0
matplotlib>=3.8.0
plotly>=5.17.0
```

### Why These Versions?

Previous deployment failures were due to:
- **numpy==1.24.3** requires `distutils` (removed from Python 3.12+)
- **pandas==2.0.3** requires `pkg_resources` (deprecated in Python 3.12+)

**Solution**: Updated to newer versions compatible with Python 3.12+

## Project Structure

```
predictive-chronic-disease-monitoring-tool/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── config.toml          # Streamlit configuration
└── README.md                # This file
```

## Model Details

### Algorithms Used

1. **Logistic Regression**
   - Fast baseline model
   - Good for binary classification
   - Provides probability estimates

2. **Decision Tree Classifier**
   - Interpretable results
   - Hyperparameter tuning via GridSearchCV
   - Feature importance visualization
   - Better at capturing non-linear relationships

### Features (Input Variables)

- **Age**: Patient age in years
- **BMI**: Body Mass Index
- **Glucose**: Blood glucose level (mg/dL)
- **Exercise_Hours**: Weekly exercise hours
- **Family_History**: Family history of disease (0/1)
- **Blood_Pressure**: Systolic blood pressure (mmHg)
- **Cholesterol**: Total cholesterol (mg/dL)

### Target Variable

- **Risk**: 0 = Lower Risk, 1 = Higher Risk

## Data

The application uses a sample dataset with 20 patient records containing:
- Health metrics (age, BMI, glucose, blood pressure, cholesterol)
- Lifestyle factors (exercise, family history)
- Disease risk labels

This can be extended with real patient data.

## Performance Metrics

The app evaluates models using:
- **Accuracy**: Overall correctness of predictions
- **Precision**: Accuracy of positive predictions
- **Recall**: Ability to identify all positive cases
- **F1-Score**: Harmonic mean of precision and recall
- **ROC AUC**: Area under the receiver operating characteristic curve
- **Confusion Matrix**: True/False positives and negatives

## Troubleshooting

### Issue: Module not found errors for numpy/pandas
**Solution**: Ensure you're using the correct versions from `requirements.txt`
```bash
pip install -r requirements.txt --upgrade
```

### Issue: App runs locally but fails to deploy
**Solution**: 
1. Ensure `requirements.txt` is in the repository root
2. Use compatible versions (≥ Python 3.12)
3. Check that all imports in `app.py` are in `requirements.txt`

### Issue: Prediction button not responding
**Solution**: Train the models first by going to the "Model Training" page

## Future Enhancements

- [ ] Upload custom datasets via CSV
- [ ] Real-time model retraining
- [ ] Additional algorithms (Random Forest, SVM, XGBoost)
- [ ] Patient data persistence
- [ ] Multi-language support
- [ ] Mobile responsive design improvements
- [ ] Integration with electronic health records (EHR)
- [ ] Individual risk trend tracking

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request with:
- Bug fixes
- New features
- Improved documentation
- Better performance
- Additional algorithms

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## Authors

- **tomassandovalc81-web** - Original creator

## Acknowledgments

This project was created to support chronic disease prevention and early detection in Puerto Rico communities.

---

**Made with ❤️ for better health outcomes**