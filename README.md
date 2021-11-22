# Developing a Simple Webserver
## AIM:
To develop a simple webserver that display top five programming languages.

## DESIGN STEPS: 
### Step 1: 
HTML content creation
### Step 2:
Design of webserver workflow
### Step 3:
Implementation using Python code
### Step 4:
Serving the HTML
### Step 5:
Testing the webserver

## PROGRAM:
''' from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<h1>TOP FIVE PROGRAMMING LANGUAGES:</h1>
1.Python<p>
2.Javascript<p>
3.Java<p>
4.C#<p>
5.C++<p>
</body>
</html>
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ("",80)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever() '''



## OUTPUT:


## RESULT:
