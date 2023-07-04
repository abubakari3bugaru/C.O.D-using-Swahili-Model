function searchData(event) {
    event.preventDefault(); // Prevent the default form submission behavior
  
    // Retrieve the search input value
    var searchQuery = $('#search-input').val();
  
    // Make the AJAX request
    $.ajax({
      url: '/dashboard', // Replace with your server-side endpoint URL
      method: 'GET', // Use 'GET' or 'POST' depending on your server-side implementation
      data: { query: searchQuery }, // Pass the search query to the server
      success: function(response) {
        // Handle the successful response from the server
        console.log(response); // Log or process the response data as needed
      },
      error: function(error) {
        // Handle any errors that occur during the AJAX request
        console.error(error);
      }
    });
  }
  