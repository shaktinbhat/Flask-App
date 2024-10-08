# Flask Data Retrieval and Processing Application

## Overview

This Flask application simulates a simplified data retrieval and processing system. The application provides API endpoints for fetching, processing, and retrieving data.

## Features

1. **/fetch-data**: Fetches mock data from an external service and processes it.
2. **/get-processed-data**: Returns the processed data stored in memory.

## Setup and Run

### Prerequisites

- Python 3.x
- Virtualenv

### Step-by-Step Guide

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/flask-app.git
   cd flask-app


2. **Set Up a Virtual Environment**

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**
pip install -r requirements.txt

4. **Run the Application**

python app.py

5. **Access the Endpoints**

Fetch data and process: GET http://127.0.0.1:5000/fetch-data
Retrieve processed data: GET http://127.0.0.1:5000/get-processed-data
