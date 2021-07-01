"""
Name: Thy Nguyen
Project: Customized Posters Ordering System
"""


from data_structures import Stack, Queue
from customize_poster import ImageGrid, ImageProcessing, \
    ImageReader, ImageClassification
from datetime import datetime


#######################################################################
#                               POSTER                                #
#######################################################################
class Poster:
    """
    Abstraction for all poster types in the system.
    Standard posters can be ordered many times, but Special posters
    are limited.
    """
    num_posters = 0

    def __init__(self, title, price, process):
        """
        A constructor to initialize instance variables.
        Input: title (str) is Poster title;
        price (double) is Poster price,
        process (bool) True if users customize the poster
        id (int) is auto-increment poster id
        """
        self.title = title
        self.price = price
        self.process = process
        self.id = Poster.num_posters
        Poster.num_posters += 1

    def __str__(self):
        """ String representation of poster """
        poster = ""
        if self.process:
            poster += "[Customized]"
        return poster + "'{}' <{}> {}$".format(self.title, self.id, self.price)

    def __repr__(self):
        """ Poster repr representation """
        return "Poster <{}>".format(self.title)


class FreePoster(Poster):
    """ A class that represents products having limited offerings """

    def __init__(self, title):
        """
        A constructor to initialize instance variables
        Input: title (str) initialized by super constructor;
        """
        super().__init__(title, 0, False)
        min_posters = 150
        multi_extra = 10 # 150 posters ==> 10 extra; 300 posters ==> 20 extra
        min_extra = 5
        self.amount = multi_extra * (Poster.num_posters / min_posters) \
            if Poster.num_posters > min_posters else min_extra
        self.amount = 0 if Poster.num_posters < min_extra else self.amount

    def __str__(self):
        """ String representation of free posters """
        return "{} free posters awarded".format(self.amount)


class SpecialPoster(Poster):
    """ Special Posters for Premium Users only """

    def __init__(self, title, price, process, description="Special"):
        """ A constructor to initialize instance variables
         Input: title, price, process are initialized by super constructor;
         default description (str) is 'Special' """
        super().__init__(title, price, process)
        self.description = description

    def __str__(self):
        """ A string representation of special poster """
        poster_type = '[Customized]' if self.process else '[Pre-styled]'
        return "{} '{}' ({}) <{}> {}".format(
            poster_type, self.title, self.id, self.price, self.description)


#######################################################################
#                      PURCHASE HISTORY                               #
#######################################################################
class PurchaseHistory:
    """ A class that provides abstraction to the purchase history. """
    num_history = 0

    def __init__(self, poster, user):
        """ A constructor to initialize instance variables
        Instance Variables: poster (Poster) being purchased by user;
        user (User) who will order poster; id (int) is an auto-increment ID
        of history; time (datetime) is time of history instance
        """
        self.poster = poster
        self.user = user
        self.id = PurchaseHistory.num_history
        PurchaseHistory.num_history += 1
        self.time = datetime.now()

    def __str__(self):
        """ String representation of purchase history """
        return "User: {} ==== Record #{} === ordered {} at {}".\
            format(self.user.name, self.id, self.poster, self.time)

    def __repr__(self):
        """ Repr String representation """
        return "Record #{} of User <{}> at {}".format(
            self.id, self.user.name, self.time)


#######################################################################
#                                USER                                 #
#######################################################################
class User:
    """ A class that provides abstraction to the users.
    The User instance is similar to a membership card. Each User
    instance can only register with 1 store. Initializing Users under
    this class will create "ordinary" users.
    """
    user_id = 0

    def __init__(self, name, email, address, balance, store):
        """ A constructor to initialize instance variables
        Instance Variables: name, email, address (str) are User info;
        store (Store) is where user orders posters;
        balance (double) is the user's money in their bank account;
        id (int) is an auto-increment ID of user;
        shopping_record (Stack) keeps the user's purchase histories;
        basket (Queue) keeps records of posters user plans to purchase
        """
        self.name = name
        self.email = email
        self.address = address
        self.balance = balance
        self.id = User.user_id
        User.user_id += 1
        self.shopping_record = Stack()
        self.basket = Queue()
        self.store = store
