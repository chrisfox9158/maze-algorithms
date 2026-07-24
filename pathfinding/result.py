from dataclasses import dataclass, field

@dataclass
class AlgorithmResult:
    exploration: list
    solution: list
    stats: dict = field(default_factory=dict)