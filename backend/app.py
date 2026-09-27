# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pandas as pd
# import pickle

# # This creates your Flask server.
# # CORS(app) basically says: "Allow requests from my frontend."
# app = Flask(__name__)
# CORS(app)

# # LOAD MODELS
# lr_model = pickle.load(open("lr_model.pkl", "rb"))
# nb_model = pickle.load(open("nb_model.pkl", "rb"))
# rf_model = pickle.load(open("rf_model.pkl", "rb"))
# vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
# # The vectorizer converts text such as:
# # "This product is amazing!"
# # into numbers that the machine-learning models can understand.
# # The .pkl files contain objects that were previously trained and saved.


# def get_best_prediction(vec):
#     # Logistic Regression
#     lr_pred = lr_model.predict(vec)[0]
#     lr_proba = max(lr_model.predict_proba(vec)[0])

#     # Naive Bayes
#     nb_pred = nb_model.predict(vec)[0]
#     nb_proba = max(nb_model.predict_proba(vec)[0])

#     # Random Forest
#     rf_pred = rf_model.predict(vec)[0]
#     rf_proba = max(rf_model.predict_proba(vec)[0])

#     # Choose best model (highest confidence)
#     best_conf = max(lr_proba, nb_proba, rf_proba)

#     if best_conf == lr_proba:
#         final_pred = lr_pred
#     elif best_conf == nb_proba:
#         final_pred = nb_pred
#     else:
#         final_pred = rf_pred

#     return {
#         "prediction": "Fake" if final_pred == 1 else "Genuine",
#         "confidence": round(float(best_conf), 2)
#     }
# # Your three models give:
# # Model	                Prediction	Confidence
# # Logistic Regression	Fake	    85%
# # Naive Bayes	        Fake	    73%
# # Random Forest	        Genuine	    94%
# # Your code does: best_conf = max(lr_proba, nb_proba, rf_proba)
# # The highest confidence is 94%, from Random Forest.
# # So:
# # final_pred = rf_pred
# # And because Random Forest predicted 0 (Genuine), this:
# # "Fake" if final_pred == 1 else "Genuine"
# # produces:
# # Genuine
# # with 94% confidence.
# # So if your frontend displays it, you would typically see:
# # Prediction: Genuine
# # Confidence: 94%


# # SINGLE REVIEW
# @app.route("/analyze", methods=["POST"])
# def analyze():
#     data = request.json
#     review = data.get("review")

#     if not review:
#         return jsonify({"error": "No review provided"}), 400

#     vec = vectorizer.transform([review])

#     result = get_best_prediction(vec)

#     return jsonify(result)

# # CSV UPLOAD ONLY
# @app.route("/upload", methods=["POST"])
# def upload():
#     file = request.files.get("file")
#     if not file:
#         return jsonify({"error": "No file uploaded"}), 400
#     # Ensure CSV only
#     if not file.filename.endswith(".csv", "json"):
#         return jsonify({"error": "Only CSV or JSON files are allowed"}), 400

#     df = pd.read_csv(file)

#     if "review" not in df.columns:
#         return jsonify({"error": "CSV must contain 'review' column"}), 400

#     results = []

#     for review in df["review"]:
#         vec = vectorizer.transform([str(review)])
#         result = get_best_prediction(vec)

#         results.append({
#             "review": review,
#             "prediction": result["prediction"],
#             "confidence": result["confidence"]
#         })

#     return jsonify(results)

# # RUN SERVER
# if __name__ == "__main__":
#     app.run(debug=True)




from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle
import re
import string


# CREATE FLASK SERVER
app = Flask(__name__)
CORS(app)


# TEXT CLEANING FUNCTION
# IMPORTANT:
# This should be the same cleaning used during model training.
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )
    return text


# LOAD TRAINED MODELS
lr_model = pickle.load(
    open("lr_model.pkl", "rb")
)

nb_model = pickle.load(
    open("nb_model.pkl", "rb")
)

rf_model = pickle.load(
    open("rf_model.pkl", "rb")
)

vectorizer = pickle.load(
    open("vectorizer.pkl", "rb")
)



# GET BEST PREDICTION
def get_best_prediction(vec):
    # ------------------------------------------
    # Logistic Regression
    # ------------------------------------------
    lr_pred = lr_model.predict(vec)[0]
    lr_proba = max(
        lr_model.predict_proba(vec)[0]
    )

    # ------------------------------------------
    # Naive Bayes
    # ------------------------------------------
    nb_pred = nb_model.predict(vec)[0]
    nb_proba = max(
        nb_model.predict_proba(vec)[0]
    )

    # ------------------------------------------
    # Random Forest
    # ------------------------------------------
    rf_pred = rf_model.predict(vec)[0]
    rf_proba = max(
        rf_model.predict_proba(vec)[0]
    )

    # ------------------------------------------
    # Choose model with highest confidence
    # ------------------------------------------
    best_conf = max(
        lr_proba,
        nb_proba,
        rf_proba
    )

    if best_conf == lr_proba:
        final_pred = lr_pred

    elif best_conf == nb_proba:
        final_pred = nb_pred

    else:
        final_pred = rf_pred

    return {
        "prediction": (
            "Fake"
            if final_pred == 1
            else "Genuine"
        ),
        "confidence": round(
            float(best_conf),
            2
        )
    }



# SINGLE REVIEW

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json

    if not data:
        return jsonify({
            "error": "Invalid JSON data"
        }), 400

    review = data.get("review")

    if not review:
        return jsonify({
            "error": "No review provided"
        }), 400

    # Clean the review in the same way
    # as the training data
    review = clean_text(review)

    # Convert text into TF-IDF numbers
    vec = vectorizer.transform([review])

    # Get prediction
    result = get_best_prediction(vec)

    return jsonify(result)



# CSV + JSON FILE UPLOAD

@app.route("/upload", methods=["POST"])
def upload():

    # Get uploaded file
    file = request.files.get("file")

    if not file:
        return jsonify({
            "error": "No file uploaded"
        }), 400

    # Get file name
    filename = file.filename.lower()

    # ------------------------------------------
    # Check file type
    # ------------------------------------------
    if not filename.endswith((".csv", ".json")):
        return jsonify({
            "error": "Only CSV or JSON files are allowed"
        }), 400


    # ------------------------------------------
    # Read CSV
    # ------------------------------------------
    if filename.endswith(".csv"):

        try:
            df = pd.read_csv(file)

        except Exception as e:
            return jsonify({
                "error": f"Unable to read CSV file: {str(e)}"
            }), 400


    # ------------------------------------------
    # Read JSON
    # ------------------------------------------
    elif filename.endswith(".json"):

        try:
            df = pd.read_json(file)

        except Exception as e:
            return jsonify({
                "error": f"Unable to read JSON file: {str(e)}"
            }), 400


    # ------------------------------------------
    # Check review column
    # ------------------------------------------
    if "review" not in df.columns:
        return jsonify({
            "error": (
                "File must contain a 'review' column"
            )
        }), 400


    # ------------------------------------------
    # Predict every review
    # ------------------------------------------
    results = []

    for review in df["review"]:

        # Clean review
        cleaned_review = clean_text(review)

        # Convert to TF-IDF
        vec = vectorizer.transform(
            [cleaned_review]
        )

        # Predict
        result = get_best_prediction(vec)

        results.append({
            "review": review,
            "prediction": result["prediction"],
            "confidence": result["confidence"]
        })


    # ------------------------------------------
    # Return results
    # ------------------------------------------
    return jsonify(results)



# RUN SERVER

if __name__ == "__main__":
    app.run(debug=True)