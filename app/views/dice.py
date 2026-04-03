import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from app.utils.simulations import run_dice_simulation

def render_dice():
    """Renders the Dice Monte Carlo simulation page."""
    st.markdown('<div class="welcome-banner"><h1>Dice Monte Carlo</h1><p>Analyze random variable aggregation and probability convergence.</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.subheader("Simulation Config")
        n_trials = st.slider("Trials (N)", 100, 100000, 10000, step=100)
        target_sum = st.slider("Target Sum", 2, 12, 7, step=1)
        run_dice = st.button("Run Simulation", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("Concept Explanation: Monte Carlo & LLN", expanded=False):
        st.write("""
        **Monte Carlo Simulation** uses repeated random sampling to obtain numerical results. It is based on the **Law of Large Numbers (LLN)**, 
         which states that the average of the results obtained from a large number of trials should be close to the expected value 
         and will tend to become closer as more trials are performed.
        """)
        st.markdown("### Mathematical Insight")
        st.write("The probability of a specific sum $S$ from two dice is given by:")
        st.latex(r"P(S=k) = \frac{\text{Number of ways to get sum } k}{36}")
        st.write(f"For example, if Target Sum is 7, the ways are (1,6), (2,5), (3,4), (4,3), (5,2), (6,1).")
        st.latex(r"P(S=7) = \frac{6}{36} = 0.1667")

    with st.expander("How It Works: Step-by-Step", expanded=False):
        st.write("""
        1. **Generate Random Values:** For each trial, generate two independent random integers between 1 and 6.
        2. **Compute Sum:** Add the two values to get the trial's sum.
        3. **Iterate:** Repeat this process for $N$ trials (as selected in the slider).
        4. **Estimate Probability:** Calculate the frequency of the 'Target Sum' and divide by total trials $N$.
        """)

    # Cache handling
    if 'dice_results' not in st.session_state or run_dice:
        st.session_state.dice_results = run_dice_simulation(n_trials, target_sum)

    res = st.session_state.dice_results
    with col2:
        m1, m2, m3 = st.columns(3)
        m1.metric(f"Sim P(S={res['target']})", f"{res['prob']:.4f}")
        m2.metric("Exact Theoretical", f"{res['exact_prob']:.4f}")
        m3.metric("Calculation Error", f"{abs(res['prob'] - res['exact_prob']):.4f}")

        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        df_plot = pd.DataFrame({
            'Sum': list(range(2, 13)), 
            'Simulated': [(res['all_sums'] == i).mean() for i in range(2, 13)], 
            'Analytical': [res['exact_counts'][i]/36 for i in range(2, 13)]
        })
        fig = go.Figure()
        fig.add_trace(go.Bar(x=df_plot['Sum'], y=df_plot['Simulated'], name='Simulated', marker_color='#C09756', opacity=0.8))
        fig.add_trace(go.Scatter(x=df_plot['Sum'], y=df_plot['Analytical'], name='Theoretical', line=dict(color='#1A1A1A', width=3), mode='lines+markers'))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=350, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.info("Academic Insight: Notice how the simulated bar chart aligns with the theoretical line. As you increase N (Trials), the 'Calculation Error' decreases, demonstrating the Law of Large Numbers.")
