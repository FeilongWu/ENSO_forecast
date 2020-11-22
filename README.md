python train.py --dataroot "./datasets/CNRM_tas_anomalies_regridded.nc" --name test_cnn --epoch 2 --startdate '1980-01-01' --enddate '2101-12-31'   --dataset CNRM

python test.py --dataroot "./datasets/sst.mon.mean.trefadj.anom.1880to2018.nc" --instrument_data "./datasets/nino34.long.anom.data.txt" --name test_cnn.pt  --startdate '2000-01-01' --enddate '2005-12-31'  --dataset observations

python test.py --dataroot "./datasets/sst.mon.mean.trefadj.anom.1880to2018.nc" --name linear_classification --startdate '1950-01-01' --enddate '2001-12-31' --instrument_data "./datasets/nino34.long.anom.data.txt" --test_start '2002-01-01' --test_end '2015-12-31'  --model linear_regression --classification True

python test.py --dataroot "./datasets/sst.mon.mean.trefadj.anom.1880to2018.nc" --instrument_data "./datasets/nino34.long.anom.data.txt" --name test_cnn.pt  --startdate '2000-01-01' --enddate '2005-12-31'  --dataset observations --classification True --leadtime 2

python reforecast.py --dataroot "./datasets/sst.mon.mean.trefadj.anom.1880to2018.nc" --instrument_data "./datasets/nino34.long.anom.data.txt" --name test_cnn.pt  --startdate '2015-01-01' --enddate '2018-12-31'  --dataset observations  --leadtime 2 --reforecast_data reforecast.txt

python reforecast.py --dataroot "./datasets/sst.mon.mean.trefadj.anom.1880to2018.nc" --instrument_data "./datasets/nino34.long.anom.data.txt" --name LR  --test_start 2015-01-01 --test_end 2018-12-31  --dataset observations  --leadtime 2 --reforecast_data reforecast.txt --model linear_regression --startdate 1980-01-01 --enddate 2000-12-31

