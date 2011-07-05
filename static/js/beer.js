var lastBeerStyle;
var lastBrewery;

$(document).ready(function(){    
    initAutoCompleteField('#id_brewery_auto', '#id_brewery', '/venues/search/json', 'name', 2, lastBrewery);
    initAutoCompleteField('#id_style_auto', '#id_style', '/beer/styles/search/json', 'name', 2, lastBeerStyle);
})
