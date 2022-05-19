from django import forms
from .models import Person, Post#import the Post model from polls/models.py

class ContactForm(forms.Form):
      name = forms.CharField(required=False, label = "Your name")
      email = forms.EmailField(
          label="Your email", 
          help_text='Must contain al least 8 characters', 
          min_length=8,
          error_messages={'required': 'Please enter a valid email address'})  
      comment = forms.CharField()


class PersonForm(forms.ModelForm):
    class Meta:      
        model = Person
        fields = '__all__'
    
    def save(self, commit=True): 
        obj = super().save(commit=False)
        # do you logic here for example:
        
        latest_id = Person.objects.latest('id').id
        available_id = latest_id + 1 

        if commit:
            # Saving your obj
            obj.id = available_id
            obj.save()
        return obj


class PostForm(forms.ModelForm):
    class Meta:      
        model = Post
        exclude = ['released_date']
        # we can add some widget : here helper class to display the form in the template
        widgets = {
            'text': forms.Textarea(attrs={'class': 'textarea'}),
            'author': forms.Select(attrs={'class': 'select'})
        }