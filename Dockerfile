FROM python:3.10

COPY app.py app.py
COPY scripts/ scripts/
COPY templates/ templates/
RUN pip install -r req.txt

ENTRYPOINT ["gunicorn", "app:app", "run", "--bind", "0.0.0.0:80"]