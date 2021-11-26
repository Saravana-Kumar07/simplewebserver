from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body bgcolor='black'>
<h1>
<font face='arial'color='yellow'>
TOP FIVE PROGRAMMING LANGUAGES:
</font></h1>
<font size='5'face='jester'color='white'>
1.<b>PYTHON: </b>Python is an interpreted high-level general-purpose programming language. It works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc)<p>
2.<b>JAVASCRIPT: </b>JavaScript (js) is a light-weight object-oriented programming language which is used by several websites for scripting the webpages.<p>
3.<b>JAVA: </b>Java is a high-level, class-based, object-oriented programming language designed to have as few implementation dependencies as possible.<p>
4.<b>C#: </b>C# is a general-purpose, multi-paradigm programming language. It is an object-oriented programming language created by Microsoft that runs on the .NET Framework<p>
5.<b>C++: </b>C++ is an enhanced C language typically used for object oriented programming. It is a low level programming language and widely used in the software development field.<p>
</font>
</body>
</html>
"""
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
httpd.serve_forever()

