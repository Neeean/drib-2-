# This is a simple Python script with a SQL injection vulnerability

user_input = input("Enter your username: ")

# Vulnerable code - directly including user input in an SQL query
query = "SELECT * FROM users WHERE username = '" + user_input + "';"

# Execute the SQL query (for demonstration purposes only, don't actually run this)
# In a real application, you should use parameterized queries to prevent SQL injection
# connection.execute(query)
