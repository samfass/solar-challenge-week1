Solar Data Discovery

 🎯 Purpose & Goals
Analyze solar potential across West African countries to identify optimal locations for solar farms.  
Key Objectives:
•	Compare GHI/DNI metrics across Benin, Sierra Leone, and Togo
•	Identify seasonal patterns in solar irradiance
•	Build a predictive model for energy output

🛠 Installation
Prerequisites:  Python 3.8+  
```bash
# Clone repository
git clone https://github.com/yourusername/solar-challenge-week1.git
cd solar-challenge-week1

# Install dependencies
pip install -r requirements.txt
🚀 Usage
Run Jupyter analysis:
jupyter lab notebooks/benin_eda.ipynb
Launch Streamlit dashboard:
streamlit run app/dashboard.py
🔍 Key Features
Feature	Description
Data Cleaning	Automated outlier detection (src/clean_data.py)
EDA Notebooks	Country-specific solar analysis
Dashboard	Interactive visualization of metrics

📂 File Structure
solar-challenge-week1/
├── data/               # Processed datasets
├── notebooks/          # Jupyter analyses
├── app/                # Dashboard code
├── src/                # Python modules
│   ├── clean_data.py   # With detailed function docs
│   └── visualize.py    # Plotting utilities
└── docs/               # Technical documentation
