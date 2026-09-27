import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
// useLocation() → gets data from the current page URL/navigation state.
// useNavigate() → lets you move the user to another page using code.

const Result = () => {
  const location = useLocation();
  const navigate = useNavigate();

  // location.state - contains information sent from the previous page.
  const { result, reviewText } = location.state || {};

  // If user refreshes page and data is lost
  if (!result) {
    return (
      <div className="text-center mt-10 text-white">
        <p>No result found. Please analyze a review first.</p>
        <button
          onClick={() => navigate("/detect")}
          className="mt-4 px-4 py-2 bg-violet-600 rounded"
        >
          Go Back
        </button>
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto px-6 py-12 text-white">
      <h1 className="text-3xl font-bold mb-6 text-center">Analysis Result</h1>

      {/* Review Text */}
      <div className="mb-6 p-4 bg-black/40 border border-gray-700 rounded-xl">
        <h3 className="font-semibold mb-2">Review:</h3>
        <p className="text-gray-300">{reviewText}</p>
      </div>

      {/* Prediction */}
      <div className="mb-6 p-4 bg-black/40 border border-gray-700 rounded-xl text-center">
        <h2 className="text-xl font-semibold mb-2">Prediction</h2>

        <p
          className={`text-2xl font-bold ${
            result.prediction === "Fake" ? "text-red-500" : "text-green-500"
          }`}
        >
          {result.prediction}
        </p>

        <p className="text-gray-400 mt-2">
          Confidence: {(result.confidence * 100).toFixed(2)}%
        </p>
      </div>

      {/* Back Button */}
      <div className="text-center">
        <button
          onClick={() => navigate("/detect")}
          className="px-6 py-2 bg-violet-600 rounded hover:bg-violet-700"
        >
          Analyze Another Review
        </button>
      </div>
    </div>
  );
};

export default Result;
