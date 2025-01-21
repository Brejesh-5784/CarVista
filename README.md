# Documentation: CarVista ( Interactive Car Comparison Tool )

## Introduction
The **Interactive Car Comparison Tool** is a Streamlit application designed to help users compare car models from different brands based on selected features and constraints. The tool enables users to select car brands, choose features for comparison, and visualize results through interactive graphs. Additionally, it suggests the best model from each selected brand based on the provided criteria.

---

## Features
- Compare exactly 3 car brands at a time.
- Select up to 5 features for comparison.
- View a detailed comparison table for the selected cars.
- Interactive visualizations using Plotly for easy feature comparison.
- Automatic suggestion of the best model from each selected brand.

---

## Installation and Setup

### Prerequisites
- Python 3.7 or higher
- Required Python libraries:
  - Streamlit
  - Pandas
  - Plotly

### Installation Steps
1. Clone this repository or download the project files.
2. Install the required dependencies using pip:
   ```bash
   pip install streamlit pandas plotly
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
4. Open the application in your browser using the provided local URL.

---

## Usage Instructions

1. **Load the Dataset**
   - The application automatically loads the dataset from the specified path in the code (`file_path`). Ensure the file exists at the specified location.

2. **Select Car Brands**
   - Use the sidebar to select exactly 3 car brands for comparison.
   - If fewer or more than 3 brands are selected, the application will prompt a warning.

3. **Select Features**
   - Choose up to 5 features for comparison from the sidebar.
   - Features must exist in the dataset to be selectable.

4. **View Comparison**
   - The application displays a comparison table of the selected cars and features.
   - Interactive bar charts for each selected feature are generated for easy visualization.

5. **Best Model Suggestion**
   - The tool calculates an average score based on the selected features and recommends the best model from each brand.

---

## Code Structure

### `app.py`
The main Streamlit application file. It contains the following sections:

- **Dataset Loading**: Loads and preprocesses the dataset using the `load_data` function.
- **Sidebar Configuration**: Allows users to select car brands and features.
- **Comparison Logic**: Uses the `compare_cars` function to filter and display results.
- **Visualization**: Generates interactive bar charts using Plotly.

### `car_comparison_model.py`
Contains backend logic, including:

1. `load_data(file_path)`
   - Loads the dataset from a CSV file and preprocesses it.
   - Cleans the `price` column to remove currency symbols and convert values to numeric.

2. `compare_cars(df, selected_cars, selected_constraints)`
   - Validates input selections.
   - Filters the dataset based on selected car brands and features.
   - Returns a comparison DataFrame for display and visualization.

---

## Dataset Requirements

The dataset should:
- Contain a `Make` column for car brands.
- Contain a `Model` column for car models.
- Include numeric or categorical columns for features that can be selected for comparison.
- Have a `price` column for price-related comparisons.

---

## Example Dataset Structure
| Make       | Model      | Feature1 | Feature2 | price  |
|------------|------------|----------|----------|--------|
| Brand A    | Model X    | 100      | 50       | 500000 |
| Brand B    | Model Y    | 150      | 70       | 600000 |
| Brand C    | Model Z    | 200      | 90       | 700000 |

---

## Improvements and Customization
- **Graph Enhancements**: Modify graph styles and layouts in the `app.py` file for better aesthetics.
- **Additional Features**: Extend the backend to include more complex scoring algorithms or additional analysis options.
- **Dynamic Dataset Loading**: Allow users to upload their datasets via the Streamlit UI.

---

## Troubleshooting

1. **Dataset Not Found**:
   - Ensure the dataset exists at the specified `file_path`.
   - Update the `file_path` variable in `app.py` to match your dataset's location.

2. **Feature/Column Missing**:
   - Verify that all selected features exist in the dataset.

3. **Graph Issues**:
   - Ensure all selected features contain numeric data for proper visualization.

---

## License
This project is open-source and available under the MIT License.

