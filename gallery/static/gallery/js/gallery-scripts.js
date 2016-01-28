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
	cookieBg = getCookie('bg');
	if (cookieBg) {
		var body = document.getElementsByTagName('body')[0];
		var photoURL = cookieBg;
		body.setAttribute('background', photoURL);
		body.setAttribute('style', 'background-size: 100%;');
	}
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
		var block = document.getElementsByClassName('comments')[0];
		block.classList.add('invisible');
		var block = document.getElementsByClassName('comments-form')[0];
		block.classList.add('invisible');
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
	if (classes.indexOf('addlike') >=0) {
		e.preventDefault();
		var photoURL = photos[id].src;
		for (var i = 0; i < 4; i++) {
			photoURL = photoURL.substr(photoURL.indexOf('/') + 1);
		}
		$.ajax({
			url: '/gallery/addlike/',
			data: {photoURL: photoURL},
			success: function (data) {
				showLikes(data.count);
			}
		});
	}
}

var setBackground = function(e) {
	var body = document.getElementsByTagName('body')[0];
	var photoURL = photos[id].src;
	if (body.getAttribute('background') == photoURL) {
		body.setAttribute('background', null);
		setCookie('bg', null, new Date(new Date().getTime() + 300000));
	} else {
		body.setAttribute('background', photoURL);
		body.setAttribute('style', 'background-size: 100%;');
		setCookie('bg', photoURL, new Date(new Date().getTime() + 300000));
	}
}

var showLikes = function (count) {
	var likes = document.getElementById('like-count');
	likes.innerHTML = count;
}

var showImage = function (flag) {
	if (!bigPhotoShow) {
		return
	}
	// flag - true, когда id-шка установилась при помощи history.back
	// нужно ловить это, иначе бесконечная ссылка на саму себя
	if (!flag) {
		window.history.pushState({'idPhoto': id}, null, null);
	}
	var photoURL = photos[id].src;
	for (var i = 0; i < 4; i++) {
		photoURL = photoURL.substr(photoURL.indexOf('/') + 1);
	}
	var block = document.getElementsByClassName('comments-form')[0];
	block.classList.remove('invisible');
	var inputPhotoURL = document.getElementById('photoURL');
	inputPhotoURL.setAttribute('value', photoURL)
	$.ajax({
		url: '/gallery/getcomments/',
		data: {photoURL: photoURL},
		success: function (data) {
			var comments = data;
			var block = document.getElementsByClassName('comments')[0];
			block.classList.remove('invisible');
			html = '';
			for (var i = 0; i < comments.length; i++){
				html += '<div class="row"><div class="col-sm-3"></div><article class="comment col-sm-6"><header><span class="nickname">' + comments[i][1] + '</span></header><p>' + comments[i][0] + '</p></article></div>';
			}
			block.innerHTML = html;
		}
	});
	$.ajax({
		url: '/gallery/getlikes/',
		data: {photoURL: photoURL},
		success: function (data) {
			showLikes(data.count);
		}
	});
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

// History Listener
window.addEventListener('popstate', function(e) {
	if (e.state !== null) {
		id = e.state.idPhoto;
		showImage(true);
	}
}, false)