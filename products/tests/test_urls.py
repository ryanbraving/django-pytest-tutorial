from django.urls import reverse, resolve


class TestUrls:

    def test_detail_url(self):
        # reverse function is equivalent of url in the templates
        # (defined in urls.py)
        # so we pass the name and then it gives us the path back
        # in this case our path is a parameter ('<int:pk>') that's why we
        # have to pass a parameter, so I am passing kwargs
        path = reverse('detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'detail'
