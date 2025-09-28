# Personal Finance Automation Tool (Streamlit) 💰📊

A simple Streamlit app that:

- Uploads a **CSV bank statement**
- Summarizes **expenses by category**
- Generates an **interactive pie chart** of expenses
- Helps you understand and track your personal finances automatically

---

## 🔧 Quick Start

### 1. Requirements
- **Python 3.9+** (recommended)

### 2. Install

Upgrade pip and install dependencies:
```bash
pip install -U pip
pip install -r requirements.txt
```

requirements.txt includes:

- streamlit
- pandas
- plotly
- numpy

### 3. Run the App

From your project folder, run:

```bash
streamlit run main.py
```

## 📂 Usage

1. Open the Streamlit web interface (default: http://localhost:8501)
2. Upload your bank statement CSV
3. The app will:
   - Process the data with pandas
   - Display an expense summary
   - Generate a pie chart with plotly

## 🖼️ Example Output

Expense summary (terminal/log output):

```
Expense Summary:
----------------
Groceries        $350
Rent             $800
Utilities        $120
Entertainment    $90
Transport        $60
```
