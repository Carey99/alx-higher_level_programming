// Include jQuery library
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
document.head.appendChild(script);

// Fetch movies data
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    // Create a new unordered list element
    var ul = $('<ul id="list_movies"></ul>');

    // Iterate over each movie and append its title to the list
    $.each(data.results, function(index, movie) {
        var li = $('<li></li>').text(movie.title);
        ul.append(li);
    });

    // Append the list to the body of the HTML document
    $('body').append(ul);
});
