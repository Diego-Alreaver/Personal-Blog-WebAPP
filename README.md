# personal_blog

## Project Overview

The blog is divided into two main sections:

### Guest Section
- **Home Page**: This page showcases a list of all published articles, allowing anyone to explore my writings.
- **Article Page**: Here, readers can view the content of each article along with its publication date.

### Admin Section
This section is restricted to me (admin), allowing for article management:
- **Dashboard**: Displays all published articles with options to add new ones, edit existing articles, or delete them.
- **Add Article Page**: Features a form where I can enter a new article's title, content, and publication date.
- **Edit Article Page**: Similar to the add page, but for updating existing articles.
- **Delete Article Page**: Deletes any article that we didn't like.

- ### Authentication
For the admin section, I implemented authentication using Django's built-in features. I employed the `@login_required` decorator to ensure that only authorized users can access the admin pages, providing a secure way to manage the articles.

- ### Front page

![image](https://github.com/user-attachments/assets/6ad07335-f710-43ed-b1c6-0770a6e294e6)
