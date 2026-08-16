# Start from an official, lightweight Python 3.12 base image.
# "slim" means it excludes extra OS packages we don't need, keeping the image small.
FROM python:3.12-slim

# Set the working directory inside the container.
# All following commands (COPY, RUN, CMD) happen relative to this path.
WORKDIR /app

# Copy ONLY requirements.txt first (not the whole project yet).
# This is a deliberate optimization: Docker caches each step. If requirements.txt
# hasn't changed, Docker reuses the cached "pip install" layer instead of
# reinstalling every dependency every single build — much faster rebuilds.
COPY requirements.txt .

# Install dependencies. --no-cache-dir keeps the image smaller by not storing
# pip's download cache inside the image.
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application code into the container.
COPY . .

# Documentation only — tells humans/tools which port the app uses.
# This does NOT actually publish the port; that happens with `docker run -p`.
EXPOSE 5000

# The command that runs when the container starts.
CMD ["python", "app.py"]
