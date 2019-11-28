from django.db import models


class Type(models.Model):
    """Category or type of service."""
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Region(models.Model):
    """General location (e.g., state, country, etc.)."""
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class City(models.Model):
    """City."""
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Vendor(models.Model):
    """An event vendor or supplier."""
    text = models.CharField(max_length=200)
    url = models.URLField
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Offering(models.Model):
    """Services or spaces offered by a vendor or supplier."""
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
