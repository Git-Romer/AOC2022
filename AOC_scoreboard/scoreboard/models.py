from django.db import models
from datetime import date

# Create your models here.

class jsoncrawler(models.Model):
    member_id = models.IntegerField(unique=True, primary_key=True)
    name = models.TextField()
    stars = models.PositiveIntegerField(default=0)
    global_score = models.PositiveIntegerField(default=0)
    local_score = models.PositiveIntegerField(default=0)
    last_star_ts = models.TextField(null=True, blank=True)
    completion_day_level = models.JSONField(null=True, blank=True)
    event = models.PositiveIntegerField(default=date.today().year)

    class Meta:
        verbose_name_plural = "aoc_scoreboard_content"
        verbose_name = "aoc_scoreboard_content"

    def save(self, *args, **kwargs):
        self.id = self.member_id # replacing the id(primary key) as the member id
        return super(jsoncrawler, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.member_id)