# Product Review Feature Extraction API

A small backend NLP project that uses **spaCy POS Tagging** and **FastAPI** to extract candidate product features from e-commerce customer reviews.

The main purpose of this project is to understand how basic NLP techniques can be implemented and exposed through a backend API.

## Problem Statement

E-commerce applications receive thousands of customer reviews. Manually reading reviews to identify which product features customers are discussing does not scale.

This project provides a backend API that automatically extracts **nouns from customer reviews as candidate product features** using POS Tagging.

For example:

> "The battery life is amazing but the camera quality is poor."

The system identifies nouns such as:

```text
battery
life
camera
quality
```

## Project Goal

Build a FastAPI REST API that:

* Accepts customer reviews as JSON.
* Processes the review using spaCy.
* Performs POS Tagging.
* Extracts nouns as candidate product features.
* Returns the extracted features as JSON.
* Supports feature-frequency analysis for multiple reviews.

## Architecture

```text
Customer Review
      ↓
FastAPI API
      ↓
spaCy NLP Pipeline
      ↓
Tokenization
      ↓
POS Tagging
      ↓
Filter NOUN tokens
      ↓
Candidate Product Features
      ↓
JSON Response
```

## Technologies Used

* **Python**
* **FastAPI** — REST API framework
* **spaCy** — NLP and POS Tagging
* **Pydantic** — Request validation
* **Uvicorn** — ASGI server
* **collections.Counter** — Feature frequency counting

## Project Structure

```text
project/
│
├── main.py
├── requirements.txt
├── README.md
└── ...
```

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <project-folder>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**macOS/Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the spaCy English model

```bash
python -m spacy download en_core_web_sm
```

## Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI also provides interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Usage

### Endpoint 1 — Single Review

**Request**

```http
POST /extract-features
```

**JSON Body**

```json
{
  "review": "The battery life is amazing but the camera quality is poor."
}
```

**Response**

```json
{
  "review": "The battery life is amazing but the camera quality is poor.",
  "features": [
    "battery",
    "life",
    "camera",
    "quality"
  ],
  "feature_count": 4
}
```

## How POS Tagging Works

spaCy processes the review into individual tokens and assigns each token a Part-of-Speech tag.

Example:

```text
The        → DET
battery    → NOUN
life       → NOUN
is         → AUX
amazing    → ADJ
camera     → NOUN
quality    → NOUN
poor       → ADJ
```

The application filters tokens where:

```python
token.pos_ == "NOUN"
```

These nouns are then returned as candidate product features.

## Feature Frequency

For multiple reviews, `collections.Counter` can be used to determine how frequently each feature appears.

Example:

```python
from collections import Counter

features = [
    "camera",
    "battery",
    "camera",
    "screen",
    "battery",
    "camera"
]

Counter(features).most_common(5)
```

Result:

```text
[
    ("camera", 3),
    ("battery", 2),
    ("screen", 1)
]
```

This allows the backend to identify the most frequently discussed features.

## Important Limitation

This project uses **POS-based noun extraction**.

Therefore, every extracted noun should not automatically be considered a true product feature.

For example:

```text
"The phone has a beautiful design."
```

The system may identify:

```text
phone
design
```

However, `phone` is not a product feature.

A production-level system could improve this using:

* Dependency Parsing
* Named Entity Recognition
* Aspect-Based Sentiment Analysis
* Machine Learning models
* Transformer-based NLP models
* LLM-based extraction

## Learning Objectives

This project was built primarily to learn and implement:

* Fundamentals of NLP
* Tokenization
* POS Tagging
* spaCy
* Noun extraction
* `collections.Counter`
* FastAPI
* REST APIs
* JSON request/response handling
* Connecting NLP processing with backend services

## Future Improvements

Possible improvements include:

1. Add bulk review processing.
2. Return feature frequency.
3. Remove generic nouns that are not product features.
4. Add sentiment analysis for each feature.
5. Use dependency parsing for better feature extraction.
6. Implement Aspect-Based Sentiment Analysis.
7. Add database storage for reviews and extracted features.
8. Add automated tests.
9. Add Docker support.
10. Add authentication and API rate limiting.

## Conclusion

This project demonstrates how a basic NLP technique such as **POS Tagging** can be integrated into a **FastAPI backend service**.

The current system intentionally uses a simple rule-based approach so that the underlying NLP and backend concepts remain clear. It can later be extended into a more advanced product-review intelligence system using modern NLP and machine-learning techniques.
