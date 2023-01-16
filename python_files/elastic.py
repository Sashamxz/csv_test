import asyncio
import csv
import sys
from elasticsearch import helpers, Elasticsearch
# from elasticsearch.helpers import async_bulk
# from elasticsearch import AsyncElasticsearch



# з'єднання з контенером elasticsearch
es = Elasticsearch('http://localhost:9200')    


# отримуємо список словників для запису в бд
def get_customers():
    list_ = []
    with open('test.csv', 'r', encoding='UTF-8') as file_csv:
        text = csv.DictReader(file_csv, restkey= None, restval=None)
        for row in text:
            list_.append(row) 
    return list_


customers = get_customers()


# записуємо данні через helper.bulk
try:
    res =  helpers.bulk(es, customers, index='customer')
    print(res)
except Exception as err:
    msg = "Elasticsearch helpers.bulk() ERROR: " + str(err)
    print(msg)
    sys.exit(1)



# асинхронний запис 
# async def gendata():

#     for customer in customers:
#         yield {
#             "_index": "customer",
#             "doc": {"customer": customer},
#         }

# async def main():
#     await async_bulk(es, gendata())


# if __name__ == '__main__':
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     try:
#         loop.run_until_complete(main())
#     except KeyboardInterrupt:
#         pass


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

