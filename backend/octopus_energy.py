"""
File that has helper functions
"""

import requests

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
  

# Test functions

if __name__ == "__main__":
  energy_products = get_energy_products()

     