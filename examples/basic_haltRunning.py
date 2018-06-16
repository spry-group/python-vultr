#!/usr/bin/env python

'''Basic app to halt all running servers'''

import logging
from os import environ
from json import dumps, load
from vultr import Vultr, VultrError

# Looks for an environment variable named "VULTR_KEY"
API_KEY = environ.get('VULTR_KEY')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s [%(funcName)s():%(lineno)d] %(message)s'
)
logging.getLogger("requests").setLevel(logging.WARNING)

def halt_running():
    '''Halts all running servers'''
    vultr = Vultr(API_KEY)

    try:
            serverList = vultr.server.list()
            #logging.info('Listing servers:\n%s', dumps(
            #serverList, indent=2
        #))
    except VultrError as ex:
        logging.error('VultrError: %s', ex)

    for serverID in serverList:
        if serverList[serverID]['power_status'] == 'running':
            logging.info(serverList[serverID]['label'] + " will be gracefully shutdown.")
            vultr.server.halt(serverID)

def main():
    '''Entry point'''
    logging.info('Vultr API Client Python Library')
    logging.info('URL: https://www.vultr.com/api/')
    halt_running()

main()
