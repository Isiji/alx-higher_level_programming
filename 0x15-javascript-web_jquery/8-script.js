$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $('UL#list_movies').text(data.results.map(film => `<li>${film.title}</li>`).join(''));
})