(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-3529a2eb"],{"951a":function(e,t,a){"use strict";var n=a("e00e"),l=a.n(n);l.a},ca0d:function(e,t,a){"use strict";a.r(t);var n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"body"},[a("el-breadcrumb",{attrs:{"separator-class":"el-icon-arrow-right"}},[a("el-breadcrumb-item",{attrs:{to:{path:"/home"}}},[e._v("首页")]),a("el-breadcrumb-item",[e._v("病种管理")]),a("el-breadcrumb-item",[e._v("病种编辑")])],1),a("div",{staticClass:"main"},[a("el-table",{staticStyle:{width:"100%"},attrs:{data:e.tableData.filter((function(t){return!e.search||t.name.toLowerCase().includes(e.search.toLowerCase())}))}},[a("el-table-column",{attrs:{label:"分类",prop:"date"}}),a("el-table-column",{attrs:{label:"病种",prop:"date"}}),a("el-table-column",{attrs:{label:"病例数",prop:"name"}}),a("el-table-column",{attrs:{align:"right"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{size:"mini"},on:{click:function(a){return e.handleEdit(t.$index,t.row)}}},[e._v("查看")]),a("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(a){return e.handleDelete(t.$index,t.row)}}},[e._v("删除")])]}}])},[a("template",{slot:"header"},[a("el-input",{attrs:{size:"mini",placeholder:"输入关键字搜索"},model:{value:e.search,callback:function(t){e.search=t},expression:"search"}})],1)],2)],1)],1)],1)},l=[],r={data:function(){return{tableData:[{date:"2016-05-02",name:"王小虎",address:"上海市普陀区金沙江路 1518 弄"},{date:"2016-05-04",name:"王小虎",address:"上海市普陀区金沙江路 1517 弄"},{date:"2016-05-01",name:"王小虎",address:"上海市普陀区金沙江路 1519 弄"},{date:"2016-05-03",name:"王小虎",address:"上海市普陀区金沙江路 1516 弄"}],search:""}},methods:{handleEdit:function(e,t){console.log(e,t)},handleDelete:function(e,t){console.log(e,t)}}},s=r,o=(a("951a"),a("2877")),c=Object(o["a"])(s,n,l,!1,null,"d795efd8",null);t["default"]=c.exports},e00e:function(e,t,a){}}]);