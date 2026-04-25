# ✅ Pre-Deployment Checklist

Use this checklist before deploying to ensure everything is configured correctly.

## Local Testing

- [ ] Python 3.12+ installed (`python --version`)
- [ ] Virtual environment created: `python -m venv venv`
- [ ] Virtual environment activated
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] App runs without errors: `streamlit run app.py`
- [ ] All pages load correctly:
  - [ ] 📊 Data Explorer
  - [ ] 🤖 Model Training
  - [ ] 🔮 Risk Prediction
  - [ ] 📈 Model Performance
- [ ] Model training completes successfully
- [ ] Risk predictions work with sample data
- [ ] Visualizations display properly
- [ ] No console errors or warnings

## Repository Configuration

- [ ] Repository is public on GitHub
- [ ] All files committed: `git status` shows no uncommitted changes
- [ ] Latest changes pushed: `git push origin main`
- [ ] Files in repository:
  - [ ] `app.py` (main application)
  - [ ] `requirements.txt` (dependencies with correct versions)
  - [ ] `README.md` (project documentation)
  - [ ] `.streamlit/config.toml` (Streamlit configuration)
  - [ ] `.gitignore` (to exclude unnecessary files)

## Dependency Versions

Verify `requirements.txt` contains:
- [ ] `streamlit>=1.32.0`
- [ ] `pandas>=2.1.0`
- [ ] `scikit-learn>=1.3.0`
- [ ] `numpy>=1.26.0`
- [ ] `matplotlib>=3.8.0`
- [ ] `plotly>=5.17.0`

⚠️ **DO NOT use**: `numpy==1.24.3`, `pandas==2.0.3`, or outdated versions

## Streamlit Cloud Setup

- [ ] GitHub account logged in
- [ ] Streamlit account created at https://streamlit.io/cloud
- [ ] GitHub connected to Streamlit Cloud
- [ ] Repository is visible in Streamlit Cloud

## Deployment

- [ ] Ready to deploy at https://share.streamlit.io/
- [ ] Deployment settings:
  - Repository: `tomassandovalc81-web/predictive-chronic-disease-monitoring-tool`
  - Branch: `main`
  - Main file: `app.py`

## Post-Deployment

- [ ] App loads at provided URL
- [ ] All pages are accessible
- [ ] Interactive components work
- [ ] Models train successfully
- [ ] Predictions generate without errors
- [ ] Visualizations display correctly
- [ ] Response time is acceptable (<5 seconds)

## Troubleshooting

If you encounter any issues:

1. **App won't deploy**
   - Check Streamlit Cloud logs
   - Verify `requirements.txt` is correct
   - Ensure `app.py` runs locally first

2. **Dependencies fail**
   - Use newer Python-compatible versions
   - See README.md for version requirements

3. **Models won't train**
   - Check scikit-learn installation
   - Ensure numpy/pandas are compatible
   - Try local training first

4. **Visualizations don't show**
   - Verify plotly is installed
   - Check browser console for errors
   - Clear browser cache

## Quick Test Commands

```bash
# Test Python version
python --version  # Should be 3.12+

# Test dependencies
python -c "import streamlit; import pandas; import sklearn; print('All imports OK')"

# Test app locally
streamlit run app.py

# Push to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main
```

## Success Criteria ✨

Your deployment is successful when:
✅ App URL is publicly accessible
✅ All 4 pages load without errors
✅ Data Explorer shows the dataset
✅ Model Training trains both models
✅ Risk Prediction generates predictions
✅ Model Performance shows metrics
✅ No console errors in browser

---

**Once all items are checked, you're ready to deploy! 🚀**

For detailed deployment instructions, see `DEPLOYMENT.md`
