var current;
var next;
$(document).ready(function () {
	current = $('.small-img')[0];
	if (current.parentNode.nextSibling.nextSibling === null) {
		next = $('.small-img')[0];
	} else {
		next = current.parentNode.nextSibling.nextSibling.childNodes[1];
	}
	$(document).on('keydown', function (e) {
		if (e.which === 39) {
			changePhoto(next, next.src);
		}
	});
	$('.small-img').on('click', function (e) {
		changePhoto(e.target, e.target.src);
	});
});

var changePhoto = function (current, newSRC) {
	$('.big-img').attr('src', newSRC);
	current = current;
	if (current.parentNode.nextSibling.nextSibling === null) {
		next = $('.small-img')[0];
	} else {
		next = current.parentNode.nextSibling.nextSibling.childNodes[1];
	}
}