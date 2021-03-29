"""Driver for Web server"""
from view import app

if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.196', port='8080')