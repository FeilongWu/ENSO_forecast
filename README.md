python train.py --dataroot "./datasets/CNRM_tas_anomalies_regridded.nc" --name test_cnn --epoch 2 --startdate 1980-01-01 --enddate 2101-12-31   --dataset CNRM

python test.py --dataroot "./datasets/sst.mon.mean.trefadj.anom.1880to2018.nc" --instrument_data "./datasets/nino34.long.anom.data.txt" --name test_cnn.pt  --startdate 2000-01-01 --enddate 2005-12-31  --dataset observations

python test.py --dataroot "./datasets/CNRM_tas_anomalies_regridded.nc" --dataroot1  "./datasets/sst.mon.mean.trefadj.anom.1880to2018.nc" --dataset CNRM --name linear_classification --startdate 1950-01-01 --enddate 2050-12-31 --instrument_data "./datasets/nino34.long.anom.data.txt" --test_start 2002-01-01 --test_end 2015-12-31  --model linear_regression --classification True

python test.py --dataroot "./datasets/sst.mon.mean.trefadj.anom.1880to2018.nc" --instrument_data "./datasets/nino34.long.anom.data.txt" --name NinoPrediction_leadtime2_timespan1850-01-01-2299-01-01.pt  --startdate "" --enddate ""  --test_start 2000-01-01 --test_end 2010-12-31 --dataset observations --classification True --leadtime 2 --num_input_time_steps 2

python reforecast.py --dataroot "./datasets/sst.mon.mean.trefadj.anom.1880to2018.nc" --instrument_data "./datasets/nino34.long.anom.data.txt" --name test_cnn.pt  --startdate "" --enddate "" --test_start 2015-01-01 --test_end 2018-12-31   --dataset observations  --leadtime 2 --reforecast_data reforecast.txt

python reforecast.py --dataroot "./datasets/CNRM_tas_anomalies_regridded.nc" --dataroot1  "./datasets/sst.mon.mean.trefadj.anom.1880to2018.nc" --instrument_data "./datasets/nino34.long.anom.data.txt" --dataset CNRM --name LR   --startdate 1980-01-01 --enddate 2030-12-31 --test_start 2015-01-01 --test_end 2018-12-31  --leadtime 2 --reforecast_data reforecast.txt --model linear_regression 

# ENSO_forecast

## Usage
### Use Microsoft Windows 10 as the operating system.
- Clone this repo using Git Bash:
```bash
git clone https://github.com/FeilongWu/ENSO_forecast.git
```

If you have pretrained models and datasets, put them under directores "/checkpoints" and "/datasets", respectively.
### All the commands below are executed using Command Prompt unless specified otherwise.
- Set the repository you just cloned as your working directory. The path to the directory may vary for different users. An example command is shown below:
```bash
cd "C://Users//your//name//ENSO_forecast"
```

- If you have <strong>venv</strong> installed, please skip. Use the following command to install  <strong>venv</strong>. This requires Python3.8:
```bash
pip install --user virtualenv
```
- Create a virtual environment (named ENSO) and activate it:
```bash
python -m venv ENSO
.\ENSO\Scripts\activate
```
- Install dependency(ies) for the environment.:
```bash
pip install -r requirements.txt
```
- You can extract a dependency list:
 ```bash
pip freeze > requirements.txt
```

### Training
You must specify "dataroot", "name", "startdate", and "enddate", which refer to the path to the training dataset, the name of your CNN model, the training starting date, and the training end date, respectively. An example command to train a CNN model with CNRM dataset is given below.
 ```bash
python train.py --dataroot "./datasets/CNRM_tas_anomalies_regridded.nc" --name test_cnn --epoch 2 --startdate '1980-01-01' --enddate '2101-12-31'   --dataset CNRM
```

