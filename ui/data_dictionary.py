import streamlit as st
import pandas as pd

@st.cache_data
def load_data_dictionary(sheet_name):
    df = pd.read_excel("Data_Input.xlsx", sheet_name=sheet_name)

    column_map = {
        "Attribute": "Column",
        "Type": "Data Type",
        "Description": "Description",
        "Description (with Calculation)": "Description"
    }
    df = df.rename(columns=column_map)
    df = df[[col for col in ["Column", "Data Type", "Description"] if col in df.columns]]
    return df

def show_data_dictionary(sheet_name):
    df = load_data_dictionary(sheet_name)

    search_term = st.text_input(f"🔍 Search columns in {sheet_name}", key=f"search_{sheet_name}").strip()

    if search_term:
        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False, na=False).any(), axis=1)]
    else:
        filtered_df = df

    # Optional: highlight matching terms
    def highlight_text(val):
        if search_term.lower() in str(val).lower():
            return f"background-color: #fef08a"  # pale yellow highlight
        return ""

    st.dataframe(
        filtered_df.style.applymap(highlight_text),
        use_container_width=True
    )
