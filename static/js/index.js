 // Retrieve the search input from localStorage when the page loads
 document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById('searchInput');
    const savedQuery = localStorage.getItem('searchQuery');
    if (savedQuery) {
        searchInput.value = savedQuery;
    }
});

// Save the search input to localStorage when the user types
document.getElementById('searchInput').addEventListener('input', function() {
    localStorage.setItem('searchQuery', this.value);
});

