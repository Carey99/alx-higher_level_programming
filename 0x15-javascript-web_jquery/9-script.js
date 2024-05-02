// Import jQuery from a CDN
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
script.onload = function() {
    // Fetch the translation from the API
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        // Display the translation in the HTML tag
        $('#hello').text(data.hello);
    });
};
document.head.appendChild(script);
