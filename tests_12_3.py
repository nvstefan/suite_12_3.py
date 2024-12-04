import unittest
from unittest import TestCase

def skip_if_frozen(method):
    def wrapper(self):
        if self.is_frozen == True:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            method(self)
    return wrapper

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
            self.distance += self.speed

    def __str__(self):
        return self.name

class RunnerTest(TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        walk = Runner('walk')
        for i in range(10):
            walk.walk()
        self.assertEqual(walk.distance, 50)

    @skip_if_frozen
    def test_run(self):
        run = Runner('run')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        run = Runner('run')
        walk = Runner('walk')
        for i in range(10):
            run.run()
            walk.walk()
        self.assertNotEqual(run.distance, walk.distance)

class Tournament:

    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)


    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            finishers = list(result.values())
            finisher_names = {i + 1: str(finisher) for i, finisher in enumerate(finishers)}
            print(finisher_names)

    @skip_if_frozen
    def test_1(self):
        tournament = Tournament(90, self.usain, self.nik)
        result = tournament.start()
        self.all_results[1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @skip_if_frozen
    def test_2(self):
        tournament = Tournament(90, self.andrey, self.nik)
        result = tournament.start()
        self.all_results[2] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @skip_if_frozen
    def test_3(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        result = tournament.start()
        self.all_results[3] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

if __name__ == '__main__':
    unittest.main()
