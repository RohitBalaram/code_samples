1. ATS Folder contains small django app that holds a large set of messy models that come from a legacy citywide student information system called ats. I'm including this because it shows a nice amount of django restframework serializer and viewset method customization/overriding, which in the end allowed me to write only one serializer, viewset, and url route/endpoint to pull from 17 different models.

2. etl.py loops through all clients and refreshes tables in client schemas, pulling from their student information database instances. I built this when mapping out a multi-tenanted solution to some of the work I've been doing at BwC, but never had the chance to implement.

3. geoupdater.py updates student city codes by calling the nyc geoclient api, which takes basic address parameters and returns city codes like school district and official neighborhood tabulation area.

4. nyc_state_growth.py wraps a sql query that returns growth on nys ela or math tests for nyc charter schools from 2006 up to academic_year arg provided.

5. complex_number.py was a solution I made for a coding challenge on hacker rank. Its pretty simple but it shows some fun customization of built-in class methods to replicate complex number math (instead of using the built in complex number type).

I include references at points to database connection configurations, but obviously didn't include them in this repo.