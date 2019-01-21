docker build -t pyrest:latest .

docker run -d -p 5005:5000 pyrest:latest

Start-Process -FilePath "http://localhost:5005/customers"