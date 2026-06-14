#FROM python:3.12-slim

#WORKDIR /app

#COPY requirements.txt .

#RUN pip install -r requirements.txt

#COPY . .

#RUN npm run build
# ... (Keep lines 1-10 exactly how you have them)

# 11. Point Uvicorn precisely to main:app through the app/core folder structure
#CMD ["uvicorn", "app.core.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.11-slim

WORKDIR /app

# Copy dependency files first to leverage caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend source code
COPY . .
ENV PYTHONPATH=/app
# Run your backend server (adjust main:app if using FastAPI/Uvicorn, or manage.py for Django)
#CMD ["python", "app/core/main.py"]
CMD ["uvicorn", "app.core.main:app", "--host", "0.0.0.0", "--port", "8000"]