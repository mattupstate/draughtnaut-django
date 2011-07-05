var lastBeerSelection;
var defaultText = $('#id_beer_auto').val();
var listItemTemplate = '<li id="beer-%id%"><a href="/beer/%id%">%name%</a> <button>X</button></li>';
var ac = $('#id_beer_auto');
var venueId = $('#venue-id').text();
console.log(venueId)
/*
function removeBtnHandler(event) {
  var beerId = $(this).parent().attr('id').replace('beer-',''); 
  $.post('/venue/beer/remove"/>', {beer:beerId, venue:venueId}, handleRemoveBeer, "json");
}
function handleAddBeer(data) {
  var str = listItemTemplate.replace(/%id%/g, data.id).replace(/%name%/g, data.name);
  var node = $('#beer-list').append(str);
  var btn = node.find('#beer-'+data.id+' button');
  btn.button();
  btn.click(removeBtnHandler);
  clearAutoComplete();
}
function handleAddBeerError() {
  alert('Venue is already serving ' + $('#beer-autocomplete').val());
  clearAutoComplete();
}
function handleRemoveBeer(data) {
  $('#beer-list #beer-'+data.id).remove();
}
function handleRemoveBeerError() {
  
}
function resetAutoComplete() {
  ac.val(defaultText);
}
function clearAutoComplete() {
  ac.val('');
}
ac.focusin(clearAutoComplete);
ac.focusout(resetAutoComplete);
ac.autocomplete({
  source: function( request, response ) {
    $.ajax({
      url: '<c:url value="/beer/search/json?name="/>'+request.term,
      success: function( data ) {
        response( $.map( data, function( item ) {
          return {
            id:item.id,
            label: item.name,
            value: item.name
          }
        }));
      }
    });
  },
  select: function( event, ui ) {
    if(ui.item) {
      $.post('<c:url value="/venue/"/>${venue.id}/beer/add',{id:ui.item.id},handleAddBeer,'json');
    }
  },
  minLength: 2
});

var btns = $('#beer-list button');
btns.button();
btns.bind('click', removeBtnHandler);
$('html .ui-autocomplete').css('max-height', '200px');
$('html .ui-autocomplete').css('overflow-y', 'auto');
*/