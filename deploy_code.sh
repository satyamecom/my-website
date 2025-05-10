#!/usr/bin/bash


PROJECT_DIR="/var/www/html-site"
TMP_DIR="/tmp/html-site"
REPO_URL="https://github.com/satyamecom/my-website.git"

# Clean and clone
rm -rf $TMP_DIR
git clone $REPO_URL $TMP_DIR

# Deploy
sudo cp -r $TMP_DIR/* $PROJECT_DIR/

# Restart Nginx (optional for static content)
sudo systemctl restart nginx
sudo systemctl reload nginx

echo "Deployment complete."
