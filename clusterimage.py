import streamlit as st
import pandas as pd

# Load the clustered DataFrame
df_sampled = pd.read_csv('drinks.csv')

# Define the Streamlit app
def app():
    st.title('Amazon drinks product Text-based Clustering')

    # Sidebar with cluster selection
    selected_cluster = st.sidebar.selectbox('Select Cluster', df_sampled['cluster'].unique())

    # Display links and descriptions for the selected cluster
    selected_df = df_sampled[df_sampled['cluster'] == selected_cluster]
    st.subheader(f"Cluster {selected_cluster}")
    
    for index, row in selected_df.iterrows():
        st.markdown(f"**Link:** {row['link']}")
        st.write(f"**Description:** {row['description']}")
        
        # Check if the image exists before rendering it
        if not pd.isnull(row['image']):
            # Use st.image() with the provided code snippet to display the image
            st.image(row['image'].split(" | ")[0], caption='Image', use_column_width=False, width=260)
        else:
            st.write("No image available for this item.")

    st.sidebar.subheader('Cluster Selection')
    st.sidebar.write('Choose a cluster from the dropdown to view its contents.')

    st.sidebar.write('Developed by Melissa Giramata')

# Run the Streamlit app
if __name__ == '__main__':
    app()
