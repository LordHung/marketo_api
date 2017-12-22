from django.db import models
from django.urls import reverse


ADDRESS_TYPES = (
    ('billing', 'Billing address'),
    ('shipping', 'Shipping address'),
)


class Address(models.Model):
    billing_profile = models.ForeignKey('billings.BillingProfile', on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True,
                            blank=True, help_text='Shipping to? Who is it for?')
    address_type = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    address_line_1 = models.CharField(max_length=120)
    address_line_2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default='VN')
    district = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)

    objects = models.Manager()

    class Meta:
        db_table = 'address'

    def __str__(self):
        if self.name:
            return str(self.name)
        return str(self.address_line_1)

    def get_absolute_url(self):
        return reverse('address-update', kwargs={'pk': self.pk})

    def get_short_address(self):
        for_name = self.name
        return '{for_name} {line1}, {city}'.format(
            for_name=for_name or '',
            line1=self.address_line_1,
            city=self.city
        )

    def get_address(self):
        return '{for_name}\n{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}'.format(
            for_name=self.name or '',
            line1=self.address_line_1,
            line2=self.address_line_2 or '',
            city=self.city,
            state=self.state,
            postal=self.postal_code,
            country=self.country
        )
