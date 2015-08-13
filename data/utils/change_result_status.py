"""Changes all debates in a round to STATUS_NONE."""

import header
from draws.models import Debate

import csv

import argparse
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("round", type=int, help="Round to change")
args = parser.parse_args()
round = args.round

for debate in Debate.objects.filter(round__seq=round):
    print debate
    debate.result_status = Debate.STATUS_NONE
    debate.save()