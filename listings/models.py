# listings/models.py

from django.db import models
from django.conf import settings 

# Define choices for property type (Rent or Sale)
PROPERTY_TYPE_CHOICES = (
    ('RENT', 'For Rent'),
    ('SALE', 'For Sale'),
)

# Define choices for toilet types
TOILET_TYPE_CHOICES = (
    ('PITLATRINE', 'Pitlatrine'),
    ('FLUSHABLE', 'Flushable'),
    ('TOILETPAN', 'Toilet Pan')
)

class Property(models.Model):
    # Financials and Pricing
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    
    # Property Physical Details
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    self_contained = models.BooleanField(default=False, help_text="Does the unit have its own bathroom/toilet?")
    toilet_type = models.CharField(
        max_length=12,
        choices=TOILET_TYPE_CHOICES,
        default='PITLATRINE',
    )
    water_onsite = models.BooleanField(default=False)
    
    # Location Details
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    
    # Categorization and Status
    property_type = models.CharField(
        max_length=4,
        choices=PROPERTY_TYPE_CHOICES,
        default='SALE',
        help_text="Is this property for Rent or Sale?"
    )
    list_date = models.DateTimeField(auto_now_add=True)
    
    # Agent/Owner Relationship
    agent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='properties',
        limit_choices_to={'is_staff': True}
    )
    
    def __str__(self):
        # Dynamically generate the string representation for the Admin/logs
        property_desc = "house" # Placeholder/Default property type
        type_display = self.get_property_type_display().lower()

        return (
            f"{self.bedrooms} bedroomed {property_desc} {type_display} "
            f"in {self.province} Province, {self.city} City, {self.area} Area"
        )

    class Meta:
        verbose_name_plural = "Properties"
        ordering = ['-list_date']