{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1a7a88b2-32f6-4307-a620-73131e1d2949",
   "metadata": {},
   "source": [
    "## TASK 3 : Flask Web App – Diabetes Prediction\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b132e1e-0384-4c8c-9a9c-8f97f204a1f8",
   "metadata": {},
   "source": [
    "📁 Project Structure:\n",
    "\n",
    "task3_diabetes_flask_app/\n",
    "│\n",
    "├── app.py                      ← Flask app\n",
    "├── mlp_diabetes_model.pkl      ← Trained model (from Task 2)\n",
    "├── templates/\n",
    "│   └── index.html              ← Simple HTML form\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6ac991f4-ae3b-46b1-88ea-77a2e97e403a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting flask\n",
      "  Downloading flask-3.1.1-py3-none-any.whl.metadata (3.0 kB)\n",
      "Collecting blinker>=1.9.0 (from flask)\n",
      "  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)\n",
      "Collecting click>=8.1.3 (from flask)\n",
      "  Downloading click-8.2.1-py3-none-any.whl.metadata (2.5 kB)\n",
      "Collecting itsdangerous>=2.2.0 (from flask)\n",
      "  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)\n",
      "Requirement already satisfied: jinja2>=3.1.2 in c:\\users\\ruppa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (3.1.4)\n",
      "Requirement already satisfied: markupsafe>=2.1.1 in c:\\users\\ruppa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (2.1.5)\n",
      "Collecting werkzeug>=3.1.0 (from flask)\n",
      "  Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)\n",
      "Requirement already satisfied: colorama in c:\\users\\ruppa\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from click>=8.1.3->flask) (0.4.6)\n",
      "Downloading flask-3.1.1-py3-none-any.whl (103 kB)\n",
      "Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)\n",
      "Downloading click-8.2.1-py3-none-any.whl (102 kB)\n",
      "Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)\n",
      "Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)\n",
      "Installing collected packages: werkzeug, itsdangerous, click, blinker, flask\n",
      "Successfully installed blinker-1.9.0 click-8.2.1 flask-3.1.1 itsdangerous-2.2.0 werkzeug-3.1.3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 24.3.1 -> 25.1.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "!pip install flask\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed2bde29-65ab-48e2-8a35-517b205fcba1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request\n",
    "import numpy as np\n",
    "import pickle\n",
    "\n",
    "# Load the trained model\n",
    "model = pickle.load(open(\"mlp_diabetes_model.pkl\", \"rb\"))\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    return render_template(\"index.html\")\n",
    "\n",
    "@app.route(\"/predict\", methods=[\"POST\"])\n",
    "def predict():\n",
    "    try:\n",
    "        # Collect data from form\n",
    "        features = [float(x) for x in request.form.values()]\n",
    "        input_data = np.array([features])\n",
    "        prediction = model.predict(input_data)[0]\n",
    "        \n",
    "        result = \"Positive (Diabetes Detected)\" if prediction == 1 else \"Negative (No Diabetes)\"\n",
    "        return render_template(\"index.html\", prediction_text=f\"Prediction: {result}\")\n",
    "    except Exception as e:\n",
    "        return f\"❌ Error: {e}\"\n",
    "\n",
    "\n",
    "app.run(debug=False, use_reloader=False)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
