from location import Address

class Brewery:
    """
    Class representing breweries. Each unique brewery is its own object.
    """

    def __init__(self, name: str, place: Address, founded: int, owner):
        """
        Brewery object init.
        Parameters:
            name: str; name of brewery.
            place: Address; brewery location (HQ).
            founded: int; year of brewery founding.
            owner: Any; brewery parent company. None if independent/private.
        Returns:
            Initializes Brewery object.
        """
        self.name = name
        self.place = place
        self.founded = founded
        self.owner = owner

        self.beers = []
