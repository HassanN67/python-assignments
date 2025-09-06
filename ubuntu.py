import os
import requests
from urllib.parse import urlparse, unquote
from pathlib import Path
import datetime

def create_directory(directory_name):
    """Create directory if it doesn't exist"""
    try:
        os.makedirs(directory_name, exist_ok=True)
        print(f"Directory '{directory_name}' is ready.")
        return True
    except OSError as e:
        print(f"Error creating directory: {e}")
        return False

def extract_filename(url, content_type=None):
    """Extract filename from URL or generate one based on content"""
    # Try to get filename from URL
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)
    filename = os.path.basename(path)
    
    # If no filename in URL or it's too generic, generate one
    if not filename or '.' not in filename or len(filename) < 3:
        # Get current timestamp for unique filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Determine extension from content type if available
        if content_type and 'image/' in content_type:
            ext = content_type.split('/')[1]
            # Handle some common content types that might have parameters
            if ';' in ext:
                ext = ext.split(';')[0]
            # Handle jpeg which often comes as jpg
            if ext == 'jpeg':
                ext = 'jpg'
            filename = f"image_{timestamp}.{ext}"
        else:
            # Fallback if we can't determine the type
            filename = f"image_{timestamp}.jpg"
    
    return filename

def download_image(url, directory="Fetched_Images"):
    """Download an image from a URL and save it to the specified directory"""
    try:
        # Send GET request with timeout and proper headers
        headers = {
            'User-Agent': 'UbuntuImageFetcher/1.0 (Community Image Collector)'
        }
        response = requests.get(url, headers=headers, timeout=10, stream=True)
        
        # Check if request was successful
        response.raise_for_status()
        
        # Determine content type
        content_type = response.headers.get('content-type', '')
        if not content_type.startswith('image/'):
            print("Warning: The URL does not point to an image content type.")
            # We'll proceed anyway as sometimes servers don't set proper content-type
        
        # Extract or generate filename
        filename = extract_filename(url, content_type)
        filepath = os.path.join(directory, filename)
        
        # Check if file already exists and modify filename if needed
        counter = 1
        base, ext = os.path.splitext(filename)
        while os.path.exists(filepath):
            filepath = os.path.join(directory, f"{base}_{counter}{ext}")
            counter += 1
        
        # Save the image
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"Successfully downloaded: {filename}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return False
    except IOError as e:
        print(f"Error saving image: {e}")
        return False

def main():
    """Main function to run the Ubuntu Image Fetcher"""
    print("=" * 50)
    print("Ubuntu Image Fetcher: I am because we are")
    print("=" * 50)
    print("This tool helps you respectfully fetch and organize")
    print("images from the global community of the internet.")
    print("=" * 50)
    
    # Create directory for images
    directory = "Fetched_Images"
    if not create_directory(directory):
        return
    
    # Prompt user for URL
    url = input("Please enter the image URL: ").strip()
    
    if not url:
        print("No URL provided. Exiting.")
        return
    
    # Validate URL format
    if not url.startswith(('http://', 'https://')):
        print("Invalid URL format. Please include http:// or https://")
        return
    
    # Download the image
    print(f"Attempting to download from: {url}")
    success = download_image(url, directory)
    
    if success:
        print("Download completed successfully!")
        print("The image has been saved to the 'Fetched_Images' directory.")
        print("Thank you for participating in our community.")
    else:
        print("Download failed. Please check the URL and try again.")

if __name__ == "__main__":
    main()