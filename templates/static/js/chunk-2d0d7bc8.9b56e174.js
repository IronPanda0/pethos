(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0d7bc8"],{"77a3":function(e,t,l){"use strict";l.r(t);var o=function(){var e=this,t=e.$createElement,l=e._self._c||t;return l("div",[l("el-card",{attrs:{shadow:"never"}},[l("div",{attrs:{slot:"header"},slot:"header"},[e._v("网站设置")]),l("div",{staticStyle:{"min-height":"60vh"}},[l("el-form",{ref:"form",attrs:{size:"small",model:e.form,"label-width":"100px"}},[l("el-form-item",{attrs:{label:"网站名称"}},[l("el-input",{model:{value:e.form.web_name,callback:function(t){e.$set(e.form,"web_name",t)},expression:"form.web_name"}})],1),l("el-form-item",{attrs:{label:"网站网址"}},[l("el-input",{model:{value:e.form.web_link,callback:function(t){e.$set(e.form,"web_link",t)},expression:"form.web_link"}})],1),l("el-form-item",{attrs:{label:"文件前缀链接"}},[l("el-input",{model:{value:e.form.file_web_link,callback:function(t){e.$set(e.form,"file_web_link",t)},expression:"form.file_web_link"}})],1),l("el-form-item",{attrs:{label:"文件上传最大"}},[l("el-input-number",{attrs:{min:1,max:1e3,label:"描述文字"},on:{change:e.handleChange},model:{value:e.form.file_max_size,callback:function(t){e.$set(e.form,"file_max_size",t)},expression:"form.file_max_size"}}),e._v(" MB ")],1),l("el-form-item",{attrs:{label:"MATE描述"}},[l("el-input",{attrs:{type:"textarea",rows:3},model:{value:e.form.web_mate_content,callback:function(t){e.$set(e.form,"web_mate_content",t)},expression:"form.web_mate_content"}})],1),l("el-form-item",{attrs:{label:"网站版权"}},[l("el-input",{attrs:{type:"textarea",rows:2},model:{value:e.form.web_copyright,callback:function(t){e.$set(e.form,"web_copyright",t)},expression:"form.web_copyright"}})],1),l("el-form-item",[l("el-button",{attrs:{type:"primary"},on:{click:e.onSubmit}},[e._v("保存设置")])],1)],1)],1)])],1)},i=[],n={data:function(){return{form:{web_name:"PetHospital-Admin",web_link:"http://www.PetHospital-Admin.com",file_web_link:"http://www.PetHospital-Admin.com/public/file",file_max_size:12,web_mate_content:"PetHospital-Admin是基于Vue加Element-Ui共同构建，快速开发学习的整体后台框架。",web_copyright:"©2019黔1920号"}}},methods:{onSubmit:function(){console.log("submit!")}}},a=n,r=l("2877"),m=Object(r["a"])(a,o,i,!1,null,null,null);t["default"]=m.exports}}]);