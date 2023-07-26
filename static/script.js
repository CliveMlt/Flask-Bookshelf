document.addEventListener('DOMContentLoaded', function() {
    var toggleModeBtn = document.getElementById('toggle-mode-btn');
  
    toggleModeBtn.addEventListener('click', function() {
      // Make a POST request to the /toggle-mode endpoint
      fetch('/toggle-mode', {
        method: 'POST'
      })
      .then(function(response) {
        // Reload the page to reflect the mode change
        window.location.reload();
      })
      .catch(function(error) {
        console.error('Error toggling mode:', error);
      });
    });
  });
  