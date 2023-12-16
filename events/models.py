from django.db import models
from users.models import Users


class Tags(models.Model):
    "Model for tags"
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f"name: {self.name}"


class Events(models.Model):
    """Model for events"""

    name = models.CharField(unique=True, max_length=100)
    image = models.ImageField(upload_to="events_images")
    description = models.TextField()
    award = models.CharField(max_length=256, null=True, blank=True)
    rule = models.TextField()
    participants = models.ManyToManyField(to=Users, related_name="events_TEAMS")
    winners = models.ManyToManyField(to=Users, blank=True, related_name="events_winners")
    tags = models.ManyToManyField(to=Tags)
    creator = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    tasks = models.TextField(null=True, blank=True)
    faq = models.TextField(null=True, blank=True)
    chat = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    text_for_email = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"name: {self.name} | tags: {self.tags.name}"


# modelsQuerySet and modelsManager
class ReviewQuerySet(models.QuerySet):
    def total_rating(self):
        if self.count() > 0:
            return round(sum([review.rating for review in self])/self.count(), 2)
        else:
            return 0.0


class ReviewManager(models.Manager):
    def get_queryset(self):
        return ReviewQuerySet(self.model)
    
    def total_rating(self):
        return self.get_queryset().total_rating()


class Reviews(models.Model):
    """Model for reviews"""

    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    event = models.ForeignKey(to=Events, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    review_manager = ReviewManager()

    class Meta:
        verbose_name = "отзыву"
        verbose_name_plural = "Отзывы"

    def __str__(self) -> str:
        return f"review: {self.user.username} | event: {self.event.name}"