from django import template
import math

register = template.Library()

millnames = ['','k','m','b']

@register.filter
def cool_number(value):
    try:
        n = float(value)
        millidx = max(0,min(len(millnames)-1,
                            int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
        result = '{:.2f}'.format(n / 10**(3 * millidx))
        if '.' in result:
            result = result.rstrip('0').rstrip('.')
        return (result + millnames[millidx])
    except Exception as e:
        return 0 
