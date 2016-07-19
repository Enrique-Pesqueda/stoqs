#!/usr/bin/env python
'''

Master loader for all Coordinated Canyon Experiment data
from October 2015 through 2016

Mike McCann
MBARI 26 January March 2016
'''

import os
import sys
from datetime import datetime
parent_dir = os.path.join(os.path.dirname(__file__), "../")
sys.path.insert(0, parent_dir)  # settings.py is one dir up

from CCE import CCELoader

cl = CCELoader('stoqs_cce2015', 'Coordinated Canyon Experiment',
                description = 'Coordinated Canyon Experiment - Measuring turbidity flows in Monterey Submarine Canyon',
                x3dTerrains = { 
                    'http://stoqs.mbari.org/x3d/MontereyCanyonBeds_1m+5m_1x_src/MontereyCanyonBeds_1m+5m_1x_src_scene.x3d': {
                        'name': 'MontereyCanyonBeds_1m+5m_1x',
                        'position': '2232.80938 10346.25515 3543.76722',
                        'orientation': '-0.98394 0.16804 -0.06017 1.25033',
                        'centerOfRotation': '0 0 0',
                        'VerticalExaggeration': '1',
                        'geoOrigin': '36.80, -121.87, -400',
                        'speed': '1.0',
                        'zNear': '100.0',
                        'zFar': '30000.0',
                        'selected': '1'
                    },
                    'http://stoqs.mbari.org/x3d/Monterey25_1x/Monterey25_1x_src_scene.x3d': {
                        'name': 'Monterey25_1x',
                        'position': '-32985.28634 88026.90417 22334.02600',
                        'orientation': '-0.99875 -0.04772 0.01482 1.31683',
                        'centerOfRotation': '-20564.015827789044 -1956.065669754069 14112.954469753739',
                        'VerticalExaggeration': '1',
                        'geoOrigin': '36.80, -121.87, -400',
                        'speed': '1.0',
                        'zNear': '-1',
                        'zFar': '-1',
                    },
                 },
                 # Do not check in .grd files to the repository, keep them in the loaders directory
                 ##grdTerrain=os.path.join(parent_dir, 'MontereyCanyonBeds_1m+5m.grd'),
                 grdTerrain=os.path.join(parent_dir, 'Monterey25.grd'),
               )

# Base OPeNDAP server
cl.bed_base = 'http://elvis64.shore.mbari.org/opendap/data/CCE_Processed/BEDs/'

# Copied from ProjectLibrary to BEDs SVN working dir for netCDF conversion, and then copied to elvis.
# See BEDs/BEDs/Visualization/py/makeBEDNetCDF_CCE.sh

cl.bed_parms = ['XA', 'YA', 'ZA', 'A', 'XR', 'YR', 'ZR', 'ROT_RATE', 'ROT_COUNT', 'P', 'P_ADJUSTED',
                'P_RATE', 'P_SPLINE', 'P_SPLINE_RATE', 'ROT_DIST', 'IMPLIED_VELOCITY', 'BED_DEPTH']

# Several BED files: 30200078 to 3020080
# bed_files, bed_platforms, bed_depths must have same number of items; they are zipped together in the load
##cl.bed_files = [('CanyonEvents/BED3/20151001_20160115/{}.nc').format(n) for n in range(30200078, 30200081)]
##cl.bed_platforms = ['BED03'] * len(cl.bed_files)
##cl.bed_depths = [201] * len(cl.bed_files)

# Just the event files for the CCE
cl.bed_files = [
                'BED05/MBCCE_BED05_20151027_Event20151201/netcdf/50200024_decimated_trajectory.nc',
                'BED03/20151001_20160115/netcdf/30200078_trajectory.nc',
                'BED06/20151001_20160115/netcdf/60100068_trajectory.nc',
                'BED03/MBCCE_BED03_20160212_Event20160217/netcdf/30300004_trajectory.nc',
                'BED05/MBCCE_BED05_20151027_Event20160115/netcdf/50200054_trajectory.nc',
                'BED05/MBCCE_BED05_20151027_Event20160115/netcdf/50200055_trajectory.nc',
                'BED05/MBCCE_BED05_20151027_Event20160115/netcdf/50200056_trajectory.nc',
                'BED05/MBCCE_BED05_20151027_Event20160115/netcdf/50200057_trajectory.nc',
                'BED03/MBCCE_BED03_20160212_Event20160306/netcdf/30300016_trajectory.nc',
                'BED04/MBCCE_BED04_20151004_Event20151201/netcdf/40100037_trajectory.nc',
               ]
cl.bed_platforms = ['BED05', 'BED03', 'BED06', 'BED03', 'BED05', 'BED05', 'BED05', 'BED05', 'BED03', 'BED04']
cl.bed_depths = [388, 201, 521, 289.3, 413, 420, 430, 433, 308, 294]
cl.bed_framegrabs = [
                'http://search.mbari.org/ARCHIVE/frameGrabs/Ventana/stills/2015/vnta3873/00_29_56_03.html',
                'http://search.mbari.org/ARCHIVE/frameGrabs/Ventana/stills/2015/vnta3874/00_21_23_28.html',
                'http://search.mbari.org/ARCHIVE/frameGrabs/Ventana/stills/2015/vnta3870/00_15_38_23.html',
                '',
                '',
                '',
                '',
                '',
                '',
                'http://search.mbari.org/ARCHIVE/frameGrabs/Ventana/stills/2015/vnta3872/00_17_50_24.html',
                    ]

# CCE BIN data
cl.ccebin_startDatetime = datetime(2016, 1, 15)
cl.ccebin_endDatetime = datetime(2016, 1, 18)
cl.ccebin_nominaldepth = 1836
cl.ccebin_base = 'http://elvis64.shore.mbari.org/opendap/data/CCE_Processed/BIN/20151013/netcdf/'
cl.ccebin_files = [
                    'MBCCE_BIN_CTD_20151013_timecorrected.nc',
                    'MBCCE_BIN_OXY_20151013_timecorrected.nc',
                    'MBCCE_BIN_ECO_20151013_timecorrected.nc',
                  ]
cl.ccebin_parms = [ 'pressure', 'temperature', 'conductivity', 'turbidity', 'optical_backscatter',
                    'oxygen', 'saturation', 'optode_temperature',
                    'chlor', 'ntu1', 'ntu2' ]

# MS1 ADCP data
cl.ccems1_nominal_depth = 225
cl.ccems1_base = 'http://elvis64.shore.mbari.org/opendap/data/CCE_Archive/MS1/20151006/ADCP300/'
cl.ccems1_files = [ 'MBCCE_MS1_ADCP300_20151006.nc' ]
cl.ccems1_parms = [ 'u_1205', 'v_1206', 'w_1204', 'AGC_1202', 'Hdg_1215', 'Ptch_1216', 'Roll_1217']

# MS2 ADCP data
cl.ccems2_nominal_depth = 462
cl.ccems2_base = 'http://elvis64.shore.mbari.org/opendap/data/CCE_Archive/MS2/20151005/ADCP300/'
cl.ccems2_files = [ 'MBCCE_MS2_ADCP300_20151005.nc' ]
cl.ccems2_parms = [ 'u_1205', 'v_1206', 'w_1204', 'AGC_1202', 'Hdg_1215', 'Ptch_1216', 'Roll_1217']

# MS3 ADCP data
cl.ccems3_nominal_depth = 764
cl.ccems3_base = 'http://elvis64.shore.mbari.org/opendap/data/CCE_Archive/MS3/20151005/ADCP300/'
cl.ccems3_files = [ 'MBCCE_MS3_ADCP300_20151005.nc' ]
cl.ccems3_parms = [ 'u_1205', 'v_1206', 'w_1204', 'AGC_1202', 'Hdg_1215', 'Ptch_1216', 'Roll_1217']

# MS4-7 ADCP data - No NetCDF files seen in http://elvis64.shore.mbari.org/opendap/hyrax/data/CCE_Archive/
##cl.ccems4_nominal_depth = 462
##cl.ccems4_base = 'http://elvis64.shore.mbari.org/opendap/data/CCE_Archive/MS4...'
##cl.ccems4_files = [ '' ]
##cl.ccems4_parms = [ 'u_1205', 'v_1206', 'w_1204', 'AGC_1202', ]
##cl.ccems2_parms = [ 'u_1205', 'v_1206', 'w_1204', 'AGC_1202', 'Hdg_1215', 'Ptch_1216', 'Roll_1217']


# Full-deployment files, exatracted from SSDS with stride of 60
##cl.ccebin_base = 'http://dods.mbari.org/opendap/data/ssdsdata/deployments/ccebin2015/201510/'
##cl.ccebin_files = [
##                'ccebin2015_aanderaaoxy_20151013.nc',
##                'ccebin2015_adcp1825_20151013.nc',
##                'ccebin2015_adcp1827_20151013.nc',
##                'ccebin2015_adcp1828_20151013.nc',
##                'ccebin2015_ecotriplet_20151013.nc',
##                'ccebin2015_sbe16_20151013.nc',
##               ]
##cl.ccebin_base = 'http://dods.mbari.org/opendap/data/ssdsdata/deployments/ccebin20160115/201601/'
##cl.ccebin_files = [
##                ##'ccebin20160115_aanderaaoxy_20160115.nc',
##                'ccebin20160115_adcp1825_20160115.nc',
##                'ccebin20160115_adcp1827_20160115.nc',
##                'ccebin20160115_adcp1828_20160115.nc',
##                ##'ccebin20160115_ecotriplet_20160115.nc',
##                ##'ccebin20160115_sbe16_20160115.nc',
##               ]
##cl.ccebin_parms = [
##                'u_component_uncorrected', 'v_component_uncorrected',
##                'echo_intensity_beam1', 
##                #'echo_intensity_beam2', 'echo_intensity_beam3', 'echo_intensity_beam4',
##                #'std_head', 'std_pitch', 'std_roll', 'xdcr_temperature',
##                ##'Pressure', 'Salinity', 'Temperature',
##                ##'AirSaturation', 'Oxygen',
##                ##'Chlor', 'NTU1', 'NTU2',
##                  ] 


# Execute the load for trajectory representation
cl.process_command_line()

if cl.args.test:
    # MS1: Low-res
    cl.ccems1_start_datetime = datetime(2016, 1, 15)
    cl.ccems1_end_datetime = datetime(2016, 1, 18)
    cl.load_ccems1(stride=200)

    # High-res
    cl.ccems1_start_datetime = datetime(2016, 1, 15, 19, 0)
    cl.ccems1_end_datetime = datetime(2016, 1, 16, 0, 30)
    cl.load_ccems1(stride=10)

    # MS2: Low-res
    cl.ccems2_start_datetime = datetime(2016, 1, 15)
    cl.ccems2_end_datetime = datetime(2016, 1, 18)
    cl.load_ccems2(stride=200)

    # High-res
    cl.ccems2_start_datetime = datetime(2016, 1, 15, 21, 0)
    cl.ccems2_end_datetime = datetime(2016, 1, 16, 2, 0)
    cl.load_ccems2(stride=10)

    # MS3: Low-res
    cl.ccems3_start_datetime = datetime(2016, 1, 15)
    cl.ccems3_end_datetime = datetime(2016, 1, 18)
    cl.load_ccems3(stride=200)

    # High-res
    cl.ccems3_start_datetime = datetime(2016, 1, 15, 21, 0)
    cl.ccems3_end_datetime = datetime(2016, 1, 16, 2, 0)
    cl.load_ccems3(stride=10)

    # MS4: Low-res
    ##cl.ccems4_start_datetime = datetime(2016, 1, 15)
    ##cl.ccems4_end_datetime = datetime(2016, 1, 18)
    ##cl.load_ccems4(stride=200)

    # High-res
    ##cl.ccems4_start_datetime = datetime(2016, 1, 15, 21, 0)
    ##cl.ccems4_end_datetime = datetime(2016, 1, 16, 2, 0)
    ##cl.load_ccems4(stride=10)


    # BIN: Low-res (10 minute) five day period
    cl.ccebin_startDatetime = datetime(2016, 1, 13)
    cl.ccebin_endDatetime = datetime(2016, 1, 18)
    cl.loadCCEBIN(stride=300)

    # High-res (2 second) 1-hour period
    cl.ccebin_startDatetime = datetime(2016, 1, 15, 23, 30)
    cl.ccebin_endDatetime = datetime(2016, 1, 16, 0, 30)
    cl.loadCCEBIN(stride=1)

    cl.loadBEDS(stride=5, featureType='trajectory')

elif cl.args.optimal_stride:
    ##cl.loadCCEBIN(stride=1)
    cl.loadBEDS(stride=1, featureType='trajectory')

else:
    cl.stride = cl.args.stride

    # MS1: Low-res (10 minute) three day period
    cl.ccems1_start_datetime = datetime(2016, 1, 15)
    cl.ccems1_end_datetime = datetime(2016, 1, 18)
    cl.load_ccems1(stride=20)

    # High-res (30 second) ~1-hour period - until data end when MS1 broke loose
    cl.ccems1_start_datetime = datetime(2016, 1, 15, 19, 0)
    cl.ccems1_end_datetime = datetime(2016, 1, 16, 0, 30)
    cl.load_ccems1(stride=1)

    # MS2: Low-res (10 minute) three day period
    cl.ccems2_start_datetime = datetime(2016, 1, 15)
    cl.ccems2_end_datetime = datetime(2016, 1, 18)
    cl.load_ccems2(stride=20)

    # High-res (30 second) 5-hour period
    cl.ccems2_start_datetime = datetime(2016, 1, 15, 21, 0)
    cl.ccems2_end_datetime = datetime(2016, 1, 16, 2, 0)
    cl.load_ccems2(stride=1)

    # MS3: Low-res (10 minute) three day period
    cl.ccems3_start_datetime = datetime(2016, 1, 15)
    cl.ccems3_end_datetime = datetime(2016, 1, 18)
    cl.load_ccems3(stride=20)

    # High-res (30 second) 5-hour period
    cl.ccems3_start_datetime = datetime(2016, 1, 15, 21, 0)
    cl.ccems3_end_datetime = datetime(2016, 1, 16, 2, 0)
    cl.load_ccems3(stride=1)

    # MS4: Low-res (10 minute) three day period
    ##cl.ccems4_start_datetime = datetime(2016, 1, 15)
    ##cl.ccems4_end_datetime = datetime(2016, 1, 18)
    ##cl.load_ccems4(stride=20)

    # High-res (30 second) 5-hour period
    ##cl.ccems4_start_datetime = datetime(2016, 1, 15, 21, 0)
    ##cl.ccems4_end_datetime = datetime(2016, 1, 16, 2, 0)
    ##cl.load_ccems4(stride=1)

    # Low-res (10 minute) three day period
    cl.ccebin_startDatetime = datetime(2016, 1, 13)
    cl.ccebin_endDatetime = datetime(2016, 1, 18)
    cl.loadCCEBIN(stride=300)

    # High-res (2 second) 1-hour period
    cl.ccebin_startDatetime = datetime(2016, 1, 15, 23, 30)
    cl.ccebin_endDatetime = datetime(2016, 1, 16, 0, 30)
    cl.loadCCEBIN()

    cl.loadBEDS(featureType='trajectory')

# Add any X3D Terrain information specified in the constructor to the database - must be done after a load is executed
cl.addTerrainResources()

print "All Done."
