import streamlit as st

def render_sidebar(DATA_DEFINITIONS, format_option_label, handle_select_unselect_all_buttons, clear_all_selections):
    with st.sidebar:
        st.title("Data Filters")
        st.header("Select Your Data Sources")
        st.write("Click buttons to select or deselect data sources for CLV analysis.")

        all_source_names = list(DATA_DEFINITIONS.keys())

        for source_name in all_source_names:
            is_selected = source_name in st.session_state.selected_sources
            button_type = "primary" if is_selected else "secondary"

            if st.button(format_option_label(source_name), key=f"btn_{source_name}", type=button_type, use_container_width=True):
                if is_selected:
                    st.session_state.selected_sources.remove(source_name)
                else:
                    st.session_state.selected_sources.append(source_name)
                st.rerun()

        st.markdown("---")

        button_label = "Unselect All" if len(st.session_state.selected_sources) == len(all_source_names) else "Select All"
        if st.button(button_label, key="select_unselect_all_sidebar", use_container_width=True):
            handle_select_unselect_all_buttons()

        if st.button("Clear Selections", key="clear_selections_sidebar", use_container_width=True):
            clear_all_selections()
