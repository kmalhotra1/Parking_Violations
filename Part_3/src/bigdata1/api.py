import json
import os
from sodapy import Socrata
from requests import get
from time import sleep
from src.bigdata1.ElasticSearch import create_and_update_index, transform_data, load_data




def get_results(output, page_size: int = 1000, num_pages: int = 1):
    
    dataset = 'nc67-uf89'
    datasource = "data.cityofnewyork.us"

    app_key = os.environ.get("APP_KEY")


    if num_pages <= 0:
        print(f"Something went wrong: num_pages must be greater than 0. ")
        return
    if page_size <= 0:
        print(f"Something went wrong: page_size must be greater than 0. ")
        return

    try:
        client = Socrata(datasource, app_key)
        es = create_and_update_index('opcv-index')

        if not num_pages:


            count_response = client.get(dataset, select = 'COUNT(*)')
            count = int(count_response[0].get('COUNT'))


            num_pages = round(count/page_size)
            page = 0

            while page < num_pages:

                if page == 0:
                    results = client.get(dataset, limit = page_size)
                else:
                    results += client.get(dataset, limit = page_size, offset = page * page_size)
                print(f"\n{page} of {num_pages} pages loaded. \n")
                page += 1
                sleep(1)


        else:
            #total number = page_size * num_pages
            limit = page_size * num_pages
            results = client.get(dataset, limit = limit)
            print(f"\n{num_pages} pages loaded. \n")

        #process results: print
        print(json.dumps(results, indent = 4))
        print(results[0])
        #process results: file output
        if output:
            json_file = json.dumps(results, indent = 4)
            with open(output, 'a') as output_file:
                output_file.write(json_file)


        for result in results:
            load_data(es, 'opcv-index', result)

    except Exception as e:
        print(f"Something went wrong: {e}")
        raise



