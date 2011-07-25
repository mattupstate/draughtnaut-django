from django.test import TestCase
from beer.models import Beer

class BeerTestCase(TestCase):
    
    fixtures = ['auth.json', 'contenttypes.json','beer.json', 'moderation.json']
    
    def setUp(self):
        pass 
        
    def tearDown(self):
        pass
    
    def test_approve_beer(self):
        beer = Beer.objects.get(approved=False)
        self.assertNotEqual(beer, None)
        self.assertFalse(beer.approved)
        beer.approve()
        self.assertTrue(beer.approved)
        
    
        
