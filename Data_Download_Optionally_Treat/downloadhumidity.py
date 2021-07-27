import cdsapi

'''

Intent

Download 1 year of humidity data per modification in a zip file.

Necessary for user to modify as the size of each file may yield storage issues.
Batch requests also yield occassional errors and file omissions that may not
be accounted for until late in processing.

Each file represents in excess of 1.3 GB and will require clipping to extent.

Network connection required to connect to API, with request also requiring stability
for download times of approximately an hour per year (download timecan be overlapped
but it is recommended that this does not exceed 4 years at a time).

'''

#Initiate clinet
c = cdsapi.Client()
    #Identify dataset alias stored at dataset web page and API code sampler
    'sis-agrometeorological-indicators',
    {   #Identify variable held at dataset web page
        'variable': '2m_relative_humidity',
        #Designate Year, months.
        'year': '2003',
        'month': [
            '01','02','03','04',
            '05','06','07','08',
            '09','10','11','12'
        ],
        #Designate time, all available are selected here.
        'time': [
            '06_00','09_00','12_00',
            '15_00','18_00',
        ],
        # Designate format
        'format': 'zip',
    },
    # Designate directory to download zipfiles to.
    'M:\Diss_data\Final\Humidity\Raw_Data\download3.zip')
