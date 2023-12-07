from django.db import models


# avtor uchun
class Author(models.Model):
    name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='author_images/')

    class Meta:
        verbose_name_plural = 'authors'

    def __str__(self) -> str:
        return self.name


# kategoriyalar modeli
class Category(models.Model):
    name = models.CharField(max_length=255)
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self) -> str:
        return self.name

# Post modeli
class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    text = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='post_images/')
    like = models.PositiveBigIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Posts'
    
    def __str__(self) -> str:
        return self.title

# komment modeli
class Comment(models.Model):
    name = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Comments'

# slide menu uchun qo'shimcha 
# bosh sahidagi e'lonlar
class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events_image')

    class Meta:
        verbose_name_plural = 'Events'
    
    def __str__(self) -> str:
        return self.title