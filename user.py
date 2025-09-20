class User:
    """
    Class representing users. Each unique user is its own object.
    """

    def __init__(self, username: str, name: str, id: int):
        """
        User object init.
        Parameters:
            username: str; username of user
            name: str; real name of user
            id: int; unique id of user
        Returns:
            Initializes User object.
        """
        self.username = username
        self.name = name
        self.id = id
