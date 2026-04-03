import streamlit as st
import plotly.graph_objects as go
from app.utils.simulations import run_convergence_analysis

def render_convergence():
    """Renders the Convergence Analysis page."""
    st.markdown('<div class="welcome-banner"><h1>Convergence Analysis</h1><p>Compare simulated results against analytical steady-state values.</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.subheader("Compute Config")
        c_lam = st.slider("λ Param", 0.1, 0.9, 0.4, step=0.05)
        c_mu = st.slider("μ Param", 0.5, 2.0, 1.0, step=0.05)
        run_comp = st.button("Execute Batch", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("Concept Explanation: Convergence", expanded=False):
        st.write("""
        **Convergence** refers to the tendency of simulation estimates to stabilize as the sample size increases. 
        In OR, we often compare these to 'Steady-State' analytical solutions.
        """)
        st.markdown("### Mathematical Reference")
        st.write("We compare $W_q$ (average wait in queue) against the M/M/1 formula:")
        st.latex(r"W_q = \frac{\rho}{\mu(1-\rho)} \quad \text{where } \rho = \lambda/\mu")

    with st.expander("How It Works: Batch Testing", expanded=False):
        st.write("""
        1. **Batch Intervals:** Define a sequence of customer sizes ($N=50, 100, \dots, 5000$).
        2. **Parallel Simulations:** Run a full M/M/1 simulation for each batch size.
        3. **Compare Result:** Plot the simulated average wait against the theoretical constant line.
        """)

    if 'compare_results' not in st.session_state or run_comp:
        st.session_state.compare_results = run_convergence_analysis(c_lam, c_mu)

    cres = st.session_state.compare_results
    with col2:
        m1, m2, m3 = st.columns(3)
        m1.metric("Theory Wq", f"{cres['theory']:.3f}")
        m2.metric("Final Converged Wq", f"{cres['sim'][-1]:.3f}")
        m3.metric("System Utilisation", f"{cres['rho']:.2f}")
        
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        fig_c = go.Figure()
        fig_c.add_trace(go.Scatter(x=cres['Ns'], y=cres['sim'], mode='lines+markers', name='Simulation', line=dict(color='#C09756', width=4)))
        fig_c.add_trace(go.Scatter(x=cres['Ns'], y=[cres['theory']]*len(cres['Ns']), mode='lines', name='Analytical', line=dict(color='#1A1A1A', dash='dash')))
        fig_c.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=400, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig_c, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.success("Convergence Insight: As N increases, the random variance averaging out ensures the simulation result plateaus near the analytical value. This validates that the simulation model is a reliable estimator.")
