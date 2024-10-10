document.addEventListener("DOMContentLoaded", function() {
    const memberNameInput = document.getElementById('member-name');
    const memberAmountInput = document.getElementById('member-amount');
    const membersList = document.getElementById('members-list');

    document.getElementById('add-member').addEventListener('click', function() {
        const memberName = memberNameInput.value;
        const memberAmount = memberAmountInput.value;

        if (memberName && memberAmount) {
            const li = document.createElement('li');
            li.textContent = `${memberName}: Rs ${memberAmount}`;
            membersList.appendChild(li);

            // Clear the input fields
            memberNameInput.value = "";
            memberAmountInput.value = "";
        }
    });
});
