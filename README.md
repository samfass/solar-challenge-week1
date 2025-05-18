 Environment Setup

 Prerequisites
- Python 3.9+ (recommended)
- Git
- GitHub account

 1. Clone the Repository
```bash
git clone https://github.com/your-username/solar-challenge-week1.git
cd solar-challenge-week1
2. Create Virtual Environment
Option A: Using venv (built-in)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
Option B: Using Conda
conda create -n solar-env python=3.9
conda activate solar-env
3. Install Dependencies
pip install -r requirements.txt
4. Verify Installation
python --version
pip list
5. Running the Project
python main.py  # or your entry point script
6. Development Tools (Optional)
pip install -e ".[dev]"  # if you have dev dependencies
pre-commit install       # if using pre-commit hooks
CI/CD Pipeline
The GitHub Actions workflow (.github/workflows/ci.yml) automatically:
Tests on Python 3.9+
Installs dependencies from requirements.txt
Runs on every push/pull request
