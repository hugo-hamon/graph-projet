from dataclasses import dataclass
import json


@dataclass
class Config:
    city_numbers: int = 5
    iterations_numbers: int = 100

    def load_config(self, filepath: str) -> None:
        with open(filepath) as f:
            config = json.load(f)
        self.__dict__.update(config)
