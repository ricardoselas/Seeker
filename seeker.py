import random

Class finder:
      """The person looking for the Hider .
    
      The Seeker keeps track of your location and distance traveled.
    
      Attributes:
          location (int): The Seeker's location (1-1000).
          distance (List[int]): The distances traveled.
      """

      def __init__(self):
          """I built a new Searcher.

          Args:
              self (Seeker): An instance of Seeker.
          """
          self._location = random.randint(1, 1000)
        
      def get_location(self):
          """Gets the current location.
        
          Returns:
              number: The current location,
          """
          return self._location
        
      def move_location(self, location):
          """Moves to the specified location.

          Args:
              self (Seeker): An instance of Seeker.
              location (int): The given location.
          """
          self._location = location