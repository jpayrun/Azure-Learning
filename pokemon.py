"""
A module for working with data from the pokemon api
"""
from __future__ import annotations
from enum import Enum
import json
from typing import Any, Literal

import requests


class PokemonImage:

    def __init__(self, image: str) -> None:
        self.image = image

    @property
    def front_default(self) -> str:
        return self.image['front_default']

class PokemonStats:

    StatsList = Literal["hp", "attack", "defense", "special-attack", "special-defense", "speed"]
    StatsDict = {"hp": 0, "attack": 1, "defense": 2, "special-attack": 3, "special-defense": 4, "speed": 5}

    def __init__(self, stats: str) -> None:
        self.stats = stats
    
    def get_stats_value(self, key: StatsList) -> int:
        return int(self.stats[self.StatsDict[key]]['base_stat'])

    @property
    def hp(self) -> int:
        return self.get_stats_value('hp')
    
    @property
    def attack(self) -> int:
        return self.get_stats_value('attack')
    
    @property
    def defense(self) -> int:
        return self.get_stats_value('defense')
    
    @property
    def speical_attack(self) -> int:
        return self.get_stats_value("special-attack")
    
    @property
    def speical_defense(self) -> int:
        return self.get_stats_value("special-defense")

    @property
    def speed(self) -> int:
        return self.get_stats_value('speed')


class Pokemon:
    """
    Class for working with pokemon data
    """

    def __init__(self, pokemon: Pokemon) -> None:
        """
        Constructor

        Args:
            pokemon (Pokemon): A pokemon instance returned from api
        """
        self._pokemon = pokemon
    
    @property
    def name(self) -> str:
        """
        Name of the pokemeon

        Returns:
            str: Pokemon name
        """
        return self._pokemon['name']
    
    @property
    def sprites(self) -> PokemonImage:
        return PokemonImage(self._pokemon['sprites'])

    @property
    def stats(self) -> PokemonStats:
        return PokemonStats(self._pokemon['stats'])

    @property
    def hp(self) -> int:
        return self.stats.hp
    
    @property
    def attack(self) -> int:
        return self.stats.attack
    
    @property
    def defense(self) -> int:
        return self.stats.defense
    
    @property
    def special_attack(self) -> int:
        return self.stats.speical_attack

    @property
    def speical_defense(self) -> int:
        return self.stats.speical_defense

    @property
    def speed(self) -> int:
        return self.stats.speed
       
    @property
    def images(self) -> str:
        return self.sprites.front_default
    
    def pokemon_stats(self) -> dict[str, int]:
        return {
            'hp': self.hp,
            'attack': self.attack,
            'defense': self.defense,
            'special-attack': self.special_attack,
            'special-defense': self.speical_defense,
            'speed': self.speed
        }

    # def __getitem__(self, key: str) -> Any:
    #     """
    #     Used for returning items from pokemon instance

    #     Args:
    #         key (str): The key of item to return

    #     Returns:
    #         Any: Value of item
    #     """
    #     return self._pokemon[key]


class PokemonAPI:
    """
    The opperations available from the pokemon api
    """
    def __init__(self, base_url: str = "https://pokeapi.co/api/v2") -> None:
        self.base_url = base_url

    @staticmethod
    def _process_request(url: str) -> dict[Any, Any]:
        """
        Process the url request and return result if valid

        Args:
            url (str): The url string to pull from

        Raises:
            requests.RequestException: Issue with the reques

        Returns:
            dict[Any, Any]: The result dictionary
        """
        req = requests.get(url)
        if req.status_code == 200:
            return req.json()
        raise requests.RequestException(f"Response error code {req.status_code}")

    def get_pokemon(self, id: int) -> Pokemon:
        """
        Get a pokemon by id

        Args:
            id (int): The id of the pokemon to get

        Returns:
            Pokemon: The data for the pokemon
        """
        # try:
        res = self._process_request(f"{self.base_url}/pokemon/{id}")
        # except requests.RequestException:
        #     raise 
        return Pokemon(res)


if __name__ == "__main__":
    pokemon = PokemonAPI()
    data = pokemon.get_pokemon(7)
    print(data.name)
    print(data.hp)
    print(data.images)
    print(data.pokemon_stats())
