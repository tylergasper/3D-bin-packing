FROM python:latest 

# upgrade pip if it can be
RUN pip install --upgrade pip



RUN mkdir /scrapy
WORKDIR /scrapy
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt



RUN plotly_get_chrome -y


RUN apt update
RUN apt install -y libnss3 libatk-bridge2.0-0 libcups2 libxcomposite1 libxdamage1
RUN apt install -y libxfixes3 libxrandr2 libgbm1 libxkbcommon0 libpango-1.0-0 libcairo2 libasound2