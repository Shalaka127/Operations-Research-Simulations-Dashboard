import streamlit as st
import pandas as pd
import plotly.express as px

def render_home():
    """Renders the dashboard main landing page."""
    st.markdown(f"""
    <div class="welcome-banner">
        <h1>Operations Research Simulations Dashboard</h1>
        <p>Monte Carlo simulation, Queueing theory, Inventory management, and Analytical convergence analysis.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Key Insights Overview")
    colA, colB, colC, colD = st.columns(4)
    colA.metric("Active Models", "4", "Ready")
    colB.metric("Total Trials Run", "25,000", "+500")
    colC.metric("System Efficiency", "92%", "Optimal")
    colD.metric("Queue Latency", "1.4s", "-0.2s")

    with st.expander("Concept Explanation: Dashboard Overview", expanded=False):
        st.write("""
        Simulation is a powerful technique in Operations Research used to model the operation of a real-world process or system over time. 
        It involves the generation of an artificial history of a system and the observation of that artificial history to draw inferences 
        concerning the operating characteristics of the real system.
        
        **This dashboard covers four critical OR domains:**
        1. **Monte Carlo Methods:** Using randomness to solve problems that might be deterministic in principle.
        2. **Queueing Theory:** Mathematical study of waiting lines.
        3. **Inventory Management:** Modeling stock levels under demand uncertainty.
        4. **Convergence Analysis:** Validating simulation stability against analytical steady-state solutions.
        """)
    
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("Recent Activity Chart")
    dummy_df = pd.DataFrame({'Day': range(1, 8), 'Simulations': [12, 19, 3, 15, 22, 10, 18]})
    fig_home = px.area(dummy_df, x='Day', y='Simulations', line_shape='spline', color_discrete_sequence=['#C09756'])
    fig_home.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300, margin=dict(t=10, b=10, l=10, r=10))
    st.plotly_chart(fig_home, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
