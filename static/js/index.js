document.addEventListener('DOMContentLoaded', () => {
    const createGroupBtn = document.getElementById('create-group-btn');
    const groupList = document.getElementById('group-list');

    createGroupBtn.addEventListener('click', () => {
        const groupName = prompt('Enter group name:');
        if (groupName) {
            createGroup(groupName);
        }
    });

    function createGroup(groupName) {
        const groups = JSON.parse(localStorage.getItem('groups')) || [];
        groups.push({ name: groupName, members: [] });
        localStorage.setItem('groups', JSON.stringify(groups));
        updateGroupList();
    }

    function updateGroupList() {
        groupList.innerHTML = '';
        const groups = JSON.parse(localStorage.getItem('groups')) || [];
        groups.forEach((group, index) => {
            const li = document.createElement('li');
            li.textContent = group.name;
            li.addEventListener('click', () => {
                localStorage.setItem('currentGroupIndex', index);
                window.location.href = '/group_details/'; // Redirect to group details page
            });
            groupList.appendChild(li);
        });
    }

    updateGroupList();
});
