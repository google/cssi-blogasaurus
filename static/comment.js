// Copyright 2017 Google Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

$(document).ready(function() {
  var commentForm = $('#comment-form');
  var commentInputs = $('#comment-form :input');
  var commentContent = $('#comment-content');
  commentForm.submit(function(event) {
    event.preventDefault();
    var formData = commentForm.serialize();
    commentInputs.prop('disabled', true);
    $.post({url: '/submit-comment', data: formData, dataType: 'json'}).then(
        function(responseData) {
          $('#no-comments').remove();
          $('#comments')
              .append($('<div/>')
                  .append($('<h4/>')
                      .append($('<a/>', {
                        href: 'mailto:' + responseData.email,
                        text: responseData.email
                      })).append(document.createTextNode(' wrote:')))
                  .append($('<p/>', {text: commentContent.val()})));
          commentContent.val('');
          commentInputs.prop('disabled', false);
          commentContent.focus();
        },
        function() {
          commentForm.append($('<p>Something went wrong.</p>'));
        });
  });
});
