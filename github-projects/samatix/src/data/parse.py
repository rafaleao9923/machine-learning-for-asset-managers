import datetime as dt
import csv
import logging

from src.data.models import Tick
from src.runner import pipeline


class ParseTickDataFn(pipeline.DoFn):
    """
    Parse the raw tick data events into a tick object
    """

    def __init__(self):
        self.ticks_counter = 0
        self.errors_parse_num = 0

    def process(self, elements):
        for e in elements:
            try:
                row = list(csv.reader([e]))[0]
                self.ticks_counter += 1
                yield Tick(
                    time=dt.datetime.strptime(
                        f"{row[0]},{row[1]}",
                        '%m/%d/%Y,%H:%M:%S'
                    ),
                    price=float(row[2]),
                    bid=float(row[3]),
                    ask=float(row[4]),
                    quantity=float(row[5])
                )
            except:
                self.errors_parse_num += 1
                logging.error(f"Parsing error of element = {e}")
