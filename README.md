# Predictive Maintenance

Predictive maintenance represents a transformative approach to equipment maintenance, leveraging data and advanced analytics to anticipate and prevent equipment failures. Unlike traditional reactive maintenance, which addresses issues post-failure, or preventive maintenance, which operates on a fixed schedule, Predictive maintenance uses real-time data to predict issues before they disrupt operations.

This project focuses on developing a predictive maintenance model that utilizes sensor data and machine learning algorithms to forecast equipment failures.

Through this project, we aim to demonstrate the effectiveness of predictive maintenance in enhancing operational efficiency and reliability, ultimately leading to significant cost savings and improved productivity.

# Data Description

*UDI*:
   - A unique identifier for each piece of equipment or device being monitored.

*Product ID*: 
   - A unique identifier for the specific product or batch being produced or maintained.

*Type*:
   - The type or category of equipment being monitored, which could indicate the model or function of the machinery.

*Air temperature*: 
   - The temperature of the air surrounding the equipment, measured in Kelvin (K).

*Process temperature*: 
   - The temperature within the equipment during the operation process, measured in Kelvin (K).

*Rotational speed*:
   - The speed at which a part of the equipment is rotating, measured in revolutions per minute (rpm).

*Torque*:  
   - The rotational force applied to the equipment, measured in Newton meters (Nm).

*Tool wear*:
   - The amount of time (in minutes) that the tool has been in use, indicating its wear level.

*Target*: 
   - A binary indicator showing whether a failure has occurred (1) or not (0).

*Failure Type*: 
- A categorical variable describing the type of failure that occurred, if any. This could include various failure modes such as mechanical failure, electrical failure, etc.


## Steps for Predictive Maintenance Project

### 1. Data Collection and Preprocessing

### 2. Data Visualization

### 3. Machine Learning Model

### 4. Use Flask for Backend

### 5. Deployment


## Steps for Predictive Maintenance Project

#### Data Collection and Preprocessing
#### Data Visualization
#### Machine Learning Model Fitting and Evaluation
#### API Development with Flask
#### Containerization with Docker
#### Deployment

## Machine Learning Model Fitting
In predictive maintenance project, we trained various machine learning models to predict equipment failures based on historical data. The models used include Random Forest, Support Vector Machine (SVM), K-Nearest Neighbors (KNN), Logistic Regression, and XGBoost.


### Why XGBoost?

XGBoost was selected as the primary model for predictive maintenance project due to several compelling reasons:

- *Performance*: 

- *Robustness*: 

- *Flexibility*: 

- *Scalability*: 

- *Interpretability*: 

## Predictive Maintenance Web Application with Flask

*Model Placement*: Pre-trained machine learning model (xgb_model.pkl) is placed in the same directory as the Flask application script (app.py).

2. *Dependency Installation*: Flask and other required dependencies need to be installed.

3. *Running the Application*: Execute the Flask application script (app.py). This will start the Flask web server locally.

4. *Accessing the Web Interface*: Once the Flask application is running, can access the web interface by navigating to http://localhost:5000 in your web browser. 

## Containerization with Docker
Containerization with Docker allows us to package our predictive maintenance application along with its dependencies into a standardized unit called a container. This enables us to run the application seamlessly across different environments without worrying about compatibility issues.

#### Steps:
##### Docker Installation.
##### Dockerfile Creation.
##### Building the Docker Image.
##### Running the Docker Container.


## Deployment on Amazon EC2 Instance

### Steps:

1. *Amazon EC2 Setup*: 
   - Sign in to the AWS Management Console 
   - Launch a new EC2 instance with  Ubuntu Server 

2. *Connect to the EC2 Instance*: 

   - Use SSH to connect to your EC2 instance from local machine.
   - Can find the public IP address of instance in the EC2 dashboard.

3. *Transfer Files*: 
   - Transfer project files, including the Flask application script (app.py), the pre-trained model file (xgb_model.pkl),requirement file, frontend file (index.html), to the EC2 instance using SCP or SFTP.

4. *Install Docker*: 
   - Install Docker on your EC2 instance to containerize application and manage dependencies efficiently.

5. *Containerize with Docker*: 
   - Create a Dockerfile in the project directory to define application's environment and dependencies.
   - Build a Docker image and run a Docker container on EC2 instance using the same steps as described earlier.

6. *Access the Application*: 
   - Once the Docker container is running on your EC2 instance, access Flask application through the public IP address or domain name of the instance.


![WhatsApp Image 2024-10-08 at 7 02 05 PM](https://github.com/user-attachments/assets/db74e572-cb59-4ec4-a301-e709bf17462f)

![WhatsApp Image 2024-10-08 at 7 02 05 PM (1)](https://github.com/user-attachments/assets/2a17e957-e4c2-446b-8e81-992d127cec78)

