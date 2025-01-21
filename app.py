import streamlit as st
import pandas as pd
import plotly.express as px
from car_comparison_model import load_data, compare_cars  # Import backend functions

# Streamlit UI
st.title("Interactive Car Comparison Tool")
st.write("Compare cars based on selected features and constraints!")

# Load dataset
file_path = "/Users/brejesh/Downloads/cars/Dataset/cars_ds_final.csv"  # Replace with the actual file path
try:
    df = load_data(file_path)
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Sidebar for selecting cars and constraints
with st.sidebar:
    st.header("Select Options")

    # Dropdown for car selection
    car_makes = df['Make'].unique()
    selected_cars = st.multiselect(
        "Select exactly 3 car brands to compare:",
        car_makes,
        max_selections=3
    )

    # Warning if fewer or more than 3 cars are selected
    if len(selected_cars) != 3:
        st.warning("Please select exactly 3 car brands to proceed.")

    # Allow selection of up to 5 constraints
    all_constraints = df.columns.tolist()[3:]  # Skip columns like 'Make', 'Model', etc.
    selected_constraints = st.multiselect(
        "Select up to 5 features to compare:",
        all_constraints,
        max_selections=5
    )

# Main section: Display comparison only if valid selections are made
if len(selected_cars) == 3 and selected_constraints:
    try:
        # Generate comparison DataFrame
        comparison_df = compare_cars(df, selected_cars, selected_constraints)

        # Display comparison table
        st.write("### Comparison Table:")
        st.dataframe(comparison_df)

        # Visualize constraints with improved graphs
        st.write("### Feature Comparisons:")
        for constraint in selected_constraints:
            fig = px.bar(
                comparison_df,
                x='Model',
                y=constraint,
                color='Make',
                title=f"{constraint} Comparison",
                labels={constraint: constraint, 'Model': 'Car Model'},
                barmode='group'
            )
            st.plotly_chart(fig, use_container_width=True)

        # Suggest the best model from each brand
        st.write("### Suggested Best Models:")
        best_models = []
        for brand in selected_cars:
            brand_df = comparison_df[comparison_df['Make'] == brand]
            if not brand_df.empty:
                # Calculate the average score for each car
                brand_df['Average Score'] = brand_df[selected_constraints].mean(axis=1)
                best_model = brand_df.loc[brand_df['Average Score'].idxmax()]
                best_models.append(
                    f"**Brand:** {brand}, **Best Model:** {best_model['Model']}, **Average Score:** {best_model['Average Score']:.2f}"
                )
        for model in best_models:
            st.write(model)

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please select 3 car brands and at least one feature for comparison.")
