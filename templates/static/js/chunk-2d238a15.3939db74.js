(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d238a15"],{ffcb:function(e,t,n){"use strict";n.r(t);var s=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-radio-group",{on:{change:e.set_theme},model:{value:e.theme,callback:function(t){e.theme=t},expression:"theme"}},e._l(e.theme_data,(function(t,s){return n("el-radio",{key:s,attrs:{label:t.link}},[e._v(e._s(t.title))])})),1)},i=[],l={data:function(){return{theme:"@/style/eui_default/index.css",theme_data:[{title:"暗色主题",link:"./style/eui_dark/index.css"},{title:"默认主题",link:"./style/eui_default/index.css"}]}},methods:{set_theme:function(e){this.theme=e,document.getElementById("themeLinkId").href=e,sessionStorage.setItem("theme_link",e),this.$message.success("应用主题成功"),this.$emit("change_theme",!1)}},mounted:function(){null!=sessionStorage.getItem("theme_link")&&(this.theme=sessionStorage.getItem("theme_link"))}},a=l,u=n("2877"),o=Object(u["a"])(a,s,i,!1,null,null,null);t["default"]=o.exports}}]);