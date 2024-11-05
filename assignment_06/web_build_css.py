import os # Importing os(OS module allows us to create a "build" directory)
import re # Importing re(regular expression module allows us to create file names from the Title)

# Slug function.
def slugify(title):
    """Convert the page title to a filename-friendly slug."""
    if title.lower() == "home":  # If the title is 'Home', make it 'index.html' for easy homepage access.
        return "index.html"
    # Replace non-word characters (anything other than letters, numbers, and underscores) with hyphens to create a filename.
    return re.sub(r'\W+', '-', title.strip().lower()) + ".html"

# Nav function.
def generate_nav(titles, active_title):
    """Generate a dynamic navigation bar with an active page highlight."""
    nav_links = ""   # Initialize an empty string to store HTML links.
    for title in titles:  # Loop through each title in the provided list.
        filename = slugify(title)   # Convert the title to a filename-friendly slug.
        active_class = ' class="active"' if title == active_title else ""   # Add an "active" class if this is the current page.
        # Create an HTML link for the title, marking it active if it matches the active title.
        nav_links += f'\t\t\t<a href="{filename}"{active_class}>{title}</a>\n'
    return nav_links.strip()   # Remove any extra whitespace from the final nav link string.

# HTML function. (OUT PUT SHOE DIRECTORY)
def create_html_file(title, titles, output_dir="build"):
    """Generate and write HTML content based on the page title."""
    filename = slugify(title)   # Convert the title to a slug filename.
    nav = generate_nav(titles, active_title=title)   # Generate the navigation HTML with the current title as active.

    # Define the HTML content with placeholders for title, nav, and content.
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

    output_path = os.path.join(output_dir, filename)   # Set the path for saving the HTML file.
    os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't already exist.
    
    # Write the generated HTML content to the file.
    with open(output_path, 'w') as file:
        file.write(html_content)

    print(f"Created {filename} in the '{output_dir}' directory.")   # Confirm the file creation.

# Create CSS function.
def create_css_file(output_dir="build"):
    """Generate and write the style.css file based on a dictionary of styles."""
    # Dictionary to define styles for various elements.
    styles = {
        "font-family": "Calibri",             # Font family for the page text.
        "body-background": "#7BAFD4",         # Background color for the body.
        "nav-background": "#13294B",          # Background color for the navigation bar.
        "nav-a-color": "#4B9CD3",             # Text color for navigation links.
        "nav-a-active-color": "#ffffff"       # Text color for the active link in navigation.
        
    }

# This is dictionary
    # Define CSS content using the styles defined in the dictionary. {{ }}: double bricket - escape, 
    css_content = f"""
    * {{ 
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: {styles["font-family"]};
    }}

    body {{
        background-color: {styles["body-background"]};
    }}

    nav {{
        background-color: {styles["nav-background"]};
        padding: 10px;
    }}

    nav a {{
        color: {styles["nav-a-color"]};
        margin-right: 10px;
        text-decoration: none;
    }}

    nav a.active {{
        color: {styles["nav-a-active-color"]};
        font-weight: bold;
    }}

    .content {{
        background-color: #F8F8F8;
        padding: 20px;
        margin: 20px;
    }}
    """

    css_path = os.path.join(output_dir, "style.css")   # Set the path for saving the CSS file.
    # Write the generated CSS content to the file.
    with open(css_path, 'w') as file:
        file.write(css_content)

    print(f"Created style.css in the '{output_dir}' directory.")   # Confirm the file creation.

# Main function.
def main():
    """Main function to generate pages and styles. MUST HAVE HOME!!!"""
    titles = ["Home", "About Us", "Used Shoes", "Clearance Shoes"]   # Define the page titles.

    # Loop to create an HTML file for each title.
    for title in titles:
        create_html_file(title, titles)   # Generate an HTML file for the current title.

    # Create the CSS file.
    create_css_file()  # Generate the CSS file.

# Execute the main function if the script is run directly.
if __name__ == "__main__":
    main()



