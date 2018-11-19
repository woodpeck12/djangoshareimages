###Desc
1. User can load images(linked URL) & Users can flag whether they like or not
- DB: ShareIamge 
    a) user: who created(one to one)
    b) who_like: users who put like(many to many)
    c) ShareImahe override save()
    
- ModelForm: ShareImageCreateForm
    a) method name :  clean_fieldname execute when run is_valid
    b) override modelform save method
3. WOW why didn't tell i need to add below code to create and accept upload file
-   'django.template.context_processors.media',
