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

function recommend_product() {
  $('#review-recommended .fa-thumbs-down').removeClass('fa-solid');
  $('#review-recommended .fa-thumbs-down').addClass('fa-regular');

  $('#review-recommended .fa-thumbs-up').removeClass('fa-regular');
  $('#review-recommended .fa-thumbs-up').addClass('fa-solid');

  $('#recommended-to-others').prop('checked', true);
  $('#recommended-text').text('I definitely recommend this to others!');
}

function not_recommend_product() {
  $('#review-recommended .fa-thumbs-up').removeClass('fa-solid');
  $('#review-recommended .fa-thumbs-up').addClass('fa-regular');

  $('#review-recommended .fa-thumbs-down').removeClass('fa-regular');
  $('#review-recommended .fa-thumbs-down').addClass('fa-solid');

  $('#recommended-to-others').prop('checked', false);
  $('#recommended-text').text('I do not recommend this to others!');

}
