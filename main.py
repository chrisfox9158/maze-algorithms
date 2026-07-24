# Library imports
from datetime import datetime
from pathlib import Path

# Local imports
from algorithms import ALGORITHMS
from generation import GENERATORS
from outputs.visualizer import Visualizer

class SingleRun:
    def run(self):
        generator_choice = input(f"Generator ({' / '.join(GENERATORS)}): ")
        generator = GENERATORS[generator_choice]()
        maze = generator.generate_maze()

        algorithm_choice = input(f"Algorithm ({' / '.join(ALGORITHMS)}): ")
        algorithm = ALGORITHMS[algorithm_choice]()
        results = algorithm.run(maze)

        self.visualize(maze, results)

    def visualize(self, maze, results):
        visualization = Visualizer(maze, results)
        visualization.run()

if int(input(f"Episode count: ")) == 1:
    instance = SingleRun()
    instance.run()