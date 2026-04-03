# Operations Research Simulations Dashboard

A professional, interactive, and academically rigorous Streamlit application designed for modeling and analyzing stochastic processes. This dashboard provides four key simulation modules: Monte Carlo methods, Queuing theory, Inventory management, and Convergence analysis.

## Key Features
- **Dice Monte Carlo**: Verifies the Law of Large Numbers (LLN) through repeated random sampling.
- **Queue Analysis (M/M/1)**: Models single-server stochastic processes, including waiting time distribution and traffic intensity ($\rho$).
- **Inventory Cycle**: Simulates stock levels under Poisson demand uncertainty, identifying stockout risks and optimal reorder points.
- **Convergence Analysis**: Validates simulation results by comparing batch averages to steady-state analytical solutions.
- **Premium UI/UX**: Custom dark brown and golden theme with a modular sidebar navigation system.
- **Academic Documentation**: Mathematical formulas (LaTeX), step-by-step logic, and institutional-quality insights included for every module.

## Project Structure
```text
├── app/
│   ├── main.py            # Main entry point and unified routing 
│   ├── views/             # Individual simulation page content (Home, Dice, Queue, etc.)
│   ├── components/        # UI components (Sidebar rendering, Style injection)
│   └── utils/             # Core simulation logic (Math & NumPy functions)
├── requirements.txt       # Unified Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignored files
```

## Setup & Installation

### 1. Requirements
Ensure you have **Python 3.9+** installed on your system.

### 2. Local Setup
Clone the repository and install the necessary dependencies:
```bash
pip install -r requirements.txt
```

### 3. Running the Dashboard
Execute the following command in your terminal:
```bash
streamlit run app/main.py
```

## Mathematical Components
The application utilizes various mathematical concepts and distributions:
- **Poisson Distribution**: For modeling daily demand in inventory systems.
- **Exponential Distribution**: For modeling inter-arrival and service times in queuing.
- **Traffic Intensity ($\rho = \lambda/\mu$)**: For assessing system stability.
- **Theoretical Probabilities**: To validate Monte Carlo simulations against analytical benchmarks.

---
**Author:** Shalaka Gangurde  
**Course:** Operations Research (Assignment 8)
