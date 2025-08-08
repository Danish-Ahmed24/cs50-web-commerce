from decimal import Decimal
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import *
 

def index(request):
    allListings = Listing.objects.all()
    listings_with_bids = []

    for listing in allListings:
        # if listing.is_active:
            current_bid = listing.bids.last().amount if listing.bids.last() else "No bids yet"
            listings_with_bids.append((listing, current_bid))

    return render(request, "auctions/index.html", {
        "listings_with_bids": listings_with_bids
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

#Creating new Listing
@login_required
def createListing(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        bid = request.POST['bid']
        url = request.POST.get('url')
        category = request.POST.get('category')
        owner = request.user

        new_listing = Listing.objects.create(
            title=title,
            desc=desc,
            url=url,
            owner= owner,
            category=category
        )

        Bid.objects.create(
            amount=bid,
            bidmaker=request.user,
            listing=new_listing
        )
        

        return redirect("index")


    return render(request,"auctions/createListing.html")

def listing(request, id):
    reqListing = Listing.objects.get(pk=id)
    isWishlisted = False
    is_owner = False
    is_winner = False


    current_bid = reqListing.bids.last().amount
    if request.user.is_authenticated:
        try:
            wishlist = WishList.objects.get(user=request.user)
            isWishlisted = reqListing in wishlist.listings.all()
        except WishList.DoesNotExist:
            isWishlisted = False

        if reqListing.owner == request.user:
            is_owner=True

    if not reqListing.is_active:
        max = 0
        win = None
        for x in reqListing.bids.all():
            if max<x.amount:
                win = x
                max = x.amount
        if request.user == win.bidmaker:
            is_winner= True
    


    return render(request, 'auctions/listing.html', {
        "listing": reqListing,
        "is_authenticated": request.user.is_authenticated,
        "isWishlisted": isWishlisted,
        "current_bid": current_bid,
        "is_owner":is_owner,
        "is_winner":is_winner,
        "comments":reqListing.comments.all(),
    })


@login_required
def addWishlist(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        try:
            wishListOfUser = WishList.objects.get(user=request.user)
        except WishList.DoesNotExist:
            wishListOfUser = WishList(user=request.user)
            wishListOfUser.save()
        wishListOfUser.listings.add(Listing.objects.get(pk=listing_id))
    return redirect("listing",id=listing_id)

@login_required
def delWishlist(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        wishListOfUser = WishList.objects.get(user=request.user)
        

        wishListOfUser.listings.remove(Listing.objects.get(pk=listing_id))
        

        wishListOfUser.save()
    return redirect("listing",id=listing_id)


# listing_id , bid_amount
@login_required
def placeBid(request):
    listing_id = request.POST['listing_id']
    bid = float(request.POST.get('bid_amount'))
    listing = Listing.objects.get(pk=listing_id)
    allBids = listing.bids.all()
    is_OK = False

    for otherBid in allBids:
        if bid >= otherBid.amount and len(allBids)==1 :
            is_OK = True 
            break
        elif bid > otherBid.amount :
            is_OK = True
        else:
            is_OK=False
            break
    
    if is_OK:
        Bid.objects.create(
            amount = bid,
            bidmaker= request.user,
            listing = listing 
        )
        return redirect('listing',id = listing_id)




    return HttpResponse("Error")

@login_required
def closeAuction(request):
    listing_id = request.POST.get('listing_id')
    if request.method == "POST":
        listing = Listing.objects.get(pk=listing_id)
        listing.is_active = False

        highest_bid = listing.bids.order_by('-amount').first()

        if highest_bid:
            listing.winner = highest_bid.bidmaker
        
        listing.save()

    return redirect('index')

@login_required
def addComment(request):
    if request.method == "POST":
        listing_id = request.POST.get('listing_id')
        text_comment = request.POST.get('text_comment')
        commenter = request.user

        Comment.objects.create(
            text=text_comment,
            commenter=commenter,
            listing=Listing.objects.get(pk = listing_id)
        )
        

    
    return redirect('listing',id = request.POST['listing_id'])

@login_required
def wishlist(request):
    user = request.user
    wishlist, created = WishList.objects.get_or_create(user=user)
    return render(request, 'auctions/wishlist.html', {
        "wishlist": wishlist.listings.all()
    })

def categories(request):
    return render(request, "auctions/categories.html")

def category(request, category):
    clistings = Listing.objects.filter(category=category).all()
    return render(request, "auctions/index.html", {
        "listings_with_bids": [
            (
                listing,
                listing.bids.last().amount if listing.bids.last() else "No bids yet"
            )
            for listing in clistings
        ]
    })