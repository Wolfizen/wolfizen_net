from django.db import models


class ShowVote(models.Model):
    show = models.ForeignKey('wolfizen_net.Show', on_delete=models.CASCADE, related_name='votes')
    source_ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} -> {} @ {}".format(self.source_ip, self.show.name, self.created_at)


class Show(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} @ {}".format(self.name, self.created_at)
