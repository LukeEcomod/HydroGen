"""
IO tools to handle BioSoil excel data compiled by Juha Heiskanen


CREATED: 28.06.2021
AUTHOR: Antti-Jussi Kieloaho
"""

import numpy as np
import pandas as pd

# columns-dict keys are original column names that are needed in further analysis
# rest of the original columns are discarded
# as a value there is a tuple containing two elements:
# 0. new column name
# 1. meta information describing the column content; pieces of information are separated by semicolon (;)

columns = {
    'VMI': ('site_id', ''),
    'Vuosi': ('year', ''),
    'Kk': ('month', ''),
    'Pv': ('day', ''),
    'Pkoord': ('lat_N', 'KKJ'),
    'Ikoord': ('lon_E', 'KKJ'),
    'Kork': ('altitude',  '[m]'),
    'Maa': ('soil_type', '3=till, 4=sorted'),
    'RaeK': ('grain_size',  '1=clay/silt (savi, hiesu, hieno hieta); 2=silt/sand (karkea hieta, hieno hiekka); 3=sand/gravel (karkea hiekka, sora)'),
    'Hpaks_cm': ('orglayer_thickness', '[cm]'),
    'Topo': ('topography', '0=flat; 1=hilltop/uphill; 2=hillside; 3=downhill; 4=hollow/depression; 5=other'),  
    'Kalt': ('slope', '[degrees]'),
    'Kost_lk': ('hydraulic_regime', '1=barren heath; 2=sub-xeric; 3=xeric; 4=mesic; 5=?; 6=hydric'),
    'Suosamm': ('peat_forming_mosses', '[%]'),
    'KPT': ('sitetype', '1=herb-rich; 2=?; 3=mesic; 4=xeric; 5=subxeric; 6=barren heath; 7=rocky or sandy areas; 8=hilltops'),   
    'Krs1': ('vmi_horizon_1', '201=0-10cm; 202=10-20cm; 203=20-40cm; 0-6cm'),
    #'Ylär1': 'sample_top_1',  # [cm] from ground
    'Clay1': ('clay_1', 'clay (<2um) content; 0-6cm'),
    'Silt1': ('silt_1', 'silt (2-20um) content; 0-6cm'),
    'Sand1': ('sand_1', 'sand (20-63um) content; 0-6cm'),
    'BD1': ('raw_bulk_density_1', 'bulk density [g cm-3]; 0-6cm'),
    #'Kost1': None,
    'Sora1': ('gravel_1', 'gravel (>2mm) content; 0-6cm'), 
    'Krs2': ('vmi_horizon_2', '201=0-10cm; 202=10-20cm; 203=20-40cm; 15-21cm'),
    #'Ylär2'; 'sample_top_2',  # [cm] from ground
    'Clay2': ('clay_2', 'clay (<2um) content; 15-21cm'),
    'Silt2': ('silt_2', 'silt (2-20um) content; 15-21cm'),
    'Sand2': ('sand_2', 'sand (20-63um) content; 15-21cm'),
    'BD2': ('raw_bulk_density_2', 'bulk density [g cm-3]; 15-21cm'),
    #'Kost2': None,
    'Sora2': ('gravel_2', 'gravel (>2mm) content; 15-21cm'), 
    'Krs3': ('vmi_horizon_3', ''),  
    #'Ylär3': 'sample_top_3',
    'Clay3': ('clay_3', 'clay (<2um) content; 30-36cm'),
    'Silt3': ('silt_3', 'silt (2-20um) content; 30-36cm'),
    'Sand3': ('sand_3', 'sand (20-63um) content; 30-36cm'),
    'BD3': ('raw_bulk_density_3', 'bulk density [g cm-3]; 30-36cm'),
    #'Kost3': None,
    'Sora3': ('gravel_3', 'gravel (>2mm) content; 30-36cm'), 
    #'Yläreuna1': None,
    #'Lieriö1': None,
    'Ds1': ('dry_density_1', 'dry density [g cm-3]; 0-6cm'),  
    'Org1': ('organic_content_1', 'organic content [g g-1]; 0-6cm'), 
    'v03_1': ('raw_vwc_03kPa_1', 'volumetric water content [cm3 cm-3] at 0.3 kPa; 0-6cm'),
    'v1_1': ('raw_vwc_1kPa_1', 'volumetric water content [cm3 cm-3] at 1 kPa; 0-6cm'),
    'v5_1': ('raw_vwc_5kPa_1', 'volumetric water content [cm3 cm-3] at 5 kPa; 0-6cm'),
    'v10_1': ('raw_vwc_10kPa_1', 'volumetric water content [cm3 cm-3] at 10 kPa; 0-6cm'),
    'v100_1': ('raw_vwc_100kPa_1', 'volumetric water content [cm3 cm-3] at 100 kPa; 0-6cm'),
    'häiriö_1': ('disturbance_flag_1', '0=undisturbed; 0-6cm'),
    #'Kivi20_1': 'mass_stones_large_1',  # [g] stones <20mm 0-6cm
    #'Kivi1020_1': 'mass_stones_small_1', # [g] stones 10-20mm 0-6cm
    'Kivi10_1': ('mass_stones_1', 'mass of stones <10mm [g]; 0-6cm'),
    'Vkiv_1': ('vol_stones_1', 'volume of stones <10mm [cm3]; 0-6cm'),
    'TPx1': ('vwc_001kPa_1', 'volumetric water content [cm3 cm-3] at 0.01 kPa stone corrected; total porosity; 0-6cm'),
    'WC03x_1': ('vwc_03kPa_1', 'volumetric water content [cm3 cm-3] at 0.3 kPa stone corrected; 0-6cm'),
    'WC1x_1': ('vwc_1kPa_1', 'volumetric water content [cm3 cm-3] at 1 kPa stone corrected; 0-6cm'),
    'WC5x_1': ('vwc_5kPa_1', 'volumetric water content [cm3 cm-3] at 5 kPa stone corrected; 0-6cm'),
    'WC10x_1': ('vwc_10kPa_1', 'volumetric water content [cm3 cm-3] at 10 kPa stone corrected; 0-6cm'),
    'WC100x_1': ('vwc_100kPa_1', 'volumetric water content [cm3 cm-3] at 100 kPa stone corrected; 0-6cm'),
    'WC1500x_1': ('vwc_1500kPa_1', 'volumetric water content [cm3 cm-3] at 1500 kPa; 0-6cm'),
    'Dbx_1': ('bulk_density_1', 'bulk density [g cm-3] stone corrected; 0-6cm'),
    #'Yläreuna2': None,
    #'Lieriö2': None,
    'Ds2': ('dry_density_2', 'dry density [g cm-3]; 15-21cm'),
    'Org2': ('organic_content_2', 'organic content [g g-1]; 15-21cm'),
    'v03_2': ('raw_vwc_03kPa_2', 'volumetric water content [cm3 cm-3] at 0.3 kPa; 15-21cm'),
    'v1_2': ('raw_vwc_1kPa_2', 'volumetric water content [cm3 cm-3] at 1 kPa; 15-21cm'),
    'v5_2': ('raw_vwc_5kPa_2', 'volumetric water content [cm3 cm-3] at 5 kPa; 15-21cm'),
    'v10_2': ('raw_vwc_10kPa_2', 'volumetric water content [cm3 cm-3] at 10 kPa; 15-21cm'),
    'v100_2': ('raw_vwc_100kPa_2', 'volumetric water content [cm3 cm-3] at 100 kPa; 15-21cm'),
    'häiriö_2': ('disturbance_flag_2', '0=undisturbed; 15-21cm'),
    #'Kivi20_2': 'mass_stones_large_2',  # [g] stones <20mm 15-21cm'),
    #'Kivi1020_2': 'mass_stones_small_2', # [g] stones 10-20mm 15-21cm'),
    'Kivi10_2': ('mass_stones_2', '[g] stones <10mm; 15-21cm'),
    'Vkiv_2': ('vol_stones_2', '[cm3] stones <10mm; 15-21cm'),
    'TPx2': ('vwc_001kPa_2', 'volumetric water content[cm3 cm-3] at 0.01 kPa stone corrected; total porosity; 15-21cm'),
    'WC03x_2': ('vwc_03kPa_2', 'volumetric water content [cm3 cm-3] at 0.3 kPa stone corrected; 15-21cm'),
    'WC1x_2': ('vwc_1kPa_2', 'volumetric water content [cm3 cm-3] at 1 kPa stone corrected; 15-21cm'),
    'WC5x_2': ('vwc_5kPa_2', 'volumetric water content [cm3 cm-3] at 5 kPa stone corrected; 15-21cm'),
    'WC10x_2': ('vwc_10kPa_2', 'volumetric water content [cm3 cm-3] at 10 kPa stone corrected; 15-21cm'),
    'WC100x_2': ('vwc_100kPa_2', 'volumetric water content [cm3 cm-3] at 100 kPa stone corrected; 15-21cm'),
    'WC1500x_2': ('vwc_1500kPa_2', 'volumetric water content [cm3 cm-3] at 1500 kPa; 15-21cm'),
    'Dbx_2': ('bulk_density_2', 'bulk density [g cm-3] stone corrected; 15-21cm'),
    #'Yläreuna3': None,
    #'Lieriö3': None,
    'Ds3': ('dry_density_3', 'dry density [g cm-3]; 30-36cm'),
    'Org3': ('organic_content_3', 'organic content [g g-1]; 30-36cm'),
    'v03_3': ('raw_vwc_03kPa_3', 'volumetric water content [cm3 cm-3] at 0.3 kPa; 30-36cm'),
    'v1_3': ('raw_vwc_1kPa_3', 'volumetric water content [cm3 cm-3] at 1 kPa; 30-36cm'),
    'v5_3': ('raw_vwc_5kPa_3', 'volumetric water content [cm3 cm-3] at 5 kPa; 30-36cm'),
    'v10_3': ('raw_vwc_10kPa_3', 'volumetric water content [cm3 cm-3] at 10 kPa; 30-36cm'),
    'v100_3': ('raw_vwc_100kPa_3', 'volumetric water content [cm3 cm-3] at 100 kPa; 30-36cm'),
    'häiriö_3': ('disturbance_flag_3', '0=undisturbed; 30-36cm'),
    #'Kivi20_3': 'mass_stones_large_3', '[g] stones <20mm 30-36cm'),
    #'Kivi1020_3': 'mass_stones_small_3', '[g] stones 10-20mm 30-36cm'),
    'Kivi10_3': ('mass_stones_3', 'mass of stones <10mm [g]; 30-36cm'),
    'Vkiv_3': ('vol_stones_3', 'volume of stones <10mm [cm3]; 30-36cm'),
    'TPx3': ('vwc_001kPa_3', 'volumetric water content [cm3 cm-3] at 0.01 kPa stone corrected; total porosity; 30-36cm'),
    'WC03x_3': ('vwc_03kPa_3', 'volumetric water content [cm3 cm-3] at 0.3 kPa stone corrected; 30-36cm'),
    'WC1x_3': ('vwc_1kPa_3', 'volumetric water content [cm3 cm-3] at 1 kPa stone corrected; 30-36cm'),
    'WC5x_3': ('vwc_5kPa_3', 'volumetric water content [cm3 cm-3] at 5 kPa stone corrected; 30-36cm'),
    'WC10x_3': ('vwc_10kPa_3', 'volumetric water content [cm3 cm-3] at 10 kPa stone corrected; 30-36cm'),
    'WC100x_3': ('vwc_100kPa_3', 'volumetric water content [cm3 cm-3] at 100 kPa stone corrected; 30-36cm'),
    'WC1500x_3': ('vwc_1500kPa_3', 'volumetric water content [cm3 cm-3] at 1500 kPa; 30-36cm'),
    'Dbx_3': ('bulk_density_3', 'bulk density [g cm-3] stone corrected; 30-36cm'),
    #'Yläreuna4': None,
    'Bhor': ('bhor', 'is sample from 0-6cm in B-horizon: 0=False, 1=True'),
    #'Lieriö4': None,
    'Ds4': ('dry_density_4', 'dry density [g cm-3]; 0-6cm'),
    'Org4': ('organic_content_4', 'organic content [g g-1]; 0-6cm'),
    'v03_4': ('raw_vwc_03kPa_4', 'volumetric water content [cm3 cm-3] at 0.3 kPa; 0-6cm'),
    'v1_4': ('raw_vwc_1kPa_4', 'volumetric water content [cm3 cm-3] at 1 kPa; 0-6cm'),
    'v5_4': ('raw_vwc_5kPa_4', 'volumetric water content [cm3 cm-3] at 5 kPa; 0-6cm'),
    'v10_4': ('raw_vwc_10kPa_4', 'volumetric water content [cm3 cm-3] at 10 kPa; 0-6cm'),
    'v100_4': ('raw_vwc_100kPa_4', 'volumetric water content [cm3 cm-3] at 100 kPa; 0-6cm'),
    'häiriö_4': ('disturbance_flag_4', '0=undisturbed; 0-6cm'),
    #'Kivi20_4': 'mass_stones_large_4',  # [g] stones <20mm 0-6cm'),
    #'Kivi1020_4': 'mass_stones_small_4', # [g] stones 0-6cm'),
    'Kivi10_4': ('mass_stones_4', 'mass of stones <10mm [g]; 0-6cm'),
    'Vkiv_4': ('vol_stones_4', 'volume of stones <10mm [cm3]; 0-6cm'),
    'TPx4': ('vwc_001kPa_4', 'volumetric water content [cm3 cm-3] at 0.01 kPa stone corrected; total porosity 0-6cm'),
    'WC03x_4': ('vwc_03kPa_4', 'volumetric water content [cm3 cm-3] at 0.3 kPa stone corrected; 0-6cm'),
    'WC1x_4': ('vwc_1kPa_4', 'volumetric water content [cm3 cm-3] at 1 kPa stone corrected; 0-6cm'),
    'WC5x_4': ('vwc_5kPa_4', 'volumetric water content [cm3 cm-3] at 5 kPa stone corrected; 0-6cm'),
    'WC10x_4': ('vwc_10kPa_4', 'volumetric water content [cm3 cm-3] at 10 kPa stone corrected; 0-6cm'),
    'WC100x_4': ('vwc_100kPa_4', 'volumetric water content [cm3 cm-3] at 100 kPa stone corrected; 0-6cm'),
    'WC1500x_4': ('vwc_1500kPa_4', 'volumetric water content [cm3 cm-3] at 1500 kPa; 0-6cm'),
    'Dbx_4': ('bulk_density_4', 'bulk density [g cm-3] stone corrected; 0-6cm'),
    #'Unnamed: 128': None,
    'AFP10_1': ('afp_10kPa_1', 'air filled porosity [volumetric %]; 0-6cm'),
    'AFP10_2': ('afp_10kPa_2', 'air filled porosity [volumetric %]; 15-21cm'),
    'AFP10_3': ('afp_10kPa_3', 'air filled porosity [volumetric %]; 30-36cm'),
    'AFP10_4': ('afp_10kPa_4', 'air filled porosity [volumetric %]; 0-6cm'),
    'PAWC_1': ('raw_paw_1', 'plant available water from 10kPa to 1500kPa []; 0-6cm'),
    'PAWC_2': ('raw_paw_2', 'plant available water from 10kPa to 1500kPa []; 15-21cm'),
    'PAWC_3': ('raw_paw_3', 'plant available water from 10kPa to 1500kPa []; 30-36cm'),
    'PAWC_4': ('raw_paw_4', 'plant available water from 10kPa to 1500kPa []; 0-6cm'),
    'PAWCx1': ('paw_1', 'plant available water from 10kPa to 1500kPa []; stone corrected 0-6cm'),
    'PAWCx2': ('paw_2', 'plant available water from 10kPa to 1500kPa []; stone corrected 15-21cm'),
    'PAWCx3': ('paw_3', 'plant available water from 10kPa to 1500kPa []; stone corrected 30-36cm'),
    'PAWCx4': ('paw_4', 'plant available water from 10kPa to 1500kPa []; stone corrected 0-6cm'),
    'Org_Clay_1': ('org+clay_ratio_1', '[%]'),
    'Org_Clay_2': ('org+clay_ratio_2', '[%]'),
    'Org_Clay_3': ('org+clay_ratio_3', '[%]'),
    'Org_Clay_4': ('org+clay_ratio_4', '[%]'),
}


categorical_vars = {
    'soil_type':  {3: 'till', 4: 'sorted'},
    'grain_size':  {1: 'clay/silt', 2: 'silt/sand', 3: 'sand/gravel'},  
    'topography':  {0: 'flat', 1: 'hilltop/uphill', 2: 'hillside', 3: 'downhill', 4: 'hollow/depression', 5: 'other'},
    'hydraulic_regime':  {1: 'barren heath', 2: 'xeric', 3: 'dry mesic', 4: 'mesic', 5: 'wet mesic', 6: 'hydric'},
    'sitetype': {1: 'OMaT', 2: 'OMT', 3: 'MT', 4: 'VT', 5: 'CT', 6: 'CIT', 7: 'outcrop or sandy areas', 8: 'hilltop forests'},
}

def read_Vedenpidatysdata(fname, sheet):
    #reads vedenpidätysdata frome excel-file, prepared by Juha Heiskanen
    #read original data, change headers 
    dat = pd.read_excel(fname, sheetname=sheet, header=1)
    cols = dat.columns.tolist()
    fi = cols.index(0.01)
    li = cols.index(1500)
    
    cols[fi:li+1] = ['tp','WC03_x', 'WC1_x', 'WC5_x', 'WC10_x', 'WC33_x', 'WC100_x', 'WC1500_x']
    
    dat.columns = cols
    
    del fi, li
    
    # list units in dictionary
    units = {
        'Db_x':'g/cm2',
        'Ds': 'g/cm2',
        'Org': '%',
        'tp': '%',
        'WCn_':'%',
        'vn_':'%',
        'KivetM': 'g',
        'KivetV': 'cm3'}

    return dat, cols, units


def read_data(file_path:str, file_name:str, sheet_name:str):
    """ Reads BioSoil data from excel sheet compiled by Juha Heiskanen
    
    Args:
        file_path (str): path to excel
        file_name (str): excel file name
        sheet_name (str): excel file sheet where data lies
    
    Retrurns:
        data (pandas.DataFrame)
    """
    data = pd.read_excel(file_path+file_name, sheet_name=sheet_name, header=0)
    data = data.dropna(axis='index', how='all')
    data.set_index('VMI', inplace=False)
    
    column_names = {key: columns[key][0] for key in columns}
    data[list(columns.keys())]
    data.rename(columns=column_names, inplace=True)

    data = data[column_names.values()]
    data.loc[data.bhor == 'B', 'bhor'] = 1
    data.loc[data.bhor.isnull(), 'bhor'] = 0
    
    return data

def preprocessing_data(data, depth_flags=['1', '2', '3', '4']):
    """ Preprocessing data
    - reconstructing data so that soil depth flag is in own column
    - removing disturbed samples according to distrubance flag
    - removing incomplete water retention data rows
    
    Args:
        data (pandas.DataFrame): containing data
        depth_flags (list): list of strings containing depth flags
    Return:
        data (pandas.DataFrame): containg reconstructed and cleaned data
    """
    
    # reconstruction
    df = pd.DataFrame({'index': range(len(data) * len(depth_flags))})
    df.set_index('index', inplace=True)
    df['depth'] = np.tile(np.array([1, 2, 3, 4]), len(data))

    for col in data:
    
        right_split = col.rsplit('_', 1)
        new_col = np.empty(len(data) * 4).fill(np.NaN)    
    
        if right_split[-1] in depth_flags:
        
            if right_split[0] not in df:
                df[right_split[0]] = new_col
        
            stop = len(df) - 1
            i = int(right_split[-1]) - 1
            j = 0

            while True:
                if i > stop:
                    break

                df[right_split[0]].iloc[i] = data[col].iloc[j]
            
                i = i + 4
                j = j + 1
            
        else:
        
            df[col] = new_col
        
            stop = len(df) - 1
            i = 0
            j = 0
        
            while True:
                for flag in depth_flags:
                    df[col].iloc[i] = data[col].iloc[j]
                
                    i = i + 1
                
                j = j + 1

                if i > stop:
                    break
    
    
    data = df
    # removing disturbed sample rows and incomplete wrc data rows
    regex = ('^(?!raw_)vwc_\d{1,4}kPa$')
    # pick the columns needed to determine water retention curves (wrc)
    # do not pick columns starting with raw_ as those are not stone corrected
    cols_wrc = data.filter(regex=regex).columns.tolist()

    # Cleaning dataframe
    # discard rows that where disturbance flag is raised
    data.loc[data['disturbance_flag'] > 0, cols_wrc] = np.NaN
    # discard rows where water retention data is incomplete 
    data = data.dropna(subset=cols_wrc, how='any')

    data.loc[:, cols_wrc] = data[cols_wrc].astype(np.float)
    
    # Changing categorical data's dtype to category instead of object
    data.replace(categorical_vars, inplace=True)
    for var in categorical_vars:
        if var in data:
            data[var] = data[var].astype(dtype='category')
    
    return data

# EOF