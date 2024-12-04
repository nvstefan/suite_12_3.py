# Домашнее задание по теме
# "Систематизация и пропуск тестов".

# Задача "Заморозка кейсов":

import unittest
from unittest import TestCase
import tests_12_3


suiteTS = unittest.TestSuite()
suiteTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
suiteTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suiteTS)

