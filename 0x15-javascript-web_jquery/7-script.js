// Include jQuery library
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

// Fetch character name from the URL
$.getJSON("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
    // Display character name in the HTML tag
    $("#character").text(data.name);
});
