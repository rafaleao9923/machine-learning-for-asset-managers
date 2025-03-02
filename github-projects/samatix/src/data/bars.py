import numpy as np
import pandas as pd

from src.runner import pipeline


class TickBarFn(pipeline.DoFn):
    """
    Parse the tick objects into Tick Bars
    """

    def __init__(self, threshold=10):
        """
        Tick Bar Function
        :param threshold: The number of ticks at which we extract the bid ask
        :type threshold: int
        """
        self.ticks_processed = 0
        self.buffer = 0
        self.threshold = threshold

    def process(self, elements):
        for e in elements:
            self.buffer += 1
            self.ticks_processed += 1
            if self.buffer == self.threshold:
                self.buffer = 0
                yield e


class VolumeBarFn(pipeline.DoFn):
    """
    Parse the tick objects into volume bars
    """

    def __init__(self, threshold=10000):
        """
        Volume Bar Function
        :param threshold: The accumulated volume threshold at which we extract
        the bid ask
        :type threshold: float
        """
        self.ticks_processed = 0
        self.buffer = 0
        self.threshold = threshold

    def process(self, elements):
        for e in elements:
            self.buffer += e.quantity * e.price
            self.ticks_processed += 1
            if self.buffer >= self.threshold:
                self.buffer = 0
                yield e
