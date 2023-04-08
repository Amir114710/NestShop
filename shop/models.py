from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

from account.models import User

class Category(models.Model):
    image = models.FileField(upload_to='shop/category', null=True , blank=True , verbose_name="عکس دسته بندی")
    title = models.CharField(max_length=150 , null=True , blank=True , verbose_name="نام دسته بندی")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = "تنظیمات قسمت دسته بندی"

class Tag(models.Model):
    title = models.CharField(max_length=500 , null=True , blank=True , verbose_name='نام برچسب')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'بر چسب'
        verbose_name_plural = 'برچسب ها'

class Sorting(models.Model):
    title = models.CharField(max_length=100 , null=True , blank=True , verbose_name='اسم طبقه بندی:')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'مرتب سازی'
        verbose_name_plural = 'مرتب سازی با'

class Sellers(models.Model):
    name = models.CharField(max_length=200 , null=True , blank=True , verbose_name='نام فروشنده')
    image = models.FileField(upload_to='shop/seller_image' , null=True , blank=True , verbose_name='عکس فروشنده')
    address = RichTextUploadingField(null=True , blank=True , verbose_name='ادرس فروشنده')
    phone = models.IntegerField(null=True , blank=True , verbose_name='شماره تلفن')
    discription = RichTextUploadingField(null=True , blank=True , verbose_name='توضیحات فروشنده')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'فروشنده'
        verbose_name_plural = 'فروشنده ها'

class Size(models.Model):
    amount = models.CharField(max_length=200 , null=True , blank=True , verbose_name='مقدار')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.amount
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'سایز و وزن'
        verbose_name_plural = 'سایز و وزن'

class Tip(models.Model):
    title = models.CharField(max_length=500 , null=True , blank=True , verbose_name='نکته ها')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'نکته'
        verbose_name_plural = ' نکات'

class Product(models.Model):
    title = models.CharField(max_length=150 , null=True , blank=True , verbose_name='نام کالا')
    english_title = models.CharField(max_length=200 , null=True , blank=True , verbose_name='نام کالا به اینگلیسی')
    slug = models.SlugField(null=True , blank=True)
    category = models.ManyToManyField(Category , related_name='products' , blank=True , verbose_name='دسته بندی')
    tag = models.ManyToManyField(Tag , related_name='products' ,  blank=True , verbose_name='بر چسب ها')
    sort_by = models.ManyToManyField(Sorting , related_name='products' , blank=True , verbose_name='مرتب سازی با:')
    seller = models.ForeignKey(Sellers , on_delete=models.CASCADE , related_name='products' , null=True , blank=True , verbose_name='فروشنده')
    size = models.ManyToManyField(Size , related_name='products' , blank=True , verbose_name='سایز و وزن')
    short_discription = RichTextUploadingField(null=True , blank=True , verbose_name='توضیحات کوتاه')
    price = models.SmallIntegerField(null=True , blank=True , verbose_name='قیمت اصلی کالا')
    discount_persent = models.SmallIntegerField(default=0 , null=True , blank=True , verbose_name='درصد تخفیف')
    discount = models.SmallIntegerField(default=0 , null=True , blank=True , verbose_name='قیمت با تخفیف')
    image = models.FileField(upload_to='shop/products' , null=True , blank=True , verbose_name='عکس اصلی کالا برای صفحه ی فروشگاه')
    type = models.CharField(max_length=150 , null=True , blank=True , verbose_name='نوع')
    code = models.SmallIntegerField(null=True , blank=True , verbose_name='شناسه')
    grantee = models.CharField(max_length=150 , null=True , blank=True , verbose_name='گارانتی')
    Availablelty = models.IntegerField(null=True , blank=True , verbose_name='تعداد موجودی کالا')
    status = models.BooleanField(default=True , verbose_name='ایا موجود است ؟')
    content = RichTextUploadingField(null=True , blank=True , verbose_name='توضیحات')
    new = models.BooleanField(default=False , verbose_name='ایا کالا نو است ؟')
    is_not_new = models.BooleanField(default=False , verbose_name='ایا کارکرده است ؟')
    tips = models.ManyToManyField(Tip , related_name='products' , blank=True , verbose_name='نکات')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = 'کالا'
        verbose_name_plural =' کالاها'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.english_title)
        super(Product , self).save(*args, **kwargs)

class MetaTip(models.Model):
    title = models.CharField(max_length=500 , null=True , blank=True , verbose_name='نکته')
    product = models.ForeignKey(Product , related_name= 'metatips' , on_delete=models.CASCADE , null=True , blank=True , verbose_name='کالا')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'نکته'
        verbose_name_plural = ' نکات اضافی'

class ProductImage(models.Model):
    image = models.FileField(upload_to='shop/image' , null=True , blank=True , verbose_name='عکس کالا')
    product = models.ForeignKey(Product , related_name='images' , on_delete=models.CASCADE , null=True , blank=True , verbose_name='کالا')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.image.url
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'عکس کالا'
        verbose_name_plural = ' عکس کالاها '


class Comments(models.Model):
    user = models.ForeignKey(User , related_name="comments" , on_delete=models.CASCADE , verbose_name = 'کاربر')
    products = models.ForeignKey(Product , related_name="comments" , on_delete=models.CASCADE, verbose_name = 'کالا ها')

    parent = models.ForeignKey('self' , on_delete=models.CASCADE , related_name = 'replies' , null=True , blank=True, verbose_name = 'پست جواب داده شده')

    message = RichTextUploadingField(null=True, blank=True, verbose_name = 'نظرات')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.phone}-{self.products.title}'

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = "تنظیمات قسمت نظرات"
        ordering = ('-created',)

class Like(models.Model):
    users = models.ForeignKey(User , related_name='likes' , on_delete=models.CASCADE , verbose_name = 'کاربر')
    products = models.ForeignKey(Product , related_name='likes' , on_delete=models.CASCADE , verbose_name = 'کالا ها')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.users.username} - {self.products.title}"

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "تنظیمات قسمت لایک ها"
        ordering = ("-created",)


class Compare(models.Model):
    products = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='compares' , verbose_name='محصول')
    users = models.ForeignKey(User , on_delete=models.CASCADE , related_name='compares' , verbose_name='کاربر')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.products.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'مقایسه'
        verbose_name_plural = 'محصولات مقایسه شده'