$(document).ready(function() {
   
    function loadMarehemuData() {
      $.ajax({
        url: '/get_marehemu_data/', // Replace with the URL of the endpoint that returns marehemu data
        method: 'GET',
        success: function(response) {
          $('#marehemu-table tbody').empty();
  
          for (const marehemu of response.marehemu_values) {
            const tableRow = `
              <tr class="data-row" data-marehemu-id="${marehemu.id}">
                <td>${marehemu.jina_kwanza} ${marehemu.jina_pili} ${marehemu.jina_mwisho}</td>
                <td>${marehemu.mahali}</td>
                <td class="editable-field">${marehemu.maelezo}</td>
                <td>${marehemu.sababu.sababu}</td>
              </tr>
            `;
            $('#marehemu-table tbody').append(tableRow);
          }
        },
        error: function(error) {
          console.error(error);
        }
      });
    }

    loadMarehemuData();
  
    $('#add-form-btn').click(function() {
      window.location.href = "{% url 'questionnaire:submit_form' %}";
    });
  
    
    $(document).on('click', '.data-row', function() {
      const marehemuId = $(this).data('marehemu-id');
      window.location.href = `/edit_marehemu/${marehemuId}`; // Replace with the URL for editing marehemu data
    });
  
   
    $('#search-form').submit(function(event) {
      event.preventDefault();
      const searchQuery = $('#search-input').val();
      // Perform search AJAX request and update the table with search results
      // You will need to implement the server-side search endpoint and update the loadMarehemuData function accordingly.
    });
  });
  