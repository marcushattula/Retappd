class Address:
    """
    Class representing addresses. Each unique address is its own object.
    """

    def __init__(self, country: str, region: str, subdivision: str, address: str):
        """
        Address object init.
        Parameters:
            country: str; name of country.
            region: str; name of district, province or other subdivision.
            subdivision: str; name of town or city.
            address: str; street address.
        Returns:
            Initializes Address object.
        """
        self.country = country
        self.district = region
        self.city = subdivision
        self.address = address

class Location:
    """
    Class representing locations or venues. Each location is its own class.
    """

    def __init__(self, name: str, place: Address, categories: list[str]):
        """
        Location object init.
        Parameters:
            name: str; name of location.
            place: Address; address of this location.
            categories: list[str]; categories of this location (e.g. beer garden and karaoke bar).
        Returns:
            Initializes Location object.
        """
        self.name = name
        self.place = place
        self.category = categories
