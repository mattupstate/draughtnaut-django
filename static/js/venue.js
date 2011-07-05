var lastBeerSelection;
var defaultText = $('#beer-autocomplete').val();
var listItemTemplate = '<li id="beer-%id%"><a href="/beer/%id%">%name%</a> [<span class="remove-ontap"><a href="javascript:void(0)">remove</a></span>]</li>';
var ac = $('#beer-autocomplete');
var venueId = $('#venue-id').text();
var csrfToken = $('#csrf-token').text()

function removeBtnHandler(event) {
  var ontapId = $(this).parent().attr('id').replace('beer-',''); 
  $.post('/venues/beer/remove/', { id:ontapId, csrfmiddlewaretoken:csrfToken }, handleRemoveBeer, "json");
}
function handleAddBeer(data) {
  if(data.error) {
    alert(data.error);
    clearAutoComplete();
    return;
  }
  var str = listItemTemplate.replace(/%id%/g, data.id).replace(/%name%/g, data.name);
  $('#beer-list').append(str);
  clearAutoComplete();
}
function handleRemoveBeer(data) {
  if(data.error) {
    return;
  }
  $('#beer-list #beer-'+data.id).remove();
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
      url: '/beer/search/json/?name='+request.term,
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
      $.post(
        '/venues/beer/add/',
        {venue_id:venueId, beer_id:ui.item.id, csrfmiddlewaretoken:csrfToken}, 
        handleAddBeer, 
        'json'
      );
    }
  },
  minLength: 2
});

$('.remove-ontap').live('click', removeBtnHandler);
$('html .ui-autocomplete').css('max-height', '200px');
$('html .ui-autocomplete').css('overflow-y', 'auto');