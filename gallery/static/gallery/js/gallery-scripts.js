var rawPhotos = document.getElementsByClassName('small-img');
var photos = [];
for (var i = 0; i < rawPhotos.length; i++) {
	photos.push(rawPhotos[i]);
}
var bigPhoto = document.getElementById('big-photo');
var id;
var bigPhotoShow = false;

window.onload = function () {
	id = parseInt(getCookie('photo-id')) || 0;
    cookieBigPhotoShow = getCookie('bigPhotoShow');
    if (cookieBigPhotoShow === 'true') {
        bigPhotoShow = true;
    }
    if (bigPhotoShow) {
        var block = document.getElementsByClassName('gallery-top')[0];
        block.classList.add('gallery-top-visible');
    }
	showImage();
}

window.onunload = function () {
	setCookie('photo-id', id, new Date(new Date().getTime() + 5000));
    setCookie('bigPhotoShow', bigPhotoShow, new Date(new Date().getTime() + 5000));
}

document.onkeydown = function (e) {
	if (e.keyCode === 39) {
		e.preventDefault();
		id += 1;
		if (id >= photos.length) {
			id = 0;
		}
		showImage();
	}
	if (e.keyCode === 37) {
		e.preventDefault();
		id -= 1;
		if (id < 0) {
			id = photos.length - 1;
		}
		showImage();
	}
    if (e.keyCode === 27) {
        e.preventDefault();
        var block = document.getElementsByClassName('gallery-top')[0];
        block.classList.remove('gallery-top-visible');
        bigPhotoShow = false;
    }
};

document.onclick = function(e) {
	var classes = e.target.className.split(' ');
	if (classes.indexOf('small-img') >= 0) {
		id = photos.indexOf(e.target);
        var block = document.getElementsByClassName('gallery-top')[0];
        block.classList.add('gallery-top-visible');
        bigPhotoShow = true;
		showImage();
	}
}

var showImage = function () {
	bigPhoto.src = photos[id].src;
}

var getCookie = function (name) {
	var matches = document.cookie.match(new RegExp(
		"(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
	));
	return matches ? decodeURIComponent(matches[1]) : undefined;
}

function setCookie(name, value, exp) {
	if (typeof exp !== "undefined") {
		document.cookie = name + "=" + value + ";" + "expires=" + exp.toUTCString() + ";";
	} else {
		document.cookie = name + "=" + value + ";";
	}
}