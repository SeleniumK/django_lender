"""Tests for the lender_profile app."""

from django.test import TestCase
from django.contrib.auth.models import User
from lender_profile.models import PatronProfile
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """User Factory class."""

    class Meta:
        """Declare factory model."""

        model = User

    username = factory.Sequence(lambda n: "The chosen {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@foo.com".format(x.username.replace(" ", ""))
    )


class ProfileTestCase(TestCase):
    """The PatronProfile Model test runner."""

    def setUp(self):
        """Set up for Profile Test Case."""
        self.foo = "bar"
        self.users = [UserFactory.create() for i in range(20)]

    def test_profile_created_when_user_is_saved(self):
        """Test post save signal and assert that profile is created when user is."""
        self.assertEqual(PatronProfile.objects.count(), 20)

    def test_profile_is_associated_with_actual_users(self):
        """."""
        pass

    def test_user_has_profile(self):
        """."""
        for user in self.users:
            self.assertTrue(hasattr(user, "profile"))
            self.assertIsInstance(user.profile, PatronProfile)
