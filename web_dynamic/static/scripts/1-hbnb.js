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