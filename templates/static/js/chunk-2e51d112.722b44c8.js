(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2e51d112"],{"057f":function(t,e,n){var a=n("fc6a"),o=n("241c").f,r={}.toString,i="object"==typeof window&&window&&Object.getOwnPropertyNames?Object.getOwnPropertyNames(window):[],s=function(t){try{return o(t)}catch(e){return i.slice()}};t.exports.f=function(t){return i&&"[object Window]"==r.call(t)?s(t):o(a(t))}},"1dde":function(t,e,n){var a=n("d039"),o=n("b622"),r=n("2d00"),i=o("species");t.exports=function(t){return r>=51||!a((function(){var e=[],n=e.constructor={};return n[i]=function(){return{foo:1}},1!==e[t](Boolean).foo}))}},"3ca3":function(t,e,n){"use strict";var a=n("6547").charAt,o=n("69f3"),r=n("7dd0"),i="String Iterator",s=o.set,l=o.getterFor(i);r(String,"String",(function(t){s(this,{type:i,string:String(t),index:0})}),(function(){var t,e=l(this),n=e.string,o=e.index;return o>=n.length?{value:void 0,done:!0}:(t=a(n,o),e.index+=t.length,{value:t,done:!1})}))},"3e0e":function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("el-card",{staticClass:"card",attrs:{shadow:"never"}},[n("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[n("span",[t._v("管理员管理")]),n("el-button",{staticStyle:{float:"right"},attrs:{type:"success",size:"small",icon:"el-icon-plus"},on:{click:function(e){return t.add("dialog")}}},[t._v("新增管理员")])],1),n("div",[n("el-button",{attrs:{size:"small",type:"danger",disabled:"未选择数据"==t.selection_button_title,icon:""}},[t._v(t._s(t.selection_button_title))]),n("el-button",{staticStyle:{foloat:"right"},attrs:{size:"small",circle:""},on:{click:function(e){return t.searchAdd()}}},[t._v(t._s(t.roomSum))]),n("div",{staticStyle:{float:"right"}},[n("el-input",{attrs:{size:"mini",placeholder:"输入关键字搜索"},model:{value:t.search,callback:function(e){t.search=e},expression:"search"}})],1)],1),n("div",{staticStyle:{width:"100%","min-height":"300px"},attrs:{id:"charts_one"}},[n("el-table",{staticStyle:{width:"100%"},attrs:{data:t.article_label_data,"max-height":"350"},on:{"selection-change":t.selection}},[n("el-table-column",{attrs:{type:"selection",width:"55"}}),n("el-table-column",{attrs:{type:"index",label:"序号",width:"70"}}),n("el-table-column",{attrs:{property:"username",label:"管理员",width:"180"}}),n("el-table-column",{attrs:{property:"password",label:"密码",width:"180"}}),n("el-table-column",{attrs:{label:"操作",width:"120"},scopedSlots:t._u([{key:"default",fn:function(e){return[n("el-button",{staticStyle:{"margin-right":"10px"},attrs:{size:"mini",type:"success"},on:{click:function(n){return t.editor_label(e.$index,e.row)}}}),n("el-popconfirm",{attrs:{confirmButtonText:"确认删除",cancelButtonText:"取消",confirmButtonType:"danger",cancelButtonType:"success",title:"这是一段内容确定删除吗？"},on:{onConfirm:function(n){return t.delete_label(e.$index,e.row)}}},[n("el-button",{attrs:{slot:"reference",size:"mini",type:"danger"},slot:"reference"},[n("i",{staticClass:"el-icon-delete"})])],1)]}}])})],1),n("el-pagination",{staticStyle:{"margin-top":"10px"},attrs:{"current-page":t.page_data.current_page,"page-sizes":[10,20,50,100,200,500],"page-size":t.page_data.page_size,layout:"total, sizes, prev, pager, next, jumper",total:this.roomSum},on:{"size-change":t.page_size_change,"current-change":t.current_change}})],1)]),n("el-dialog",{attrs:{title:t.dialog_title,width:"30%",visible:t.dialog_viside_state},on:{"update:visible":function(e){t.dialog_viside_state=e}}},[n("el-form",{ref:"form",attrs:{size:"small",model:t.label_form,"label-width":"80px"}},[n("el-form-item",{attrs:{label:"管理员"}},[n("el-input",{attrs:{placeholder:"请输入管理员名称"},model:{value:t.label_form.username,callback:function(e){t.$set(t.label_form,"username",e)},expression:"label_form.username"}})],1),n("el-form-item",{attrs:{label:"密码内容"}},[n("el-input",{attrs:{placeholder:"请输入密码内容"},model:{value:t.label_form.password,callback:function(e){t.$set(t.label_form,"password",e)},expression:"label_form.password"}})],1),n("el-form-item",{attrs:{label:"密码确定"}},[n("el-input",{attrs:{placeholder:"请重新输入密码内容"},model:{value:t.label_form.checkpwd,callback:function(e){t.$set(t.label_form,"checkpwd",e)},expression:"label_form.checkpwd"}})],1),n("div",{attrs:{align:"center"}},[n("el-button",{directives:[{name:"show",rawName:"v-show",value:!t.password_input_state,expression:"!password_input_state"}],attrs:{type:"danger",size:"small"},on:{click:function(e){return t.editor()}}},[t._v("确认修改")]),n("el-button",{directives:[{name:"show",rawName:"v-show",value:t.password_input_state,expression:"password_input_state"}],attrs:{type:"success",size:"small"},on:{click:function(e){return t.add("add")}}},[t._v("确认新增")])],1)],1)],1)],1)},o=[],r=(n("a434"),n("53ca")),i=n("cebe"),s=n.n(i),l=n("4328"),c=n.n(l),u={data:function(){return{testMsg:"",userId:"userId",token:"token",index:"",roomSum:0,value:"",dialog_viside_state:!1,password_input_state:!1,selection_button_title:"未选择数据",selection_button_state:!0,selection_data:[],dialog_title:"管理员修改",label_form:{checkpwd:"2",password:"2",username:"2"},article_label_data:[],page_data:{page_size:10,current_page:1,page_total:500},NowPage:1,excel_name:""}},computed:function(){},mounted:function(){this.NowPage=1;var t=!0;this.GetList(t)},methods:{searchAdd:function(){this.$alert("数据共有 "+this.roomSum+" 条。","提示",{confirmButtonText:"确定",callback:function(t){}})},deepClone:function(t){var e=Array.isArray(t)?[]:{};if(t&&"object"===Object(r["a"])(t))for(var n in t)Object.prototype.hasOwnProperty.call(t,n)&&(t[n]&&"object"===Object(r["a"])(t[n])?e[n]=this.deepClone(t[n]):e[n]=t[n]);return e},GetList:function(t){var e=this;console.log(c.a.stringify()),1==t&&s()({url:"/manager/list",method:"post",dataType:"json",params:{userId:this.$Cookies.get(this.userId),token:this.$Cookies.get(this.token),page:this.NowPage,per_page:1e4}}).then((function(t){e.roomSum=t.data.data.length})).catch((function(t){return console.log(t)})),s()({url:"/manager/list",method:"post",params:{userId:this.$Cookies.get(this.userId),token:this.$Cookies.get(this.token),page:this.NowPage,per_page:this.page_data.page_size}}).then((function(t){console.log("res=>",t),e.article_label_data=e.deepClone(t.data.data),e.page_data.page_total=e.roomSum/e.page_data.per_page,console.log(e.article_label_data)})).catch((function(t){return console.log(t)}))},add:function(t){switch(t){case"dialog":this.dialog_viside_state=!0,this.password_input_state=!0;break;case"add":this.GetAddData(t);break}},GetAddData:function(t){var e=this;s()({url:"/mregister",method:"post",params:{username:this.label_form.username,checkpwd:this.label_form.checkpwd,password:this.label_form.password},headers:{"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}}).then((function(t){console.log("res=>",t),console.log(t.data.msg),e.$message.warning(t.data.msg),200==t.data.code&&(e.article_label_data.splice(0,0,e.label_form),e.roomSum=e.roomSum+1,setTimeout((function(){e.dialog_viside_state=!1,e.password_input_state=!1}),1500))})).catch((function(t){return console.log(t)}))},editor_label:function(t){this.label_form=this.article_label_data[t],this.index=this.article_label_data[t].username,console.log(this.index),this.dialog_title="修改（"+this.article_label_data[t].username+"）",this.dialog_viside_state=!0},editor:function(){var t=this;s()({url:"/mregister/update",method:"post",params:{usernameOld:this.index,usernameNew:this.label_form.username,checkpwd:this.label_form.checkpwd,password:this.label_form.password},headers:{"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}}).then((function(e){console.log("res=>",e),t.$message.success("修改成功")})).catch((function(t){return console.log(t)})),setTimeout((function(){t.dialog_viside_state=!1}),1500)},selection:function(t){t.length>0&&this.article_label_data.length!=t.length?(this.selection_button_title="已选择"+t.length+"条数据",this.selection_button_state=!1,this.selection_data=t):this.article_label_data.length==t.length?(this.selection_button_title="已全选",this.selection_button_state=!1,this.selection_data=t):(this.selection_button_title="未选择数据",this.selection_button_state=!0)},delete_label:function(t){var e=this;console.log(this.article_label_data[t].username);this.article_label_data[t].username;s()({url:"/manager/delete",method:"post",dataType:"json",params:{userName:this.article_label_data[t].username+"",userId:this.$Cookies.get(this.userId),token:this.$Cookies.get(this.token)},headers:{"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}}).then((function(t){e.roomSum--,console.log("res=>",t),e.$message.success("删除成功")})).catch((function(t){return console.log(t)})),setTimeout((function(){e.article_label_data.splice(t,1)}),1500)},page_size_change:function(t){this.page_data.page_size=t,this.$message.success("每页显示"+t+"条数据"),this.get_user_data()},current_change:function(t){this.page_data.current_page=t,this.NowPage=t,this.GetList(),this.$message.success("正在展示第"+t+"页数据"),this.get_user_data()}}},d=u,f=n("2877"),p=Object(f["a"])(d,a,o,!1,null,null,null);e["default"]=p.exports},"53ca":function(t,e,n){"use strict";n.d(e,"a",(function(){return a}));n("a4d3"),n("e01a"),n("d28b"),n("d3b7"),n("3ca3"),n("ddb0");function a(t){return a="function"===typeof Symbol&&"symbol"===typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"===typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},a(t)}},"746f":function(t,e,n){var a=n("428f"),o=n("5135"),r=n("e538"),i=n("9bf2").f;t.exports=function(t){var e=a.Symbol||(a.Symbol={});o(e,t)||i(e,t,{value:r.f(t)})}},8418:function(t,e,n){"use strict";var a=n("c04e"),o=n("9bf2"),r=n("5c6c");t.exports=function(t,e,n){var i=a(e);i in t?o.f(t,i,r(0,n)):t[i]=n}},a434:function(t,e,n){"use strict";var a=n("23e7"),o=n("23cb"),r=n("a691"),i=n("50c4"),s=n("7b0b"),l=n("65f0"),c=n("8418"),u=n("1dde"),d=n("ae40"),f=u("splice"),p=d("splice",{ACCESSORS:!0,0:0,1:2}),h=Math.max,m=Math.min,g=9007199254740991,b="Maximum allowed length exceeded";a({target:"Array",proto:!0,forced:!f||!p},{splice:function(t,e){var n,a,u,d,f,p,_=s(this),v=i(_.length),y=o(t,v),w=arguments.length;if(0===w?n=a=0:1===w?(n=0,a=v-y):(n=w-2,a=m(h(r(e),0),v-y)),v+n-a>g)throw TypeError(b);for(u=l(_,a),d=0;d<a;d++)f=y+d,f in _&&c(u,d,_[f]);if(u.length=a,n<a){for(d=y;d<v-a;d++)f=d+a,p=d+n,f in _?_[p]=_[f]:delete _[p];for(d=v;d>v-a+n;d--)delete _[d-1]}else if(n>a)for(d=v-a;d>y;d--)f=d+a-1,p=d+n-1,f in _?_[p]=_[f]:delete _[p];for(d=0;d<n;d++)_[d+y]=arguments[d+2];return _.length=v-a+n,u}})},a4d3:function(t,e,n){"use strict";var a=n("23e7"),o=n("da84"),r=n("d066"),i=n("c430"),s=n("83ab"),l=n("4930"),c=n("fdbf"),u=n("d039"),d=n("5135"),f=n("e8b5"),p=n("861d"),h=n("825a"),m=n("7b0b"),g=n("fc6a"),b=n("c04e"),_=n("5c6c"),v=n("7c73"),y=n("df75"),w=n("241c"),S=n("057f"),k=n("7418"),x=n("06cf"),O=n("9bf2"),j=n("d1e7"),T=n("9112"),$=n("6eeb"),z=n("5692"),C=n("f772"),P=n("d012"),N=n("90e3"),I=n("b622"),A=n("e538"),E=n("746f"),B=n("d44e"),F=n("69f3"),G=n("b727").forEach,J=C("hidden"),M="Symbol",D="prototype",L=I("toPrimitive"),U=F.set,Q=F.getterFor(M),R=Object[D],W=o.Symbol,q=r("JSON","stringify"),H=x.f,K=O.f,V=S.f,X=j.f,Y=z("symbols"),Z=z("op-symbols"),tt=z("string-to-symbol-registry"),et=z("symbol-to-string-registry"),nt=z("wks"),at=o.QObject,ot=!at||!at[D]||!at[D].findChild,rt=s&&u((function(){return 7!=v(K({},"a",{get:function(){return K(this,"a",{value:7}).a}})).a}))?function(t,e,n){var a=H(R,e);a&&delete R[e],K(t,e,n),a&&t!==R&&K(R,e,a)}:K,it=function(t,e){var n=Y[t]=v(W[D]);return U(n,{type:M,tag:t,description:e}),s||(n.description=e),n},st=c?function(t){return"symbol"==typeof t}:function(t){return Object(t)instanceof W},lt=function(t,e,n){t===R&&lt(Z,e,n),h(t);var a=b(e,!0);return h(n),d(Y,a)?(n.enumerable?(d(t,J)&&t[J][a]&&(t[J][a]=!1),n=v(n,{enumerable:_(0,!1)})):(d(t,J)||K(t,J,_(1,{})),t[J][a]=!0),rt(t,a,n)):K(t,a,n)},ct=function(t,e){h(t);var n=g(e),a=y(n).concat(ht(n));return G(a,(function(e){s&&!dt.call(n,e)||lt(t,e,n[e])})),t},ut=function(t,e){return void 0===e?v(t):ct(v(t),e)},dt=function(t){var e=b(t,!0),n=X.call(this,e);return!(this===R&&d(Y,e)&&!d(Z,e))&&(!(n||!d(this,e)||!d(Y,e)||d(this,J)&&this[J][e])||n)},ft=function(t,e){var n=g(t),a=b(e,!0);if(n!==R||!d(Y,a)||d(Z,a)){var o=H(n,a);return!o||!d(Y,a)||d(n,J)&&n[J][a]||(o.enumerable=!0),o}},pt=function(t){var e=V(g(t)),n=[];return G(e,(function(t){d(Y,t)||d(P,t)||n.push(t)})),n},ht=function(t){var e=t===R,n=V(e?Z:g(t)),a=[];return G(n,(function(t){!d(Y,t)||e&&!d(R,t)||a.push(Y[t])})),a};if(l||(W=function(){if(this instanceof W)throw TypeError("Symbol is not a constructor");var t=arguments.length&&void 0!==arguments[0]?String(arguments[0]):void 0,e=N(t),n=function(t){this===R&&n.call(Z,t),d(this,J)&&d(this[J],e)&&(this[J][e]=!1),rt(this,e,_(1,t))};return s&&ot&&rt(R,e,{configurable:!0,set:n}),it(e,t)},$(W[D],"toString",(function(){return Q(this).tag})),$(W,"withoutSetter",(function(t){return it(N(t),t)})),j.f=dt,O.f=lt,x.f=ft,w.f=S.f=pt,k.f=ht,A.f=function(t){return it(I(t),t)},s&&(K(W[D],"description",{configurable:!0,get:function(){return Q(this).description}}),i||$(R,"propertyIsEnumerable",dt,{unsafe:!0}))),a({global:!0,wrap:!0,forced:!l,sham:!l},{Symbol:W}),G(y(nt),(function(t){E(t)})),a({target:M,stat:!0,forced:!l},{for:function(t){var e=String(t);if(d(tt,e))return tt[e];var n=W(e);return tt[e]=n,et[n]=e,n},keyFor:function(t){if(!st(t))throw TypeError(t+" is not a symbol");if(d(et,t))return et[t]},useSetter:function(){ot=!0},useSimple:function(){ot=!1}}),a({target:"Object",stat:!0,forced:!l,sham:!s},{create:ut,defineProperty:lt,defineProperties:ct,getOwnPropertyDescriptor:ft}),a({target:"Object",stat:!0,forced:!l},{getOwnPropertyNames:pt,getOwnPropertySymbols:ht}),a({target:"Object",stat:!0,forced:u((function(){k.f(1)}))},{getOwnPropertySymbols:function(t){return k.f(m(t))}}),q){var mt=!l||u((function(){var t=W();return"[null]"!=q([t])||"{}"!=q({a:t})||"{}"!=q(Object(t))}));a({target:"JSON",stat:!0,forced:mt},{stringify:function(t,e,n){var a,o=[t],r=1;while(arguments.length>r)o.push(arguments[r++]);if(a=e,(p(e)||void 0!==t)&&!st(t))return f(e)||(e=function(t,e){if("function"==typeof a&&(e=a.call(this,t,e)),!st(e))return e}),o[1]=e,q.apply(null,o)}})}W[D][L]||T(W[D],L,W[D].valueOf),B(W,M),P[J]=!0},d28b:function(t,e,n){var a=n("746f");a("iterator")},ddb0:function(t,e,n){var a=n("da84"),o=n("fdbc"),r=n("e260"),i=n("9112"),s=n("b622"),l=s("iterator"),c=s("toStringTag"),u=r.values;for(var d in o){var f=a[d],p=f&&f.prototype;if(p){if(p[l]!==u)try{i(p,l,u)}catch(m){p[l]=u}if(p[c]||i(p,c,d),o[d])for(var h in r)if(p[h]!==r[h])try{i(p,h,r[h])}catch(m){p[h]=r[h]}}}},e01a:function(t,e,n){"use strict";var a=n("23e7"),o=n("83ab"),r=n("da84"),i=n("5135"),s=n("861d"),l=n("9bf2").f,c=n("e893"),u=r.Symbol;if(o&&"function"==typeof u&&(!("description"in u.prototype)||void 0!==u().description)){var d={},f=function(){var t=arguments.length<1||void 0===arguments[0]?void 0:String(arguments[0]),e=this instanceof f?new u(t):void 0===t?u():u(t);return""===t&&(d[e]=!0),e};c(f,u);var p=f.prototype=u.prototype;p.constructor=f;var h=p.toString,m="Symbol(test)"==String(u("test")),g=/^Symbol\((.*)\)[^)]+$/;l(p,"description",{configurable:!0,get:function(){var t=s(this)?this.valueOf():this,e=h.call(t);if(i(d,t))return"";var n=m?e.slice(7,-1):e.replace(g,"$1");return""===n?void 0:n}}),a({global:!0,forced:!0},{Symbol:f})}},e538:function(t,e,n){var a=n("b622");e.f=a}}]);