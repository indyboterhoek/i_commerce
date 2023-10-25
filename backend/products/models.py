from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.IntegerField()
	description = models.TextField()
	image = models.ImageField(upload_to='')
	images = models.ManyToManyField('OptionImage', blank=True)
	stock = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	sale = models.ForeignKey('Sale', on_delete=models.CASCADE, blank=True, null=True)
	status = models.BooleanField(default=True)
	slug = models.SlugField(max_length=100, unique=True)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	display_home = models.BooleanField(default=False)
	display_slider = models.BooleanField(default=False)
	option_categorys = models.ManyToManyField('OptionCategory', blank=True)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return self.name
	
class Sale(models.Model):
	name = models.CharField(max_length=100)
	percent = models.IntegerField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)
	slug = models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return self.name

class Coupon(models.Model):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=20)
	percent = models.IntegerField()
	discount = models.IntegerField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	def __str__(self):
		return self.name

class Option(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	category = models.ForeignKey('OptionCategory', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class OptionCategory(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return self.name

class OptionImage(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/')
	option = models.ForeignKey('Option', on_delete=models.CASCADE)
	option_category = models.ForeignKey('OptionCategory', on_delete=models.CASCADE)
	option_product = models.ForeignKey('Product', on_delete=models.CASCADE, blank=True, null=True)
	slug = models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return self.option.name