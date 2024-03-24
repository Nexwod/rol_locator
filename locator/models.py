from django.db import models
from django.urls import reverse


REGION_CHOICE = ('Region 1 (Amansea - School gate)', 'Region 2 (Inside Unizik and Environ)', 'Region 3 (School gate - Second Market)',  'Region 4 (Second Market - First Market)',  'Region 5 (First Market - Aroma)',  'Region 6 (Aroma - Tempsite)',  'Region 7 (Tempsite - Okpuno and Environ)', 'Others' )

# Create your models here.
class RolPoints(models.Model):
    region = models.CharField(max_length = 20)
    address = models.TextField()
    image = models.ImageField(blank = True, upload_to = 'google_map_image/')
    co_ordinator = models.CharField(max_length = 200, blank = True)
    contact = models.CharField(max_length = 14, blank = True)
    date_time = models.TextField(blank = True)
    google_map_url = models.TextField(blank=True)

    # def get_absolute_url(self):
    #     return reverse("locator:all_points", kwargs={id : self.id})