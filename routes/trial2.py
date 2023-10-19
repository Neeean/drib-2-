# This is a simple Python script with a Cross-Site Scripting (XSS) vulnerability

user_input = input("Enter your name: ")

# Vulnerable code - directly rendering user input in HTML without proper encoding
html_output = "<p>Hello, " + user_input + "!</p>"

# In a real application, you should properly encode user input to prevent XSS
# For example, you can use a library like 'html.escape' in Python to encode user input:
# import html
# html_output = "<p>Hello, " + html.escape(user_input) + "!</p>"

# Display the HTML content (for demonstration purposes only, don't actually run this)
print(html_output)
