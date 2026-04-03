import streamlit as st

def inject_styles():
    """Injects the custom premium theme and CSS overrides."""
    st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #F0EEE9;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #2D1E17 !important;
        color: white !important;
        border-right: none;
    }
    
    section[data-testid="stSidebar"] .stMarkdown h1, 
    section[data-testid="stSidebar"] .stMarkdown h2, 
    section[data-testid="stSidebar"] .stMarkdown h3,
    section[data-testid="stSidebar"] label {
        color: #FFFFFF !important;
    }

    /* Sidebar Radio Buttons */
    div[data-testid="stSidebarNav"] { padding-top: 2rem; }
    .st-emotion-cache-1vt4y6f { color: #D1D1D1; }
    div[data-testid="stSidebar"] .st-bs { background-color: transparent !important; }
    
    /* Global Rounded Corners */
    .stMetric, .stPlotlyChart, div.stButton > button, .stDataFrame, .stSlider, .stNumberInput {
        border-radius: 20px !important;
    }

    /* Banner Styling */
    .welcome-banner {
        background-color: #C09756;
        color: white;
        padding: 2.5rem;
        border-radius: 25px;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    .welcome-banner h1 { margin: 0; font-size: 2rem; font-weight: 700; color: white !important; }
    .welcome-banner p { margin: 0.5rem 0 0; opacity: 0.9; font-size: 1.1rem; color: white !important; }

    /* Card Styling */
    .custom-card {
        background-color: white;
        padding: 2rem;
        border-radius: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
    }

    /* Metric Styling */
    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #EAEAEA;
        padding: 20px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    [data-testid="stMetricValue"] { color: #2D1E17 !important; font-weight: 700 !important; }

    /* Sidebar Navigation Links */
    .sidebar-brand {
        padding: 1.5rem 1rem;
        font-size: 1.8rem;
        font-weight: 800;
        color: #FFFFFF;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Hide standard sidebar radio circle */
    [data-testid="stSidebar"] .st-ba { display: none !important; }
    
    /* Style radio selection as pills */
    [data-testid="stSidebar"] div[role="radiogroup"] label {
        padding: 10px 15px !important;
        border-radius: 12px !important;
        margin-bottom: 5px !important;
        transition: 0.2s;
        cursor: pointer;
    }
    [data-testid="stSidebar"] div[role="radiogroup"] label:hover { background-color: rgba(255,255,255,0.05); }
    [data-testid="stSidebar"] div[role="radiogroup"] label[data-selected="true"] {
        background-color: #C09756 !important;
        color: white !important;
    }

    /* Main Area Text */
    div.main .stMarkdown h1, div.main .stMarkdown h2, div.main .stMarkdown h3,
    div.main h1, div.main h2, div.main h3, div.main label, div.main p, div.main span {
        color: #2D1E17 !important;
    }
    [data-testid="stHeader"] { background-color: rgba(0,0,0,0) !important; }
    [data-testid="stMetricLabel"], [data-testid="stSidebarNav"] label { color: #2D1E17 !important; }
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { color: #D1D1D1 !important; }
    .stSlider > div > div > div > div { background-color: #C09756 !important; }
</style>
""", unsafe_allow_html=True)
