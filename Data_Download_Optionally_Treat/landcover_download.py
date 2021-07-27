import cdstoolbox as ct

@ct.application(title='Download data')
@ct.output.download()
def download_application():
    data = ct.catalogue.retrieve(
        'satellite-land-cover',
        {
            'year': [
                '2004'
            ],
            'version': [
                'v2.0.7cds',
            ],
            'variable': 'all',
        }
    )
    #area selection introduced in 2021 update, spatially limit by coordinates
    #West,East,South,North latitude,longitude geographic
    area_sel = ct.cube.select(data, extent = [29,35.2,-2,4.295])
    print(area_sel)
    return data
