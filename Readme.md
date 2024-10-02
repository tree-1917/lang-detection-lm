# 🌍 Language Detection API

This project provides a simple FastAPI-based API to detect the language of a given text using a trained machine learning model. 🚀

## ✨ Features

- **FastAPI Framework**: Lightweight and fast web API framework.
- **Machine Learning Model**: Language detection using a trained scikit-learn pipeline.
- **Predict Endpoint**: Send a POST request with a text input to get the detected language.
- **Health Check**: Simple GET endpoint for checking API status.

## 🚀 How to Use

1. **Clone the repository**:
   ```
   git clone <repository-url>
   ```
2. **Navigate to the project directory**:

   ```
   cd /path/to/project
   ```

3. **Build the Docker image**:  
   Make sure you have Docker installed.

   ```
   sudo docker build -t lang-detection-model .
   ```

4. **Run the Docker container**:

   ```
   sudo docker run -d -p 3002:80 lang-detection-model
   ```

5. **Access the API**:
   - Health check:
     ```
     GET http://localhost:3002/
     ```
     Response: `{"health_check": "OK", "API version": "0.1.0", "model_version": "x.x.x"}`
   - Prediction:
     ```
     POST http://localhost:3002/predict
     Body: { "text": "Your input text" }
     ```

## 💡 Contributing

We welcome contributions to improve this project! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request. 🚀

## 🔧 Requirements

- **FastAPI**
- **scikit-learn**
- **pydantic**
- **Docker**

---
