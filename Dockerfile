FROM python:3

RUN git clone https://github.com/santigg19/Parcial3
WORKDIR /Parcial3

RUN pip install -r requirements.txt
RUN pip install parameterized

CMD [ "python3", "test_tateti.py" ]