FROM continuumio/miniconda3:latest
RUN mkdir ~/python_flask
WORKDIR ~/python_flask
COPY  * ./

RUN conda env create -f ./environment.yml

ENTRYPOINT ["conda", "run", "-n", "python_flask", "python", "api.py"]
