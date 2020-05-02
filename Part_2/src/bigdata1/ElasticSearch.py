from datetime import datetime
from elasticsearch import Elasticsearch
import json


def create_and_update_index(index_name):
	es = Elasticsearch()
	try:
		es.indices.create(index=index_name)
	except Exception:
		pass

	# es.indices.put_mapping(
 #        index=index_name,
 #        doc_type=doc_type,
 #        body={
 #            doc_type: {
 #                "properties": {
 #                    "issue_date_time": {"type": "date"}, 
 #                    #"issue_date": {"type": "text"},
 #                    "fine_amount" : {"type": "float"},
 #                    "penalty_amount" : {"type": "float"},
 #                    "interest_amount" : {"type": "float"},
 #                    "reduction_amount" : {"type": "float"},
 #                    "payment_amount" : {"type": "float"},
 #                    "amount_due" : {"type": "float"}
                
 #                }
 #            }
 #        }
 #    )

	return es

def transform_data(data_item):
	for key, value in data_item.items():
		#all amounts convert to float
		if key in ['fine_amount', 'penalty_amount', 'interest_amount', 'reduction_amount', 'payment_amount', 'amount_due']:
			data_item[key] = float(value)

		# #if date and time both exist, convert them into issue date time
		# elif 'issue_date_time' in key and 'violation_time' in key:
		# 	data_item[key] = datetime.strptime(data_item['issue_date'] + " " + data_item['violation_time'] + "M", '%m/%d/%Y %I:%M%p')
		else:
			pass
		



def load_data(es, index_name, data_item):
	if data_item:
		transform_data(data_item)
		es.index(index=index_name, doc_type="", body=data_item, id=data_item['summons_number'])
