(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d21314a"],{aac7:function(t,e,n){"use strict";n.r(e);var l=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("el-table",{staticStyle:{width:"100%"},attrs:{size:"small",data:t.data,"max-height":"310px",id:"table"},on:{"selection-change":t.selection}},[t._l(t.columns,(function(t,e){return n("el-table-column",{key:e,attrs:{property:t.prop,label:t.name}})})),n("el-table-column",{attrs:{label:"操作",width:"150"},scopedSlots:t._u([{key:"default",fn:function(e){return[n("el-button",{attrs:{size:"mini"},on:{click:function(n){return t.handleEdit(e.$index,e.row)}}},[t._v("编辑")]),n("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(n){return t.handleDelete(e.$index,e.row)}}},[t._v("删除")])]}}])})],2)},a=[],i={props:["data","columns"],data:function(){return{}},methods:{handleEdit:function(t){this.$emit("edit",t)},handleDelete:function(t){this.$emit("remove",t)}}},o=i,r=n("2877"),c=Object(r["a"])(o,l,a,!1,null,null,null);e["default"]=c.exports}}]);