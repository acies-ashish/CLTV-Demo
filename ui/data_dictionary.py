# ui/data_dictionary.py

import streamlit as st
import pandas as pd

# Explicit mapping between logical data source names and Excel sheet names
SHEET_NAME_MAP = {
    "Transactional": "transactional",
    "Order": "orders",
    "Demographic": "demographic",
    "Behavioral": "behavioral",
    "Audit Data": "audit",
    "Marketing Touchpoint": "marketing_touchpoint",
    "Referral / Network Data": "referral_or_network",
    "Subscription / Plan": "subscription_or_plan",
    "Customer Support": "customer_support",
    "Psychographic Data": "psychographic",
    "Social/Sentiment Data": "social_or_sentiment",
    "Device / Tech Stack Data": "device_or_techstack",
    "Economic / Environmental Data": "economic_or_environment",
    "Cost Table": "cost"
}

@st.cache_data
def load_data_dictionary(sheet_name):
    df = pd.read_excel("Data_Input.xlsx", sheet_name=sheet_name)
    column_map = {
        "Attribute": "Column",
        "Type": "Data Type",
        "Description": "Description",
        "Typical Values": "Typical Values"
    }
    df = df.rename(columns=column_map)
    df = df[[col for col in ["Column", "Data Type", "Description", "Typical Values"] if col in df.columns]]
    return df

def get_data_dictionary(source_names):
    """Load data dictionaries for multiple sources using SHEET_NAME_MAP."""
    dicts = {}
    for source in source_names:
        sheet = SHEET_NAME_MAP.get(source, source)
        df = load_data_dictionary(sheet)
        df["__source"] = source  # Use logical name for 'Source'
        dicts[source] = df
    all_data = pd.concat(dicts.values(), ignore_index=True)
    return all_data

def show_data_dictionary(sheet_name):
    """Show a data dictionary for a single data source."""
    sheet = SHEET_NAME_MAP.get(sheet_name, sheet_name)
    df = load_data_dictionary(sheet)
    st.dataframe(df, use_container_width=True)

def combined_data_dictionary_table(source_names):
    """
    Generate a combined data dictionary table for multiple data sources with common fields highlighted.
    'Source' column shows 'common' for common fields, otherwise the logical source name.
    """
    all_data = get_data_dictionary(source_names)
    field_groups = all_data.groupby("Column")["__source"].agg(list).reset_index()
    common_fields = set(field_groups[field_groups["__source"].apply(lambda x: len(x) > 1)]["Column"])

    # Build rows for display
    rows = []
    already_added_common = set()
    for _, row in field_groups.iterrows():
        col_name = row["Column"]
        sources = row["__source"]
        is_common = len(sources) > 1
        if is_common:
            if col_name not in already_added_common:
                rec = all_data[all_data["Column"] == col_name].iloc[0]
                rows.append({
                    "Source": "common",
                    "Column": rec["Column"],
                    "Data Type": rec.get("Data Type", ""),
                    "Description": rec.get("Description", ""),
                    "Typical Values": rec.get("Typical Values", "")
                })
                already_added_common.add(col_name)
        else:
            rec = all_data[(all_data["Column"] == col_name) & (all_data["__source"] == sources[0])].iloc[0]
            rows.append({
                "Source": sources[0],
                "Column": rec["Column"],
                "Data Type": rec.get("Data Type", ""),
                "Description": rec.get("Description", ""),
                "Typical Values": rec.get("Typical Values", "")
            })

    # Assemble and sort the output
    df_out = pd.DataFrame(rows)
    df_out_common = df_out[df_out["Source"] == "common"].sort_values("Column")
    df_out_unique = df_out[df_out["Source"] != "common"].sort_values(["Source", "Column"])
    final_df = pd.concat([df_out_common, df_out_unique], ignore_index=True)

    # Style: highlight common fields with pale blue background
    def highlight_common(row):
        if row["Source"] == "common":
            return ['background-color: #dbeafe'] * len(row)
        return [''] * len(row)

    st.dataframe(
        final_df.style.apply(highlight_common, axis=1),
        use_container_width=True
    )

def show_data_dictionary_combined(source_names):
    """
    Display the combined data dictionary for a list of logical data sources.
    """
    st.markdown(f"#### Combined Data Dictionary: ")
    combined_data_dictionary_table(source_names)
