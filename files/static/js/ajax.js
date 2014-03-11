function follow_reader(follower_id) {
    ajaxPost('/reader/ajax/follow/', {
        'follower_id': follower_id
    });
}

function delete_article(button) {
    button.parent().fadeOut(100);
    var article_id = button.parent().prop('id');
    ajaxPost('/ajax/article/delete/', {
        'article_id': article_id
    }, function(content) {

    });
}