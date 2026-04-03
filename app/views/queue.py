import streamlit as st
import plotly.express as px
from app.utils.simulations import run_queue_simulation

def render_queue():
    """Renders the Queue Analysis simulation page."""
    st.markdown('<div class="welcome-banner"><h1>Queue Analysis</h1><p>Model M/M/1 stochastic processes and system utilisation.</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.subheader("Model Variables")
        lam = st.slider("Arrival (λ)", 0.1, 0.9, 0.5, step=0.05)
        mu = st.slider("Service (μ)", 0.2, 2.0, 1.0, step=0.05)
        q_n = st.slider("Sample Size", 50, 5000, 1000, step=50)
        run_queue = st.button("Compute Queue", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("Concept Explanation: M/M/1 Queuing", expanded=False):
        st.write("""
        An **M/M/1 queue** represents a system with Poisson arrivals (M), exponential service times (M), and a single server (1).
        - **$\lambda$ (Lambda):** Mean arrival rate (customers per unit time).
        - **$\mu$ (Mu):** Mean service rate (customers processed per unit time).
        """)
        st.markdown("### Mathematical Formulas")
        st.write("Expected waiting time in queue ($W_q$):")
        st.latex(r"W_q = \frac{\lambda}{\mu(\mu - \lambda)}")
        st.write("Expected number of customers in queue ($L_q$):")
        st.latex(r"L_q = \frac{\lambda^2}{\mu(\mu - \lambda)}")

    with st.expander("How It Works: Simulation Logic", expanded=False):
        st.write("""
        1. **Inter-arrival Generation:** Use an exponential distribution with rate $\lambda$ to find when the next customer arrives.
        2. **Service Time Generation:** Use an exponential distribution with rate $\mu$ for task duration.
        3. **Compute Wait Time:** 
           $Wait = \max(0, \text{Server Free Time} - \text{Arrival Time})$
        4. **Track System State:** Update the time the server will next be free after processing the current customer.
        """)

    if 'queue_results' not in st.session_state or run_queue:
        st.session_state.queue_results = run_queue_simulation(lam, mu, q_n)

    qres = st.session_state.queue_results
    with col2:
        m1, m2, m3 = st.columns(3)
        m1.metric("Avg Wait Time", f"{qres['avg']:.3f}")
        m2.metric("Traffic Intensity", f"{qres['rho']:.2f}")
        m3.metric("Simulated Loads", f"{qres['n']:,}")

        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        fig_q = px.histogram(qres['waits'], nbins=25, title="Wait Time Distribution", color_discrete_sequence=['#C09756'])
        fig_q.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=350, margin=dict(t=40, b=40, l=40, r=40))
        st.plotly_chart(fig_q, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.info(f"Academic Insight: The Traffic Intensity $\rho = \lambda/\mu$ is currenty **{lam/mu:.2f}**. If $\rho \ge 1$, the queue becomes unstable and grows infinitely. Simulation helps visualize the random spikes in wait times even when the system is stable on average.")
