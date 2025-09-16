# BookVerse - Book Recommendation System

BookVerse is an intelligent book recommendation web app built with Flask, pandas, numpy, and scikit-learn. It provides users with curated book suggestions based on popularity and collaborative filtering.

## Features

- **Trending Books:** Shows top 50 books based on ratings and popularity.
- **Intelligent Recommendations:** Enter a book title to get personalized suggestions using collaborative filtering.
- **Modern UI:** Responsive, dark-themed interface with smooth hover effects and animations.
- **Error Handling:** Friendly messages for unrecognized books or empty input.
- **Star Ratings:** Ratings are rounded up and displayed as stars.
- **Logo Branding:** Custom favicon and logo animation on navbar hover.
- **Ready for Deployment:** Compatible with Render and GitHub Pages (static version).

## Tech Stack

- **Backend:** Python 3.11+, Flask, pandas, numpy, scikit-learn, pickle
- **Frontend:** HTML5, CSS3, Bootstrap 5, Font Awesome
- **Deployment:** Render.com, GitHub Pages (static)

## File Structure

```
BookVerse-Book-Recommendation-System-/
│
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
├── runtime.txt             # Python version for deployment
├── templates/
│   ├── index.html          # Home page (trending books)
│   └── recommand.html      # Recommendation page
├── static/
│   └── logo.png            # Logo for favicon and navbar
├── Dataset/
│   ├── Books.csv
│   ├── Ratings.csv
│   └── Users.csv
├── popular.pkl             # Pickled DataFrame for trending books
├── pt.pkl                  # Pivot table for collaborative filtering
├── books.pkl               # Book metadata
├── similarity_score.pkl    # Cosine similarity matrix
└── README.md
```

## How It Works

- **Trending Books:** Uses ratings and popularity thresholds to select top books.
- **Recommendations:** Finds similar books using cosine similarity on user-book ratings matrix.
- **Star Ratings:** Ratings are rounded up (e.g., 3.2 → 4 stars).
- **Error Handling:** Displays messages if the book is not found or input is empty.

## Deployment

### Render.com

1. Make sure you have `requirements.txt` and `runtime.txt` in your repo root.
2. `runtime.txt` should contain:
    ```
    python-3.11.9
    ```
3. `requirements.txt` example:
    ```
    flask>=3.0.0,<4.0.0
    numpy>=1.24.0,<2.0.0
    pandas>=2.0.0,<3.0.0
    scikit-learn>=1.3.0,<2.0.0
    gunicorn>=21.2.0
    Werkzeug>=3.0.0,<4.0.0
    ```
4. Deploy on Render.com with the build command:
    ```
    pip install -r requirements.txt
    ```
5. The app will run on the port specified by the `PORT` environment variable.

### GitHub Pages (Static)

- For a static showcase, copy `index.html` and `static/logo.png` to a `/docs` folder.
- Update image and asset paths to be relative.
- Enable GitHub Pages from the `/docs` folder in repo settings.

## Usage

- Visit `/` for trending books.
- Visit `/recommand` to get recommendations.
- Enter a book title and click "Recommend" for suggestions.

## Contributing

Pull requests and suggestions are welcome! Please open an issue for major changes.

## License

MIT License

## Credits

- [Render.com](https://render.com/)
- [Font Awesome](https://fontawesome.com/)
- [Bootstrap](https://getbootstrap.com/)
- [LottieFiles](https://lottiefiles.com/)

---

**Contact:** [shob0902](https://github.com/shob0902)