import streamlit as st

def main():
    st.title("Financial Dashboard")
    
    st.write("## Overview")
    st.markdown(
        """
        Welcome to the Financial Dashboard! This dashboard provides insights into financial data.
        """
    )
    
    st.write("## GDP Analysis")
    st.write(
        """
        This section provides analysis of GDP trends over time.
        """
    )
    
    
    st.write("## Import/Export Analysis")
    st.write(
        """
        This section provides analysis of import / export trends over time.
        """
    )
    
    st.write("## Pakistan Products import / export Analysis")
    st.write(
        """
        This section provides analysis of Products import / export trends over time.
        """
    )
    
    st.write("## Population")
    st.write(
        """
        This section provides Population analysis trends over time.
        """
    )
    
    st.write("## Portfolio")
    st.write(
        """
        This is my Portfolio
        """
    )
    st.write("## About Us")
    st.write(
        """
        We are a team of financial analysts dedicated to providing valuable insights and analysis for investors and businesses.
        """
    )

if __name__ == "__main__":
    main()

