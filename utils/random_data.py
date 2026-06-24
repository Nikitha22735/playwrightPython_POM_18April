import random
import string
from faker import Faker

fake = Faker()


class RandomDataGenerator:
    """Utility class to generate random test data"""

    @staticmethod
    def random_string(length=10):
        """Generate a random string of specified length"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def random_number(min_val=1, max_val=1000):
        """Generate a random number between min and max"""
        return random.randint(min_val, max_val)

    @staticmethod
    def random_email():
        """Generate a random email"""
        return fake.email()

    @staticmethod
    def random_name():
        """Generate a random full name"""
        return fake.name()

    @staticmethod
    def random_first_name():
        """Generate a random first name"""
        return fake.first_name()

    @staticmethod
    def random_last_name():
        """Generate a random last name"""
        return fake.last_name()

    @staticmethod
    def random_phone():
        """Generate a random phone number"""
        return fake.phone_number()

    @staticmethod
    def random_address():
        """Generate a random address"""
        return fake.address()

    @staticmethod
    def random_city():
        """Generate a random city"""
        return fake.city()

    @staticmethod
    def random_country():
        """Generate a random country"""
        return fake.country()

    @staticmethod
    def random_date(start_date=None, end_date=None):
        """Generate a random date between start_date and end_date"""
        return fake.date_between(start_date=start_date, end_date=end_date)

    @staticmethod
    def random_text(max_chars=100):
        """Generate random text of specified length"""
        return fake.text(max_nb_chars=max_chars)

    @staticmethod
    def random_password(length=12):
        """Generate a random password"""
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(characters, k=length))

    @staticmethod
    def random_username():
        """Generate a random username"""
        return fake.user_name()

    @staticmethod
    def random_product():
        """Generate random product data"""
        return {
            "title": fake.word(),
            "price": round(random.uniform(10, 500), 2),
            "description": fake.text(max_nb_chars=100),
            "category": random.choice(["electronics", "clothing", "books", "home", "sports"])
        }

    @staticmethod
    def random_user():
        """Generate random user data"""
        return {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": fake.address(),
            "username": fake.user_name(),
            "password": RandomDataGenerator.random_password()
        }
