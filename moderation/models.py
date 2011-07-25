from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from utils.mixins import TimestampMixin

# Handy moderation manager
class ModerationManager(models.Manager):
    def unapproved(self):
        return self.filter(approved=False)
    
    def approved(self):
        return self.filter(approved=True)

# Moderation Flag model
class ModerationFlag(TimestampMixin):
    
    REASONS = (
        ('duplicate','duplicate'),
        ('inappropriate','inappropriate'),
    )
    
    reason = models.CharField(max_length=50, choices=REASONS)
    object_id = models.PositiveIntegerField()
    
    # Relationships
    content_type = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    flagged_by = models.ForeignKey(User, related_name='moderation_flags')
    
    def __unicode__(self):
        return '%s[%s] - %s' % (self.content_object.name, self.object_id, self.reason)
    
    class Meta:
        verbose_name_plural = "Moderation Flags"
        ordering = ['-date_created']
