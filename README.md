# project_3

project goal:
Climate can have a very real effect on home prices. As global climate change continues to trend, its effects are felt around the world in very real ways. Analyzing climate data can help identify potential effect of temperature on home values in major cities in the United States
This application can help identify trends in precipitation to identify potential changes in housing prices. Average city temperature trends are going to be used to flag housing price hotspots. 

City Selection:
When choosing major cities within the U.S. for analysis, it's essential to select a diverse range to get a comprehensive understanding of how temperature might influence home values (1 bedroom). This means considering cities from different geographic regions, with varying climates, and with distinct economic and social profiles.
We chose 14 major U.S. cities, spread across different climatic zones and representing different parts of the country:
Northeast:  New York City, NY & Boston, MA: 
Southeast: Miami, FL & Atlanta, GA
Midwest: Chicago, IL & Minneapolis, MN
South: Dallas, TX & Houston, TX
West: Los Angeles, CA & San Francisco, CA & Seattle, WA
Mountain West: Denver, CO
Desert Southwest: Phoenix, AZ & Las Vegas, NV

Application Features:
Default map of the US with 14 cities marked. Zoom into each city when clicked on. 
Drop down menu: 14 cities to choose from, map automatically zoomed into each city when selected
Home Value chart for the past five years data (montly), automatically shown according to the city selected
Temperature chart for past five years data (montly), automatically shown according to the city selected

Data Cleaning:
Combining 14 cities data into two files: Home Value and Temperature
Coverting daily temperatures to monthly by taking averages
Dates of temperature file and home value files matches (end of each month)

Summary:
1. HTML Structure:
Map & Selector: A web page is set up with a map area, a city selector dropdown, and two canvas elements for charts.
Containers: The map, selector, and charts are wrapped in divs for styling.
2. Styling:
The map, selector, and charts are styled using CSS for better appearance and layout.
3. Map Initialization:
Leaflet Map: A map is created using the Leaflet library and centered on the U.S.
City Markers: Markers for various cities are added to the map.
Swipe & Zoom: Touch swipe gestures and smooth zoom transitions are implemented for map navigation.
4. City Selector:
The dropdown is populated with the names of the cities, and a change listener is attached for updating the map view and charts when a city is selected.
5. Home Value Chart:
Data Fetching: A function is set up to fetch home value data from a server-side API.
Chart Drawing: The data is used to draw a line chart using Chart.js.
Update Function: A function is provided to update the chart based on the selected city.
6. Temperature Chart:
Similar to the home value chart, functions are created for fetching temperature data, drawing the temperature chart, and updating the chart based on the selected city.
7. Miscellaneous Scripts:
Additional scripts are included for examples and checks related to a Results variable, although this variable is not defined or used elsewhere in the provided code.
8. Event Listeners:
Event listeners are set up to update the charts and map view when a city is selected from the dropdown.

In our analysis of 14 major U.S. cities, we observed a significant decrease in home values for San Francisco, Seattle, and Minneapolis. In contrast, the remaining 11 cities exhibited a predominantly upward trend in housing prices. Despite these trends, our data did not reveal a consistent correlation between temperature variations and home values across these cities. This indicates that temperature alone may not be a decisive factor in determining property prices.
Nevertheless, our application aims to serve as a valuable resource for potential homebuyers, helping them incorporate climate considerations into their decision-making process. While the relationship between temperature and home values remains inconclusive, we believe our tool provides users with additional insights to make informed choices.
Due to time constraints, we were unable to implement certain features, such as tracking sunshine hours, monitoring air quality, and expanding our focus to include a variety of home types, beyond single-bedroom properties. These are areas we aim to address in future updates to enhance the functionality and comprehensiveness of our application.

