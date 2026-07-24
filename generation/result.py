from dataclasses import dataclass, field

@dataclass
class GenerationResult:
    carved_paths: list
    maze: dict
    stats: dict = field(default_factory=dict)