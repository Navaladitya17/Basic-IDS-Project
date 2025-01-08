# **Basic IDS (Intrusion Detection System)**  

This project is a **prototype** for a Basic Intrusion Detection System (IDS). It demonstrates a functional **front-end interface** and a foundational **back-end implementation**. The focus is on showcasing the **front-end design** using HTML, CSS, and JavaScript, while the back-end uses **Python** and **Flask** for basic server-side operations.  

--
## **Features**  

### **Front-End**  

 - Developed using **HTML**, **CSS**, and optional **JavaScript** for responsiveness and interactivity.  
- Provides a **simple and user-friendly interface** to upload files for analysis.  
- **Responsive Design**: Works well on both desktop and mobile devices.  
- **CSV File Upload Section**: Allows users to upload datasets for processing.  

### **Back-End**  
 
 - Built using **Python** and **Flask**.  
- Accepts CSV files and validates them for processing.  
- **Machine Learning Component**: Uses a Random Forest Classifier to process uploaded data and generate a basic classification report.  
- Handles errors gracefully, such as missing columns or unsupported file types.  

---

## **Project Structure**  

<!-- Explanation of the folder and file structure -->
```plaintext  
project/  
├── ids.py                   # Backend Flask application  
├── uploads/                 # Directory for storing uploaded CSV files  
├── templates/               # HTML templates for rendering pages  
│   ├── index.html           # Home page with upload form  
│   ├── result.html          # Results page to display the output or errors  
├── static/                  # Static files for styling and other frontend resources  
│   ├── css/  
│   │   └── style.css        # Custom CSS styles  
│   └── js/  
│       └── script.js        # (Optional) JavaScript for interactivity  
└── README.md                # Documentation for the project  

## How to Run the Project :- 

Prerequisites
<!-- List of tools and libraries required to run the project -->
To run this project locally, you need the following installed:

Python 3.7+
Flask (install using pip install flask)
Libraries such as pandas, scikit-learn (install using pip install pandas scikit-learn).

## Steps
<!-- Step-by-step instructions to set up and run the project -->

Clone the repository:

git clone https://github.com/yourusername/basic-ids.git  
cd basic-ids  

Ensure the uploads/ directory exists in the project root (if not, create it manually):

mkdir uploads
  
Run the Flask application:
python ids.py  

Open your web browser and navigate to:
arduino

http://127.0.0.1:5000  

Upload a CSV file using the interface.

## Limitations

<!-- Brief description of the limitations of the current implementation -->
The back-end is currently in a prototype stage and may not provide robust IDS results.
Designed primarily for demonstration purposes and is not suitable for production environments.

Dataset Requirements:
The uploaded file must be in CSV format.
The dataset should include a class column as the target variable for model training.

## **Screenshots**
<!-- Provide examples of how the project looks -->

1) Home Page
2)Results Page

# Future Enhancements
<!-- Suggestions for improving the project -->

Enhanced Back-End:
Support for multiple dataset formats.
Implement additional machine learning algorithms.

Improved Front-End:
Add status indicators and progress bars for file uploads.
Provide more detailed error messages.

Robust Error Handling:
Handle edge cases for large files and unsupported data types.

Deploy the Application:
Host on a public server for real-world usage.

## Contributors
@Navaladitya17
