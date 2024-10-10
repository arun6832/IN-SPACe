from django.urls import path
from Expense_splitter_app.views import create_group, view_groups, split_expenses,index

urlpatterns = [
        path('', index, name='index'),  
    path('create_group/', create_group, name='create_group'),
    path('view_groups/', view_groups, name='view_groups'),
    path('split_expenses/<int:group_id>/', split_expenses, name='split_expenses'),
]
