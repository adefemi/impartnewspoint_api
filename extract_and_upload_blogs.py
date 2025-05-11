import os
import django
import json
import cloudinary
import cloudinary.uploader
# from datetime import date, datetime # No longer needed with serializer

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_api.settings')
django.setup()

from blog.models import Blog
from blog.serializer import BlogSerializer # Import the serializer

def main():
    # Ensure Cloudinary is configured
    # Credentials should be set via DJANGO_SETTINGS_MODULE and settings.CLOUDINARY_STORAGE
    # or environment variables CLOUDINARY_URL
    # cloudinary.config() will be called automatically by django-cloudinary-storage
    # based on settings.CLOUDINARY_STORAGE
    
    print("Fetching blog posts from the database...")
    blogs = Blog.objects.all()
    
    print("Serializing blog posts using BlogSerializer...")
    # When using serializers with querysets (many=True), 
    # you need to pass the request context if your serializer uses it (e.g., for HyperlinkedRelatedField).
    # For basic ModelSerializer usage like this, it's often not strictly necessary for read-only operations.
    # However, it's good practice if the serializer might evolve to need it.
    # For a standalone script, a mock request or None context might be needed if the serializer is complex.
    # Given the current BlogSerializer, direct instantiation should work.
    serializer = BlogSerializer(blogs, many=True)
    blogs_data = serializer.data

    json_file_path = 'blogs_export.json'
    print(f"Serializing {len(blogs_data)} blog posts to {json_file_path}...") # This message is slightly redundant now
    with open(json_file_path, 'w') as f:
        json.dump(blogs_data, f, indent=4) # No longer need custom default serializer
    
    print(f"Successfully wrote blog data to {json_file_path}")

    # Upload to Cloudinary
    print(f"Uploading {json_file_path} to Cloudinary...")
    try:
        upload_options = {
            'resource_type': 'raw',
            'public_id': f'blog_exports/{os.path.basename(json_file_path)}', 
            'overwrite': True
        }
        result = cloudinary.uploader.upload(json_file_path, **upload_options)
        print(f"Successfully uploaded to Cloudinary.")
        print(f"Cloudinary URL: {result.get('secure_url') or result.get('url')}")
        
        os.remove(json_file_path)
        print(f"Removed local file: {json_file_path}")
        
    except Exception as e:
        print(f"Error uploading to Cloudinary: {e}")
        print("Please ensure your Cloudinary credentials (CLOUD_NAME, API_KEY, API_SECRET) are correctly set in your environment or Django settings.")

if __name__ == '__main__':
    main() 