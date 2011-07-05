function initAutoCompleteField(iS, oS, eP, pN, mL, lS) { 
    $(iS).autocomplete({
        source: function(request, response) {
            $.ajax({
                url: eP+"?"+pN+"="+request.term,
                success: function(data) {
                    response($.map(data, function(item) {
                        return {
                            id: item.id,
                            label: item.name,
                            value: item.name
                        }
                    }));
                }
            });
        },
        select: function(event, ui) {
            if(ui.item) {
                $(iS).val(ui.item.label);
                $(oS).val(ui.item.id);
                lS = ui.item.label;
            }
        },
        close: function(event, ui) {
            if(lS) {
                $(iS).val(lS);
            }
        },
        minLength: mL
    });
}