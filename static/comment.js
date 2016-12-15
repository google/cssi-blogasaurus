$(document).ready(() => {
  const commentForm = $('#comment-form');
  const commentInputs = $('#comment-form :input');
  const commentContent = $('#comment-content');
  commentForm.submit((event) => {
    event.preventDefault();
    const formData = commentForm.serialize();
    commentInputs.prop('disabled', true);
    $.post({url: '/submit-comment', data: formData, dataType: 'json'}).then(
        (responseData) => {
          $('#comments')
              .append($('<div/>')
                  .append($('<h4/>')
                      .append($('<a/>', {
                        href: 'mailto:' + responseData.email,
                        text: responseData.nickname,
                      })).append(document.createTextNode(' wrote:')))
                  .append($('<p/>', {text: commentContent.val()})));
          commentContent.val('');
          commentInputs.prop('disabled', false);
          commentContent.focus();
        },
        () => {
          commentForm.append($('<p>Something went wrong.</p>'));
        });
  });
});
