from django import template

register=template.Library()

def swap(value):
    return value.swapcase()

register.filter('swapping',swap)


@register.filter()
def ct(value,arg):
    return value.count(arg)
 
@register.filter()
def rp(value,arg):
    return value.replace(arg,'H')


#def ct(value,arg):
#    return value.count(arg)

#register.filter('counting',ct)
