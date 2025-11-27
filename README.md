# Commerce - eBay-like Auction Site

An eBay-like e-commerce auction site built with Django that allows users to post auction listings, place bids on listings, comment on listings, and add listings to a watchlist.

## 🌐 Live Demo

Check out the live site: [https://danishahmed2.pythonanywhere.com](https://danishahmed2.pythonanywhere.com)

## ✨ Features

- **User Authentication**: Register, login, and logout functionality
- **Create Listings**: Users can create auction listings with title, description, starting bid, image URL, and category
- **Active Listings**: Browse all currently active auction listings
- **Listing Page**: View detailed information about each listing including:
  - Current price (highest bid)
  - Number of bids placed
  - Item description and image
  - Comments from other users
- **Bidding System**: Place bids on active listings (must be higher than current bid)
- **Watchlist**: Add/remove listings to your personal watchlist
- **Close Auction**: Listing creators can close their auctions and declare a winner
- **Comments**: Add comments to listing pages
- **Categories**: Browse listings by category (Fashion, Toys, Electronics, Home)
- **Winner Notification**: Users are notified if they win an auction

## 🛠️ Technologies Used

- Python 3.13
- Django 5.2.5
- SQLite3 (Database)
- HTML/CSS
- Bootstrap (for styling)

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🚀 Installation & Setup

### Method 1: Clone with Git

```bash
git clone https://github.com/Danish-Ahmed24/cs50-web-commerce.git
cd cs50-web-commerce
```

### Method 2: Download ZIP (No Git Required)

If you don't have Git installed:

1. Go to: [https://github.com/Danish-Ahmed24/cs50-web-commerce](https://github.com/Danish-Ahmed24/cs50-web-commerce)
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. Extract the ZIP file to a folder on your computer
5. Open Terminal/Command Prompt and navigate to the extracted folder:

**On Windows:**
```bash
cd C:\Users\YourName\Downloads\cs50-web-commerce-main
```

**On macOS/Linux:**
```bash
cd ~/Downloads/cs50-web-commerce-main
```

### 2. Create a Virtual Environment

**On Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

You should see `(venv)` at the beginning of your command line when activated.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install Django manually:
```bash
pip install django
```

### 4. Apply Database Migrations

```bash
python manage.py makemigrations auctions
python manage.py migrate
```

### 5. Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to set:
- Username
- Email (optional)
- Password

### 6. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## 📱 Using the Application

### For Regular Users:

1. **Register**: Create a new account at `/register`
2. **Login**: Sign in with your credentials at `/login`
3. **Browse Listings**: View all active listings on the homepage
4. **Create Listing**: Click "Create Listing" to post a new auction
5. **Place Bids**: Enter a bid amount higher than the current price
6. **Add to Watchlist**: Click the watchlist button to save listings
7. **Comment**: Share your thoughts on listing pages
8. **Categories**: Filter listings by category

### For Listing Creators:

1. **Close Auction**: When ready, close your listing to declare a winner
2. **Winner**: The highest bidder wins when you close the auction

### For Admins:

1. Access the admin panel at: `http://127.0.0.1:8000/admin`
2. Login with your superuser credentials
3. Manage users, listings, bids, and comments

## 📁 Project Structure

```
commerce/
├── auctions/               # Main application directory
│   ├── migrations/        # Database migrations
│   ├── static/           # CSS, JavaScript, images
│   ├── templates/        # HTML templates
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── urls.py           # URL routing
│   └── admin.py          # Admin configuration
├── commerce/             # Project settings directory
│   ├── settings.py       # Django settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── db.sqlite3           # SQLite database
├── manage.py            # Django management script
└── README.md            # This file
```

## 🗃️ Database Models

### User
- Extends Django's AbstractUser
- Handles authentication and user information

### Listing
- `title`: CharField (max 64 characters)
- `desc`: TextField
- `url`: URLField (optional image URL)
- `is_active`: BooleanField (default: True)
- `owner`: ForeignKey to User
- `winner`: ForeignKey to User (nullable)
- `category`: CharField with choices (Fashion, Toys, Electronics, Home)

### Bid
- `amount`: DecimalField (max 20 digits, 2 decimal places)
- `bidmaker`: ForeignKey to User
- `listing`: ForeignKey to Listing

### Comment
- `text`: CharField (max 128 characters)
- `commenter`: ForeignKey to User
- `listing`: ForeignKey to Listing
- `date`: DateTimeField (auto-generated)

### WishList
- `listings`: ManyToManyField to Listing
- `user`: OneToOneField to User

## 🔧 Common Issues & Solutions

### Issue: "Python is not recognized" (Windows)
**Solution**: 
1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, CHECK the box "Add Python to PATH"
3. Restart your terminal/command prompt

### Issue: "No module named 'django'"
**Solution**: Make sure your virtual environment is activated and Django is installed:
```bash
pip install django
```

### Issue: Can't find the downloaded folder
**Solution**: 
- The folder name will be `cs50-web-commerce-main` (note the `-main` suffix)
- Check your Downloads folder
- On Windows: `C:\Users\YourName\Downloads\cs50-web-commerce-main`
- On Mac: `/Users/YourName/Downloads/cs50-web-commerce-main`

### Issue: Virtual environment won't activate (Windows)
**Solution**: If you get an execution policy error, run PowerShell as Administrator and execute:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: Database errors after downloading
**Solution**: The database might not be included. Create a fresh one:
```bash
python manage.py migrate
python manage.py createsuperuser
```

### Issue: Static files not loading
**Solution**: Run the collect static command:
```bash
python manage.py collectstatic
```

### Issue: Port already in use
**Solution**: Run the server on a different port:
```bash
python manage.py runserver 8080
```

## 🧪 Testing

To test the application:

1. Create multiple user accounts
2. Create several listings with different categories
3. Place bids from different accounts
4. Test the watchlist functionality
5. Add comments to listings
6. Close an auction and verify the winner

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is part of CS50's Web Programming with Python and JavaScript course.

## 👤 Author

**Danish Ahmed**

- GitHub: [@Danish-Ahmed24](https://github.com/Danish-Ahmed24)
- Live Site: [danishahmed2.pythonanywhere.com](https://danishahmed2.pythonanywhere.com)

## 🙏 Acknowledgments

- CS50's Web Programming with Python and JavaScript course
- Harvard University
- Django Documentation

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Common Issues](#-common-issues--solutions) section
2. Open an issue on GitHub
3. Contact the author

---

**Happy Bidding! 🎉**