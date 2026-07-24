# Library imports
from datetime import datetime
from pathlib import Path

# Local imports
from algorithms import ALGORITHMS
from generation import GENERATORS
from outputs.visualizer import Visualizer

class SingleRun:
    """Run a single episode for a given generator and algorithm."""
    def run(self):
        generator_choice = input(f"Generator ({' / '.join(GENERATORS)}): ")
        generator = GENERATORS[generator_choice]()
        maze = generator.generate_maze()

        algorithm_choice = input(f"Algorithm ({' / '.join(ALGORITHMS)}): ")
        algorithm = ALGORITHMS[algorithm_choice]()
        results = algorithm.run(maze)

        self.visualize(maze, results)
        return results

    def visualize(self, maze, results):
        visualization = Visualizer(maze, results)
        visualization.run()

class MultiRun():
    """Run multiple episodes for a given generator and algorithm."""
    def run(self, episode_count):
        generator_choice = input(f"Generator ({' / '.join(GENERATORS)}): ")
        algorithm_choice = input(f"Algorithm ({' / '.join(ALGORITHMS)}): ")
        results = []

        for episode in range(episode_count):
            generator = GENERATORS[generator_choice]()
            maze = generator.generate_maze()

            algorithm = ALGORITHMS[algorithm_choice]()
            results.append(algorithm.run(maze))

        return results

if __name__ == "__main__":
    episodes = int(input(f"Episode count: "))
    if episodes == 1:
        instance = SingleRun()
        instance.run()
        print("Simulation complete!")
    else:
        instance = MultiRun()
        instance.run(episodes)
        print("Simulation complete!")