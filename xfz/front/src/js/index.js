function Banner() {
    this.bannerGroup = $("#banner-group");
    this.index = 0;
    this.leftArrow = $('.left-arrow');
    this.rightArrow = $('.right-arrow');
    this.bannerUl = $('#banner-ul');
    this.liList = this.bannerUl.children('li');
    this.bannerCount = this.liList.length;
    this.listenBannerHover();
    this.bannerWidth = 798;
    this.pageControl = $(".page-control");
}

Banner.prototype.initBanner = function () {
    var self = this;
    this.bannerUl.css({"width": self.bannerWidth * self.bannerCount});
};


Banner.prototype.initPageControl = function () {
    var self = this;
    for (var i = 0; i < self.bannerCount; i++) {
        var circle = $("<li></li>")
        self.pageControl.append(circle);
        if (i === 0) {
            circle.addClass("active")
        }
    }
    self.pageControl.css({"width": 16 + (self.bannerCount - 1) * 16 + self.bannerCount * 10 + 2 * self.bannerCount});
};


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

Banner.prototype.animate = function () {
    var self = this;
    self.bannerUl.animate({"left": -798 * self.index}, 500);
    self.pageControl.children('li').eq(self.index).addClass("active").siblings().removeClass('active')
};

Banner.prototype.loop = function () {
    var self = this;
    this.timer = setInterval(function () {
        if (self.index >= self.bannerCount - 1) {
            self.index = 0;
        } else {
            self.index++;
        }
        self.animate();
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
        self.animate();
    });
    self.rightArrow.click(function () {
        if (self.index === self.bannerCount - 1) {
            self.index = 0;
        } else {
            self.index++;
        }
        self.animate();
    });
};

Banner.prototype.listenPageControl = function () {
    var self = this;
    self.pageControl.children("li").each(function (index, obj) {
        $(obj).click(function () {
            self.index = index;
            self.animate();
        });
    });
};

Banner.prototype.run = function () {
    this.initBanner();
    this.initPageControl();
    this.loop();
    this.listenArrowClick();
    this.listenPageControl();
};

$(function () {
    var banner = new Banner();
    banner.run();
});