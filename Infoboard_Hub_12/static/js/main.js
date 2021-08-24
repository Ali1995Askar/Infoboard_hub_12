   
 $("#appointment_form").submit(function (e) {
    // preventing default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    var serializedData = $(this).serialize();
    // Ajax Call
    $.ajax({
        type: 'POST',
        url: "{% url 'display-data' %}",
        data: serializedData,
        // handle a successful response
        success: function (response) {
            // On successful, clear all form data
            $("#appointment_form").trigger('reset');

            // Display new participant to table
            var instance = JSON.parse(response["instance"]);
            var fields = instance[0]["fields"];
            $("#showdata tbody").prepend(
               `<tr>
                <td>ali askar</td><td>ali askar</td><td>ali askar</td><td>ali askar</td><td>ali askar</td>
              
                </tr>`
            )
        },
        error: function (response) {
            // alert non successful response
            alert(response["responseJSON"]["error"]);
        }
    })
})