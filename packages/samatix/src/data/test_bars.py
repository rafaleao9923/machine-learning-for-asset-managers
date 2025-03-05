import logging
import unittest

from src.testing.fixtures import BaseTestCase, TickFactory
from src.data import bars


class TickBarTestCase(BaseTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ticks_factory = TickFactory(
            tick_number=100,
            store_ticks=True
        )

    def test_tick_bar_data(self):

        expected_ticks = []
        count = 1
        for tick in self.ticks_factory.ticks:
            if count % 10 == 0:
                expected_ticks.append(tick)
            count += 1

        self.assertEqual(
            expected_ticks,
            list(
                bars.TickBarFn(threshold=10).process(
                    self.ticks_factory.ticks
                )
            )
        )


class VolumeBarTestCase(BaseTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ticks_factory = TickFactory(
            tick_number=2,
            store_ticks=True
        )

    def test_volume_bar_data(self):
        expected_ticks = []
        volume_threshold = 100000
        volume = 0
        for tick in self.ticks_factory.ticks:
            volume += tick.price * tick.quantity
            if volume >= volume_threshold:
                expected_ticks.append(tick)
                volume = 0
        logging.info(f"Volume threshold = {volume_threshold}")
        logging.info(expected_ticks)

        self.assertEqual(
            expected_ticks,
            list(bars.VolumeBarFn(threshold=volume_threshold).process(
                self.ticks_factory.ticks
            ))
        )

    def test_sample_volume_bar_data(self):
        self.assertEqual(
            [self.TICK_DATA_PARSED[1], self.TICK_DATA_PARSED[3],
             self.TICK_DATA_PARSED[4], self.TICK_DATA_PARSED[6]],
            list(
                bars.VolumeBarFn(threshold=100000).process(
                    self.TICK_DATA_PARSED
                )
            )
        )


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    unittest.main()
