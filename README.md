# BookVerse - Intelligent Book Recommendation System

BookVerse is a modern, AI-powered book recommendation system that helps users discover their next great read. Built with Flask and powered by collaborative filtering algorithms, it provides personalized book recommendations based on user preferences and reading patterns.

![BookVerse Interface](Dataset/classicRec.png)

## Features

- **Personalized Recommendations**: Get book suggestions based on your reading preferences
- **Trending Books**: Discover the top 50 most acclaimed books
- **Smart Search**: Find books easily with intelligent search functionality
- **Rating System**: View book ratings and user feedback
- **Responsive Design**: Seamless experience across all devices
- **Modern UI**: Clean, intuitive interface with smooth animations

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Processing**: NumPy, Pandas
- **Machine Learning**: Scikit-learn (Collaborative Filtering)
- **Database**: Pickle for data storage
- **UI Framework**: Bootstrap 5.3.7
- **Icons**: Font Awesome 6.0.0

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shob0902/BookVerse.git
   cd BookVerse
   ```

2. Install dependencies:
   ```bash
   pip install flask numpy pandas scikit-learn
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
BookVerse/
│
├── app.py                 # Flask application main file
├── one.ipynb             # Jupyter notebook with data processing
├── Dataset/              # Dataset files
│   ├── Books.csv        # Books information
│   ├── Ratings.csv      # User ratings data
│   └── Users.csv        # User information
│
├── static/              # Static files
│   └── logo.png        # Website logo
│
├── templates/           # HTML templates
│   ├── index.html      # Home page
│   └── recommand.html  # Recommendation page
│
└── *.pkl               # Processed data files
```

## How It Works

1. **Data Processing**:
   - Processes book ratings and user data
   - Calculates popularity scores
   - Implements collaborative filtering

2. **Recommendation System**:
   - Uses cosine similarity for book recommendations
   - Considers user ratings and book popularity
   - Provides personalized suggestions

3. **User Interface**:
   - Clean and intuitive design
   - Responsive layout
   - Interactive elements with smooth animations

## API Endpoints

- `/` - Home page with trending books
- `/recommand` - Book recommendation interface
- `/recommand_books` - POST endpoint for getting book recommendations

## Future Enhancements

- User authentication system
- Personal reading lists
- Social sharing features
- Advanced filtering options
- Reading history tracking

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Credits

- Book dataset provided by Goodreads
- UI design inspired by modern web practices
- Special thanks to all contributors

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Developed by Shobhit Negi
- Twitter: [@gaurav__dadhich](https://x.com/gaurav__dadhich)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/gdadhich-5025aa252)

---

⭐ Star us on GitHub if you like this project!
