import dataclasses


@dataclasses.dataclass
class User:
    name: str
    lastname: str
    email: str
    gender: str
    number: str
    subject: str
    birthday_day: str
    birthday_year: int
    birthday_month: str
    hobbies: str
    photo: str
    address: str
    state: str
    city: str


marina = User(name='Kam', lastname='Mar', email='m81321184@gmail.com', gender='Female',
              number='1234567890', subject='Computer Science',
              birthday_day='02', birthday_year=2000, birthday_month='April',
              hobbies='Sports', photo='img.png.png', address='ЦАО', state='Rajasthan', city='Jaiselmer')
