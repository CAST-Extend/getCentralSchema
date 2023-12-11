import json
from argparse import ArgumentParser
import requests

def get_central_schema(console_url, console_api_key, guid):
    url=f"{console_url}api/aic/applications/{guid}"
    headers = {
        "x-api-key": console_api_key
    }

    try:
        #fetching the app schemas.
        rsp = requests.get(url, headers=headers)
        # print(rsp.status_code)
        if rsp.status_code == 200:
            data = json.loads(rsp.text) 

            for i in range(len(data["schemas"])):
                if data["schemas"][i]["type"] == 'central':
                    return data["schemas"][i]["name"]

        else:
            print("Some error has occured! ")
            print(rsp.text)

    except Exception as e:
        print('some exception has occured! \n Please resolve them or contact developers')
        print(e)

if __name__ == "__main__":

    parser = ArgumentParser()
 
    parser.add_argument('-console_url', '--console_url', required=True, help='AIP Console URL')
    parser.add_argument('-console_api_key', '--console_api_key', required=True, help='AIP Console API KEY')
    parser.add_argument('-ApplicationGUID', '--ApplicationGUID', required=True, help='AIP Console ApplicationGUID')

    args=parser.parse_args()

    if not args.console_url.endswith('/'):
        args.console_url = args.console_url + '/'

    print(f'Getting the central schema name for the ApplicationGUID-> {args.ApplicationGUID}.............')

    central_schema = get_central_schema(args.console_url, args.console_api_key, args.ApplicationGUID)

 
    name = 'ApplicationCentralSchema'    
    # set variable
    print(f'##vso[task.setvariable variable={name};]{central_schema}')
