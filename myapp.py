import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection setup
DATABASE_URI = "postgresql+psycopg2://postgres:190701@localhost:5432/Tennis_Project"
engine = create_engine(DATABASE_URI)

# Query helper function with parameterization
def execute_query(query, params=None):
    with engine.connect() as connection:
        return pd.read_sql(query, connection, params=params)

# Streamlit app
st.set_page_config(page_title="Sports Competitor Dashboard", layout="wide")

# Sidebar navigation with emojis
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Homepage Dashboard 🏆", 
    "Search & Filter Competitors 🔍", 
    "Competitor Details Viewer 👤", 
    "Country-Wise Analysis 🌍", 
    "Leaderboards 🏅"
])

# 1. Homepage Dashboard
if page == "Homepage Dashboard 🏆":
    st.title("🏆 Sports Competitor Dashboard")
    st.write("Get insights about competitors, rankings, and countries.")

    # Summary statistics
    try:
        total_competitors = execute_query("SELECT COUNT(*) AS total FROM Competitors")['total'][0]
        total_countries = execute_query("SELECT COUNT(DISTINCT country) AS total FROM Competitors")['total'][0]
        highest_points = execute_query("SELECT MAX(points) AS max_points FROM Competitor_Rankings")['max_points'][0]

        st.metric("Total Competitors", total_competitors)
        st.metric("Number of Countries Represented", total_countries)
        st.metric("Highest Points Scored", highest_points)

        st.write("### Top Insights")
        top_insights_query = """ 
        SELECT c.name AS competitor_name, c.country, cr.rank, cr.points
        FROM Competitors c
        JOIN Competitor_Rankings cr ON c.competitor_id = cr.competitor_id
        ORDER BY cr.points DESC LIMIT 5;
        """
        top_competitors = execute_query(top_insights_query)
        st.table(top_competitors)

        # Adding a graph: Competitors by Country
        st.write("### Competitors by Country")
        country_distribution_query = """
        SELECT c.country, COUNT(c.competitor_id) AS total_competitors
        FROM Competitors c
        GROUP BY c.country
        ORDER BY total_competitors DESC
        """
        country_distribution = execute_query(country_distribution_query)
        
        # Display the bar chart
        st.bar_chart(country_distribution.set_index("country")["total_competitors"])
    except Exception as e:
        st.write(f"Error fetching data: {e}")

# 2. Search & Filter Competitors
elif page == "Search & Filter Competitors 🔍":
    st.title("🔍 Search & Filter Competitors")

    # Search bar
    name_search = st.text_input("Search Competitor by Name")
    filter_rank = st.slider("Filter by Rank Range", 1, 100, (1, 10))
    filter_country = st.text_input("Filter by Country")
    filter_points = st.slider("Filter by Points Threshold", 0, 5000, 1000)

    query = """
    SELECT c.name AS competitor_name, c.country, cr.rank, cr.points
    FROM Competitors c
    JOIN Competitor_Rankings cr ON c.competitor_id = cr.competitor_id
    WHERE cr.rank BETWEEN %s AND %s AND cr.points >= %s
    """
    params = (filter_rank[0], filter_rank[1], filter_points)

    if name_search:
        query += " AND c.name ILIKE %s"
        params += ('%' + name_search + '%',)
    if filter_country:
        query += " AND c.country ILIKE %s"
        params += ('%' + filter_country + '%',)

    competitors = execute_query(query, params)
    st.table(competitors)

# 3. Competitor Details Viewer
elif page == "Competitor Details Viewer 👤":
    st.title("👤 Competitor Details Viewer")

    competitor_name = st.text_input("Enter Competitor Name")
    if competitor_name:
        query = """
        SELECT c.name AS competitor_name, c.country, cr.rank, cr.movement, cr.competitions_played, cr.points
        FROM Competitors c
        JOIN Competitor_Rankings cr ON c.competitor_id = cr.competitor_id
        WHERE c.name ILIKE %s
        """
        details = execute_query(query, (competitor_name,))
        if not details.empty:
            st.table(details)
        else:
            st.write("No competitor found with this name.")
    else:
        st.write("Please enter a competitor name.")

# 4. Country-Wise Analysis
elif page == "Country-Wise Analysis 🌍":
    st.title("🌍 Country-Wise Analysis")

    try:
        query = """
        SELECT c.country, COUNT(c.competitor_id) AS total_competitors, AVG(cr.points) AS avg_points
        FROM Competitors c
        JOIN Competitor_Rankings cr ON c.competitor_id = cr.competitor_id
        GROUP BY c.country
        """
        country_analysis = execute_query(query)
        st.table(country_analysis)

        st.write("### Bar Chart: Total Competitors by Country")
        st.bar_chart(country_analysis.set_index("country")["total_competitors"])
    except Exception as e:
        st.write(f"Error fetching country data: {e}")

# 5. Leaderboards
elif page == "Leaderboards 🏅":
    st.title("🏅 Leaderboards")

    st.write("### Top-Ranked Competitors")
    top_ranks_query = """
    SELECT c.name AS competitor_name, c.country, cr.rank, cr.points
    FROM Competitors c
    JOIN Competitor_Rankings cr ON c.competitor_id = cr.competitor_id
    ORDER BY cr.rank ASC LIMIT 10
    """
    try:
        top_ranked = execute_query(top_ranks_query)
        st.table(top_ranked)
    except Exception as e:
        st.write(f"Error fetching top-ranked competitors: {e}")

    st.write("### Competitors with the Highest Points")
    highest_points_query = """
    SELECT c.name AS competitor_name, c.country, cr.rank, cr.points
    FROM Competitors c
    JOIN Competitor_Rankings cr ON c.competitor_id = cr.competitor_id
    ORDER BY cr.points DESC LIMIT 10
    """
    try:
        highest_points = execute_query(highest_points_query)
        st.table(highest_points)
    except Exception as e:
        st.write(f"Error fetching highest points competitors: {e}")
