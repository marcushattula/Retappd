from brewery import Brewery

class Beer:
    """
    Class representing beers. Each unique beer is its own object.
    """

    def __init__(self, name: str, category: str, style: str, brewer: Brewery, abv: float, ibu: float, collaborators: list[Brewery]=None):
        """
        Beer object init.
        Parameters:
            name: str; name of beer.
            category: str; beer category (lager, IPA, etc.).
            style: str; modifier to category (e.g. 'Pale' for Lager).
            brewer: Brewery: Brewery responsible for this beer.
            abv: float; beer alcohol (in percent).
            ibu: float: beer bitterness in International Bitterness Units scale (IBU).
            (Optional) collaborators: list[Brewery]; Other breweries who collaborated on this beer. Default = None.
        Returns:
            Initializes Beer object.
        """
        self.name = name
        self.category = category
        self.style = style
        self.brewer = brewer
        self.abv = abv
        self.ibu = ibu
        self.collaborators = collaborators

        self.check_ins = []
