FROM python:3.11-slim
WORKDIR /app
RUN apt update && apt-get install libgl1-mesa-glx libglib2.0-0 -y
RUN python3 -m venv venv
RUN venv/bin/pip install matplotlib
RUN venv/bin/pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
COPY . .
CMD ["bash"]