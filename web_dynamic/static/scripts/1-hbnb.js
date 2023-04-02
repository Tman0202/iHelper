$(document).ready(function() {
    $("input[type='checkbox']").change(function() {
      var selected = $("input[type='checkbox']:checked");
      var text = "";
  
      selected.each(function() {
        text += $(this).data("name") + ", ";
      });
  
      if (text !== "") {
        text = text.slice(0, -2); // remove last ", "
        $(".amenities h4").text(text);
      } else {
        $(".amenities h4").text("");
      }
    });
  });





  // $(document).ready(function() {
  //   var selectedCity = '';
  //   $('.list_content').click(function() {
  //     var city = $(this).data('name');
  //     if (selectedCity === city) {
  //       selectedCity = '';
  //       $(this).prop('checked', false);
  //       $('h4').text('');
  //     } else {
  //       selectedCity = city;
  //       $('.list_content').not(this).prop('checked', false);
  //       $('h4').text(selectedCity);
  //     }
  //   });
  // });



  // // add event listener to each dropdown menu item
  // const cities = document.querySelectorAll('.city');
  // cities.forEach(city => {
  //   city.addEventListener('click', () => {
  //     // remove selected class from all items
  //     cities.forEach(city => {
  //       city.classList.remove('selected');
  //     });
  //     // toggle selected class on clicked item
  //     city.classList.toggle('selected');
  //     // store selected value in h4 element
  //     const selectedCity = document.querySelector('.selected');
  //     const selectedValue = selectedCity ? selectedCity.getAttribute('data-value') : '';
  //     const h4 = document.querySelector('h4');
  //     h4.textContent = selectedValue;
  //   });
  // });




  //  // get the radio buttons
  //  const radioButtons = document.querySelectorAll('input[type="radio"]');
  
  //  // add event listener to each radio button
  //  radioButtons.forEach((radioButton) => {
  //    radioButton.addEventListener('change', () => {
  //      // get the selected city name
  //      const selectedCity = document.querySelector('input[name="city"]:checked').value;
       
  //      // set the selected city name as the text of the h4 element
  //      document.querySelector('h4').textContent = selectedCity;
  //    });
  //  });





   $(document).ready(function() {
    // Add event listener to radio buttons
    $('#cities-popover input[type="radio"]').on('change', function() {
      // Get selected city name
      var selectedCity = $('input[name="city"]:checked').val();
      // Update h4 tag with selected city name
      $('#selected-city').text(selectedCity);
    });
  });



//   const selectedCity = document.querySelector('#selected-city');

// selectedCity.addEventListener('click', () => {
//   const selectedCityName = selectedCity.getAttribute('data-selected-city');
//   const selectedRadioButton = document.querySelector(`#cities-popover input[type="radio"][value="${selectedCityName}"]`);

//   if (selectedRadioButton) {
//     selectedRadioButton.removeAttribute('checked');
//   }
// });





// // Get all radio buttons with name "city"
// const cityRadios = document.querySelectorAll('input[type="radio"][name="city"]');

// // Attach click event listener to each radio button
// cityRadios.forEach(radio => {
//   radio.addEventListener('click', event => {
//     // If the clicked radio button was already checked, uncheck it
//     if (event.target.checked) {
//       event.target.checked = false;
//     }
//   });
// });




// $(document).ready(function() {
//   // Get all radio buttons with name "city"
//   const cityRadios = $('input[type="radio"][name="city"]');

//   // Attach click event listener to each radio button
//   cityRadios.click(function(event) {
//     // If the clicked radio button was already checked, uncheck it
//     if ($(this).prop('checked')) {
//       $(this).prop('checked', false);
//     }
//   });
// });






  // $(document).ready(function() {
  //   $('#search-btn').click(function() {
  //     var selectedCity = $('input[name=city]:checked').val();
  //     var selectedAmenities = [];
  //     $('input[type=checkbox]:checked').each(function() {
  //       selectedAmenities.push($(this).data('id'));
  //     });
  //     var url = 'http://127.0.0.1:5000/iHelper/search?city=' + selectedCity + '&amenities=' + selectedAmenities.join(',');
  //     window.location.href = url;
  //   });
  // });



  // $(function() {
  //   // when the search button is clicked
  //   $('#search-btn').click(function() {
  //     // get the selected city
  //     var city = $('input[name=city]:checked').val();
  //     // get the selected services
  //     var services = [];
  //     $('.amenities input:checked').each(function() {
  //       services.push($(this).data('id'));
  //     });
  //     // send an AJAX request to the server with the selected city and services as parameters
  //     $.ajax({
  //       url: '/iHelper/search',
  //       method: 'GET',
  //       data: {
  //         city: city,
  //         services: services
  //       },
  //       success: function(data) {
  //         // display the search results on the page
  //         $('.results').html(data);
  //       }
  //     });
  //   });
  // });



  function search() {
    // Get the selected location and service values
    var city = $("input[name='city']:checked").val();
    var amenities = [];
    $("input[type='checkbox']:checked").each(function() {
      amenities.push($(this).data("name"));
    });
  
    // Redirect to the search results page with the selected values as URL parameters
    window.location.href = "http://127.0.0.1:5000/iHelper/search?city=" + encodeURIComponent(city) + "&amenities=" + encodeURIComponent(amenities.join(","));
  }