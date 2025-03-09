from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 'description', 'due_date', 'priority', 'urgent', 'assigned_to', 'category'
        ]
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get 'user' from kwargs and remove it
        super().__init__(*args, **kwargs)

        if user:
            # Filter assigned_to to allow selecting the user or their partner
            self.fields['assigned_to'].queryset = user.__class__.objects.filter(id__in=[user.id])
            # Set all categories for the category field
            self.fields['category'].queryset = Category.objects.all()
