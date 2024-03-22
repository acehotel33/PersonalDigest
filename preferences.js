document.getElementById('preferencesForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Clear previous error message
    document.getElementById('errorMessage').textContent = '';

    const topics = document.getElementById('topics').value;
    const email = document.getElementById('email').value;

    // Log the email input for debugging
    console.log('Email input:', email);

    // Email validation regex pattern, slightly adjusted for clarity
    const emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    // Check if the email matches the pattern
    if (!emailPattern.test(email)) {
        // Log for debugging
        console.log('Invalid email format');
        document.getElementById('errorMessage').textContent = 'Please enter a valid email address.';
        return; // Stop the function if the email is invalid
    }

    // Proceed if email is valid
    console.log('Proceeding with valid email');

    const preferences = {
        topics: topics.split(',').map(topic => topic.trim()),
        email: email
    };

    fetch('http://127.0.0.1:5000/api/preferences', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(preferences),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('Preferences saved!');
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('errorMessage').textContent = 'An error occurred while saving preferences.';
    });
});
