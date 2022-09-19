$(function()
{
	$.get("https://swapi-api.hbtn.io/api/films/?format=json", function(response)
	{
        for (let index in response.results){
		    $('UL#list_movies').append('<li>' + response.results[index].title + '</li>')
        }
	});
});