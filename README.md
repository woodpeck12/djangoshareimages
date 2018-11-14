###Desc
1. User can load images(linked URL) & Users can flag whether they like or not
- DB: ShareIamge - user: who created(one to one), who_like: users who put like(many to many)
2. override modelFrom save method
3. WOW why didn't tell i need to add below code to create and accept upload file
-   'django.template.context_processors.media',
