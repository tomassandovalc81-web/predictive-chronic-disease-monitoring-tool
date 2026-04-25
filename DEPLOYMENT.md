# 📋 Deployment Guide

## Prerequisites

- Python 3.12+
- Git
- GitHub account
- Streamlit Cloud account (free at https://streamlit.io/cloud)

## Step-by-Step Deployment to Streamlit Cloud

### 1. Local Testing (Before Deployment)

```bash
# Clone or navigate to your repository
cd predictive-chronic-disease-monitoring-tool

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

Visit `http://localhost:8501` to test the app.

### 2. Push to GitHub

```bash
git add .
git commit -m "Initial Streamlit app for chronic disease monitoring"
git push origin main
```

### 3. Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Click **"New app"**
3. Select your GitHub repository:
   - **Repository**: `tomassandovalc81-web/predictive-chronic-disease-monitoring-tool`
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. Click **Deploy**

### 4. Streamlit Cloud will:
- ✅ Clone your repository
- ✅ Install dependencies from `requirements.txt`
- ✅ Run the app
- ✅ Provide a public URL

Your app will be live at: `https://[random-name].streamlit.app`

## Fixing Dependency Issues

### Issue: `ModuleNotFoundError: No module named 'distutils'`

**Cause**: Old numpy/pandas versions trying to use Python 3.12 deprecated modules

**Solution**: Ensure `requirements.txt` has these compatible versions:

```
streamlit>=1.32.0
pandas>=2.1.0
scikit-learn>=1.3.0
numpy>=1.26.0
matplotlib>=3.8.0
plotly>=5.17.0
```

### Issue: `ModuleNotFoundError: No module named 'pkg_resources'`

**Cause**: Old pandas versions with setuptools dependency

**Solution**: Same as above - update to newer versions

## Monitoring Your Deployment

1. Visit your app URL
2. Check Streamlit Cloud dashboard for:
   - App logs
   - Deployment status
   - Memory usage
   - Runtime

## Making Updates

After making changes:

```bash
git add .
git commit -m "Description of changes"
git push origin main
```

Streamlit Cloud will **automatically redeploy** within seconds!

## Troubleshooting

### App takes too long to load
- Check app.py for heavy computations
- Models are trained on page load - consider caching with `@st.cache_data`

### Models not training
- Ensure scikit-learn version is compatible
- Check for numpy/pandas version conflicts

### Permission denied on GitHub
- Ensure your GitHub token is configured
- Re-authenticate at https://streamlit.io/cloud

## Environment Variables (Optional)

If you need to use secrets (API keys, etc.):

1. In Streamlit Cloud dashboard, go to **App settings → Secrets**
2. Add your secrets in TOML format:
   ```toml
   database_url = "your-secret-here"
   api_key = "another-secret"
   ```
3. Access in your app with:
   ```python
   import streamlit as st
   secret = st.secrets["api_key"]
   ```

## Performance Tips

1. **Cache computationally expensive functions**:
   ```python
   @st.cache_data
   def load_data():
       return pd.read_csv("data.csv")
   ```

2. **Use session state for models**:
   - Already implemented in app.py
   - Models stay in memory between interactions

3. **Optimize visualizations**:
   - Use Plotly for interactivity
   - Already implemented in app.py

## Next Steps

1. ✅ Deploy using this guide
2. 📊 Analyze user interactions with Streamlit analytics
3. 📈 Collect real patient data (with proper consents/privacy)
4. 🔄 Retrain models with new data
5. 🚀 Add advanced features (file uploads, multi-disease prediction, etc.)

## Support Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-cloud)
- [GitHub Pages](https://help.github.com)
- [scikit-learn Docs](https://scikit-learn.org)

---

**Your app is now ready to deploy! 🚀**
