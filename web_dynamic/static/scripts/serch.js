// // /* Global styles */
// // $(function() {
// //     // when the search button is clicked
// //     $('#search-btn').click(function() {
// //       // get the selected city
// //       var city = $('input[name=city]:checked').val();
// //       // get the selected services
// //       var services = [];
// //       $('.amenities input:checked').each(function() {
// //         services.push($(this).data('id'));
// //       });
// //       // send an AJAX request to the server with the selected city and services as parameters
// //       $.ajax({
// //         url: '/iHelper/search',
// //         method: 'GET',
// //         data: {
// //           city: city,
// //           services: services
// //         },
// //         success: function(data) {
// //           // display the search results on the page
// //           $('.results').html(data);
// //         }
// //       });
// //     });
// //   });






// //   $(document).ready(function() {
// //     $('#search-btn').click(function() {
// //       var selectedCity = $('input[name=city]:checked').val();
// //       var selectedAmenities = [];
// //       $('input[type=checkbox]:checked').each(function() {
// //         selectedAmenities.push($(this).data('id'));
// //       });
// //       var url = 'http://127.0.0.1:5000/iHelper/search?city=' + selectedCity + '&amenities=' + selectedAmenities.join(',');
// //       window.location.href = url;
// //     });
// //   });





// // $(document).ready(function() {
// //     // When the Get Price button is clicked
// //     $('#get-price-button').click(function() {
// //       // Get the appointment date and time
// //       var appointment = $('#appointment').val();
// //       // Get the selected task size
// //       var taskSize = $('input[name=task-size]:checked').val();
// //       // Get the selected amenities
// //       var amenities = [];
// //       $('input[name=amenities]:checked').each(function() {
// //         amenities.push($(this).val());
// //       });
// //       // Get the selected city
// //       var city = $('#city').val();
  
// //       // Redirect to the price page with the selected options as query parameters
// //       var url = 'http://127.0.0.1:5000/iHelper/price';
// //       url += '?appointment=' + appointment;
// //       url += '&task-size=' + taskSize;
// //       url += '&amenities=' + amenities.join(',');
// //       url += '&city=' + city;
// //       window.location.href = url;
// //     });
// //   });


$(document).ready(function() {
  // When the "Get Price" button is clicked
  $('button.button').click(function() {
    // Get the selected appointment date
    var appointment = $('input#appointment').val();
    // Get the selected task size
    var taskSize = $('input[name="task-size"]:checked').val();
    // Get the selected amenities
    var amenities = $('input[name="amenities"]:checked').map(function() {
      return $(this).val();
    }).get().join(", ");
    // Get the selected city
    var city = $('select#city').val();

    // Send the selected values to the Flask route
    window.location.href = "/iHelper/price?appointment=" + appointment + "&taskSize=" + taskSize + "&amenities=" + amenities + "&city=" + city;
  });
});