
from __future__ import annotations
import json
from typing import Any

import requests

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

    def __getitem__(self, key: str) -> Any:
        """
        Used for returning items from pokemon instance

        Args:
            key (str): The key of item to return

        Returns:
            Any: Value of item
        """
        return self._pokemon[key]

class PokemonAPI:

    def __init__(self, base_url: str = "https://pokeapi.co/api/v2") -> None:
        self.base_url = base_url

    @staticmethod
    def _process_request(url: str) -> dict[Any, Any]:
        req = requests.get(url)
        if req.status_code == 200:
            return req.json()
        raise requests.RequestException(f"Response error code {req.status_code}")

    def get_pokemon(self, id: int) -> dict[Any, Any]:
        res = self._process_request(f"{self.base_url}/pokemon/{id}")
        return Pokemon(res)

if __name__ == "__main__":
    pokemon = PokemonAPI()
    data = pokemon.get_pokemon(7)
    print(data["name"])
