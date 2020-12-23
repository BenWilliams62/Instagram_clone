var btn = document.getElementById("modal-button");
var modal = document.getElementsByClassName("modal-content")[0];



// like modal
function openModal() {
    document.getElementsByClassName("likes-modal")[0].style.display = "block";
    document.getElementsByClassName("modal-content")[0].style.display = "grid";
}


function closeModal() {
    document.getElementsByClassName("likes-modal")[0].style.display = "none";
    document.getElementsByClassName("modal-content")[0].style.display = "none";
}

// follower modal

function openFollowerModal() {
    console.log('clicking works')
    document.getElementsByClassName("follower-modal")[0].style.display = "block";
    document.getElementsByClassName("modal-content")[0].style.display = "grid";
}


function closeFollowerModal() {
    document.getElementsByClassName("follower-modal")[0].style.display = "none";
    document.getElementsByClassName("modal-content")[0].style.display = "none";
}

// following modal

function openFollowingModal() {
    document.getElementsByClassName("following-modal")[0].style.display = "block";
    document.getElementsByClassName("modal-content")[1].style.display = "grid";
}


function closeFollowingModal() {
    document.getElementsByClassName("following-modal")[0].style.display = "none";
    document.getElementsByClassName("modal-content")[1].style.display = "none";
}