from options.test_options import Test_options
from models import *
import importlib
from create_dataset import *
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch
from scipy.stats import pearsonr
from sklearn.metrics import mean_squared_error
import copy
from matplotlib import pyplot as plt
import os
from sklearn import linear_model
import pandas as pd
import numpy as np





if __name__=='__main__':
    opt=Test_options().parse()
    opt.startdate = strTodate(opt.startdate)
    opt.enddate = strTodate(opt.enddate)
    opt.test_start = strTodate(opt.test_start)
    opt.test_end = strTodate(opt.test_end)
    if opt.model=='cnn':
        test_predictors, test_predictands = assemble_predictors_predictands(opt)
        test_dataset = ENSODataset(test_predictors, test_predictands)
        testloader = DataLoader(test_dataset, batch_size=opt.batch_size)
        pred_CNN=cnn_predict('./checkpoints/'+opt.name,testloader)
        if opt.classification:
            pred_CNN = classify(pred_CNN,threshold= opt.threshold)
            test_predictands=classify_pd(test_predictands,threshold= opt.threshold)
            experiment_name = 'CNN Classification'
        else:
            experiment_name = 'CNN Regression'
        corr, _ = pearsonr(test_predictands, pred_CNN)
        rmse = mean_squared_error(test_predictands, pred_CNN) ** 0.5
        
        if '.' in opt.name:
            fname = opt.name[:opt.name.index('.')]
        else:
            fname = opt.name
        plot_nino_time_series(test_predictands, pred_CNN, '{} Predictions. Corr: {:3f}. RMSE: {:3f}.'.format(experiment_name,
                                                                      corr, rmse),'./results/'+fname)
    elif opt.model == 'linear_regression':
        x_train,y_train=assemble_basic_predictors_predictands(opt)
        opt.startdate=opt.test_start
        opt.enddate=opt.test_end
        x_test,y_test=assemble_basic_predictors_predictands(opt)
        pred_reg=lin_reg(x_train, y_train,x_test)
        if opt.classification:
            pred_reg = classify(pred_reg,threshold= opt.threshold)
            y_test = classify_pd(y_test,threshold= opt.threshold)
            experiment_name = 'Linear Classification'
        else:
            experiment_name = 'Linear Regression'
        corr, _ = pearsonr(y_test, pred_reg)
        rmse = mean_squared_error(y_test, pred_reg) ** 0.5
        plot_nino_time_series(y_test, pred_reg, '{} Predictions. Corr: {:3f}. RMSE: {:3f}.'.format(experiment_name,
                                                                      corr, rmse),'./results/'+fname)
        
        
        
