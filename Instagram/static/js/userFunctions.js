function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(
                        name.length + 1));
                    break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getToken('csrftoken');



function addLike(postID) {

    var url = '/update_like/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'postID': postID,
            //'action': action
        })
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
    })

}


function Follow(user) {


    var url = '/update_follow/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'Followee': user,
        })
    })


    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
    })

    

}