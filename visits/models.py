from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class VisitCount(models.Model):
    # NUMBER OF VISITS
    visit_count = models.IntegerField(default=0, help_text="Total number of visits of item")

    # ITEM (any Model)
    item_type = models.ForeignKey(ContentType, related_name="visit_count")
    item_id = models.PositiveIntegerField()
    item = GenericForeignKey('item_type', 'item_id')

    # TIMESTAMPS
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['item_type', 'item_id']
        verbose_name = "Visit Count"
        verbose_name_plural = "Visits Counts"
        ordering = ['item_type']

    def __unicode__(self):
        return u'Visit Count - {0}'.format(self.item.__unicode__())

    def increase_visit_count(self, by=1, commit=False):
        self.visit_count += by
        if commit:
            self.save()

        if hasattr(self.item, 'visit_count'):
            self.item.visit_count = self.visit_count
            if commit:
                self.item.save()


class BlacklistedIP(models.Model):
    # BLACKLISTED IP
    ip = models.CharField(max_length=40, unique=True)

    # TIMESTAMPS
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blacklisted IP"
        verbose_name_plural = "Blacklisted IPs"

    def __unicode__(self):
        return unicode(self.ip)


class BlacklistedUserAgent(models.Model):
    # BLACKLISTED USER AGENT
    user_agent = models.CharField(max_length=255, unique=True)

    # TIMESTAMPS
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blacklisted User Agent"
        verbose_name_plural = "Blacklisted User Agents"

    def __unicode__(self):
        return unicode(self.user_agent)