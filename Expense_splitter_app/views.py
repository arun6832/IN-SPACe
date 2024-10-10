from django.shortcuts import render, redirect, get_object_or_404
from .models import Group, Member, Split

def index(request):
    return render(request, 'index.html')

def create_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        member_names = request.POST.get('member_names')

        if group_name and member_names:  # Ensure both fields are provided
            group = Group.objects.create(name=group_name)
            for name in member_names.split(','):
                Member.objects.create(name=name.strip(), group=group)

            return redirect('view_groups')

    return render(request, 'create_group.html')


def view_groups(request):
    groups = Group.objects.all()
    return render(request, 'view_groups.html', {'groups': groups})


def split_expenses(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == 'POST':
        total_amount = float(request.POST.get('total_amount'))
        split_method = request.POST.get('split_method')

        split = Split.objects.create(group=group, total_amount=total_amount)

        if split_method == 'equal':
            amount_per_member = total_amount / group.members.count()
            for member in group.members.all():
                member.amount += amount_per_member
                member.save()

        elif split_method == 'custom':
            for member in group.members.all():
                member.amount = float(request.POST.get(f'amount_{member.id}', 0))
                member.save()

        elif split_method == 'checkbox':
            for member in group.members.all():
                if request.POST.get(f'checkbox_{member.id}'):
                    member.amount = total_amount
                else:
                    member.amount = 0
                member.save()

        return redirect('group_view', group_id=group_id)

    return render(request, 'split_expense.html', {'group': group})
