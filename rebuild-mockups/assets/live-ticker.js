/* Live-site hello ticker behaviour, copied from origin/main hello.html: today's date, last month's name,
   and the marquee wrap (.tk > .tk-in + aria-hidden copy). Scoped to .tickerbar only. */
(function(){
  var d = new Date();
  var months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'];
  var days = ['SUN','MON','TUE','WED','THU','FRI','SAT'];
  document.querySelectorAll('.tickerbar .js-date').forEach(function(el){
    el.textContent = days[d.getDay()] + ' · ' + months[d.getMonth()] + ' ' + d.getDate() + ' · ' + d.getFullYear();
  });
  var p = new Date(); p.setDate(1); p.setDate(0);
  var M = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER'];
  document.querySelectorAll('.tickerbar .js-prevmonth').forEach(function(el){ el.textContent = M[p.getMonth()] + ' ' + p.getFullYear(); });
  document.querySelectorAll('.tickerbar').forEach(function(t){
    var inner = t.innerHTML;
    t.innerHTML = '<div class="tk"><div class="tk-in">' + inner + '</div><div class="tk-in" aria-hidden="true">' + inner + '</div></div>';
    t.style.padding = '0';
  });
})();
