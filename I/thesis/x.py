import cdsapi

c = cdsapi.Client()

c.retrieve(
    'seasonal-original-single-levels',
    {
        'format':'grib',
        'originating_centre':'ukmo',
        'year':'2017',
        'month':'08',
        'variable':'total_precipitation',
        'leadtime_hour':[
            '24','48'
        ],
        'day':[
            '06','07'
        ]
    },
    'download.grib')
