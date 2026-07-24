from dataclasses import dataclass, field

@dataclass
class GenerationResult:
    carved_path: list
    maze: dict
    stats: dict = field(default_factory=dict)