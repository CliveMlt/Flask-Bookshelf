import os
import fitz
from flask import Flask, render_template, request, redirect, url_for, session, make_response

app = Flask(__name__)
app.secret_key = os.urandom(24)  

@app.route('/')
def index():
    return redirect('/books')

# Dark Mode Toggle
@app.route('/toggle-mode', methods=['GET', 'POST'])
def toggle_mode():
    if request.method == 'POST':
        mode = request.cookies.get('mode', 'light-mode')
        print("Mode before toggle:", mode)
        mode = 'dark-mode' if mode == 'light-mode' else 'light-mode'
        print("Mode after toggle:", mode)
        response = make_response(redirect(url_for('display_books')))
        response.set_cookie('mode', mode)
        return response
    return redirect(url_for('display_books'))

# Bookshelf
@app.route('/books')
def display_books():
    mode = request.cookies.get('mode', 'light-mode')

    try:
        book_list = []
        directory = 'static/images/books'
        for filename in os.listdir(directory):
            if filename.endswith('.pdf'):
                book_id = os.path.splitext(filename)[0]
                cover_image_path = f"images/books/{book_id}.jpg"
                cover_image_full_path = os.path.join(directory, f"{book_id}.jpg")

                # Check if the cover image file exists
                if os.path.isfile(cover_image_full_path):
                    book_list.append({'book_id': book_id, 'cover_image_path': cover_image_path})
                else:
                    # If cover image doesn't exist, generate it
                    generate_cover_image(directory, filename, book_id, cover_image_full_path)
                    book_list.append({'book_id': book_id, 'cover_image_path': cover_image_path})

        return render_template('book_list.html', book_list=book_list, mode=mode)
    except Exception as e:
        # Log the exception
        app.logger.error(f"An error occurred: {str(e)}")
        return "An error occurred while retrieving the book list. Please try again later.", 500

# Cover Image
def generate_cover_image(directory, filename, book_id, cover_image_full_path):
    try:
        # Generate the path to the PDF file
        pdf_path = os.path.join(directory, filename)
        
        # Open the PDF file
        doc = fitz.open(pdf_path)
        
        # Select the first page of the PDF
        page = doc.load_page(0)
        
        # Render the page as an image
        pix = page.get_pixmap()
        
        # Save the image as the cover image
        pix.save(cover_image_full_path)
        
        # Close the PDF file
        doc.close()
    except Exception as e:
        # Log the exception
        app.logger.error(f"An error occurred while generating the cover image: {str(e)}")

@app.route('/books/<book_id>')
def display_book(book_id):
    return render_template('book.html', book_id=book_id)

if __name__ == '__main__':
    app.run(port=8080, threaded=True, debug=False)
