import os # Importing os(OS module allows us to create a "build" directory)
import re # Importing re(regular expression module allows us to create file names from the Title)

# Slug function.
def slugify(title):
    """Convert the page title to a filename-friendly slug."""
    if title.lower() == "home":  # Check if the title is 'Home' and assign it 'index.html' to designate it as the homepage.
        return "index.html"
    # Use regular expressions to replace non-word characters with hyphens and return the filename with ".html" extension.
    return re.sub(r'\W+', '-', title.strip().lower()) + ".html"

# Nav function.
def generate_nav(titles, active_title):
    """Generate a dynamic navigation bar with an active page highlight."""
    nav_links = ""  # Initialize an empty string to store HTML navigation links.
    for title in titles:  # Loop through each title in the list.
        filename = slugify(title)  # Convert each title to a filename using the slugify function.
        active_class = ' class="active"' if title == active_title else ""  # Apply an "active" class if the title matches the active page.
        # Create a navigation link for each title, marking it active if it's the current page.
        nav_links += f'\t\t\t<a href="{filename}"{active_class}>{title}</a>\n'
    return nav_links.strip()  # Remove any extra whitespace from the final navigation link string.

# HTML function. (OUT PUT SHOE DIRECTORY)
def create_html_file(title, titles, output_dir="build"):
    """Generate and write HTML content based on the page title."""
    filename = slugify(title)  # Convert the title to a slugified filename.
    nav = generate_nav(titles, active_title=title)  # Generate navigation links with the current title marked as active.

    # Define the HTML content structure with placeholders for title, navigation, and page content.
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <nav>
            {nav}
        </nav>
        <div class="content">
            <h1>{title}</h1>
            <p>This is the {title.lower()} content.</p>
        </div>
    </body>
    </html>
    """

    output_path = os.path.join(output_dir, filename)  # Define the path for saving the HTML file in the output directory.
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists, creating it if necessary.

    # Write the generated HTML content to the file at the specified path.
    with open(output_path, 'w') as file:
        file.write(html_content)

    print(f"Created {filename} in the '{output_dir}' directory.")   


# Main function.
def main():
    """Main function to generate pages and styles. MUST HAVE HOME!!!"""
    titles = ["Home", "About Us", "Used Shoes", "Clearance Shoes"]   # List of titles for the pages to be generated.

    # Loop to create an HTML file for each title in the list.
    for title in titles:
        create_html_file(title, titles)

    # Create the style.css file
    #create_css_file() 
    # uncomment the create_css_file() function if you add the function.

# Run the main function if this script is executed as the main program.
if __name__ == "__main__":
    main()