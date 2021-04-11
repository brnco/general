'''
does some operations to files on my hard drive based on airtable data
primarily using it to clean up my own ancient music library
'''

from pprint import pprint
from airtable import Airtable
import configparser
import os

def iterate_records(to_delete_files, kwargs):
    '''
    goes through each airtable record and coordinates operations
    '''
    to_del = []
    for f in to_delete_files:
        to_del.append(f.strip())
    pprint(len(to_del))

def get_Airtable_data(config, kwargs):
    '''
    gets Airtable data, returns a list of records
    '''
    pprint("getting Airtable data...")
    bearer = config.get('airtable login','bearer')
    api_key = config.get('airtable login','api_key')
    kwargs['at'] = Airtable(bearer,'tunes',api_key=api_key)
    kwargs['tunes'] = kwargs['at'].get_all(view='Everything')
    return kwargs

def read_tunes_delete():
    '''
    reads text file of full paths to delete
    '''
    with open("tunes_delete.txt","r") as f:
        to_delete = f.readlines()
    return to_delete

def init():
    '''
    initializes arguments and variables, gets config
    '''
    config = configparser.ConfigParser()
    #config.optionxform = str
    config.read("config.ini")
    kwargs = {}
    return config, kwargs

def main():
    '''
    do the thing
    '''
    config, kwargs = init()
    pprint(config['airtable login']['bearer'])
    #kwargs = get_Airtable_data(config, kwargs)
    files = read_tunes_delete()
    iterate_records(files, kwargs)

if __name__ == "__main__":
    main()
