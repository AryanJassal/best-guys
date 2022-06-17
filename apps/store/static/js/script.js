$(document).ready(() => {

});

function toggle_show_more(self) {
  if ($(self).hasClass('show-more')) {
    $(self).removeClass('show-more');
    $(self).addClass('show-less');
    $(self).text('Show less.');
    $('div.description').removeClass('multiline-clamped');
  } else {
    $(self).removeClass('show-less');
    $(self).addClass('show-more');
    $(self).text('Show more.');
    $('div.description').addClass('multiline-clamped');
  }
}
