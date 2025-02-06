FROM python:3.9-slim

WORKDIR /Models

COPY ./Models /Models

RUN cd ..

WORKDIR /app

# Copy requirements first to optimize caching
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN python -c "import nltk; \
    nltk.download('punkt_tab'); \
    nltk.download('stopwords'); \
    nltk.download('wordnet')"

COPY ./server /app

EXPOSE 80

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]
