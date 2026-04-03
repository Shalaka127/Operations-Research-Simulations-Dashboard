# Operations Research Simulations Dashboard

Professional Streamlit application for modeling and analyzing stochastic processes, including Monte Carlo methods, Queuing theory, and Inventory management.

## 📁 Project Structure
The project follows a clean, modular structure for scalability and maintainability:

```text
├── app/
│   ├── main.py            # Main entry point
│   ├── pages/             # Individual simulation pages
│   ├── components/        # UI elements (Sidebar, Styles)
│   └── utils/             # Math & Simulation logic
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignored files
```

## ⚙️ Setup & Running

### 1. Requirements
Ensure you have Python 3.9+ installed.

### 2. Installation
Install the necessary dependencies:
```bash
pip install -r requirements.txt
```

### 3. Running the App
Execute the following command in your terminal:
```bash
streamlit run app/main.py
```

## 📖 Simulations Included
- **Dice Monte Carlo**: Verification of the Law of Large Numbers (LLN).
- **Queue Analysis**: M/M/1 stochastic process modeling and traffic intensity analysis.
- **Inventory Cycle**: Poisson demand simulation and stockout risk assessment.
- **Convergence Analysis**: Steady-state vs. Simulated value comparison across large sample sizes.
