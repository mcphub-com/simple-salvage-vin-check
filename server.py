import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/nadkabbani/api/simple-salvage-vin-check'

mcp = FastMCP('simple-salvage-vin-check')

@mcp.tool()
def salvagecheck(vin: Annotated[str, Field(description='')]) -> dict: 
    '''Returns true if the VIN was in a salvage database in the past. False otherwise. Must be a valid 17 digit vin from North America.'''
    url = 'https://simple-salvage-vin-check.p.rapidapi.com/'
    headers = {'Referer': 'rapidAPI', 'User-Agent': 'rapidAPI', 'x-rapidapi-host': 'simple-salvage-vin-check.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'vin': vin,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def vindecoder(DecodeVIN: Annotated[str, Field(description='')]) -> dict: 
    '''Provides a VIN decoder for all US standard VINS'''
    url = 'https://simple-salvage-vin-check.p.rapidapi.com/'
    headers = {'Referer': 'rapidAPI', 'User-Agent': 'rapidAPI', 'x-rapidapi-host': 'simple-salvage-vin-check.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'DecodeVIN': DecodeVIN,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
