from sodapy import Socrata
from requests import get
import json
import os



def get_results(page_size, num_pages, output):

    client = Socrata('data.cityofnewyork.us', os.environ.get("APP_KEY"))
    dataset_id = 'nc67-uf89'

    for num_page in range(int(num_pages)):
        offset = num_page * page_size
        get_results.data = client.get(dataset_id, limit = page_size, offset = num_pages)
        
        for data in get_results.data:
            print(json.dumps(data, indent = 4))
            json_file = json.dumps(data, indent=4)
            
            with open(output, 'a') as output_file: 
                output_file.write(json_file)


def write_results(output):
    # with open(output, 'a') as output_file: 
    #     output_file.write(json_file)

    #with open(output, 'a') as output_file:
    with open(output, 'w') as output_file:
        #try
            #output_file.write(json_file)
            ##file.write(json.dumps(data, indent=4))
            ##file.write(json.dumpts(results))
        pass