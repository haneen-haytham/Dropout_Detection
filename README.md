#  Student Dropout Prediction System

An AI-powered machine learning project that predicts the risk of student dropout based on academic performance, personal factors, and environmental conditions.

---

##  Project Overview

This project uses a trained Machine Learning model to analyze multiple student-related features and predict whether a student is at risk of dropping out or not.

The system is deployed as an interactive **Streamlit web app** with a modern UI and real-time predictions.

---

##  Problem Statement

Student dropout is a serious issue affecting education systems worldwide.  
This project aims to:
- Identify at-risk students early
- Help institutions take preventive actions
- Provide data-driven insights into academic performance

---

##  Input Features

The model takes the following inputs:

### Academic Factors:
- JEE Main Score  
- JEE Advanced Score  
- Mock Test Average  
- Class 12 Percentage  
- Attempt Count  
- Daily Study Hours  

### Personal & Social Factors:
- Family Income  
- Peer Pressure Level  
- School Board  
- Coaching Institute  
- Parent Education  
- Location Type  
- Mental Health Issues  
- Admission Status  

---

##  Output

The model predicts:
- **Dropout Risk Level**
  - Low Risk 
  - Medium Risk   
  - High Risk   

- Probability score of dropout risk

---

## Tech Stack

- Python   
- Pandas / NumPy  
- Scikit-learn   
- Random Forest Classifier  
- Streamlit 
- Plotly  
- Pickle (model serialization)

---

##  Features

- Interactive web dashboard  
- Real-time prediction system  
- Risk level classification  
- Visual analytics & charts  
- Modern dark-themed UI  
- Responsive layout  

---

##  Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/dropout-project.git
cd dropout-project
2. Install dependencies
pip install -r requirements.txt
3. Run the app
streamlit run app.py
 Project Structure
dropout-project/
│
├── app.py
├── model.pkl
├── columns.pkl
├── requirements.txt
├── README.md
Future Improvements
Add more student behavioral data
Deploy on cloud (Streamlit Cloud / Render)
Improve model accuracy with advanced algorithms
Add explainability (feature importance per prediction)
Mobile-friendly UI
 Author

Developed by: Haneen Abdelwahed
Machine Learning & Backend Enthusiast 

 Note

This project is for educational and demonstration purposes.
