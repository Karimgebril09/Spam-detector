document.getElementById('submitButton').addEventListener('click', function () {
    const text = document.getElementById('textInput').value;

    const apiUrl = 'http://localhost:8000/predict';

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text }),
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        if (data.prediction === 'SPAM') {
            resultDiv.textContent = 'This is SPAM!';
            resultDiv.style.color = 'red';
            document.body.style.backgroundColor = 'red'; // Light red background
        } else if (data.prediction === 'HAM') {
            resultDiv.textContent = 'This is HAM!';
            resultDiv.style.color = 'green';
            document.body.style.backgroundColor = '#ccffcc'; // Light green background
        } else {
            resultDiv.textContent = 'Error: Unable to classify.';
            resultDiv.style.color = 'black';
            document.body.style.backgroundColor = '#f4f4f4'; // Reset to default background
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').textContent = 'Error: Unable to connect to the server.';
        document.body.style.backgroundColor = '#f4f4f4'; // Reset to default background
    });
});