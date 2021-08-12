import cdstoolbox as ct

'''

Script to download temperature- adapt for variable only for precipitation

'''

# establish connection and function needed

@ct.application(title='Download data')
@ct.output.download()
def download_application():
    data = ct.catalogue.retrieve(
        # select dataset
        'reanalysis-era5-land',
        {   # select variable (can be changed for precipitation)
            'variable': '2m_temperature',
            
            # select year (no more than 7 recommended as this will fill download capacity)
            
            'year': [
                '2015', '2016', '2017',
                '2018', '2019', '2020',
                '2021',
            ],
            
             # select months (all months acceptable if needed and data is aportioned by year 
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            # select days (overfill for all days, months with less numbers will disregard excess days)
            'day': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
                '13', '14', '15',
                '16', '17', '18',
                '19', '20', '21',
                '22', '23', '24',
                '25', '26', '27',
                '28', '29', '30',
                '31',
            ],
            
            # select hours
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
        }
    )
    return data
