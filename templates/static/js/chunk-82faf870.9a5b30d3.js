(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-82faf870","chunk-35b90b0f","chunk-5e91d658","chunk-9033dcfa","chunk-093fce96"],{3206:function(t,e,i){"use strict";i.d(e,"a",(function(){return a})),i.d(e,"b",(function(){return c}));var n=i("ade3"),s=(i("99af"),i("2b0e")),r=i("d9bd");function o(t,e){return function(){return Object(r["c"])("The ".concat(t," component must be used inside a ").concat(e))}}function a(t,e,i){var r=e&&i?{register:o(e,i),unregister:o(e,i)}:null;return s["a"].extend({name:"registrable-inject",inject:Object(n["a"])({},t,{default:r})})}function c(t){var e=arguments.length>1&&void 0!==arguments[1]&&arguments[1];return s["a"].extend({name:"registrable-provide",provide:function(){return Object(n["a"])({},t,e?this:{register:this.register,unregister:this.unregister})}})}},"36a7":function(t,e,i){},"4e82":function(t,e,i){"use strict";i.d(e,"a",(function(){return r}));var n=i("ade3"),s=i("3206");function r(t,e,i){return Object(s["a"])(t,e,i).extend({name:"groupable",props:{activeClass:{type:String,default:function(){if(this[t])return this[t].activeClass}},disabled:Boolean},data:function(){return{isActive:!1}},computed:{groupClasses:function(){return this.activeClass?Object(n["a"])({},this.activeClass,this.isActive):{}}},created:function(){this[t]&&this[t].register(this)},beforeDestroy:function(){this[t]&&this[t].unregister(this)},methods:{toggle:function(){this.$emit("change")}}})}r("itemGroup")},"5e23":function(t,e,i){},8336:function(t,e,i){"use strict";var n=i("53ca"),s=i("3835"),r=i("5530"),o=(i("c7cd"),i("a9e3"),i("caad"),i("86cc"),i("10d2")),a=(i("99af"),i("8d4f"),i("a9ad")),c=i("80d2"),l=a["a"].extend({name:"v-progress-circular",props:{button:Boolean,indeterminate:Boolean,rotate:{type:[Number,String],default:0},size:{type:[Number,String],default:32},width:{type:[Number,String],default:4},value:{type:[Number,String],default:0}},data:function(){return{radius:20}},computed:{calculatedSize:function(){return Number(this.size)+(this.button?8:0)},circumference:function(){return 2*Math.PI*this.radius},classes:function(){return{"v-progress-circular--indeterminate":this.indeterminate,"v-progress-circular--button":this.button}},normalizedValue:function(){return this.value<0?0:this.value>100?100:parseFloat(this.value)},strokeDashArray:function(){return Math.round(1e3*this.circumference)/1e3},strokeDashOffset:function(){return(100-this.normalizedValue)/100*this.circumference+"px"},strokeWidth:function(){return Number(this.width)/+this.size*this.viewBoxSize*2},styles:function(){return{height:Object(c["e"])(this.calculatedSize),width:Object(c["e"])(this.calculatedSize)}},svgStyles:function(){return{transform:"rotate(".concat(Number(this.rotate),"deg)")}},viewBoxSize:function(){return this.radius/(1-Number(this.width)/+this.size)}},methods:{genCircle:function(t,e){return this.$createElement("circle",{class:"v-progress-circular__".concat(t),attrs:{fill:"transparent",cx:2*this.viewBoxSize,cy:2*this.viewBoxSize,r:this.radius,"stroke-width":this.strokeWidth,"stroke-dasharray":this.strokeDashArray,"stroke-dashoffset":e}})},genSvg:function(){var t=[this.indeterminate||this.genCircle("underlay",0),this.genCircle("overlay",this.strokeDashOffset)];return this.$createElement("svg",{style:this.svgStyles,attrs:{xmlns:"http://www.w3.org/2000/svg",viewBox:"".concat(this.viewBoxSize," ").concat(this.viewBoxSize," ").concat(2*this.viewBoxSize," ").concat(2*this.viewBoxSize)}},t)},genInfo:function(){return this.$createElement("div",{staticClass:"v-progress-circular__info"},this.$slots.default)}},render:function(t){return t("div",this.setTextColor(this.color,{staticClass:"v-progress-circular",attrs:{role:"progressbar","aria-valuemin":0,"aria-valuemax":100,"aria-valuenow":this.indeterminate?void 0:this.normalizedValue},class:this.classes,style:this.styles,on:this.$listeners}),[this.genSvg(),this.genInfo()])}}),h=l,u=i("4e82"),d=i("f2e7"),p=i("c995"),f=i("fe6c"),v=i("1c87"),g=i("af2b"),m=i("58df"),b=i("d9bd"),S=Object(m["a"])(o["a"],v["a"],f["a"],g["a"],Object(u["a"])("btnToggle"),Object(d["b"])("inputValue"));e["a"]=S.extend().extend({name:"v-btn",props:{activeClass:{type:String,default:function(){return this.btnToggle?this.btnToggle.activeClass:""}},block:Boolean,depressed:Boolean,fab:Boolean,icon:Boolean,loading:Boolean,outlined:Boolean,plain:Boolean,retainFocusOnClick:Boolean,rounded:Boolean,tag:{type:String,default:"button"},text:Boolean,tile:Boolean,type:{type:String,default:"button"},value:null},data:function(){return{proxyClass:"v-btn--active"}},computed:{classes:function(){return Object(r["a"])(Object(r["a"])(Object(r["a"])(Object(r["a"])(Object(r["a"])({"v-btn":!0},v["a"].options.computed.classes.call(this)),{},{"v-btn--absolute":this.absolute,"v-btn--block":this.block,"v-btn--bottom":this.bottom,"v-btn--disabled":this.disabled,"v-btn--is-elevated":this.isElevated,"v-btn--fab":this.fab,"v-btn--fixed":this.fixed,"v-btn--has-bg":this.hasBg,"v-btn--icon":this.icon,"v-btn--left":this.left,"v-btn--loading":this.loading,"v-btn--outlined":this.outlined,"v-btn--plain":this.plain,"v-btn--right":this.right,"v-btn--round":this.isRound,"v-btn--rounded":this.rounded,"v-btn--router":this.to,"v-btn--text":this.text,"v-btn--tile":this.tile,"v-btn--top":this.top},this.themeClasses),this.groupClasses),this.elevationClasses),this.sizeableClasses)},computedElevation:function(){if(!this.disabled)return p["a"].options.computed.computedElevation.call(this)},computedRipple:function(){var t,e=!this.icon&&!this.fab||{circle:!0};return!this.disabled&&(null!=(t=this.ripple)?t:e)},hasBg:function(){return!this.text&&!this.plain&&!this.outlined&&!this.icon},isElevated:function(){return Boolean(!this.icon&&!this.text&&!this.outlined&&!this.depressed&&!this.disabled&&!this.plain&&(null==this.elevation||Number(this.elevation)>0))},isRound:function(){return Boolean(this.icon||this.fab)},styles:function(){return Object(r["a"])({},this.measurableStyles)}},created:function(){var t=this,e=[["flat","text"],["outline","outlined"],["round","rounded"]];e.forEach((function(e){var i=Object(s["a"])(e,2),n=i[0],r=i[1];t.$attrs.hasOwnProperty(n)&&Object(b["a"])(n,r,t)}))},methods:{click:function(t){!this.retainFocusOnClick&&!this.fab&&t.detail&&this.$el.blur(),this.$emit("click",t),this.btnToggle&&this.toggle()},genContent:function(){return this.$createElement("span",{staticClass:"v-btn__content"},this.$slots.default)},genLoader:function(){return this.$createElement("span",{class:"v-btn__loader"},this.$slots.loader||[this.$createElement(h,{props:{indeterminate:!0,size:23,width:2}})])}},render:function(t){var e=[this.genContent(),this.loading&&this.genLoader()],i=this.generateRouteLink(),s=i.tag,r=i.data,o=this.hasBg?this.setBackgroundColor:this.setTextColor;return"button"===s&&(r.attrs.type=this.type,r.attrs.disabled=this.disabled),r.attrs.value=["string","number"].includes(Object(n["a"])(this.value))?this.value:JSON.stringify(this.value),t(s,this.disabled?r:o(this.color,r),e)}})},"86cc":function(t,e,i){},"8a79":function(t,e,i){"use strict";var n=i("23e7"),s=i("06cf").f,r=i("50c4"),o=i("5a34"),a=i("1d80"),c=i("ab13"),l=i("c430"),h="".endsWith,u=Math.min,d=c("endsWith"),p=!l&&!d&&!!function(){var t=s(String.prototype,"endsWith");return t&&!t.writable}();n({target:"String",proto:!0,forced:!p&&!d},{endsWith:function(t){var e=String(a(this));o(t);var i=arguments.length>1?arguments[1]:void 0,n=r(e.length),s=void 0===i?n:u(r(i),n),c=String(t);return h?h.call(e,c,s):e.slice(s-c.length,s)===c}})},"8b0d":function(t,e,i){},"8d4f":function(t,e,i){},"8efc":function(t,e,i){},"90a2":function(t,e,i){"use strict";var n=i("53ca");i("7db0");function s(t,e){var i=e.modifiers||{},s=e.value,o="object"===Object(n["a"])(s)?s:{handler:s,options:{}},a=o.handler,c=o.options,l=new IntersectionObserver((function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],n=arguments.length>1?arguments[1]:void 0;if(t._observe){if(a&&(!i.quiet||t._observe.init)){var s=Boolean(e.find((function(t){return t.isIntersecting})));a(e,n,s)}t._observe.init&&i.once?r(t):t._observe.init=!0}}),c);t._observe={init:!1,observer:l},l.observe(t)}function r(t){t._observe&&(t._observe.observer.unobserve(t),delete t._observe)}var o={inserted:s,unbind:r};e["a"]=o},adda:function(t,e,i){"use strict";var n=i("53ca"),s=(i("a9e3"),i("a15b"),i("8a79"),i("2ca0"),i("8efc"),i("90a2")),r=(i("36a7"),i("24b2")),o=i("58df"),a=Object(o["a"])(r["a"]).extend({name:"v-responsive",props:{aspectRatio:[String,Number],contentClass:String},computed:{computedAspectRatio:function(){return Number(this.aspectRatio)},aspectStyle:function(){return this.computedAspectRatio?{paddingBottom:1/this.computedAspectRatio*100+"%"}:void 0},__cachedSizer:function(){return this.aspectStyle?this.$createElement("div",{style:this.aspectStyle,staticClass:"v-responsive__sizer"}):[]}},methods:{genContent:function(){return this.$createElement("div",{staticClass:"v-responsive__content",class:this.contentClass},this.$slots.default)}},render:function(t){return t("div",{staticClass:"v-responsive",style:this.measurableStyles,on:this.$listeners},[this.__cachedSizer,this.genContent()])}}),c=a,l=i("7560"),h=i("d9f7"),u=i("d9bd"),d="undefined"!==typeof window&&"IntersectionObserver"in window;e["a"]=Object(o["a"])(c,l["a"]).extend({name:"v-img",directives:{intersect:s["a"]},props:{alt:String,contain:Boolean,eager:Boolean,gradient:String,lazySrc:String,options:{type:Object,default:function(){return{root:void 0,rootMargin:void 0,threshold:void 0}}},position:{type:String,default:"center center"},sizes:String,src:{type:[String,Object],default:""},srcset:String,transition:{type:[Boolean,String],default:"fade-transition"}},data:function(){return{currentSrc:"",image:null,isLoading:!0,calculatedAspectRatio:void 0,naturalWidth:void 0,hasError:!1}},computed:{computedAspectRatio:function(){return Number(this.normalisedSrc.aspect||this.calculatedAspectRatio)},normalisedSrc:function(){return this.src&&"object"===Object(n["a"])(this.src)?{src:this.src.src,srcset:this.srcset||this.src.srcset,lazySrc:this.lazySrc||this.src.lazySrc,aspect:Number(this.aspectRatio||this.src.aspect)}:{src:this.src,srcset:this.srcset,lazySrc:this.lazySrc,aspect:Number(this.aspectRatio||0)}},__cachedImage:function(){if(!(this.normalisedSrc.src||this.normalisedSrc.lazySrc||this.gradient))return[];var t=[],e=this.isLoading?this.normalisedSrc.lazySrc:this.currentSrc;this.gradient&&t.push("linear-gradient(".concat(this.gradient,")")),e&&t.push('url("'.concat(e,'")'));var i=this.$createElement("div",{staticClass:"v-image__image",class:{"v-image__image--preload":this.isLoading,"v-image__image--contain":this.contain,"v-image__image--cover":!this.contain},style:{backgroundImage:t.join(", "),backgroundPosition:this.position},key:+this.isLoading});return this.transition?this.$createElement("transition",{attrs:{name:this.transition,mode:"in-out"}},[i]):i}},watch:{src:function(){this.isLoading?this.loadImage():this.init(void 0,void 0,!0)},"$vuetify.breakpoint.width":"getSrc"},mounted:function(){this.init()},methods:{init:function(t,e,i){if(!d||i||this.eager){if(this.normalisedSrc.lazySrc){var n=new Image;n.src=this.normalisedSrc.lazySrc,this.pollForSize(n,null)}this.normalisedSrc.src&&this.loadImage()}},onLoad:function(){this.getSrc(),this.isLoading=!1,this.$emit("load",this.src),this.image&&(this.normalisedSrc.src.endsWith(".svg")||this.normalisedSrc.src.startsWith("data:image/svg+xml"))&&(this.image.naturalHeight&&this.image.naturalWidth?(this.naturalWidth=this.image.naturalWidth,this.calculatedAspectRatio=this.image.naturalWidth/this.image.naturalHeight):this.calculatedAspectRatio=1)},onError:function(){this.hasError=!0,this.$emit("error",this.src)},getSrc:function(){this.image&&(this.currentSrc=this.image.currentSrc||this.image.src)},loadImage:function(){var t=this,e=new Image;this.image=e,e.onload=function(){e.decode?e.decode().catch((function(e){Object(u["c"])("Failed to decode image, trying to render anyway\n\n"+"src: ".concat(t.normalisedSrc.src)+(e.message?"\nOriginal error: ".concat(e.message):""),t)})).then(t.onLoad):t.onLoad()},e.onerror=this.onError,this.hasError=!1,e.src=this.normalisedSrc.src,this.sizes&&(e.sizes=this.sizes),this.normalisedSrc.srcset&&(e.srcset=this.normalisedSrc.srcset),this.aspectRatio||this.pollForSize(e),this.getSrc()},pollForSize:function(t){var e=this,i=arguments.length>1&&void 0!==arguments[1]?arguments[1]:100,n=function n(){var s=t.naturalHeight,r=t.naturalWidth;s||r?(e.naturalWidth=r,e.calculatedAspectRatio=r/s):t.complete||!e.isLoading||e.hasError||null==i||setTimeout(n,i)};n()},genContent:function(){var t=c.options.methods.genContent.call(this);return this.naturalWidth&&this._b(t.data,"div",{style:{width:"".concat(this.naturalWidth,"px")}}),t},__genPlaceholder:function(){if(this.$slots.placeholder){var t=this.isLoading?[this.$createElement("div",{staticClass:"v-image__placeholder"},this.$slots.placeholder)]:[];return this.transition?this.$createElement("transition",{props:{appear:!0,name:this.transition}},t):t[0]}}},render:function(t){var e=c.options.render.call(this,t),i=Object(h["a"])(e.data,{staticClass:"v-image",attrs:{"aria-label":this.alt,role:this.alt?"img":void 0},class:this.themeClasses,directives:d?[{name:"intersect",modifiers:{once:!0},value:{handler:this.init,options:this.options}}]:void 0});return e.children=[this.__cachedSizer,this.__cachedImage,this.__genPlaceholder(),this.genContent()],t(e.tag,i,e.children)}})},af2b:function(t,e,i){"use strict";i("c96a");var n=i("2b0e");e["a"]=n["a"].extend({name:"sizeable",props:{large:Boolean,small:Boolean,xLarge:Boolean,xSmall:Boolean},computed:{medium:function(){return Boolean(!this.xSmall&&!this.small&&!this.large&&!this.xLarge)},sizeableClasses:function(){return{"v-size--x-small":this.xSmall,"v-size--small":this.small,"v-size--default":this.medium,"v-size--large":this.large,"v-size--x-large":this.xLarge}}}})},c96a:function(t,e,i){"use strict";var n=i("23e7"),s=i("857a"),r=i("af03");n({target:"String",proto:!0,forced:r("small")},{small:function(){return s(this,"small","","")}})},cf05:function(t,e,i){t.exports=i.p+"static/img/logo.4ce643e1.png"},d10f:function(t,e,i){"use strict";var n=i("2b0e");e["a"]=n["a"].extend({name:"ssr-bootable",data:function(){return{isBooted:!1}},mounted:function(){var t=this;window.requestAnimationFrame((function(){t.$el.setAttribute("data-booted","true"),t.isBooted=!0}))}})},d3dd:function(t,e,i){},dfe6:function(t,e,i){"use strict";i.r(e);var n=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("v-app-bar",{attrs:{app:"",height:"70",color:"indigo lighten-4"}},[n("v-toolbar-title",[n("v-img",{attrs:{src:i("cf05"),width:"80",height:"80"}})],1),t._l(t.items,(function(e,i){return n("v-btn",{key:i,staticClass:"home-btn",attrs:{rounded:"",color:"light-blue lighten-2",width:"100px",to:t.getPath(e)}},[t._v(" "+t._s(e.name)+" ")])})),n("v-spacer"),n("span",{staticStyle:{"margin-right":"30px"}},[t._v(t._s(t.user.name))]),n("v-btn",{attrs:{href:"#",color:"light-blue lighten-2"},on:{click:t.logout}},[t._v("退出登录")])],2)],1)},s=[],r=(i("b0c0"),{name:"NavbarMenu",data:function(){return{items:[{name:"首页",path:"/index_a"},{name:"医院导览",path:"/tour"},{name:"角色扮演",path:"/roleplay"},{name:"病例学习",path:"/case"},{name:"考核",path:"/exam"}],bool:!1,user:{name:"test",email:"",password:""},is_login:!0}},created:function(){this.user.name=window.sessionStorage.getItem("userName")},methods:{getPath:function(t){return t.path},logout:function(){window.sessionStorage.clear(),window.location.href="http://127.0.0.1:5000"}}}),o=r,a=(i("e959"),i("2877")),c=i("6544"),l=i.n(c),h=i("5530"),u=(i("c7cd"),i("a9e3"),i("8b0d"),i("3835")),d=(i("0481"),i("5e23"),i("8dd9")),p=i("adda"),f=i("80d2"),v=i("d9bd"),g=d["a"].extend({name:"v-toolbar",props:{absolute:Boolean,bottom:Boolean,collapse:Boolean,dense:Boolean,extended:Boolean,extensionHeight:{default:48,type:[Number,String]},flat:Boolean,floating:Boolean,prominent:Boolean,short:Boolean,src:{type:[String,Object],default:""},tag:{type:String,default:"header"}},data:function(){return{isExtended:!1}},computed:{computedHeight:function(){var t=this.computedContentHeight;if(!this.isExtended)return t;var e=parseInt(this.extensionHeight);return this.isCollapsed?t:t+(isNaN(e)?0:e)},computedContentHeight:function(){return this.height?parseInt(this.height):this.isProminent&&this.dense?96:this.isProminent&&this.short?112:this.isProminent?128:this.dense?48:this.short||this.$vuetify.breakpoint.smAndDown?56:64},classes:function(){return Object(h["a"])(Object(h["a"])({},d["a"].options.computed.classes.call(this)),{},{"v-toolbar":!0,"v-toolbar--absolute":this.absolute,"v-toolbar--bottom":this.bottom,"v-toolbar--collapse":this.collapse,"v-toolbar--collapsed":this.isCollapsed,"v-toolbar--dense":this.dense,"v-toolbar--extended":this.isExtended,"v-toolbar--flat":this.flat,"v-toolbar--floating":this.floating,"v-toolbar--prominent":this.isProminent})},isCollapsed:function(){return this.collapse},isProminent:function(){return this.prominent},styles:function(){return Object(h["a"])(Object(h["a"])({},this.measurableStyles),{},{height:Object(f["e"])(this.computedHeight)})}},created:function(){var t=this,e=[["app","<v-app-bar app>"],["manual-scroll",'<v-app-bar :value="false">'],["clipped-left","<v-app-bar clipped-left>"],["clipped-right","<v-app-bar clipped-right>"],["inverted-scroll","<v-app-bar inverted-scroll>"],["scroll-off-screen","<v-app-bar scroll-off-screen>"],["scroll-target","<v-app-bar scroll-target>"],["scroll-threshold","<v-app-bar scroll-threshold>"],["card","<v-app-bar flat>"]];e.forEach((function(e){var i=Object(u["a"])(e,2),n=i[0],s=i[1];t.$attrs.hasOwnProperty(n)&&Object(v["a"])(n,s,t)}))},methods:{genBackground:function(){var t={height:Object(f["e"])(this.computedHeight),src:this.src},e=this.$scopedSlots.img?this.$scopedSlots.img({props:t}):this.$createElement(p["a"],{props:t});return this.$createElement("div",{staticClass:"v-toolbar__image"},[e])},genContent:function(){return this.$createElement("div",{staticClass:"v-toolbar__content",style:{height:Object(f["e"])(this.computedContentHeight)}},Object(f["p"])(this))},genExtension:function(){return this.$createElement("div",{staticClass:"v-toolbar__extension",style:{height:Object(f["e"])(this.extensionHeight)}},Object(f["p"])(this,"extension"))}},render:function(t){this.isExtended=this.extended||!!this.$scopedSlots.extension;var e=[this.genContent()],i=this.setBackgroundColor(this.color,{class:this.classes,style:this.styles,on:this.$listeners});return this.isExtended&&e.push(this.genExtension()),(this.src||this.$scopedSlots.img)&&e.unshift(this.genBackground()),t(this.tag,i,e)}}),m=i("53ca");function b(t,e){var i=e.modifiers||{},n=i.self,s=void 0!==n&&n,r=e.value,o="object"===Object(m["a"])(r)&&r.options||{passive:!0},a="function"===typeof r||"handleEvent"in r?r:r.handler,c=s?t:e.arg?document.querySelector(e.arg):window;c&&(c.addEventListener("scroll",a,o),t._onScroll={handler:a,options:o,target:s?void 0:c})}function S(t){if(t._onScroll){var e=t._onScroll,i=e.handler,n=e.options,s=e.target,r=void 0===s?t:s;r.removeEventListener("scroll",i,n),delete t._onScroll}}var O={inserted:b,unbind:S},y=O,x=i("fe6c"),_=i("58df");function B(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[];return Object(_["a"])(Object(x["b"])(["absolute","fixed"])).extend({name:"applicationable",props:{app:Boolean},computed:{applicationProperty:function(){return t}},watch:{app:function(t,e){e?this.removeApplication(!0):this.callUpdate()},applicationProperty:function(t,e){this.$vuetify.application.unregister(this._uid,e)}},activated:function(){this.callUpdate()},created:function(){for(var t=0,i=e.length;t<i;t++)this.$watch(e[t],this.callUpdate);this.callUpdate()},mounted:function(){this.callUpdate()},deactivated:function(){this.removeApplication()},destroyed:function(){this.removeApplication()},methods:{callUpdate:function(){this.app&&this.$vuetify.application.register(this._uid,this.applicationProperty,this.updateApplication())},removeApplication:function(){var t=arguments.length>0&&void 0!==arguments[0]&&arguments[0];(t||this.app)&&this.$vuetify.application.unregister(this._uid,this.applicationProperty)},updateApplication:function(){return 0}}})}var j=i("2b0e"),w=j["a"].extend({name:"scrollable",directives:{Scroll:O},props:{scrollTarget:String,scrollThreshold:[String,Number]},data:function(){return{currentScroll:0,currentThreshold:0,isActive:!1,isScrollingUp:!1,previousScroll:0,savedScroll:0,target:null}},computed:{canScroll:function(){return"undefined"!==typeof window},computedScrollThreshold:function(){return this.scrollThreshold?Number(this.scrollThreshold):300}},watch:{isScrollingUp:function(){this.savedScroll=this.savedScroll||this.currentScroll},isActive:function(){this.savedScroll=0}},mounted:function(){this.scrollTarget&&(this.target=document.querySelector(this.scrollTarget),this.target||Object(v["c"])("Unable to locate element with identifier ".concat(this.scrollTarget),this))},methods:{onScroll:function(){var t=this;this.canScroll&&(this.previousScroll=this.currentScroll,this.currentScroll=this.target?this.target.scrollTop:window.pageYOffset,this.isScrollingUp=this.currentScroll<this.previousScroll,this.currentThreshold=Math.abs(this.currentScroll-this.computedScrollThreshold),this.$nextTick((function(){Math.abs(t.currentScroll-t.savedScroll)>t.computedScrollThreshold&&t.thresholdMet()})))},thresholdMet:function(){}}}),C=i("d10f"),z=i("f2e7"),$=Object(_["a"])(g,w,C["a"],z["a"],B("top",["clippedLeft","clippedRight","computedHeight","invertedScroll","isExtended","isProminent","value"])),k=$.extend({name:"v-app-bar",directives:{Scroll:y},provide:function(){return{VAppBar:this}},props:{clippedLeft:Boolean,clippedRight:Boolean,collapseOnScroll:Boolean,elevateOnScroll:Boolean,fadeImgOnScroll:Boolean,hideOnScroll:Boolean,invertedScroll:Boolean,scrollOffScreen:Boolean,shrinkOnScroll:Boolean,value:{type:Boolean,default:!0}},data:function(){return{isActive:this.value}},computed:{applicationProperty:function(){return this.bottom?"bottom":"top"},canScroll:function(){return w.options.computed.canScroll.call(this)&&(this.invertedScroll||this.elevateOnScroll||this.hideOnScroll||this.collapseOnScroll||this.isBooted||!this.value)},classes:function(){return Object(h["a"])(Object(h["a"])({},g.options.computed.classes.call(this)),{},{"v-toolbar--collapse":this.collapse||this.collapseOnScroll,"v-app-bar":!0,"v-app-bar--clipped":this.clippedLeft||this.clippedRight,"v-app-bar--fade-img-on-scroll":this.fadeImgOnScroll,"v-app-bar--elevate-on-scroll":this.elevateOnScroll,"v-app-bar--fixed":!this.absolute&&(this.app||this.fixed),"v-app-bar--hide-shadow":this.hideShadow,"v-app-bar--is-scrolled":this.currentScroll>0,"v-app-bar--shrink-on-scroll":this.shrinkOnScroll})},scrollRatio:function(){var t=this.computedScrollThreshold;return Math.max((t-this.currentScroll)/t,0)},computedContentHeight:function(){if(!this.shrinkOnScroll)return g.options.computed.computedContentHeight.call(this);var t=this.dense?48:56,e=this.computedOriginalHeight;return t+(e-t)*this.scrollRatio},computedFontSize:function(){if(this.isProminent){var t=1.25,e=1.5;return t+(e-t)*this.scrollRatio}},computedLeft:function(){return!this.app||this.clippedLeft?0:this.$vuetify.application.left},computedMarginTop:function(){return this.app?this.$vuetify.application.bar:0},computedOpacity:function(){if(this.fadeImgOnScroll)return this.scrollRatio},computedOriginalHeight:function(){var t=g.options.computed.computedContentHeight.call(this);return this.isExtended&&(t+=parseInt(this.extensionHeight)),t},computedRight:function(){return!this.app||this.clippedRight?0:this.$vuetify.application.right},computedScrollThreshold:function(){return this.scrollThreshold?Number(this.scrollThreshold):this.computedOriginalHeight-(this.dense?48:56)},computedTransform:function(){if(!this.canScroll||this.elevateOnScroll&&0===this.currentScroll&&this.isActive)return 0;if(this.isActive)return 0;var t=this.scrollOffScreen?this.computedHeight:this.computedContentHeight;return this.bottom?t:-t},hideShadow:function(){return this.elevateOnScroll&&this.isExtended?this.currentScroll<this.computedScrollThreshold:this.elevateOnScroll?0===this.currentScroll||this.computedTransform<0:(!this.isExtended||this.scrollOffScreen)&&0!==this.computedTransform},isCollapsed:function(){return this.collapseOnScroll?this.currentScroll>0:g.options.computed.isCollapsed.call(this)},isProminent:function(){return g.options.computed.isProminent.call(this)||this.shrinkOnScroll},styles:function(){return Object(h["a"])(Object(h["a"])({},g.options.computed.styles.call(this)),{},{fontSize:Object(f["e"])(this.computedFontSize,"rem"),marginTop:Object(f["e"])(this.computedMarginTop),transform:"translateY(".concat(Object(f["e"])(this.computedTransform),")"),left:Object(f["e"])(this.computedLeft),right:Object(f["e"])(this.computedRight)})}},watch:{canScroll:"onScroll",computedTransform:function(){this.canScroll&&(this.clippedLeft||this.clippedRight)&&this.callUpdate()},invertedScroll:function(t){this.isActive=!t||0!==this.currentScroll}},created:function(){this.invertedScroll&&(this.isActive=!1)},methods:{genBackground:function(){var t=g.options.methods.genBackground.call(this);return t.data=this._b(t.data||{},t.tag,{style:{opacity:this.computedOpacity}}),t},updateApplication:function(){return this.invertedScroll?0:this.computedHeight+this.computedTransform},thresholdMet:function(){this.invertedScroll?this.isActive=this.currentScroll>this.computedScrollThreshold:(this.hideOnScroll&&(this.isActive=this.isScrollingUp||this.currentScroll<this.computedScrollThreshold),this.currentThreshold<this.computedScrollThreshold||(this.savedScroll=this.currentScroll))}},render:function(t){var e=g.options.render.call(this,t);return e.data=e.data||{},this.canScroll&&(e.data.directives=e.data.directives||[],e.data.directives.push({arg:this.scrollTarget,name:"scroll",value:this.onScroll})),e}}),E=i("8336"),T=(i("20f6"),Object(f["f"])("spacer","div","v-spacer")),A=Object(f["f"])("v-toolbar__title"),R=(Object(f["f"])("v-toolbar__items"),Object(a["a"])(o,n,s,!1,null,"7722c1d8",null));e["default"]=R.exports;l()(R,{VAppBar:k,VBtn:E["a"],VImg:p["a"],VSpacer:T,VToolbarTitle:A})},e959:function(t,e,i){"use strict";i("d3dd")},f2e7:function(t,e,i){"use strict";i.d(e,"b",(function(){return r}));var n=i("ade3"),s=i("2b0e");function r(){var t,e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"value",i=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"input";return s["a"].extend({name:"toggleable",model:{prop:e,event:i},props:Object(n["a"])({},e,{required:!1}),data:function(){return{isActive:!!this[e]}},watch:(t={},Object(n["a"])(t,e,(function(t){this.isActive=!!t})),Object(n["a"])(t,"isActive",(function(t){!!t!==this[e]&&this.$emit(i,t)})),t)})}var o=r();e["a"]=o}}]);
//# sourceMappingURL=chunk-82faf870.9a5b30d3.js.map