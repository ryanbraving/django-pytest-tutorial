import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testing.settings')

import django
django.setup()

from datetime import datetime
from products.models import Product

def populate():
    out = Product.objects.all()
    print (len(out))
    for m in out:
        m.delete()
    out = Product.objects.get_or_create(name='Book',
                        description='An awesome book about Django',
                        price='19.99',
                        quantity= 100,
                        published_on=datetime.now())[0]
    # out = Product.objects.all()
    # print (len(out))
    # out.save()

if __name__ == "__main__":
	print("populating script started.")
	populate()
	print("populating complete!")
