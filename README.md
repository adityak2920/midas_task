# MIDAS TASK
  This repository is divided into different parts.
  
   1. Data Collection(Part 1) - It includes code for the collection of data and also includes what all the ways through which I have tried to collect data.

   2. EDA(Part 2) - It includes code for Exploratry Data Analysis. It also generates a file "final_profile.html" created using pandas profiling.

   3. Building a flare detector(Part 3) - In the model folder, I have demonstrated different training and results of different machine learning and deep learning models.

   4. Building a Web Application(Part 4) - In the deploy folder, I have included all the files necessary to build application and deploy on herko. These files are:                                                                                          
    a) "deploy/app.py" - This is a script for the flask app.                                                                   
    b) "deploy/Procfile" - It is necessary for heroku deployment. It includes instructions for heroku to run the app.          
    c) "requirements.txt" - It includes the libraries with their versions. It is important for heroku  deployment.             
    d) "count_vectors.sav" - The weights of count vectorizer, which is right now being used in heroku deployment.              
    e) "lgr_count.sav" - The weights for the Logistic Regression classifier with count vectors. This weights are being used for deployment on heroku.

   5. Deploy(Part 5) - The app is successfully deployed on heroku, but when I am making a request from postman it's not responding. I have tried to run the app using gunicorn in my system and it's successfully running, here is the [video](https://drive.google.com/open?id=1KkbIxj4mRA4iRxAqEFcLFKr1uQee3QGv) to prove. But in heroku, it was not working. According to logs, the worker is crashing. I don't know the reason behind worker crashing.                                                 
   Here is the link for the app: https://midasiiitd.herokuapp.com/                                                             
   As the app doesn't have any html template and also it's only available at "/automated_testing" endpoint, so the above link of app is not much useful.
   
   ## What all I have tried to make the heroku app work?
   1. I have tried to increase the no. of workers for gunicorn.
   2. I have tried to change the port of gunicorn app.
   3. I have also tried to run Flask app without gunicorn.

   
   After all these tries and 2 days of debugging, it still not working.
   
   I have also included CSVs in data which are being used in this repositori in ```data``` folder.

   **Note: model folder has it's own readme.md so, please read it**
    
