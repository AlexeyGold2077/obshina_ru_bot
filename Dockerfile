FROM python
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install telebot
#EXPOSE port
CMD [ "python", "main.py" ]