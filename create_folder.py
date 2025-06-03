from supabase import create_client

# Initialize Supabase client with your URL and key
supabase_url = 'https://rsquvjyzomaqtogxfetb.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJzcXV2anl6b21hcXRvZ3hmZXRiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDg5NDY2MjcsImV4cCI6MjA2NDUyMjYyN30.6mfPnySk1-1e9_6z4kSAZApjCKS8nqwbGiYV6nXVjgU'
supabase = create_client(supabase_url, supabase_key)

# Read the empty file
with open('assignments_folder_marker.txt', 'rb') as f:
    file_content = f.read()

# Upload to create the assignments folder
file_path = "assignments/.keep"
try:
    # Upload to Supabase Storage
    result = supabase.storage.from_('student-documents').upload(file_path, file_content)
    
    if hasattr(result, 'error') and result.error:
        print(f"Upload error: {result.error}")
    else:
        # Get public URL
        file_url = supabase.storage.from_('student-documents').get_public_url(file_path)
        print(f"Folder created successfully. URL: {file_url}")
except Exception as e:
    print(f"Exception during upload: {e}") 