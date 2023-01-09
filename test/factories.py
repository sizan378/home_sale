import factory
from apps.profiles.models import Profile
from django.db.models.signals import post_save
from django.core.files.base import ContentFile
from faker import Factory as FakerFactory
from home_sale.settings.development import AUTH_USER_MODEL
from apps.enquiries.models import Enquire
from apps.properties.models import Property
from test.factories import UserFactory

faker = FakerFactory.create()

'''A lambda function which handles the object instance as argument
lambda = function
x: = object 
faker.(anything) = This is object instance use as  a argument
'''


@factory.django.mute_signals(post_save)
class UserProfileFactory(factory.django.DjangoModelFactory):
    # user = factory.SubFactory(UserFactory)
    phone_number = factory.LazyAttribute(lambda x: faker.phone_number())
    about_me = factory.LazyAttribute(lambda x: faker.sentence())
    license = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=6))
    profile_photo = factory.LazyAttribute(lambda x: faker.file_extension(category="image"))
    gender = factory.LazyAttribute(lambda x: f"male")
    country = factory.LazyAttribute(lambda x: faker.country_code())
    city = factory.LazyAttribute(lambda x: faker.city())
    is_buyer = False
    is_seller = False
    is_agent = False
    top_agent = False
    rating = factory.LazyAttribute(lambda x: faker.random_int(min=1, max=5))
    num_reviews = factory.LazyAttribute(lambda x: faker.random_int(min=0, max=25))

    class Meta:
        model = Profile


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    username = factory.LazyAttribute(lambda x: faker.first_name())
    email = factory.LazyAttribute(lambda x: f"homesales@gmail.com")
    password = factory.LazyAttribute(lambda x: faker.password())
    is_active = True
    is_staff = False

    class Meta:
        model = AUTH_USER_MODEL

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)


class EnquireFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    phone_number = factory.LazyAttribute(lambda x: f'01234567891')
    email = factory.LazyAttribute(lambda x: f"homesales@gmail.com")
    subject = factory.LazyAttribute(lambda x: faker.words())
    message = factory.LazyAttribute(lambda x: faker.sentence())

    class Meta:
        model = Enquire


class PropertiesFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    title = factory.LazyAttribute(lambda x: faker.sentence())
    slug = factory.LazyAttribute(lambda x: f"django-slug")
    ref_code = factory.LazyAttribute(lambda x: faker.random_int(min=5, max=10))
    description = factory.LazyAttribute(lambda x: faker.sentence())
    country = factory.LazyAttribute(lambda x: faker.country_code())
    city = factory.LazyAttribute(lambda x: faker.city())
    postal_code = factory.LazyAttribute(lambda x: faker.random_int(min=3, max=10))
    street_address = factory.LazyAttribute(lambda x: faker.street_address())
    property_number = factory.LazyAttribute(lambda x: faker.random_number())
    price = factory.LazyAttribute(lambda x: f"100.01")
    tax = factory.LazyAttribute(lambda x: f"100.01")
    plot_area = factory.LazyAttribute(lambda x: f"100.01")
    total_floors = factory.LazyAttribute(lambda x: 1)
    bedrooms = factory.LazyAttribute(lambda x: faker.random_int(min=3, max=10))
    bathrooms = factory.LazyAttribute(lambda x: 1)
    advert_type = factory.LazyAttribute(lambda x: faker.words())
    property_type = factory.LazyAttribute(lambda x: faker.words())
    cover_photo = factory.LazyAttribute(lambda x: ContentFile(
        factory.django.ImageField()._make_data({'width': 1024,  'height': 768}), 'example.jpg'))
    photo1 = factory.LazyAttribute(lambda x: ContentFile(
        factory.django.ImageField()._make_data({'width': 1024,  'height': 768}), 'example.jpg'))
    photo2 = factory.LazyAttribute(lambda x: ContentFile(
        factory.django.ImageField()._make_data({'width': 1024,  'height': 768}), 'example.jpg'))
    photo3 = factory.LazyAttribute(lambda x: ContentFile(
        factory.django.ImageField()._make_data({'width': 1024,  'height': 768}), 'example.jpg'))
    photo4 = factory.LazyAttribute(lambda x: ContentFile(
        factory.django.ImageField()._make_data({'width': 1024,  'height': 768}), 'example.jpg'))
    published_status = False
    views = factory.LazyAttribute(lambda x: faker.random_int())

    class Meta:
        model = Property
