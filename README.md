# Game Analytics: Unlocking Tennis Data with SportRadar API

## Project Overview
The "Game Analytics" project aims to develop a comprehensive solution for managing, visualizing, and analyzing tennis competition data extracted from the Sportradar API. The application allows users to explore competition hierarchies, analyze trends, and gain insights into player performance through an interactive web interface built with Streamlit.

### Objectives
- To extract and manage tennis data using the Sportradar API.
- To store structured data in a relational database (PostgreSQL).
- To provide an interactive web application for data visualization and analysis.

## Technologies Used
- **Programming Language**: Python
- **Database**: PostgreSQL
- **Web Application Framework**: Streamlit
- **API Integration**: Sportradar API
- **Data Visualization**: Matplotlib, Pandas

## Setup Instructions

### Prerequisites
- Python 3.0 installed on your machine.
- PostgreSQL database set up.
- Access to the Sportradar API (API key required).

### Installation
1. **Install Required Packages**:
   ```bash
   pip install streamlit pandas sqlalchemy matplotlib requests
   ```
2. **Database Configuration**:
   - Create a database in PostgreSQL.
   - Update the database connection details in the `Tennisapi.ipynb` file.
   
3. **API Configuration**:
   - Obtain an API key from Sportradar.
   - Store the API key in the `Tennisapi.ipynb` file.

4. **Run the Streamlit Application**:
   ```bash
   streamlit run myapp.py
   ```
   
## Project Structure
```
Game-Analytics/
│── myapp.py                     # Main Streamlit application
│── Tennisapi.ipynb              # Configuration file for database and API keys
│── Competitions_queries.sql     # Handles queries
│── README.md                    # Project documentation
└── data/                        # Stores cached or processed data
```

## API Integration

### API Endpoints Used
- **Competitor Data**: Fetches player information.
- **Competition Data**: Retrieves tournament details.
- **Ranking Data**: Gets real-time rankings of players.

### API Request Example
```python
import requests

url = "https://api.sportradar.com/tennis/trial/v3/en/double_competitors_rankings.json?api_key=eKiOVgkKozgVXUP6CCQNkKrUjNibzgkOGfrf1uko"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
print(response.text)
```
## Database Schema

### Tables
- **Competitors Table**: Stores information about each competitor.
- **Competitor_Rankings Table**: Stores ranking-related information about competitors.
- **Categories Table**: Stores information about competition categories.
- **Competitions Table**: Stores information about competitions linked to categories.
- **Complexes Table**: Stores information about sports complexes.
- **Venues Table**: Stores information about venues linked to complexes.

### SQL Queries
- List all competitions along with their category name.
- Count the number of competitions in each category.
- Get all competitors with their rank and points.

## User Interface
The Streamlit application features an intuitive user interface with:
- A sidebar for navigation between different sections.
- Interactive widgets for searching and filtering data.
- Visualizations for better data understanding.

## Features

### Homepage Dashboard
- Displays summary statistics such as total competitors, number of countries represented, and highest points scored by a competitor.

### Competitor Analysis
- Allows users to search for competitors by name and view their ranking details.

### Country-Wise Analysis
- Lists countries with the total number of competitors and their average points, along with a bar chart visualization.

### Leaderboards
- Displays a leaderboard of the top-ranked competitors based on their points.

## Challenges and Solutions

### Challenges
- Handling API rate limits and data retrieval errors.
- Designing a normalized database schema.

### Solutions
- Implemented error handling in API calls and SQL queries.
- Followed best practices for database design to ensure data integrity.

## Future Enhancements
- Integrate additional data sources for more comprehensive analysis.
- Implement user authentication for personalized experiences.
- Enhance visualizations with more interactive charts and graphs.

## Conclusion
The "Game Analytics" project successfully demonstrates the ability to extract, manage, and visualize sports data using modern technologies. The interactive web application provides valuable insights into tennis competitions and player performance.

## References
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Sportradar API Documentation](https://developer.sportradar.com/)

   
