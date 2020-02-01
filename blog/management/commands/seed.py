from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from blog.models import BlogPost


class Command(BaseCommand):
    help = 'Seed database with some data!'

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout=None, stderr=None, no_color=False, force_color=False)
        self.users = []
        self.fake = Faker()
        self.fake_fa = Faker(['fa_IR'])

    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise CommandError('Seed command only run in debug mode!')

        self.seed_users()
        self.seed_blog_posts()

    def seed_blog_posts(self):
        self.stdout.write('Seed Blog posts...\n')
        BlogPost.objects.all().delete()
        date = self.fake.date_between(start_date='-30y', end_date='today')
        for i in range(4):
            post = BlogPost(
                author=self.get_random_user(),
                poster=None,
                subject=self.fake_fa.sentence(),
                content=self.fake_fa.text(),
                published_at=date,
                updated_at=date
            )
            post.save()

    def get_random_user(self):
        return self.fake.random_element(self.users)

    def seed_users(self):
        self.stdout.write('Seed Users... \n')
        User.objects.all().delete()
        for i in range(5):
            user = User.objects.create_user(self.fake.user_name(),
                                            self.fake.free_email(),
                                            'user{}pass'.format(i))
            user.save()
            self.users.append(user)
