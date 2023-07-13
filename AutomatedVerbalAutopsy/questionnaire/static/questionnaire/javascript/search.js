const searchInput = document.getElementById('search-input');
searchInput.addEventListener('input', function() {
    const query = searchInput.value.trim();
    if (query.length > 0) {
        const url = `/search/?query=${query}`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                // Process the search results and update the UI
                const searchResultsDiv = document.getElementById('search-results');
                searchResultsDiv.innerHTML = '';

                data.marehemu_list.forEach(marehemu => {
                    const resultItem = document.createElement('div');
                    resultItem.textContent = marehemu.jina;
                    // Add more fields or HTML elements as needed
                    searchResultsDiv.appendChild(resultItem);
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
});
