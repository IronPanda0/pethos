(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-3c7d5a98"],{"66f2":function(e,a,n){"use strict";n.r(a);var t=function(){var e=this,a=e.$createElement,n=e._self._c||a;return n("div",[n("el-card",{staticClass:"card",attrs:{shadow:"never"}},[n("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[n("span",[e._v("EuiTable")])]),n("vEuiTable",{attrs:{columns:e.columns,data:e.data},on:{edit:e.edit,remove:e.remove}})],1)],1)},o=[],s=(n("b0c0"),{data:function(){return{columns:[{name:"用户名",prop:"name"},{name:"电话号码",prop:"phone"},{name:"年龄",prop:"age"}],data:[{name:"小明",phone:"123456",age:12},{name:"小龙",phone:"123456",age:12},{name:"小李",phone:"123456",age:12},{name:"小陈",phone:"123456",age:12},{name:"李白",phone:"123456",age:12},{name:"张三",phone:"123456",age:12}]}},methods:{edit:function(e){this.$message.success("编辑"+this.data[e].name)},remove:function(e){this.$message.error("删除"+this.data[e].name)}}}),r=s,c=n("2877"),i=Object(c["a"])(r,t,o,!1,null,null,null);a["default"]=i.exports},b0c0:function(e,a,n){var t=n("83ab"),o=n("9bf2").f,s=Function.prototype,r=s.toString,c=/^\s*function ([^ (]*)/,i="name";t&&!(i in s)&&o(s,i,{configurable:!0,get:function(){try{return r.call(this).match(c)[1]}catch(e){return""}}})}}]);