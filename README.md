# InstaScraper

Live: http://ec2-3-141-106-98.us-east-2.compute.amazonaws.com/

This project features a light weight Instagram image downloader built using the Python requests library and Flask for its UI.

The Flask UI prompts the user to enter a URL (for example, https://www.instagram.com/p/Cmo_a46Jtwj/). Once the user hits the submit button on the backend the Python requests library calls Instagrams GraphQL API which returns JSON. However, in order to access the API a user session is created to login using Requests Session.

This JSON data can easily be used to extract the links that correspond to the images. Finally the links are rendered on the page with the help of a Python templating engine called Jinja. 

The links can be clicked to view the full size images that one can right click as 'Save As' to their device!
