(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-e27b216e"],{c79e:function(e,t,n){"use strict";n.r(t);var a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"body"},[n("el-breadcrumb",{attrs:{"separator-class":"el-icon-arrow-right"}},[n("el-breadcrumb-item",{attrs:{to:{path:"/home"}}},[e._v("首页")]),n("el-breadcrumb-item",[e._v("病种管理")]),n("el-breadcrumb-item",[e._v("病种增加")])],1),n("div",{staticClass:"main"},[n("el-collapse",{attrs:{accordion:""},on:{change:e.handleChange},model:{value:e.activeNames,callback:function(t){e.activeNames=t},expression:"activeNames"}},[n("el-collapse-item",{attrs:{title:"寄生虫病",name:"1"}},[e._l(e.dynamicTags,(function(t){return n("el-tag",{key:t,attrs:{closable:"","disable-transitions":!1},on:{close:function(n){return e.handleClose(t)}}},[e._v(" "+e._s(t)+" ")])})),e.inputVisible?n("el-input",{ref:"saveTagInput",staticClass:"input-new-tag",attrs:{size:"small"},on:{blur:e.handleInputConfirm},nativeOn:{keyup:function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.handleInputConfirm(t)}},model:{value:e.inputValue,callback:function(t){e.inputValue=t},expression:"inputValue"}}):n("el-button",{staticClass:"button-new-tag",attrs:{size:"small"},on:{click:e.showInput}},[e._v("+ New Tag")])],2),n("el-collapse-item",{attrs:{title:"内科病",name:"2"}},[e._l(e.dynamicTags,(function(t){return n("el-tag",{key:t,attrs:{closable:"","disable-transitions":!1},on:{close:function(n){return e.handleClose(t)}}},[e._v(" "+e._s(t)+" ")])})),e.inputVisible?n("el-input",{ref:"saveTagInput",staticClass:"input-new-tag",attrs:{size:"small"},on:{blur:e.handleInputConfirm},nativeOn:{keyup:function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.handleInputConfirm(t)}},model:{value:e.inputValue,callback:function(t){e.inputValue=t},expression:"inputValue"}}):n("el-button",{staticClass:"button-new-tag",attrs:{size:"small"},on:{click:e.showInput}},[e._v("+ New Tag")])],2),n("el-collapse-item",{attrs:{title:"外科病",name:"3"}},[e._l(e.dynamicTags,(function(t){return n("el-tag",{key:t,attrs:{closable:"","disable-transitions":!1},on:{close:function(n){return e.handleClose(t)}}},[e._v(" "+e._s(t)+" ")])})),e.inputVisible?n("el-input",{ref:"saveTagInput",staticClass:"input-new-tag",attrs:{size:"small"},on:{blur:e.handleInputConfirm},nativeOn:{keyup:function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.handleInputConfirm(t)}},model:{value:e.inputValue,callback:function(t){e.inputValue=t},expression:"inputValue"}}):n("el-button",{staticClass:"button-new-tag",attrs:{size:"small"},on:{click:e.showInput}},[e._v("+ New Tag")])],2),n("el-collapse-item",{attrs:{title:"神经科",name:"4"}},[e._l(e.dynamicTags,(function(t){return n("el-tag",{key:t,attrs:{closable:"","disable-transitions":!1},on:{close:function(n){return e.handleClose(t)}}},[e._v(" "+e._s(t)+" ")])})),e.inputVisible?n("el-input",{ref:"saveTagInput",staticClass:"input-new-tag",attrs:{size:"small"},on:{blur:e.handleInputConfirm},nativeOn:{keyup:function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.handleInputConfirm(t)}},model:{value:e.inputValue,callback:function(t){e.inputValue=t},expression:"inputValue"}}):n("el-button",{staticClass:"button-new-tag",attrs:{size:"small"},on:{click:e.showInput}},[e._v("+ New Tag")])],2)],1)],1)],1)},i=[],l=(n("c975"),n("a434"),{data:function(){return{activeNames:["1"],dynamicTags:["病种一","病种二","病种三"],inputVisible:!1,inputValue:""}},methods:{handleChange:function(e){console.log(e)},handleClose:function(e){this.dynamicTags.splice(this.dynamicTags.indexOf(e),1)},showInput:function(){var e=this;this.inputVisible=!0,this.$nextTick((function(t){e.$refs.saveTagInput.$refs.input.focus()}))},handleInputConfirm:function(){var e=this.inputValue;e&&this.dynamicTags.push(e),this.inputVisible=!1,this.inputValue=""}}}),s=l,u=(n("f2f4"),n("2877")),o=Object(u["a"])(s,a,i,!1,null,null,null);t["default"]=o.exports},c975:function(e,t,n){"use strict";var a=n("23e7"),i=n("4d64").indexOf,l=n("a640"),s=n("ae40"),u=[].indexOf,o=!!u&&1/[1].indexOf(1,-0)<0,r=l("indexOf"),c=s("indexOf",{ACCESSORS:!0,1:0});a({target:"Array",proto:!0,forced:o||!r||!c},{indexOf:function(e){return o?u.apply(this,arguments)||0:i(this,e,arguments.length>1?arguments[1]:void 0)}})},f2f4:function(e,t,n){"use strict";var a=n("f60a"),i=n.n(a);i.a},f60a:function(e,t,n){}}]);