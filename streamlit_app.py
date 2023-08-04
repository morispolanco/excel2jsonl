import streamlit as st
import pandas as pd
import json

def to_jsonl(df):
    """
    Convert dataframe to jsonl format.
    """
    jsonl = ""
    for i, row in df.iterrows():
        row_dict = row.to_dict()
        jsonl += json.dumps(row_dict) + "\n"
    return jsonl

def main():
    st.set_page_config(page_title="Excel to JSONL Converter")

    st.header("Excel to JSONL Converter")

    file = st.file_uploader("Upload Excel file", type=['xlsx'])

    if file:
        df = pd.read_excel(file)
        jsonl = to_jsonl(df)

        st.text_area("Output", value=jsonl, height=400)

        # Add download button
        st.download_button(
            "Download JSONL",
            data=jsonl,
            file_name="output.jsonl",
            mime="text/csv")

if __name__ == "__main__":
    main()
