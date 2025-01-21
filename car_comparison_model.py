import pandas as pd

# Function to clean the 'price' column
def clean_price_column(df):
    # Remove any non-numeric characters (currency symbols, commas, etc.)
    df['price'] = df['price'].replace({'Rs.': '', ',': '', '₹': '', ' ': ''}, regex=True)
    
    # Convert the 'price' column to numeric, coercing errors to NaN
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    
    # Ensure any NaN values are handled (e.g., filling with 0 or removing them)
    df = df.dropna(subset=['price'])  # Or df['price'].fillna(0, inplace=True) if you'd prefer to fill NaNs
    
    return df

# Function to load the dataset
def load_data(file_path):
    try:
        # Load the dataset
        df = pd.read_csv(file_path)

        # Clean the 'price' column
        df = clean_price_column(df)
        
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Dataset not found at the specified path: {file_path}")
    except Exception as e:
        raise Exception(f"Error loading dataset: {e}")








# Function to compare selected cars based on constraints
def compare_cars(df, selected_cars, selected_constraints):
    # Ensure exactly 3 cars are selected
    if len(selected_cars) != 3:
        raise ValueError("You must select exactly 3 cars for comparison.")

    # Validate that the selected constraints exist in the dataset
    missing_columns = [col for col in selected_constraints if col not in df.columns]
    if missing_columns:
        raise ValueError(f"The following selected constraints are missing from the dataset: {', '.join(missing_columns)}")
    
    # Filter the dataset for the selected cars
    comparison_df = df[df['Make'].isin(selected_cars)]
    
    # Check if the filtered DataFrame is empty
    if comparison_df.empty:
        raise ValueError("No data available for the selected cars.")

    # Include only relevant columns and handle missing values
    comparison_df = comparison_df[['Make', 'Model'] + selected_constraints].fillna('nil')
    
    return comparison_df

