function generateRandomID() {
    return Math.floor(Math.random() * 90000) + 10000;
}


function addUser(event) {
    event.preventDefault();

    // Get the input values
    const name = document.getElementById("name").value;

    // generate random ID
    const s_nom = generateRandomID();

    // create data json object with name and random ID
    const data = {
        name: name,
        id: s_nom,
    }

    // send the data json object to the backend using http request
    fetch('/add_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        // handle response from the backend if needed
        console.log(result);
    })
    .catch(error => {
        // handle any errors that occur during the request
        console.error('Error:', error);
    });
}

document.getElementById("add-user-form").addEventListener("submit", addUser);