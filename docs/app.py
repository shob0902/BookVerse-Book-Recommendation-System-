from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# Get the absolute path to the directory containing app.py
app_dir = os.path.dirname(os.path.abspath(__file__))

# Load the model files using absolute paths
popularDF = pickle.load(open(os.path.join(app_dir, 'popular.pkl'), 'rb'))
pt = pickle.load(open(os.path.join(app_dir, 'pt.pkl'), 'rb'))
book = pickle.load(open(os.path.join(app_dir, 'books.pkl'), 'rb'))
similarity_score = pickle.load(open(os.path.join(app_dir, 'similarity_score.pkl'), 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    # Round up ratings to nearest whole number using ceil
    rounded_ratings = [int(np.ceil(rating)) for rating in popularDF['avg_rating'].values]
    return render_template('index.html',
                           bookName = list(popularDF['Book-Title'].values),
                           bookAuthor = list(popularDF['Book-Author'].values),
                           image = list(popularDF['Image-URL-M'].values),
                           votes = list(popularDF['num_rating'].values),
                           rating = rounded_ratings
                           )

@app.route('/recommand')
def recommand_ui():
    return render_template('recommand.html')

@app.route('/recommand_books', methods=['POST'])
def recommand():
    user_input = request.form.get('user_input')
    
    if not user_input:
        return render_template('recommand.html', error="Please enter a book title")
    
    # Check if the book exists in our dataset
    matching_indices = np.where(pt.index == user_input)[0]
    
    if len(matching_indices) == 0:
        return render_template('recommand.html', error="The book is not recognized in our database")
    
    try:
        index = matching_indices[0]
        similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:7]

        data = []
        for i in similar_items:
            item = []
            temp_df = book[book['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            # Add rating - default to 4 if not available
            try:
                rating = int(np.ceil(float(list(temp_df.drop_duplicates('Book-Title')['avg_rating'].values)[0])))
            except:
                rating = 4  # Default rating if not available
            item.append(rating)

            data.append(item)

        return render_template('recommand.html', data=data)
    
    except Exception as e:
        return render_template('recommand.html', error="Sorry, something went wrong. Please try again.")

if __name__ == '__main__':
    app.run(debug=True)
