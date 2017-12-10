FROM python:2.7.14
RUN git clone https://github.com/D4Vinci/Cr3dOv3r.git
WORKDIR /Cr3dOv3r
RUN ls -la && pwd
RUN pip install -r requirements.txt
RUN ls -la
ENTRYPOINT ["python", "Cr3d0v3r.py"]
