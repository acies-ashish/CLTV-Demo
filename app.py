import streamlit as st
from config.styling import apply_custom_css
from data.definitions import DATA_DEFINITIONS
from logic.analysis import generate_cltv_analysis
from utils.session import init_session_state, format_option_label, handle_select_unselect_all_buttons, clear_all_selections
from ui.sidebar import render_sidebar
from ui.main import render_main_content

st.set_page_config(
    page_title="CLTV Data Dictionary",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_css()
init_session_state()
render_sidebar(DATA_DEFINITIONS, format_option_label, handle_select_unselect_all_buttons, clear_all_selections)
render_main_content(DATA_DEFINITIONS, generate_cltv_analysis)
