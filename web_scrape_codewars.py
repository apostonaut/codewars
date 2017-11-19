from bs4 import BeautifulSoup
import requests

class Leaderboard:
  """
  Stores User objects representing users on the Codewars leaderboard.
  """

  def __init__(self, position):
    """
    :param position: list of User objects
    """
    self.position = position

  def add_user(self, user):
    """
    Adds a User to the Leaderboard.
    :param user:
    :return: None
    """
    self.position.append(user)



class User:
  """
  Stores information about a user on the Codewars leaderboard.
  """
  def __init__(self, name, clan, honor):
    """

    :param name: The user's username (str)
    :param clan: The user's clan (str) or None
    :param honor: The user's honour points (int)
    """
    self.name = name
    self.clan = clan
    self.honor = honor


Url = 'https://www.codewars.com/users/leaderboard'

request = requests.get(Url)

data = request.text

soup = BeautifulSoup(data, 'html.parser')

# first tr tag is table header, so 1-500 are the user rows
users_tr = soup.find_all('tr')[1:]
users_td = soup.find_all('td')[1:]

leaderboard = Leaderboard([])
for user in users_tr:
  # extract username, clan, honour of user
  # order of td tags: rank, user(kyu, profile pic, username), clan, honor
  td_tags = user.find_all('td')
  username = td_tags[1].get_text()[5:]

  clan = td_tags[2].get_text()

  honor = td_tags[3].get_text()

  # initialize User object using extracted data
  user_object = User(username, clan, honor)

  # add User object to Leaderboard object
  leaderboard.add_user(user_object)

print(leaderboard.position)