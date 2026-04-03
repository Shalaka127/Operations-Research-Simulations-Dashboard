import streamlit as st

def render_sidebar():
    """Renders the custom sidebar with navigation and activity feed."""
    with st.sidebar:
        st.markdown('<div class="sidebar-brand">OR Simulations</div>', unsafe_allow_html=True)
        
        st.markdown("### Menu")
        page = st.radio(
            label="Navigation",
            options=["Dashboard", "Dice Simulation", "Queue Analysis", "Inventory Cycle", "Convergence"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        st.markdown("### Activity")
        st.caption("Latest simulations run:")
        st.caption("• Queue Analysis (2m ago)")
        st.caption("• Inventory (15m ago)")
        
        if st.button("Clear Cache", type="secondary", use_container_width=True):
            st.session_state.clear()
            st.rerun()
            
    return page
