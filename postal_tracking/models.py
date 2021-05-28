from django.db import models

class tracking_numbers(models.Model):
	user_id = models.IntegerField(null=False, blank=False)
	created = models.DateTimeField(auto_now_add=True)
	tracking_number = models.CharField(max_length=30)
	description = models.CharField(max_length=200)

	class Meta:
		verbose_name = 'item'
		verbose_name_plural = 'items'
	def __str__(self):
		return '%s - %s' % (self.tracking_number, self.description)
