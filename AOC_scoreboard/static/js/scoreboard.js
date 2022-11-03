var sum = 50; // rank 1.
var time = 250;

$(document).ready(function () {
  $(".js-podium").each(function () {
    var t = $(this);
    setTimeout(function () {
      t.addClass("is-visible");
      var h = t.data("height");
      // console.log(h);
      t.find(".scoreboard__podium-base").css("height", h).addClass("is-expanding");
    }, time);
    time += 250;
  });

  // randomizeData();
  startBars();
  alignItems();
});

function randomizeData() {
  $(".scoreboard__item").each(function () {
    var rand = Math.floor(Math.random() * 50) + 1;
    $(this).data("count", rand);
    $(this).find(".js-number").text(rand);
  });
}

function startBars() {
  $(".js-bar").each(function () {
    console.log("running");
    // calculate %.
    var t = $(this);
    setTimeout(function () {
      var width = t.parent(".scoreboard__item").data("count");
      width = (width / sum) * 100;
      width = Math.round(width);
      t.find(".scoreboard__bar-bar").css("width", width + "%");
      t.parent("li").addClass("is-visible");
    }, time);
    time += 0;
  });
}

function alignItems() {
  var ul = document.getElementById("scoreboard__items"),
    lis = ul.querySelectorAll("li"),
    liHeight = lis[0].offsetHeight;
  ul.style.height = ul.offsetHeight + "px";
  for (var i = 0, l = lis.length; i < l; i++) {
    var li = lis[i];
    li.style.position = "absolute";
    li.style.top = i * liHeight + "px";
  }
}
