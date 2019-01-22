docker build -t pyrest:latest .

docker run -d -p 8305:5000 pyrest:latest

Start-Process -FilePath "http://localhost:8305/customers"