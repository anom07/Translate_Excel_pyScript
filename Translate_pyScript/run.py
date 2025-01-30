import pandas as pd
from deep_translator import GoogleTranslator

# Load the Excel file
def load_excel(file_path):
    try:
        data = pd.read_excel(file_path)
        print("Excel file loaded successfully!")
        return data
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

# Translate text function with check for valid text
def translate_text(text, target_lang='mr'):  # Changed target_lang to 'mr' for Marathi
    if not isinstance(text, str) or len(text.strip()) == 0:
        print(f"Skipping empty or non-text entry: {text}")
        return text  # Skip non-text or empty entries
    try:
        translated_text = GoogleTranslator(source='auto', target=target_lang).translate(text)
        print(f"Original: {text} -> Translated: {translated_text}")
        return translated_text
    except Exception as e:
        print(f"Error translating text '{text}': {e}")
        return text

# Translate all columns in the DataFrame
def translate_columns(df, target_lang='mr'):  # Changed target_lang to 'mr' for Marathi
    for column in df.columns:
        print(f"Translating column: {column}")
        df[column] = df[column].apply(lambda x: translate_text(x, target_lang))
    return df

# Save the translated DataFrame to a new Excel file
def save_translated_data(df, output_file):
    try:
        df.to_excel(output_file, index=False)
        print(f"Translated data saved to {output_file}")
    except Exception as e:
        print(f"Error saving the translated data: {e}")

# Main function to run the translation process
def main(input_file, output_file, target_lang='mr'):  # Changed target_lang to 'mr' for Marathi
    data = load_excel(input_file)
    if data is not None:
        print("Translating all columns in the file...")
        translated_data = translate_columns(data, target_lang)
        save_translated_data(translated_data, output_file)

# Example usage
if __name__ == "__main__":
    input_file = r"D:\projcect translate\d0.xlsx"  # Use raw string (r"")
    output_file = "translated_output_marathi.xlsx"  # Updated output file name for Marathi
    main(input_file, output_file, target_lang='mr')  # Target language set to Marathi ('mr')
