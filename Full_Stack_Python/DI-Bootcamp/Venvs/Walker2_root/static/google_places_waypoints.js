
$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&libraries=places") 
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initAutocomplete())

})






var auto_fields = ['a', 'b', 'c', 'd']

function initAutocomplete() {
    console.log('autocomplete');
  for (i = 0; i < auto_fields.length; i++) {
    var field = auto_fields[i]
    window['autocomplete_'+field] = new google.maps.places.Autocomplete(
      document.getElementById('id-google-address-' + field),
    {
       types: ['address'],
       componentRestrictions: {'country': [base_country.toLowerCase()]},
    })
  }

  autocomplete_a.addListener('place_changed', function(){
          onPlaceChanged('a')
          console.log('a')
      });
  autocomplete_b.addListener('place_changed', function(){
          onPlaceChanged('b')
          console.log('b')

      });
  autocomplete_c.addListener('place_changed', function(){
          onPlaceChanged('c')
          console.log('c')

      });
  autocomplete_d.addListener('place_changed', function(){
          onPlaceChanged('d')
          console.log('d')

      });
}


function onPlaceChanged (addy){

    var auto = window['autocomplete_'+addy]
    var el_id = 'id-google-address-'+addy
    var lat_id = 'id-lat-' + addy
    var long_id = 'id-long-' + addy

    var geocoder = new google.maps.Geocoder()
    var address = document.getElementById(el_id).value

    geocoder.geocode( { 'address': address}, function(results, status) {

        if (status == google.maps.GeocoderStatus.OK) {
            var latitude = results[0].geometry.location.lat();
            var longitude = results[0].geometry.location.lng();

            $('#' + lat_id).val(latitude) 
            $('#' + long_id).val(longitude) 
            // CalcRoute()
        } 
    }); 
}


function validateForm() {
    var valid = true;
    if (field1.value == '' || field2.value == '' || field3.value == '') {
        console.log(field1, field2, field3)
        return false
    } 
    return valid
}


function CalcRoute(){
    console.log('calculating')
    if ( validateForm() == true){
        console.log("validate")
      var params = {
          lat_a: $('#id-lat-a').val(),
          long_a: $('#id-long-a').val(),
          lat_b: $('#id-lat-b').val(),
          long_b: $('#id-long-b').val(),
          lat_c: $('#id-lat-c').val(),
          long_c: $('#id-long-c').val(),
          lat_d: $('#id-lat-d').val(),
          long_d: $('#id-long-d').val(),
      };

      var esc = encodeURIComponent;
      var query = Object.keys(params)
          .map(k => esc(k) + '=' + esc(params[k]))
          .join('&');

      url = '/map?' + query
      window.location.assign(url)
    }
}
let submit = document.querySelector("#submit");
let field1 = document.querySelector('#id-google-address-a');
let field2 = document.querySelector('#id-google-address-d');
let field3 = document.querySelector('#id-google-address-c');
let field4 = document.querySelector('#id-google-address-b');
field1.addEventListener('mouseleave', ()=> {
    field4.value = field1.value;
    console.log(field4.value);
});

submit.addEventListener('click', () => {
    field4.value = field1.value;
    CalcRoute()
});

