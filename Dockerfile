FROM continuumio/miniconda3:latest

RUN conda update -y conda \
    && conda install -y -c anaconda graphviz \
    && conda install -y -c anaconda pygraphviz

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]