from django.db.models.signals import pre_delete
from django.db import models


#  Motivating Example
class OrderReport(models.Model):
    pass


class Order(models.Model):
    report = models.ForeignKey(OrderReport, related_name='orders', on_delete=models.CASCADE, null=True)


class OrderLine(models.Model):
    order = models.ForeignKey(Order, related_name='order_lines', on_delete=models.CASCADE, null=True)


#  Many to Many
class ManyToManyParent(models.Model):
    def print_relations(self):
        print(f'{self.__class__.__name__} id: {self.id} has children '
              f'{[f"{child.__class__.__name__} {child.id}" for child in self.children.all()]}')


class ManyToManyChild(models.Model):
    parents = models.ManyToManyField(ManyToManyParent,
                                     related_name='children')


# Many to One
class ManyToOneParent(models.Model):
    def print_relations(self):
        print(f'{self.__class__.__name__} id: {self.id} has cascade children '
              f'{[f"{child.__class__.__name__} {child.id}" for child in self.children_cascade.all()]}')

        print(f'{self.__class__.__name__} id: {self.id} has null children '
              f'{[f"{child.__class__.__name__} {child.id}" for child in self.children_null.all()]}')

        print(f'{self.__class__.__name__} id: {self.id} has protect children '
              f'{[f"{child.__class__.__name__} {child.id}" for child in self.children_protect.all()]}')


class ManyToOneChildCascade(models.Model):
    parent = models.ForeignKey(ManyToOneParent,
                               related_name='children_cascade',
                               on_delete=models.CASCADE)  # Default is CASCADE


class ManyToOneChildNull(models.Model):
    parent = models.ForeignKey(ManyToOneParent,
                               related_name='children_null',
                               on_delete=models.SET_NULL,
                               null=True)  # Allows field to be nullable, required for on_delete=SET_NULL


class ManyToOneChildProtect(models.Model):
    parent = models.ForeignKey(ManyToOneParent,
                               related_name='children_protect',
                               on_delete=models.PROTECT)


# One to One
class OneToOneParent(models.Model):
    def print_relations(self):
        if hasattr(self, 'child_cascade'):
            print(f'{self.__class__.__name__} id: {self.id} has cascade child '
                  f'{self.child_cascade.__class__.__name__} {self.child_cascade.id}')
        else:
            print(f'{self.__class__.__name__} id: {self.id} has no cascade child')

        if hasattr(self, 'child_null'):
            print(f'{self.__class__.__name__} id: {self.id} has null child '
                  f'{self.child_null.__class__.__name__} {self.child_null.id}')
        else:
            print(f'{self.__class__.__name__} id: {self.id} has no null child')

        if hasattr(self, 'child_protect'):
            print(f'{self.__class__.__name__} id: {self.id} has protect child '
                  f'{self.child_protect.__class__.__name__} {self.child_protect.id}')
        else:
            print(f'{self.__class__.__name__} id: {self.id} has no protect child')


class OneToOneChildCascade(models.Model):
    parent = models.OneToOneField(OneToOneParent,
                                  related_name='child_cascade',
                                  on_delete=models.CASCADE)  # Default is CASCADE


class OneToOneChildNull(models.Model):
    parent = models.OneToOneField(OneToOneParent,
                                  related_name='child_null',
                                  on_delete=models.SET_NULL,
                                  null=True)  # Allows field to be nullable, required for on_delete=SET_NULL


class OneToOneChildProtect(models.Model):
    parent = models.OneToOneField(OneToOneParent,
                                  related_name='child_protect',
                                  on_delete=models.PROTECT)


def report_deletion(sender, **kwargs):
    instance = kwargs['instance']
    print(f'Delete called on {instance.__class__.__name__} {instance.id}')


for model in [OrderReport, Order, OrderLine,
              ManyToManyParent, ManyToManyChild,
              ManyToOneParent, ManyToOneChildCascade, ManyToOneChildNull, ManyToOneChildProtect,
              OneToOneParent, OneToOneChildCascade, OneToOneChildNull, OneToOneChildProtect]:
    pre_delete.connect(report_deletion, sender=model)
