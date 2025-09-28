// Copy to clipboard functionality for navbar
function copyToClipboard(text, itemName) {
  if (navigator.clipboard && window.isSecureContext) {
    // Use the modern Clipboard API
    navigator.clipboard.writeText(text).then(function() {
      showCopyToast(itemName, text);
    }).catch(function(err) {
      console.error('Failed to copy: ', err);
      fallbackCopyTextToClipboard(text, itemName);
    });
  } else {
    // Fallback for older browsers
    fallbackCopyTextToClipboard(text, itemName);
  }
}

function fallbackCopyTextToClipboard(text, itemName) {
  var textArea = document.createElement("textarea");
  textArea.value = text;
  
  // Avoid scrolling to bottom
  textArea.style.top = "0";
  textArea.style.left = "0";
  textArea.style.position = "fixed";
  textArea.style.opacity = "0";

  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();

  try {
    var successful = document.execCommand('copy');
    if (successful) {
      showCopyToast(itemName, text);
    } else {
      console.error('Fallback: Could not copy text');
      // Show error toast
      showErrorToast(itemName);
    }
  } catch (err) {
    console.error('Fallback: Oops, unable to copy', err);
    showErrorToast(itemName);
  }

  document.body.removeChild(textArea);
}

function showCopyToast(itemName, text) {
  var toastBody = document.getElementById('copy-toast-body');
  if (toastBody) {
    toastBody.innerHTML = '<strong>' + itemName + '</strong><br><small>' + text + '</small><br>Copied to clipboard';
    
    var toastElement = document.getElementById('copy-toast');
    if (toastElement && typeof bootstrap !== 'undefined') {
      var toast = new bootstrap.Toast(toastElement, {
        delay: 3000
      });
      toast.show();
    }
  }
}

function showErrorToast(itemName) {
  var toastBody = document.getElementById('copy-toast-body');
  if (toastBody) {
    toastBody.innerHTML = '<strong>' + itemName + '</strong><br>Copy failed, please copy manually';
    
    var toastElement = document.getElementById('copy-toast');
    if (toastElement && typeof bootstrap !== 'undefined') {
      var toast = new bootstrap.Toast(toastElement, {
        delay: 4000
      });
      toast.show();
    }
  }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  console.log('Copy functionality loaded');
});
