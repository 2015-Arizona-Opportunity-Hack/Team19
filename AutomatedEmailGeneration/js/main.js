$(function() {
  $('#sty').click(function (e) {
    $.ajax({
      'method': 'get',
      'url': 'http://localhost/cgi-bin/generateEmail.py'
    }).done(function(res) {
      $('.alert-success').html(res);
    });
  });

  $('#rnp').click(function (e) {
  	setTimeout(function(){
  		$.ajax({
	      'method': 'get',
	      'url': 'http://localhost/cgi-bin/generateRecoEmail.py'
	    }).done(function(res) {
	      $('.alert-success').html(res);
	    });
  	}, 750);
  });

  $('#rnd').click(function (e) {
    $.ajax({
      'method': 'get',
      'url': 'http://localhost/cgi-bin/generateRecoEmail.py'
    }).done(function(res) {
      $('.alert-success').html(res);
    });
  });
});
