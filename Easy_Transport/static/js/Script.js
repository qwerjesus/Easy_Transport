document.getElementById('comment-form').addEventListener('submit', function(e) {
    e.preventDefault();
  
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var comment = document.getElementById('comment').value;
  
    var commentElement = document.createElement('div');
    commentElement.innerHTML = '<strong>' + name + '</strong><br>' + email + '<br>' + comment;
    document.getElementById('comments-container').appendChild(commentElement);
  
    document.getElementById('comment-form').reset();
  });
  