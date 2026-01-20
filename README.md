# Google Play Store Analytics

## Task 1 – Internship Requirement

### Objective
Compare average rating and total review count for the top 10 app categories
by number of installs using a grouped bar chart.

### Filters Applied
- Average rating ≥ 4.0
- App size < 10 MB
- Last updated month = January
- Top 10 categories by total installs

### Time-Based Condition
- Chart is visible only between **3 PM and 5 PM IST**
- Outside this window, the visualization is hidden

### Tools Used
- Python
- Pandas
- Matplotlib
- Streamlit

### Deployment
- Hosted on Streamlit Community Cloud
- Same Google Play Store dataset used during training

## Data Preprocessing

Raw datasets used:
- Play Store Data.csv
- User Reviews.csv

A preprocessing script (`preprocessing/preprocess_data.py`) was created to:
- Clean numeric and date fields
- Normalize installs, size, and price
- Aggregate user review sentiment
- Merge both datasets on App name

The processed output (`cleaned_apps.csv`) is used by all dashboard tasks.
# google-play-analytics
