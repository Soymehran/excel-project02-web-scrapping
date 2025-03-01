### **IMDB Top 250 Movies Web Scraping & Dashboard Project**  

#### **Phase 1: Web Scraping**  
**Objective:** Extract detailed information from 250 movie pages on IMDB without using APIs.  

**Data to Extract from Each Movie Page:**  
- **Basic Info:** Title, Year, Parental Guide, Runtime (minutes), Genre(s).  
- **People Involved:** Directors, Writers, Stars (actors).  
- **Financial Data:** Gross earnings in the US & Canada.  
- **Identifiers:** Extract unique IDs for movies and people from URLs (e.g., `tt0111161` for movies, `nm0000209` for individuals).  

**Crawling Approach:**  
- Start from the main list of 250 movies and extract their individual links.  
- Visit each movie’s page and scrape the required details.  
- Store the collected data in a structured format (e.g., CSV, database).  

---

#### **Phase 2: Data Visualization & Dashboard**  
**Objective:** Build an interactive dashboard to explore movie data.  

**Required Visualizations & Features:**  
1. **Filtered Movie Table:**  
   - Users can filter based on title, genre, runtime, etc.  
2. **Bar Chart: Top 10 Highest-Grossing Movies.**  
3. **Bar Chart: Top 5 Most Frequent Actors (appearing in most movies).**  
4. **Pie Chart: Distribution of Movie Ratings (Parental Guide).**  
5. **Heatmap: Frequency of Parental Ratings by Genre.**  
6. **Count of Movies Earning Above the Average Gross of the Top 250.**  
7. **Decade-Wise Movie Distribution (How many top movies per decade).**  
8. **Interactive Bar Chart:**  
   - User selects a genre → Top-grossing movies in that genre are displayed.  

**Optional Enhancements:**  
- Additional visualizations providing deeper insights.  
- Extra filters to improve user experience.
