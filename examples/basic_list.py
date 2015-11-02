#!/usr/bin/env python

'''Basic app to list Vultr account & server information'''

import logging
from os import environ
from json import dumps
from vultr import Vultr, VultrError

# Looks for an environment variable named "VULTR_KEY"
API_KEY = environ.get('VULTR_KEY')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s [%(funcName)s():%(lineno)d] %(message)s'
)
logging.getLogger("requests").setLevel(logging.WARNING)


def dump_info():
    '''Shows various details about the account & servers'''
    vultr = Vultr(API_KEY)

    try:
        logging.info('Listing account info:\n%s', dumps(
            vultr.account.info(), indent=2
        ))

        logging.info('Listing apps:\n%s', dumps(
            vultr.app.list(), indent=2
        ))

        logging.info('Listing backups:\n%s', dumps(
            vultr.backup.list(), indent=2
        ))

        logging.info('Listing DNS:\n%s', dumps(
            vultr.dns.list(), indent=2
        ))

        logging.info('Listing ISOs:\n%s', dumps(
            vultr.iso.list(), indent=2
        ))

        logging.info('Listing OSs:\n%s', dumps(
            vultr.os.list(), indent=2
        ))

        logging.info('Listing plans:\n%s', dumps(
            vultr.plans.list(), indent=2
        ))

        logging.info('Listing regions:\n%s', dumps(
            vultr.regions.list(), indent=2
        ))

        logging.info('Listing servers:\n%s', dumps(
            vultr.server.list(), indent=2
        ))

        logging.info('Listing snapshots:\n%s', dumps(
            vultr.snapshot.list(), indent=2
        ))

        logging.info('Listing SSH keys:\n%s', dumps(
            vultr.sshkey.list(), indent=2
        ))

        logging.info('Listing startup scripts:\n%s', dumps(
            vultr.startupscript.list(), indent=2
        ))
    except VultrError as ex:
        logging.error('VultrError: %s', ex)


def main():
    '''Entry point'''
    logging.info('Vultr API Client Python Library')
    logging.info('URL: https://www.vultr.com/api/')
    dump_info()

main()
