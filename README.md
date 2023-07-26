# Flask-Bookshelf
 
This is a simple Flask web application that serves as a bookshelf. It allows users to view a list of books (in PDF format) and automatically creates cover images.

# Usage
Upon accessing the web application, you will be redirected to the book list page (/books), which displays the available books with their cover images.

Click on a book's cover image to view its individual book page (/books/<book_id>). However, please note that the provided code only renders a template with the book_id as a placeholder. You can customize this page to display book details, content, or any other relevant information.

To switch between light and dark modes, click on the "Toggle Mode" button located on the top right corner of the book list page. The mode will be remembered through cookies, so your preference will persist across sessions.

# Adding Books
To add new books to the bookshelf, place the PDF files in the static/images/books directory.

The application will automatically generate cover images for new books in case they don't already have one. Cover images are saved as JPEG files with the same name as the corresponding PDF file.

# Disclaimer
This project is for educational and demonstrative purposes only. It does not include full-fledged book reading functionality or advanced features typically found in commercial bookshelf applications.
