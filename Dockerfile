FROM python:3.9-slim  # Lightweight Python image

WORKDIR /app  # Set working directory inside the container

COPY requirements.txt requirements.txt  # Copy dependency file
COPY app.py app.py  # Copy the app script

RUN pip install --no-cache-dir -r requirements.txt  # Install dependencies

EXPOSE 8501  # Expose the default Streamlit port

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
