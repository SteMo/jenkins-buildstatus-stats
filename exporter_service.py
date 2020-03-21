from __future__ import print_function

from time_interval import TimeInterval
from datetime import datetime
import csv
import sys


def create_export_format(jobname, fail_time_list):
    # Über Datenmodell Gedanken machen: fail time list, sollte das eine Klasse sein mit Jobnamen etc?
    return fail_time_list

def export_to_csv(export_data, filename):
    with open(filename, 'w', newline='') as csvfile:        
        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        entry_row_list = []
        for interval in export_data:
            entry_row_list.append(interval.get_start() + "-" + interval.get_end())

        writer.writerow(entry_row_list)
