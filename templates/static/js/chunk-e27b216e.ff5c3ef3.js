(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-e27b216e"],{c79e:function(e,n,t){"use strict";t.r(n);var a=function(){var e=this,n=e.$createElement,t=e._self._c||n;return t("div",{staticClass:"body"},[t("el-breadcrumb",{attrs:{"separator-class":"el-icon-arrow-right"}},[t("el-breadcrumb-item",{attrs:{to:{path:"/home"}}},[e._v("首页")]),t("el-breadcrumb-item",[e._v("病种管理")]),t("el-breadcrumb-item",[e._v("病种增加")])],1),t("div",{staticClass:"main"},[t("el-collapse",{attrs:{accordion:""},on:{change:e.handleChange},model:{value:e.activeNames,callback:function(n){e.activeNames=n},expression:"activeNames"}},[t("el-collapse-item",{attrs:{title:"传染病",name:"1"}},[e._l(e.dynamicTags,(function(n){return t("el-tag",{key:n,attrs:{closable:"","disable-transitions":!1},on:{close:function(t){return e.handleClose(n)}}},[e._v(" "+e._s(n)+" ")])})),e.inputVisible?t("el-input",{ref:"saveTagInput",staticClass:"input-new-tag",on:{blur:e.handleInputConfirm},nativeOn:{keyup:function(n){return!n.type.indexOf("key")&&e._k(n.keyCode,"enter",13,n.key,"Enter")?null:e.handleInputConfirm(n)}},model:{value:e.inputValue,callback:function(n){e.inputValue=n},expression:"inputValue"}}):t("el-button",{staticClass:"button-new-tag",on:{click:e.showInput}},[e._v("+ New Tag")])],2),t("el-collapse-item",{attrs:{title:"寄生虫病",name:"2"}},[e._l(e.dynamicTags,(function(n){return t("el-tag",{key:n,attrs:{closable:"","disable-transitions":!1},on:{close:function(t){return e.handleClose(n)}}},[e._v(" "+e._s(n)+" ")])})),e.inputVisible?t("el-input",{ref:"saveTagInput",staticClass:"input-new-tag",attrs:{type:"success"},on:{blur:e.handleInputConfirm},nativeOn:{keyup:function(n){return!n.type.indexOf("key")&&e._k(n.keyCode,"enter",13,n.key,"Enter")?null:e.handleInputConfirm(n)}},model:{value:e.inputValue,callback:function(n){e.inputValue=n},expression:"inputValue"}}):t("el-button",{staticClass:"button-new-tag",on:{click:e.showInput}},[e._v("+ New Tag")])],2),t("el-collapse-item",{attrs:{title:"内科",name:"3"}},[e._l(e.dynamicTags,(function(n){return t("el-tag",{key:n,attrs:{closable:"","disable-transitions":!1},on:{close:function(t){return e.handleClose(n)}}},[e._v(" "+e._s(n)+" ")])})),e.inputVisible?t("el-input",{ref:"saveTagInput",staticClass:"input-new-tag",on:{blur:e.handleInputConfirm},nativeOn:{keyup:function(n){return!n.type.indexOf("key")&&e._k(n.keyCode,"enter",13,n.key,"Enter")?null:e.handleInputConfirm(n)}},model:{value:e.inputValue,callback:function(n){e.inputValue=n},expression:"inputValue"}}):t("el-button",{staticClass:"button-new-tag",on:{click:e.showInput}},[e._v("+ New Tag")])],2),t("el-collapse-item",{attrs:{title:"神经科",name:"4"}},[e._l(e.dynamicTags,(function(n){return t("el-tag",{key:n,attrs:{closable:"","disable-transitions":!1},on:{close:function(t){return e.handleClose(n)}}},[e._v(" "+e._s(n)+" ")])})),e.inputVisible?t("el-input",{ref:"saveTagInput",staticClass:"input-new-tag",on:{blur:e.handleInputConfirm},nativeOn:{keyup:function(n){return!n.type.indexOf("key")&&e._k(n.keyCode,"enter",13,n.key,"Enter")?null:e.handleInputConfirm(n)}},model:{value:e.inputValue,callback:function(n){e.inputValue=n},expression:"inputValue"}}):t("el-button",{staticClass:"button-new-tag",on:{click:e.showInput}},[e._v("+ New Tag")])],2),t("el-collapse-item",{attrs:{title:"常用手术",name:"5"}},[e._l(e.dynamicTags,(function(n){return t("el-tag",{key:n,attrs:{closable:"","disable-transitions":!1},on:{close:function(t){return e.handleClose(n)}}},[e._v(" "+e._s(n)+" ")])})),e.inputVisible?t("el-input",{ref:"saveTagInput",staticClass:"input-new-tag",on:{blur:e.handleInputConfirm},nativeOn:{keyup:function(n){return!n.type.indexOf("key")&&e._k(n.keyCode,"enter",13,n.key,"Enter")?null:e.handleInputConfirm(n)}},model:{value:e.inputValue,callback:function(n){e.inputValue=n},expression:"inputValue"}}):t("el-button",{staticClass:"button-new-tag",on:{click:e.showInput}},[e._v("+ New Tag")])],2),t("el-collapse-item",{attrs:{title:"免疫",name:"6"}},[e._l(e.dynamicTags,(function(n){return t("el-tag",{key:n,attrs:{closable:"","disable-transitions":!1},on:{close:function(t){return e.handleClose(n)}}},[e._v(" "+e._s(n)+" ")])})),e.inputVisible?t("el-input",{ref:"saveTagInput",staticClass:"input-new-tag",on:{blur:e.handleInputConfirm},nativeOn:{keyup:function(n){return!n.type.indexOf("key")&&e._k(n.keyCode,"enter",13,n.key,"Enter")?null:e.handleInputConfirm(n)}},model:{value:e.inputValue,callback:function(n){e.inputValue=n},expression:"inputValue"}}):t("el-button",{staticClass:"button-new-tag",on:{click:e.showInput}},[e._v("+ New Tag")])],2)],1)],1)],1)},i=[],l=(t("c975"),t("a434"),{data:function(){return{activeNames:["1"],dynamicTags:["病种一","病种二","病种三"],inputVisible:!1,inputValue:""}},methods:{handleChange:function(e){console.log(e)},handleClose:function(e){this.dynamicTags.splice(this.dynamicTags.indexOf(e),1)},showInput:function(){var e=this;this.inputVisible=!0,this.$nextTick((function(n){e.$refs.saveTagInput.$refs.input.focus()}))},handleInputConfirm:function(){var e=this.inputValue;e&&this.dynamicTags.push(e),this.inputVisible=!1,this.inputValue=""}}}),u=l,s=(t("f2f4"),t("2877")),o=Object(s["a"])(u,a,i,!1,null,null,null);n["default"]=o.exports},c975:function(e,n,t){"use strict";var a=t("23e7"),i=t("4d64").indexOf,l=t("a640"),u=t("ae40"),s=[].indexOf,o=!!s&&1/[1].indexOf(1,-0)<0,r=l("indexOf"),c=u("indexOf",{ACCESSORS:!0,1:0});a({target:"Array",proto:!0,forced:o||!r||!c},{indexOf:function(e){return o?s.apply(this,arguments)||0:i(this,e,arguments.length>1?arguments[1]:void 0)}})},f2f4:function(e,n,t){"use strict";var a=t("f60a"),i=t.n(a);i.a},f60a:function(e,n,t){}}]);