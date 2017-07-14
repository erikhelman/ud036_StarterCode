# Movie Website

The Movie Website project is several Python modules that take in movie information and output an HTML file to display that information, such as the director, year of release and the movie's trailer. The program can be executed by running entertainment_center.py

# media.py

This file contains the Movie() class definition. The type of information to be displayed on the web page can be modified here.

# entertainment_center.py

This file contains the content to be displayed for each instance of the Movie() class and then executes the open_movies_page function to create and display the web page.

# fresh_tomatoes.py

This file contains the HTML code for the web page as well as the functions to create the movie tiles and the HTML page.

**create_movie_tiles_content(movies)**

This function takes in the list of Movie objects and creates the HTML content to display them

**open_movies_page(movies)**

This function creates and opens the HTML page 
