import streamlit as st
from data.definitions import DATA_DEFINITIONS

def init_session_state():
    if 'selected_sources' not in st.session_state:
        st.session_state.selected_sources = []

def format_option_label(source_name):
    """Formats the label for multiselect to include icons."""
    return f"{DATA_DEFINITIONS[source_name]['icon']} {source_name}"

def handle_select_unselect_all_buttons():
    """Handles the dynamic Select All / Unselect All button for the individual buttons."""
    all_source_names = list(DATA_DEFINITIONS.keys())
    
    if len(st.session_state.selected_sources) == len(all_source_names):
        # All are selected, so unselect all
        st.session_state.selected_sources = []
    else:
        # Not all are selected (or none are), so select all
        st.session_state.selected_sources = all_source_names
    st.rerun()

def clear_all_selections():
    """Clears all selected data sources."""
    st.session_state.selected_sources = []
    st.rerun()
