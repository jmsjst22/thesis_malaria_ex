import pandas as pd
import glob
'''
years = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]

datasets = (glob.glob('*.csv'))

print(datasets)
'''

DHS2006 = pd.read_csv('2006_DHS.csv')
DHS2009 = pd.read_csv('2009_DHS.csv')
DHS2011 = pd.read_csv('2011_DHS.csv')
DHS2014 = pd.read_csv('2014_DHS.csv')
DHS2016 = pd.read_csv('2016_DHS.csv')
DHS2018 = pd.read_csv('2018_DHS.csv')

ENV2005 = pd.read_csv('2005_env.csv')
ENV2006 = pd.read_csv('2006_env.csv')
ENV2008 = pd.read_csv('2008_env.csv')
ENV2009 = pd.read_csv('2009_env.csv')
ENV2010 = pd.read_csv('2010_env.csv')
ENV2011 = pd.read_csv('2011_env.csv')
ENV2013 = pd.read_csv('2013_env.csv')
ENV2014 = pd.read_csv('2014_env.csv')
ENV2015 = pd.read_csv('2015_env.csv')
ENV2016 = pd.read_csv('2016_env.csv')
ENV2017 = pd.read_csv('2017_env.csv')
ENV2018 = pd.read_csv('2018_env.csv')

EC2006 = ENV2005.merge(ENV2006,on='DName2018')
EC2009 = ENV2008.merge(ENV2009,on='DName2018')
EC2011 = ENV2010.merge(ENV2011,on='DName2018')
EC2014 = ENV2013.merge(ENV2014,on='DName2018')
EC2016 = ENV2015.merge(ENV2016,on='DName2018')
EC2018 = ENV2017.merge(ENV2018,on='DName2018')

ALL2006 = DHS2006.merge(EC2006,on='DName2018',how='outer')
ALL2009 = DHS2009.merge(EC2009,on='DName2018',how='outer')
ALL2011 = DHS2011.merge(EC2011,on='DName2018',how='outer')
ALL2014 = DHS2014.merge(EC2014,on='DName2018',how='outer')
ALL2016 = DHS2016.merge(EC2016,on='DName2018',how='outer')
ALL2018 = DHS2018.merge(EC2018,on='DName2018',how='outer')

ALL2006.to_csv('f_ALL2006.csv')
ALL2009.to_csv('f_ALL2009.csv')
ALL2011.to_csv('f_ALL2011.csv')
ALL2014.to_csv('f_ALL2014.csv')
ALL2016.to_csv('f_ALL2016.csv')
ALL2018.to_csv('f_ALL2018.csv')

ALL2006 = EC2006.merge(DHS2006,on='DName2018',how='outer')
ALL2009 = EC2009.merge(DHS2009,on='DName2018',how='outer')
ALL2011 = EC2011.merge(DHS2011,on='DName2018',how='outer')
ALL2014 = EC2014.merge(DHS2014,on='DName2018',how='outer')
ALL2016 = EC2016.merge(DHS2016,on='DName2018',how='outer')
ALL2018 = EC2018.merge(DHS2018,on='DName2018',how='outer')

ALL2006.to_csv('o_ALL2006.csv')
ALL2009.to_csv('o_ALL2009.csv')
ALL2011.to_csv('o_ALL2011.csv')
ALL2014.to_csv('o_ALL2014.csv')
ALL2016.to_csv('o_ALL2016.csv')
ALL2018.to_csv('o_ALL2018.csv')
