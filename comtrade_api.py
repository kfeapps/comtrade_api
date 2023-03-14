import pandas as pd
import requests
import pandas as pd
import requests

def fetch_comtrade_data(type_code, freq_code, cl_code, reporter_code=None, period=None, partner_code=None, partner2_code=None, cmd_code=None, flow_code=None, customs_code=None, mot_code=None):
    base_url = 'https://comtradeapi.un.org/public/v1/preview'
    endpoint_url = f"{base_url}/{type_code}/{freq_code}/{cl_code}"
    if reporter_code:
        endpoint_url += f"?reporterCode={reporter_code}"
    if period:
        endpoint_url += f"&period={period}"
    if partner_code:
        endpoint_url += f"&partnerCode={partner_code}"
    if partner2_code:
        endpoint_url += f"&partner2Code={partner2_code}"
    if cmd_code:
        endpoint_url += f"&cmdCode={cmd_code}"
    if flow_code:
        endpoint_url += f"&flowCode={flow_code}"
    if customs_code:
        endpoint_url += f"&customsCode={customs_code}"
    if mot_code:
        endpoint_url += f"&motCode={mot_code}"
    response = requests.get(endpoint_url)
    data = response.json()['data']
    return endpoint_url, pd.json_normalize(data)



url, df = fetch_comtrade_data(type_code='C',
                         freq_code='A',
                         cl_code='HS',
                         reporter_code='156',
                         partner_code= '24',
                         partner2_code = '0',
                         period='2021,2020',
                         flow_code='M,X',
                         mot_code="0",
                         customs_code="C00",
                         cmd_code="TOTAL")

