$(document).ready(() => {
  const commentContent = $('#comment-content');
  $('#comment-form').submit((event) => {
    event.preventDefault();
    $('#no-comments').remove();
    $('#comments')
        .append($('<div/>')
            .append($('<h4>You wrote:</h4>'))
            .append($('<p/>', {text: commentContent.val()})));
    commentContent.val('');
    commentContent.focus();
  });
});
