function sendMessage() {
    var userInput = $('#user-input').val();
    // Clear previous messages
    $('#chat-area .user-message').remove();
    $('#chat-area .server-message').remove();
    // Append new user message
    $('#chat-area').append('<div class="user-message">Text: ' + userInput + '</div>');
    $('#user-input').val('');
    $.ajax({
      url: '/send_message',
      type: 'POST',
      data: { user_input: userInput },
      success: function(data) {
        // Append new server message
        $('#chat-area').append('<div class="server-message">Sense: ' + data.computer_response + '</div>');
      }
    });
  }