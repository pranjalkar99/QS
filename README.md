# Quality-AssesmentCompfox
This simple website is for Workers to perform Quality  Checking on HTML files, It extracts files from GCP bucket, and allows editing of pdfs, converted into HTML in simple text-type format, and saves in the GCP bucket.


To start the server on your local machine, follow these steps:

1. Clone the repository:
```
git clone https://github.com/pranjalkar99/QS.git
```

2. Create a virtual environment:
```
python -m venv env
```

3. Activate the virtual environment:
   - For Windows:
   ```
   .\env\Scripts\activate
   ```
   - For Linux/Mac:
   ```
   source env/bin/activate
   ```

4. Install the project dependencies:
```
pip install -r requirements.txt
```

5. Start the server using Uvicorn:
```
uvicorn main:app --reload --port 8000
```

With these steps, the server should start running on your local machine. You can access it at `http://localhost:8000`. The `--reload` flag enables auto-reloading, so any code changes you make will trigger the server to restart automatically.

Make sure you have Python, Git, and venv installed on your machine before following these steps.