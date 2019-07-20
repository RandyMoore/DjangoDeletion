from django.db import models


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    one_item_null = models.ForeignKey('OneToOneItem', related_name='subject_null', on_delete=models.SET_NULL, null=True)
    one_item_protect = models.ForeignKey('OneToOneItem', related_name='subject_protect', on_delete=models.PROTECT)
    one_item_cascade = models.ForeignKey('OneToOneItem', related_name='subject_cascade', on_delete=models.CASCADE)

    many_items_null = models.ForeignKey('OneOfManyItems', related_name='subject_null', on_delete=models.SET_NULL, null=True)
    many_items_protect = models.ForeignKey('OneOfManyItems', related_name='subject_protect', on_delete=models.PROTECT)
    many_items_cascade = models.ForeignKey('OneOfManyItems', related_name='subject_cascade', on_delete=models.CASCADE)

    shared_item_null = models.ForeignKey('SharedItem', related_name='subject_null', on_delete=models.SET_NULL, null=True)
    shared_item_protect = models.ForeignKey('SharedItem', related_name='subject_protect', on_delete=models.PROTECT)
    shared_item_cascade = models.ForeignKey('SharedItem', related_name='subject_cascade', on_delete=models.CASCADE)


class OneToOneItem(models.Model):
    id = models.AutoField(primary_key=True)


class OneOfManyItems(models.Model):
    id = models.AutoField(primary_key=True)


class SharedItem(models.Model):
    id = models.AutoField(primary_key=True)
