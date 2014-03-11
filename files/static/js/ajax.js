function follow_reader(follower_id) {
    ajaxPost('/reader/ajax/follow/', {
        'follower_id': follower_id
    });
}