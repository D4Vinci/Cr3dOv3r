FROM python:3-slim

RUN apt-get update && apt-get -y install git
RUN git clone https://github.com/D4Vinci/Cr3dOv3r.git
WORKDIR Cr3dOv3r/
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "Cr3d0v3r.py"]
