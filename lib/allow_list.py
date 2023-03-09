def is_allowed_url(test):
    allow_list = ['https://cmr.earthdata.nasa.gov/',
                  'https://cmr.uat.earthdata.nasa.gov/']
    allowed = []

    for url in allow_list:
        allowed.append(url in test)

    return any(allowed)
