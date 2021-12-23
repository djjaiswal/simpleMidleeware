import requests
import traceback
from tabulate import tabulate


base_url = "https://api.stackexchange.com/2.3/search/advanced?"
endpoint = base_url + "order=desc&sort=activity&q={}&answers=7&tagged=python&site=stackoverflow"



def search_stack(error):
    url = endpoint.format(error)
    response = requests.get(url)
    result = response.json()['items']
    print(f"\n {error}. Below are some stackoverflow questions that can help.")
    items = []
    for res in result:
        items.append([res['title'], res['link']])
    table = tabulate(items, headers=['Title', 'Link'], tablefmt='orgtbl')
    return table


def handleError(ex):
    res = traceback.format_exception_only(type(ex), ex)[-1].strip()
    error = str(res).split(":")[0]
    tab = search_stack(error)
    print(tab)