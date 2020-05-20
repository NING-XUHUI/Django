//面向对象

// function Banner() {
//     //这里的所有代码
//     //相当于python中的__init__方法代码
//     console.log('init');
//     this.person = 'zhiliao'
// }
//
// Banner.prototype.greet = function (word) {
//     console.log("hello zhiliao",word
//     )
// }
//
// var banner = new Banner();
// console.log(banner.person);
//
// banner.greet("!!!");

function Banner() {
    this.bannerGroup = $("#banner-group");
    this.index = 0;
    this.leftArrow = $('.left-arrow');
    this.rightArrow = $('.right-arrow');
    this.bannerUl = $('#banner-ul');
    this.liList = this.bannerUl.children('li');
    this.bannerCount = this.liList.length;
    this.listenBannerHover();
}

Banner.prototype.toggleArrow = function (isShow) {
    var self = this;
    if (isShow) {
        self.leftArrow.show();
        self.rightArrow.show();
    } else {
        self.leftArrow.hide();
        self.rightArrow.hide();
    }
};


Banner.prototype.listenBannerHover = function () {
    var self = this;
    this.bannerGroup.hover(function () {
        //第一个函数，鼠标移到banner执行的函数
        clearInterval(self.timer);
        self.toggleArrow(true);
    }, function () {
        //第二个函数，鼠标离开banner执行的函数
        self.loop();
        self.toggleArrow(false);
    });
};

Banner.prototype.loop = function () {
    var self = this;
    var bannerUl = $("#banner-ul");
    this.timer = setInterval(function () {
        self.index++;
        bannerUl.animate({"left": -798 * self.index}, 500);
        if (self.index >= 3) {
            self.index = -1;
        }
    }, 2000);
};

Banner.prototype.listenArrowClick = function () {
    console.log("111");
    var self = this;
    self.leftArrow.click(function () {
        if (self.index === 0) {
            self.index = self.bannerCount - 1;
        } else {
            self.index--;
        }
        self.bannerUl.animate({"left": -798 * self.index}, 500);
    });

    self.rightArrow.click(function () {
        if (self.index === self.bannerCount - 1) {
            self.index = 0;
        } else {
            self.index++;
        }
        self.bannerUl.animate({"left": -798 * self.index}, 500);
    });
};

Banner.prototype.run = function () {
    this.loop();
    this.listenArrowClick();
};

$(function () {
    var banner = new Banner();
    banner.run();
});