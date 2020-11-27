FROM python:3
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir ENSO_forecast
Add reforecast.py /ENSO_forecast/
Add test.py /ENSO_forecast/
Add train.py /ENSO_forecast/
Add reforecast.txt /ENSO_forecast/
Add models.py /ENSO_forecast/
Add create_dataset.py /ENSO_forecast/
Add ENSO_forecast.ipynb /ENSO_forecast/
Add README.md /ENSO_forecast/
Add checkpoints /ENSO_forecast/checkpoints 
Add datasets /ENSO_forecast/datasets
Add options /ENSO_forecast/options
Add results /ENSO_forecast/results
WORKDIR /ENSO_forecast
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]