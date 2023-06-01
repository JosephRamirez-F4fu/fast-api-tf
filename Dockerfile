FROM python
WORKDIR /app
COPY . .
RUN pip install -r requeriments.txt
EXPOSE 8001
CMD ["python","app.py"]
