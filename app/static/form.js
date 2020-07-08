 $(document).ready(function(){
    var myInput = document.getElementById("total_amount_due");
    if(myInput==null){

      $('#get_quote').attr("disabled", true);}
    else{
      
      $('#get_quote').removeAttr("disabled");
    }
  $("#get_price").click(function(){
  $('#get_quote').removeAttr("disabled");
});
});