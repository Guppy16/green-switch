"""
File that has helper functions
"""

import requests
import pandas as pd
import time

# Function to return a list of energy products
def get_energy_products(**kwargs):
  """Return list of energy products
  kwargs: params to be used in url
  Return: list of energy product codes
  """
  url = "https://api.octopus.energy/v1/products/?"

  default_url_params = {
    "is_variable": "true",
    "is_business": "false",
    "is_green": "true"
  }

  default_url_params.update(kwargs)

  for k,v in default_url_params.items():
    url += f"{k}=v&"
  
  print("Requesting energy products:")
  print(f"GET: {url}")

  res = requests.get(url)
  res = res.json()

  energy_product_codes = [tariff['code'] for tariff in res['results']] 
  print(f"Found  {len(energy_product_codes)}/{res['count']} energy products")

  return energy_product_codes

def get_today():
    current_year = time.strftime("%Y")
    current_month = time.strftime("%m")
    current_day = time.strftime("%d")
    return get_csv(current_year, current_month, current_day)


def get_csv(year, month, day, year_end, month_end, day_end):
    url = ('https://api.octopus.energy/v1/products/VAR-19-04-12/gas-tariffs/G-1R-VAR-19-04-12-A/standard-unit-rates/?period_from=' + str(year) + '-' + str(month) + '-' + str(day) + 'T00:00Z&period_to=' + str(year_end) + '-' + str(month_end) + '-' + str(day_end) + 'T23:59Z&page_size=2500')

    r = requests.get(url)
    output_dict = r.json()
    print(output_dict)

    # Only results
    #output_dict = output_dict['results'] # Uncomment if only wanting results list

    # save output_dict to csv
    df = pd.DataFrame(output_dict)

    # if dataframe is not empty
    if df.empty == False:
        df.to_csv(str(year) + '-' + str(month) + '-' + str(day) + 'gas.csv')
        
    return output_dict

  

# Test functions

if __name__ == "__main__":
  energy_products = get_energy_products()

     
