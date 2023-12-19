from http.server import SimpleHTTPRequestHandler, HTTPServer, BaseHTTPRequestHandler
from jinja2 import Template, Environment, FileSystemLoader, PackageLoader, select_autoescape


# file_loader = FileSystemLoader('cleaningcompany')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('basis.html')
# msg = tm.render()
#
# print(msg)

class CustomHandler(SimpleHTTPRequestHandler):
    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )

    def do_GET(self):
        if self.path.startswith('/media/'):
            super().do_GET()
        elif self.path == '/':
            self.render_index()
        elif self.path == '/index/':
            self.render_index()
        elif self.path == '/contact/':
            self.render_contact()
        elif self.path == '/about/':
            self.render_about()
        elif self.path == '/blog/':
            self.render_blog()
        elif self.path == '/blog-single/':
            self.render_blog_single()
        elif self.path == '/portfolio/':
            self.render_portfolio()
        elif self.path == '/pricing/':
            self.render_pricing()
        elif self.path == '/services/':
            self.render_services()

    def render_index(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        body = self.env.get_template('index.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_contact(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        body = self.env.get_template('contact.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_about(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        body = self.env.get_template('about.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))


    def render_blog(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        body = self.env.get_template('blog.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_blog_single(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        body = self.env.get_template('blog-single.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))


    def render_portfolio(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        body = self.env.get_template('portfolio.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_pricing(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        body = self.env.get_template('pricing.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_services(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        body = self.env.get_template('services.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))



def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Create table')
    print('Server starting')
    httpd.serve_forever()


if __name__ == '__main__':
    run(handler_class=CustomHandler)