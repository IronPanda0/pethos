(function(e){function n(n){for(var t,u,o=n[0],h=n[1],f=n[2],i=0,d=[];i<o.length;i++)u=o[i],Object.prototype.hasOwnProperty.call(a,u)&&a[u]&&d.push(a[u][0]),a[u]=0;for(t in h)Object.prototype.hasOwnProperty.call(h,t)&&(e[t]=h[t]);b&&b(n);while(d.length)d.shift()();return r.push.apply(r,f||[]),c()}function c(){for(var e,n=0;n<r.length;n++){for(var c=r[n],t=!0,u=1;u<c.length;u++){var o=c[u];0!==a[o]&&(t=!1)}t&&(r.splice(n--,1),e=h(h.s=c[0]))}return e}var t={},u={app:0},a={app:0},r=[];function o(e){return h.p+"static/js/"+({}[e]||e)+"."+{"chunk-36591b79":"09cfb443","chunk-113fbbd0":"e62f62d7","chunk-65403dc5":"c9907f8e","chunk-cae70e2a":"a4b7b6b0","chunk-5b528ffd":"6b9969f6","chunk-c88957a6":"32de06f2","chunk-2a190c3b":"693ffe1b","chunk-599fea06":"088f6fda","chunk-1deb5f75":"436f449f","chunk-70061e38":"59d5e78e","chunk-7717860e":"e18b1b72","chunk-7c96c12e":"929bb411","chunk-7db4d4e2":"ddb0fdce","chunk-a88408e6":"cdad553a","chunk-1c9fe97b":"553bb6ab","chunk-1f2c0e14":"3961e0d6","chunk-6e639374":"db273ac0","chunk-1810e012":"afcb68c6","chunk-5ed3f2d1":"cba916f1","chunk-5e91d658":"cfeb6fa9","chunk-9033dcfa":"217be85b","chunk-35b90b0f":"ff7c463a","chunk-b31fb184":"0d249752","chunk-82faf870":"9a5b30d3","chunk-093fce96":"77c0a26f"}[e]+".js"}function h(n){if(t[n])return t[n].exports;var c=t[n]={i:n,l:!1,exports:{}};return e[n].call(c.exports,c,c.exports,h),c.l=!0,c.exports}h.e=function(e){var n=[],c={"chunk-36591b79":1,"chunk-113fbbd0":1,"chunk-65403dc5":1,"chunk-cae70e2a":1,"chunk-5b528ffd":1,"chunk-c88957a6":1,"chunk-2a190c3b":1,"chunk-599fea06":1,"chunk-1deb5f75":1,"chunk-70061e38":1,"chunk-7717860e":1,"chunk-7c96c12e":1,"chunk-7db4d4e2":1,"chunk-a88408e6":1,"chunk-1c9fe97b":1,"chunk-1f2c0e14":1,"chunk-6e639374":1,"chunk-1810e012":1,"chunk-5ed3f2d1":1,"chunk-5e91d658":1,"chunk-9033dcfa":1,"chunk-35b90b0f":1,"chunk-b31fb184":1,"chunk-82faf870":1,"chunk-093fce96":1};u[e]?n.push(u[e]):0!==u[e]&&c[e]&&n.push(u[e]=new Promise((function(n,c){for(var t="static/css/"+({}[e]||e)+"."+{"chunk-36591b79":"34bc152d","chunk-113fbbd0":"38050dab","chunk-65403dc5":"a16e1b75","chunk-cae70e2a":"bb3fcc83","chunk-5b528ffd":"afe9d393","chunk-c88957a6":"711e31d2","chunk-2a190c3b":"117b5253","chunk-599fea06":"c7af056b","chunk-1deb5f75":"45ce5c86","chunk-70061e38":"89016dfe","chunk-7717860e":"ab70d8e1","chunk-7c96c12e":"467cd425","chunk-7db4d4e2":"3c1739f9","chunk-a88408e6":"c903cbf3","chunk-1c9fe97b":"c6445661","chunk-1f2c0e14":"e1843c9f","chunk-6e639374":"8731734a","chunk-1810e012":"be02fe1f","chunk-5ed3f2d1":"a0df1223","chunk-5e91d658":"ad2b5a35","chunk-9033dcfa":"ad2b5a35","chunk-35b90b0f":"2c040d32","chunk-b31fb184":"31b85913","chunk-82faf870":"b0806ee7","chunk-093fce96":"2c040d32"}[e]+".css",a=h.p+t,r=document.getElementsByTagName("link"),o=0;o<r.length;o++){var f=r[o],i=f.getAttribute("data-href")||f.getAttribute("href");if("stylesheet"===f.rel&&(i===t||i===a))return n()}var d=document.getElementsByTagName("style");for(o=0;o<d.length;o++){f=d[o],i=f.getAttribute("data-href");if(i===t||i===a)return n()}var b=document.createElement("link");b.rel="stylesheet",b.type="text/css",b.onload=n,b.onerror=function(n){var t=n&&n.target&&n.target.src||a,r=new Error("Loading CSS chunk "+e+" failed.\n("+t+")");r.code="CSS_CHUNK_LOAD_FAILED",r.request=t,delete u[e],b.parentNode.removeChild(b),c(r)},b.href=a;var l=document.getElementsByTagName("head")[0];l.appendChild(b)})).then((function(){u[e]=0})));var t=a[e];if(0!==t)if(t)n.push(t[2]);else{var r=new Promise((function(n,c){t=a[e]=[n,c]}));n.push(t[2]=r);var f,i=document.createElement("script");i.charset="utf-8",i.timeout=120,h.nc&&i.setAttribute("nonce",h.nc),i.src=o(e);var d=new Error;f=function(n){i.onerror=i.onload=null,clearTimeout(b);var c=a[e];if(0!==c){if(c){var t=n&&("load"===n.type?"missing":n.type),u=n&&n.target&&n.target.src;d.message="Loading chunk "+e+" failed.\n("+t+": "+u+")",d.name="ChunkLoadError",d.type=t,d.request=u,c[1](d)}a[e]=void 0}};var b=setTimeout((function(){f({type:"timeout",target:i})}),12e4);i.onerror=i.onload=f,document.head.appendChild(i)}return Promise.all(n)},h.m=e,h.c=t,h.d=function(e,n,c){h.o(e,n)||Object.defineProperty(e,n,{enumerable:!0,get:c})},h.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},h.t=function(e,n){if(1&n&&(e=h(e)),8&n)return e;if(4&n&&"object"===typeof e&&e&&e.__esModule)return e;var c=Object.create(null);if(h.r(c),Object.defineProperty(c,"default",{enumerable:!0,value:e}),2&n&&"string"!=typeof e)for(var t in e)h.d(c,t,function(n){return e[n]}.bind(null,t));return c},h.n=function(e){var n=e&&e.__esModule?function(){return e["default"]}:function(){return e};return h.d(n,"a",n),n},h.o=function(e,n){return Object.prototype.hasOwnProperty.call(e,n)},h.p="",h.oe=function(e){throw console.error(e),e};var f=window["webpackJsonp"]=window["webpackJsonp"]||[],i=f.push.bind(f);f.push=n,f=f.slice();for(var d=0;d<f.length;d++)n(f[d]);var b=i;r.push([0,"chunk-vendors"]),c()})({0:function(e,n,c){e.exports=c("56d7")},"33ec":function(e,n,c){},"56d7":function(e,n,c){"use strict";c.r(n);c("e260"),c("e6cf"),c("cca6"),c("a79d");var t=c("2b0e"),u=function(){var e=this,n=e.$createElement,c=e._self._c||n;return c("v-app",[c("router-view")],1)},a=[],r={name:"App"},o=r,h=c("2877"),f=c("6544"),i=c.n(f),d=c("7496"),b=Object(h["a"])(o,u,a,!1,null,null,null),l=b.exports;i()(b,{VApp:d["a"]});c("d3b7"),c("3ca3"),c("ddb0");var s=c("8c4f");t["a"].use(s["a"]);var k=s["a"].prototype.push;s["a"].prototype.push=function(e){return k.call(this,e).catch((function(e){return e}))};var p=[{path:"/",name:"login_a",component:function(){return Promise.all([c.e("chunk-36591b79"),c.e("chunk-c88957a6"),c.e("chunk-113fbbd0"),c.e("chunk-599fea06"),c.e("chunk-1deb5f75")]).then(c.bind(null,"fc8a"))},meta:{hidden:!0}},{name:"首页",path:"/index_a",component:function(){return Promise.all([c.e("chunk-36591b79"),c.e("chunk-113fbbd0"),c.e("chunk-cae70e2a")]).then(c.bind(null,"b38f"))}},{name:"医院导览",path:"/tour",component:function(){return Promise.all([c.e("chunk-36591b79"),c.e("chunk-c88957a6"),c.e("chunk-113fbbd0"),c.e("chunk-599fea06"),c.e("chunk-a88408e6")]).then(c.bind(null,"37f6"))}},{name:"角色扮演",path:"/roleplay",component:function(){return Promise.all([c.e("chunk-36591b79"),c.e("chunk-5b528ffd")]).then(c.bind(null,"54d2"))}},{name:"医师扮演",path:"/roleplay/doctor",component:function(){return Promise.all([c.e("chunk-36591b79"),c.e("chunk-c88957a6"),c.e("chunk-113fbbd0"),c.e("chunk-599fea06"),c.e("chunk-7717860e")]).then(c.bind(null,"be82"))}},{name:"医助扮演",path:"/roleplay/assist",component:function(){return Promise.all([c.e("chunk-36591b79"),c.e("chunk-c88957a6"),c.e("chunk-113fbbd0"),c.e("chunk-599fea06"),c.e("chunk-7c96c12e")]).then(c.bind(null,"3db3"))}},{name:"前台扮演",path:"/roleplay/front",component:function(){return Promise.all([c.e("chunk-36591b79"),c.e("chunk-c88957a6"),c.e("chunk-113fbbd0"),c.e("chunk-599fea06"),c.e("chunk-7db4d4e2")]).then(c.bind(null,"7efd"))}},{name:"病例学习",path:"/case",component:function(){return Promise.all([c.e("chunk-36591b79"),c.e("chunk-113fbbd0"),c.e("chunk-65403dc5")]).then(c.bind(null,"9fe4"))}},{path:"/case/real",name:"CaseReal",component:function(){return Promise.all([c.e("chunk-36591b79"),c.e("chunk-c88957a6"),c.e("chunk-1f2c0e14")]).then(c.bind(null,"16e8"))},meta:{hidden:!0}},{name:"病例学习具体病例",path:"/case/item",component:function(){return Promise.all([c.e("chunk-36591b79"),c.e("chunk-c88957a6"),c.e("chunk-1c9fe97b")]).then(c.bind(null,"935d"))}},{name:"考核",path:"/exam",component:function(){return Promise.all([c.e("chunk-36591b79"),c.e("chunk-c88957a6"),c.e("chunk-113fbbd0"),c.e("chunk-599fea06"),c.e("chunk-70061e38")]).then(c.bind(null,"13b2"))}},{name:"试卷内容",path:"/exam/item",component:function(){return Promise.all([c.e("chunk-36591b79"),c.e("chunk-c88957a6"),c.e("chunk-113fbbd0"),c.e("chunk-2a190c3b")]).then(c.bind(null,"1a78"))}}],m=new s["a"]({mode:"hash",base:"/",routes:p}),v=m,g=c("2f62"),y={namespaced:!0,state:{msg:"",color:"",visible:!1,showClose:!0,timeout:5e3},mutations:{OPEN_SNACKBAR:function(e,n){e.visible=!0,e.msg=n.msg,e.color=n.color},CLOSE_SNACKBAR:function(e){e.visible=!1},setShowClose:function(e,n){e.showClose=n},setTimeout:function(e,n){e.timeout=n}},actions:{openSnackbar:function(e,n){var c=e.state.timeout;e.commit("OPEN_SNACKBAR",{msg:n.msg,color:n.color}),setTimeout((function(){e.commit("CLOSE_SNACKBAR")}),c)}}},w=y;t["a"].use(g["a"]);var P=new g["a"].Store({state:{},mutations:{},actions:{},modules:{snackbar:w}}),S=c("f309");t["a"].use(S["a"]);var A=new S["a"]({}),C=(c("33ec"),c("bc3a")),O=c.n(C);t["a"].config.productionTip=!1,O.a.interceptors.request.use((function(e){return e.headers.Authorization=window.sessionStorage.getItem("token"),e.headers.UserId=window.sessionStorage.getItem("userId"),e})),new t["a"]({router:v,store:P,vuetify:A,render:function(e){return e(l)}}).$mount("#app")}});
//# sourceMappingURL=app.3c17a32e.js.map