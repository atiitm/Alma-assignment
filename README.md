# O-1A Visa Assessor

## Overview
The O-1A Visa Assessor is a FastAPI-based application designed to evaluate CVs (in PDF format) against a set of predefined criteria for the O-1A visa. It extracts text from PDFs using `pypdf` and leverages the spaCy NLP library (with the `en_core_web_lg` model) to perform criteria analysis. The result is a JSON output detailing the matched criteria and an overall rating (high, medium, or low).

## Features
- **PDF Processing:** Extracts text from PDF documents.
- **NLP Analysis:** Uses spaCy to perform text processing and analyze criteria.
- **Criteria Matching:** Matches extracted text against predefined criteria from `Criteria_rules.py`.
- **Rating Calculation:** Provides a rating based on the number of criteria met.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/atiitm/Alma-assignment.git
   cd Alma-assignment
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the spaCy Model:**
   ```bash
   python -m spacy download en_core_web_lg
   ```

## Running the Application

Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```
By default, the application will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoints

## Using Swagger UI for POST Requests
You can use Swagger UI to interact with the API without writing any code:
1. Start the server and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
2. Find the **POST /assess** endpoint.
3. Click on **Try it out**.
4. Upload a PDF file.
5. Click **Execute** to analyze the PDF.

## Design Choices

- **FastAPI:** Chosen for its speed and ease of use when building RESTful APIs.
- **spaCy:** Provides robust NLP capabilities; the `en_core_web_lg` model is used for detailed language analysis.
- **pypdf:** Reliable PDF text extraction to facilitate the analysis.
- **Modular Functions:** Each functionality (text extraction, criteria analysis, rating calculation) is encapsulated in separate functions, making the code easier to maintain and extend.



