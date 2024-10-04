
# Multi Language Invoice Extractor

## Project Overview

This project aims to develop a **Multi-Language Invoice Extractor** that utilizes **Gemini Pro** for accurate extraction of invoice details in various languages. It also integrates **Streamlit** to build an interactive web interface for seamless user experience.

## Key Features

- **Multi-Language Support**: The extractor is capable of processing invoices written in different languages, ensuring wide applicability across global businesses.
  
- **Accurate Invoice Extraction**: With the help of Gemini Pro, the system can accurately extract essential invoice details such as:
  - Invoice Number
  - Invoice Date
  - Total Amount
  - Tax Information
  - Vendor and Customer Details

- **Interactive UI with Streamlit**: A user-friendly interface that allows users to upload invoices and visualize extracted information in real-time.

- **Data Export**: The extracted information can be exported to various formats like CSV or JSON for further processing or analysis.

## How to Use

1. **Set Up**: Clone this repository and install the necessary dependencies using the command:
    ```bash
    pip install -r requirements.txt
    ```
2. **Run the Application**: Use the following command to start the Streamlit interface:
    ```bash
    streamlit run app.py
    ```

3. **Upload Invoice**: Upload an invoice in the supported languages via the provided UI.

4. **View and Export Data**: Once the invoice is processed, view the extracted details and export them as needed.

## Tools and Technologies Used

- **Gemini Pro**: For multi-language invoice data extraction.
- **Streamlit**: For building the interactive user interface.
- **Python**: Backend logic and data processing.

## Conclusion

The **Multi-Language Invoice Extractor** provides a powerful tool for businesses to automate the extraction of key information from invoices in various languages. With its easy-to-use interface and robust extraction capabilities, this solution can enhance the efficiency of processing financial documents.
