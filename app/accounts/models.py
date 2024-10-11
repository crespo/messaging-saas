import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models, transaction


class CompanyManager(models.Manager):
    """Manager for the Company model. Also handles the account creation"""

    @transaction.atomic
    def create_account(self, company_name, username, password, company_address=None):
        """Creates a Company along with the User and returns them both"""

        company = self.all().filter(name=company_name)

        if not company:
            company = Company(
                name=company_name,
                address=company_address,
            )
            company.save()
        else:
            company = company.get()

        user = User.objects.create_user(
            username=username,
            password=password,
            company=company,
        )

        return company, user


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("name", max_length=100)
    address = models.CharField("address", max_length=250, blank=True)

    objects = CompanyManager()

    class Meta:
        db_table = "companies"

    def __str__(self):
        return f"id: {self.id}\nname: {self.name}\naddress: {self.address}"


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(
        Company, related_name="%(class)s", on_delete=models.CASCADE, editable=False
    )

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"({self.company.name}) - {self.username}"
