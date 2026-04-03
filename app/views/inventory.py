import streamlit as st
from app.utils.simulations import run_inventory_simulation

def render_inventory():
    """Renders the Inventory Cycle simulation page."""
    st.markdown('<div class="welcome-banner"><h1>Inventory Cycle</h1><p>Simulate stock levels and stockout risks over time.</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.subheader("Policy Parameters")
        init_s = st.number_input("Start Stock", 10, 200, 50, step=5)
        avg_d = st.number_input("Avg Demand", 1, 30, 8)
        re_pt = st.number_input("Reorder At", 0, 50, 15)
        run_inv = st.button("Run Simulation", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("Concept Explanation: Inventory Control", expanded=False):
        st.write("""
        Inventory simulation models the trade-off between holding costs and stockout costs. 
        Uncertainty in demand makes it difficult to maintain a perfect service level.
        """)
        st.markdown("### How Demand is Generated")
        st.write("""
        In this model, daily demand follows a **Poisson Distribution**. 
        The Poisson distribution is ideal for modeling the number of times an event occurs in a fixed interval of time (e.g., items sold per day).
        """)

    with st.expander("How It Works: Operational Logic", expanded=False):
        st.write("""
        1. **Initial State:** Start Day 1 with the 'Start Stock'.
        2. **Process Demand:** Generate a random Poisson value for daily demand.
        3. **Inventory Update:** Subtract demand from opening stock. If demand > stock, record a 'Stockout'.
        4. **Reorder Check:** If closing stock $\le$ Reorder Point, immediately trigger a replenishment (adding 'Initial Stock' amount).
        """)

    if 'inv_results' not in st.session_state or run_inv:
        st.session_state.inv_results = run_inventory_simulation(init_s, avg_d, re_pt)

    ires = st.session_state.inv_results
    with col2:
        m1, m2 = st.columns(2)
        m1.metric("Stockout Events", ires['outs'], delta_color="inverse")
        m2.metric("Mean Closing Stock", f"{ires['avg']:.1f}")
        
        def style_inv(row):
            if "Stockout" in row['Status']: return ['background-color: #fce4e4; color: #cc0000;'] * len(row)
            if "Reordered" in row['Status']: return ['background-color: #e3f2fd; color: #0d47a1;'] * len(row)
            return ['background-color: #f1f8e9; color: #33691e;'] * len(row)

        st.dataframe(ires['df'].style.apply(style_inv, axis=1), use_container_width=True)

    st.warning("Risk Analysis: A low reorder point increases the risk of stockouts during high-demand days, while a high reorder point increases daily average stock (carrying cost). This simulation helps find the optimal balance.")
