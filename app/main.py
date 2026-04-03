import streamlit as st
import sys
import os

# Add the current directory to sys.path to allow absolute imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.components.styles import inject_styles
from app.components.sidebar import render_sidebar
from app.views.home import render_home
from app.views.dice import render_dice
from app.views.queue import render_queue
from app.views.inventory import render_inventory
from app.views.convergence import render_convergence

# Page configuration
st.set_page_config(
    page_title="Operations Research Simulations Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # 1. Inject custom CSS
    inject_styles()

    # 2. Render Sidebar & Get Current Page
    page = render_sidebar()

    # 3. Routing Logic
    if page == "Dashboard":
        render_home()
    elif page == "Dice Simulation":
        render_dice()
    elif page == "Queue Analysis":
        render_queue()
    elif page == "Inventory Cycle":
        render_inventory()
    elif page == "Convergence":
        render_convergence()

if __name__ == "__main__":
    main()
