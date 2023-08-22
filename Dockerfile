FROM python
WORKDIR /app
COPY . .
VOLUME [ "/app/data" ]
RUN pip install --upgrade pip
RUN pip install telebot
#EXPOSE port
CMD [ "python", "main.py" ]