document.addEventListener('DOMContentLoaded', () => {
    const groupNameSpan = document.getElementById('group-name');
    const membersList = document.getElementById('members-list');
    const addMemberBtn = document.getElementById('add-member-btn');
    const totalAmountInput = document.getElementById('total-amount');
    const setAmountBtn = document.getElementById('set-amount-btn');
    const expenseSummary = document.getElementById('expense-summary');

    const groups = JSON.parse(localStorage.getItem('groups')) || [];
    const currentGroupIndex = localStorage.getItem('currentGroupIndex');
    const currentGroup = groups[currentGroupIndex];

    groupNameSpan.textContent = currentGroup.name;

    // Load existing members
    currentGroup.members.forEach(member => {
        addMemberToList(member);
    });

    addMemberBtn.addEventListener('click', () => {
        const memberName = document.getElementById('member-name').value;
        if (memberName) {
            currentGroup.members.push(memberName);
            groups[currentGroupIndex].members = currentGroup.members; // Update local storage
            localStorage.setItem('groups', JSON.stringify(groups));
            addMemberToList(memberName);
            document.getElementById('member-name').value = '';
        }
    });

    setAmountBtn.addEventListener('click', () => {
        const totalAmount = parseFloat(totalAmountInput.value);
        if (!isNaN(totalAmount) && currentGroup.members.length > 0) {
            const equalSplit = totalAmount / currentGroup.members.length;
            displayExpenseSummary(equalSplit);
        }
    });

    function addMemberToList(member) {
        const li = document.createElement('li');
        li.textContent = member;
        membersList.appendChild(li);
    }

    function displayExpenseSummary(equalSplit) {
        expenseSummary.innerHTML = '';
        currentGroup.members.forEach(member => {
            const li = document.createElement('li');
            li.innerHTML = `${member}: <input type="number" class="custom-amount" value="${equalSplit}" style="width: 80px;">`;
            expenseSummary.appendChild(li);
        });
    }
});
