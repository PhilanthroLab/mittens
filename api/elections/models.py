from django.db import models


class Kind(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Region(models.Model):

    kind = models.ForeignKey(Kind, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    # TODO: Store GeoJSON for each region?
    # geo = models.JSONField()
    verified = models.NullBooleanField(default=None)

    class Meta:
        unique_together = ['kind', 'name']

    def __str__(self):
        return f"{self.kind}: {self.name}"


class Election(models.Model):

    name = models.CharField(max_length=100)
    date = models.DateField()
    reference_url = models.URLField(blank=True, null=True)

    class Meta:
        unique_together = ['name', 'date']
        ordering = ['-date']

    def __str__(self):
        return self.name
