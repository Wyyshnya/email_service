from django.db import models


class CustomerManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, email):
        return self.get(email=email)

    def create_user(self, email, first_name, second_name):
        try:
            user = self.model(email=email, first_name=first_name, second_name=second_name)
            user.save()
            return user
        except Exception as err:
            print(err)
            return err


class ThemeManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)


class ThemeCustomerManager(models.Manager):
    use_in_migrations = True
