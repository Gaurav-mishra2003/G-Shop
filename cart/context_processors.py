from .cart import Cart

# Create context processor so our cart can work on all pages of the site
def cart(request):
	# Return the default data from our CartAdd commentMore actions
	return {'cart': Cart(request)}