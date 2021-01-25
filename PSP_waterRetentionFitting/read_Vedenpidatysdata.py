# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:50:42 2016

@author: slauniai

Script to read and massage VMI water retention data
USES modules PSP_waterRetention and PSP_Marquardt; these are from Bitelli et al. (2015) Soil Physics wit Python, chapter 5.3.
"""
import os
import numpy as np
import pandas as pd
from PSP_Marquardt import * #Bitelli et al. ch 5.3; fitting WRC. 

from matplotlib import pyplot as plt
plt.interactive(False)

def WRC_fitcurves(showfigs=False):
    #from matplotlib.backends.backend_pdf import PdfPages
    #pp = PdfPages('multipage.pdf')
    
    #pandas.read_excel(io, sheetname=0, header=0, skiprows=None, skip_footer=0, index_col=None, names=None, parse_cols=None, 
    #                  parse_dates=False, date_parser=None, na_values=None, thousands=None, convert_float=True, 
    #                  has_index_names=None, converters=None, engine=None, squeeze=False, **kwds)
    
    """ ---- Read data from excel file into pandas DataFrame 'dat' """
       
    inpath='D:\Datat\Vedenpidatys\Datakooste\\'
    infile='WRC_datakoosteVMI2016v1.xlsx'
    insheet='Data1'
    modelstr=['Campbell','vanG-5par','vanG-4par', 'Ippish-vaG','Cam-Ipp-vanG']
    dat, cols, units = read_Vedenpidatysdata(inpath+infile, insheet)
    #rows are samples, columns contain water contents at a given soil water tension psi
    
    """ create dataframes for WRC fitting results. Index is as in dat
    
    #Camp=pd.DataFrame(np.NaN, index=dat.index, columns=['thetaS', 'b','AirEntry', 'R2','resid'])
    #vanG5=pd.DataFrame(np.NaN, index=dat.index, columns=['thetaS', 'thetaR','alpha','n','m', 'R2','resid'])
    #vanG4=pd.DataFrame(np.NaN, index=dat.index, columns=['thetaS', 'thetaR','alpha','n', 'R2','resid'])
    #Ipp_vanG=pd.DataFrame(np.NaN, index=dat.index, columns=['thetaS', 'thetaR','alpha','n','m','AirEntry', 'R2','resid'])
    #Camp_Ipp_vanG=pd.DataFrame(np.NaN, index=dat.index, columns=['thetaS', 'thetaR','alpha','n','m','AirEntry', 'R2','resid'])
    """
    WRC=[] #list where elements are as: 0 = Campbell, 1= vanGen5par, 2=vanGen4par, 3=Ipp_vanGen, 4=Camp_Ipp_vanG
    
    WRC.append(pd.DataFrame(np.NaN, index=dat.index, columns=['thetaS', 'b','AirEntry', 'resid', 'NrIter']))
    WRC.append(pd.DataFrame(np.NaN, index=dat.index, columns=['thetaS', 'thetaR','alpha','n','m','resid', 'NrIter']))
    WRC.append(pd.DataFrame(np.NaN, index=dat.index, columns=['thetaS', 'thetaR','alpha','n', 'resid', 'NrIter']))
    WRC.append(pd.DataFrame(np.NaN, index=dat.index, columns=['thetaS', 'thetaR','alpha','n','AirEntry', 'resid', 'NrIter']))
    WRC.append(pd.DataFrame(np.NaN, index=dat.index, columns=['thetaS', 'thetaR','alpha','n','AirEntry', 'resid', 'NrIter']))
    
    # soil water tension (-Psi, kPa) at which the measurements are done
    psi=np.array([0.01, 0.3, 0.981, 4.905, 9.81, 33.0, 98.1, 1500.0]) #kPa

    """ --- fit water retention curves to data --- """
    #initialize parameters
    #thetaS = max(waterContent)
    #thetaR = min(waterContent)
    #thetaR = 0.08
    air_entry = 1.0
    Campbell_b = 4.0
    VG_alpha = 1/air_entry
    VG_n = 1.5
    VG_m = 1. - 1./VG_n
    
    for k in range(min(dat.index), max(dat.index)+1): #loop through samples, i.e. rows in 'dat'
        #os.system("pause")
        #select data from dataframe, convert % to m3/m3    
        wc=np.array(dat.loc[k,['tp', 'WC03_x','WC1_x','WC5_x','WC10_x','WC33_x', 'WC100_x', 'WC1500_x' ]]/100.0)    
        
        # initialize parameters
        thetaS = max(wc)
        thetaR = 0.5*min(wc)
    
        for model in [1,2,3,4,5]: #loop through models. NOTE: CAMPBELL, VAN_GENUCHTEN etc. have got values when PSP_Marquard is imported
            if (model == CAMPBELL):
                #these define parameter initial guesses (b0) and allowed range (bmin, bmax)
                b0 = np.array([thetaS, air_entry, Campbell_b], float)
                bmin = np.array([thetaS, 0.1, 0.1], float)
                bmax = np.array([min(1.0,thetaS*1.05), 20., 10.], float)
                
            elif (model == VAN_GENUCHTEN):
                b0 = np.array([thetaS, thetaR, VG_alpha, VG_n, VG_m], float)
                bmin = np.array([thetaS, 0.0, 0.01, 0.01, 0.01], float)
                bmax = np.array([min(1.0,thetaS*1.05), thetaR, 200., 200., 1.], float)
            elif (model == RESTRICTED_VG):
                b0 = np.array([thetaS, thetaR, VG_alpha, VG_n], float)
                bmin = np.array([thetaS, 0.0, 0.01, 1.], float)
                bmax = np.array([min(1.0,thetaS*1.05), thetaR, 200., 200.], float)
            elif (model == IPPISCH_VG):
                b0 = np.array([thetaS, thetaR, air_entry, VG_alpha, VG_n], float)
                bmin = np.array([thetaS, 0.0, 0.1, 0.01, 1.], float)
                bmax = np.array([min(1.0,thetaS*1.05), thetaR, 20., 200., 20.], float)
            elif (model == CAMPBELL_IPPISCH_VG):
                b0 = np.array([thetaS, thetaR, air_entry, VG_alpha, VG_n], float)
                bmin = np.array([thetaS, 0.0, 0.1, 0.01, 1.], float)
                bmax = np.array([min(1.0,thetaS*1.05), thetaR, 20., 200., 20.], float)   


            #fit model to data and save variables into dataframes

            #find finite wc value indexes (water potentials)
            ix=list(np.where(wc>0)[0])
            b,sse,iterno = Marquardt(model, b0, bmin, bmax, psi[ix], wc[ix])
            b=list(b) #fitting coefficients b into list, append sse and interno to list
            b.append(sse); b.append(iterno)
            WRC[model-1].loc[k,:]=b #set b into dataframe row in list WRC[model-1]
            
            if showfigs and model==1 and len(wc[ix])>0:
                plt.figure(1)
                #plt.cla()                
                plt.title('sample' + str(k))
                plt.semilogx(psi[ix],wc[ix],'ko',label='obs')
                plt.xlabel('kPa'); plt.ylabel('WC (m3/m3)')
                #plt.draw(); plt.show()
                
            
            if showfigs and len(wc[ix])>0:
                myWP = np.logspace(-5, 5, 100)
                myWC = estimate(model, b, myWP)
                             
                plt.semilogx(myWP, myWC, '-', label=modelstr[model-1])
                plt.legend()            
        
        if showfigs: plt.draw(); plt.show(block=True)        
        #raw_input('press enter')
        
    #return dataframe 'dat' and list of fitting values in WRC                
    return dat, WRC

def read_Vedenpidatysdata(fname, sheet):
    #reads vedenpidätysdata frome excel-file, prepared by Juha Heiskanen
    #read original data, change headers 
    dat=pd.read_excel(fname, sheetname=sheet, header=1)
    cols=dat.columns.tolist()
    fi=cols.index(0.01); li=cols.index(1500)
    cols[fi:li+1]=['tp','WC03_x',	'WC1_x',	'WC5_x',	'WC10_x',	'WC33_x',	'WC100_x',	'WC1500_x']
    dat.columns=cols
    del fi, li
    
    # list units in dictionary
    units={'Db_x':'g/cm2', 'Ds': 'g/cm2', 'Org': '%', 'tp': '%','WCn_':'%','vn_':'%', 'KivetM': 'g', 'KivetV': 'cm3'}

    return dat, cols, units
    
#def WRC_Campbell(v, psi):
#    theta=np.empty(len(psi))
#    thetaS = v[0]
#    he = v[1]
#    Campbell_b= v[2]
#    for i in range(len(psi)):
#        if psi[i] <= he:
#            theta[i] = thetaS
#        else:
#            Se = (psi[i]/he)**(-1./Campbell_b) 
#            theta[i] = Se * thetaS 
#    return theta
#def WRC_VanGenuchten(v, psi):
#    theta=np.empty(len(psi))
#    thetaS = v[0]
#    VG_thetaR = v[1]
#    VG_alpha = v[2]
#    VG_n = v[3]
#    VG_m = v[4]
#    for i in range(len(psi)):
#        Se = 1. / pow(1. + pow(VG_alpha * psi[i], VG_n), VG_m)       
#        theta[i] = Se * (thetaS - VG_thetaR) + VG_thetaR
#    return theta
#        
#def WRC_VanGenuchtenRestricted(v, psi):
#    theta=np.empty(len(psi))    
#    thetaS = v[0]
#    VG_thetaR = v[1]
#    VG_alpha = v[2]
#    VG_n = v[3]
#    VG_m = 1. - (1. / VG_n)
#    for i in range(len(psi)):
#        if psi[i] <= 0: 
#            Se = 0
#        else:
#            Se = (1. + (VG_alpha * abs(psi[i]))**VG_n)**(-VG_m)       
#        theta[i] = Se * (thetaS - VG_thetaR) + VG_thetaR  
#    return theta 
#    
#def WRC_IppischVanGenuchten(v, psi):
#    theta=np.empty(len(psi))
#    thetaS = v[0]
#    VG_thetaR = v[1]
#    he = v[2]
#    VG_alpha = v[3]
#    VG_n = v[4]
#    VG_m = 1. - (1./VG_n)
#    VG_Sc = (1. + (VG_alpha * he)**VG_n)**VG_m
#    for i in range(len(psi)):
#        if (psi[i] <= he): 
#            Se = 1.0
#        else: 
#            Se = VG_Sc * (1. + (VG_alpha * abs(psi[i]))**VG_n)**(-VG_m)  
#        theta[i] = Se * (thetaS - VG_thetaR) + VG_thetaR  
#    return theta
#     
#def WRC_CampbellIppischVanGenuchten(v, psi, theta):
#    theta=np.empty(len(psi))    
#    thetaS = v[0]
#    VG_thetaR = v[1]
#    he = v[2]
#    VG_alpha = v[3]
#    VG_n = v[4]
#    VG_m = 1. - (1./VG_n)
#    VG_Sc = (1. + (VG_alpha * he)**VG_n)**VG_m
#    for i in range(len(psi)):
#        if (psi[i] <= he): 
#            Se = 1.0
#        else: 
#            Se = VG_Sc * (1. + (VG_alpha * abs(psi[i]))**VG_n)**(-VG_m)  
#        residual = VG_thetaR * (1 - ((np.log(VG_alpha*psi[i] + 1.0)/np.log(VG_alpha*(10**6) + 1.0))))
#        theta[i] = max(0.0, Se * (thetaS - residual) + residual)
#    return theta