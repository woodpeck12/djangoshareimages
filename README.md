###Desc
1. User can load images(linked URL) & Users can flag whether they like or not
- DB: ShareIamge 
    -- user: who created(one to one)
    -- who_like: users who put like(many to many)
    -- ShareImahe override save()
    
- ModelForm: ShareImageCreateForm
    -- method name :  clean_fieldname execute when run is_valid
    -- override modelform save method
3. WOW why didn't tell i need to add below code to create and accept upload file
-   'django.template.context_processors.media',
4. If CERTIFICATE_VERIFY_FAILED error when trying requests-html out on Mac
- pip install --upgrade certifi
- open /Applications/Python\ 3.7/Install\ Certificates.command