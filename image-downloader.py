import os
import requests

def download_images():
    # Create 'downloads' folder if it doesn't exist
    os.makedirs("downloads", exist_ok=True)
    
    base_url = "https://targetwebsite.com/wp-content/uploads/2025/03/"
    
    for i in range(1, 21):
        # Construct image URL
        url = f"{base_url}{i}.png"
        
        try:
            # Send request to download the image
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Raise error for bad responses
            
            # Save the file to 'downloads' folder
            filename = os.path.join("downloads", f"{i}.png")
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            
            print(f"{i}.png downloaded successfully.")
            
        except Exception as e:
            print(f"Error downloading {i}.png: {str(e)}")

if __name__ == "__main__":
    download_images()
