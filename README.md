# Simple Data Handler File Servers

Simple HTTP Web Servers in a couple of different programming languages to handle POST requests mostly (Receive Data).

Notes: 
For HTTP Tunneling use [Neo-reGeorg](https://github.com/L-codes/Neo-reGeorg/blob/master/README-en.md
This extremely simple web servers are not designed for security. Authentication is not secure, and were built for testing purposes in a sandbox, as part of another project/research.

- [Flask Upload Server with authentication](flask/app.py) (Uses basic authentication. Can Upload and Download files)
- [Php simple Upload server](php/app.php) (No authentication. Can only receive files)

- HTTPS: Additionally, instructions for setting up a self-signed SSL cert in Apache found in this [blog by Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-18-04)
