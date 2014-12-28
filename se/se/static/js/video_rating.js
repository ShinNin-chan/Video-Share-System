
var frm = $('#RatingForm');
frm.submit(function () {
    $.ajax({
        type: frm.attr('method'),
        url: frm.attr('action'),
        data: frm.serialize(),
        success: function (data) {
            $("#ratings").html(data);
   			$('#RatingForm').hide();
   			$("#RateYes").show();
        },
        error: function(data) {
            $("#ratings").html("Something went wrong!");
        }
    });
    return false;
});  



var Cfrm = $('#CommentForm');
Cfrm.submit(function (e) {
    $.ajax({
        type: Cfrm.attr('method'),
        url: Cfrm.attr('action'),
        data: Cfrm.serialize(),
        success: function (data) {
            //$("#Comment").prepend("<p>"+str(data.name)+"/"+str(data.date)+"/"+str(data.content)+"</p>")
        	//$('#Comment').html("<p>"+str(data.name)+"/"+str(data.date)+"/"+str(data.content)+"</p>");
        	$("#Comment").prepend(data);
        	$('#id_title').val('');
        },
        error: function(data) {
            $("#Comment").html("Something went wrong!");
        }
    });
    return false;
});  
