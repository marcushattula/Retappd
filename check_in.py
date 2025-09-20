from datetime import date, time

from beer import Beer
from user import User
from location import Location

class Check_In:
    """
    Class representing check-ins. Each unique check-in is its own object.
    """

    def __init__(self, user: User, beer: Beer, rating: float, profile: list[str], location: Location, tags: list[User], checkin_date: date, checkin_time: time):
        """
        Check_In object init.
        Parameters:
            user: User; check-in creator.
            beer: Beer; checked in beer.
            rating: float; rating given to beer. None if unrated.
            profile: list[str]; profile tags given to beer as array.
            location: Location; where the check-in was created.
            tags: list[User]; users who were tagged in this check in.
            checkin_date: date; date when check-in was created.
            checkin_time: time; time when check-in was created
        Returns:
            Initializes Check_In object.
        """
        self.user = user
        self.beer = beer
        self.rating = rating
        self.profile = profile
        self.location = location
        self.tags = tags
        self.checkin_date = checkin_date
        self.checkin_time = checkin_time
