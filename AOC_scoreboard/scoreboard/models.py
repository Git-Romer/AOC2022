from django.db import models

# Create your models here.

class jsoncrawler(models.Model):
    member_id = models.IntegerField(unique=True, primary_key=True)
    name = models.TextField()
    stars = models.IntegerField()
    global_score = models.IntegerField()
    local_score = models.IntegerField()
    last_star_ts = models.TextField()
    completition_day_level = models.JSONField(blank=True)
    event = models.TextField()

    class Meta:
        verbose_name_plural = "aoc_scoreboard_content"
        verbose_name = "aoc_scoreboard_content"

    def save(self, *args, **kwargs):
        self.id = self.member_id # replacing the id(primary key) as the member id
        return super(jsoncrawler, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.member_id)