from flask import Flask, request, render_template
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import os

# Flask application setup
app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to process the dataset and train the model
def train_model(file_path):
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        return f"Error: Unable to read the file. {str(e)}"

    # Validate dataset structure
    if 'class' not in data.columns:
        return "Error: The dataset must have a 'class' column as the target variable."
    
    try:
        X = data.drop('class', axis=1)  # Features
        y = data['class']               # Target
    except KeyError as e:
        return f"Error: Unable to process dataset. {str(e)}"

    # Normalize the data
    scaler = StandardScaler()
    try:
        X_scaled = scaler.fit_transform(X)
    except Exception as e:
        return f"Error: Unable to scale the data. {str(e)}"

    # Split the data
    try:
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    except Exception as e:
        return f"Error: Unable to split the data. {str(e)}"

    # Train a Random Forest model
    try:
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
    except Exception as e:
        return f"Error: Model training or prediction failed. {str(e)}"

    # Generate classification report
    try:
        report = classification_report(y_test, y_pred)
    except Exception as e:
        return f"Error: Unable to generate report. {str(e)}"

    return report

# Route to render the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload and result generation
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', error_message="No file part")
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template('index.html', error_message="No selected file")
    
    if file and allowed_file(file.filename):
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Ensure the upload folder exists
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        
        file.save(file_path)
        
        # Generate report
        report = train_model(file_path)
        
        # Handle errors during processing
        if "Error" in report:
            return render_template('index.html', error_message=report)
        
        return render_template('result.html', report=report)
    else:
        return render_template('index.html', error_message="Invalid file type. Please upload a CSV file.")

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
