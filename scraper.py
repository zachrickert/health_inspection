import requests


DOMAIN = 'http://info.kingcounty.gov/'
PATH = 'health/ehs/foodsafety/inspections/Results/Results.aspx'

PARAMS = {
    'Output': 'W',
    'Business_Name': '',
    'Business_Address': '',
    'Longitude': '',
    'Latitude': '',
    'City': '',
    'Zip_Code': '',
    'Inspection_Type': 'All',
    'Inspection_Start': '',
    'Inspection_End': '',
    'Inspection_Closed_Business': 'A',
    'Violation_Points': '',
    'Violation_Red_Points': '',
    'Violation_Descr': '',
    'Fuzzy_Search': '',
    'Sort': 'B',
}

def get_inspection_page(**kwargs):
    my_dict = PARAMS
    query_list = []
    for key in kwargs:
        if key not in PARAMS:
            raise AttributeError
        my_dict[key] = kwargs[key]

    for key in my_dict:
        query_list.append('{0}={1}'.format(key, my_dict[key]))

    query = '&'.join(query_list)
    request = requests.get(DOMAIN + PATH, query)
    request.raise_for_status()
    return request.content, request.encoding


if __name__ == '__main__':
    keywords = {'Business_Name': 'Zeeks'}
    get_inspection_page(**keywords)

