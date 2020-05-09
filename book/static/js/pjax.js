// 浏览器支持情况
var support = history.pushState ? 'HTML5' : ("onhashchange" in window ? 'HASH' : 'PASS');

var cache = {
  key: function (url) {
    return "x-pjax[" + url + "]";
  },
  get: function (url) {
    var value = sessionStorage.getItem(cache.key(url));
    return value && JSON.parse(value);
  },
  set: function (url, value) {
    // storage有容量上限，超出限额会报错
    try {
      sessionStorage.setItem(cache.key(url), JSON.stringify(value));
    } catch (e) {
      console.log("超出本地存储容量上线，本次操作将不使用本地缓存");
    }
  },
  clear: function () {
    var i = sessionStorage.length;
    while (i--) {
      var key = sessionStorage.key(i);
      if (key.indexOf("x-pjax") > -1) {
        sessionStorage.removeItem(key);
      }
    }
  },
};

var event = {
  //浏览器前进后退时执行
  popstate: function () {
    pjax.fnb = true;
    pjax.jump(location.href, null, null);
  },
  hashchange: function () {
    if (!pjax.fnb) return;
    pjax.jump(location.href.replace("#/", ""), null, null);
  },
  click: function (e) {
    var element = e.target || e.srcElement;
    url = element.href;
    //过滤空值
    if (url === undefined || url === "") return;
    //阻止默认跳转
    e.preventDefault ? e.preventDefault() : (window.event.returnValue = false);
    // var data = encodeURI(element.getAttribute("title"));

    pjax.fnb = false;
    pjax.jump(url, null, null);
  },
  bindEvent: function () {
    var nav = document.getElementsByClassName('chapter-control');
    if (support === 'HTML5') {
      window.addEventListener("popstate", event.popstate);

      nav[0].addEventListener("click", event.click);
      nav[1].addEventListener("click", event.click);
      //window.addEventListener("click", event.click);
    } else {
      window.attachEvent("onhashchange", event.hashchange);
      nav[0].attachEvent("onclick", event.click);
      nav[1].attachEvent("onclick", event.click);
      //document.documentElement.attachEvent("onclick", event.click);
    }
  }
};

var pjax = {
  // Forward And Back，表示当前操作是否由前进和后退触发
  fnb: false,
  // 显示新页面内容
  show: function (html) {
    // document.title = title;
    document.getElementsByClassName('content_wrap')[0].innerHTML = html;
  },

  //跳转到指定页面
  jump: function (url, data, callback) {

    // 如果是由前进后退触发，则试着从缓存中获取数据
    if (pjax.fnb) {
      var value = cache.get(url);
      //console.log(value);
      if (value !== null) {
        pjax.show(value.title, value.html);
        return;
      }
    }


    document.getElementsByClassName('content_wrap')[0].innerHTML = '加载中...';
    //ajax发送请求
    var xhr = new XMLHttpRequest();

    xhr.open("GET", url, true);
    /*xhr.setRequestHeader("X-PJAX", "true");
    xhr.setRequestHeader("X-PJAX-TITLE", data);
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");*/
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status >= 200 && xhr.status < 300 || xhr.status === 304) { //304是缓存
          var html = xhr.responseText;
          title = document.title;
          // if(title==null){
          // 	title = document.title;
          // }else{
          // 	title = decodeURI(title);
          // }
          //console.log(title);

          // 显示新页面
          pjax.show(html);

          //不是前进和后退按钮触发
          if (!pjax.fnb) {
            // 修改URL,URL地址栏会变换
            if (support === 'HTML5') {
              history.pushState(null, null, url);
            } else {
              var path = url.replace(location.protocol + "//" + location.host, "");
              location.hash = path;
            }
            // 添加到缓存
            cache.set(url, {
              // title: title,
              html: html
            });
          }

        } else {
          console.log('请求失败！');
        }
        pjax.fnb = true;
      }
    };
    xhr.send();
  },

  init: function () {
    event.bindEvent();
  }
};

pjax.init();