$.getJSON('https://swapi.co/api/people/5/?format=json', function(data) {
    const text =`${data.name}`;
    $("#character").text(text);
});
