(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-30ffedc2"],{"1a78":function(t,e,i){"use strict";i.r(e);var s=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-app",[i("NavbarMenu"),i("div",{staticClass:"content"},[i("v-container",{staticClass:"mb-12",staticStyle:{"margin-top":"30px"}},[t._l(t.questions,(function(e,s){return i("v-card",{key:s,staticClass:"ques_item"},[i("v-container",{attrs:{fluid:""}},[i("p",[i("span",[t._v(t._s(s+1)+".["+t._s(e.diseaseName)+"]")]),t._v(" "+t._s(e.questionInfo)+"("+t._s(e.score)+" 分) ")]),i("v-radio-group",{model:{value:t.rs[s].value,callback:function(e){t.$set(t.rs[s],"value",e)},expression:"rs[index].value"}},[i("v-radio",{attrs:{label:e.choiceA,color:"red",value:"A"}}),i("v-radio",{attrs:{label:e.choiceB,color:"red",value:"B"}}),i("v-radio",{attrs:{label:e.choiceC,color:"red",value:"C"}}),i("v-radio",{attrs:{label:e.choiceD,color:"red",value:"D"}})],1)],1)],1)})),i("div",{staticClass:"text-center"},[i("v-btn",{staticStyle:{"margin-top":"20px"},attrs:{rounded:"",color:"primary",dark:""},on:{click:function(e){return t.getscore()}}},[t._v(" 查看分数 ")])],1)],2)],1)],1)},n=[],a=(i("d3b7"),i("3ca3"),i("ddb0"),i("159b"),i("bc3a")),o=i.n(a),r={name:"ExamItem",answer:[],components:{NavbarMenu:function(){return i.e("chunk-5e91d658").then(i.bind(null,"dfe6"))}},data:function(){return{choice:[],questions:[{questionId:"011",questionInfo:"题干1",diseaseName:"病种名1",score:"10",choiceA:"aaa1",choiceB:"bbb1",choiceC:"ccc1",choiceD:"ddd1"},{questionId:"012",questionInfo:"题干2",diseaseName:"病种名2",score:"10",choiceA:"aaa2",choiceB:"bbb2",choiceC:"ccc2",choiceD:"ddd2"}],rs:[]}},created:function(){var t=this;console.log(this.$route.query.id),this.updata(),this.questions.forEach((function(e){t.rs.push({questionId:e.questionId,value:""})}))},methods:{updata:function(){var t=this;o.a.post("/test/paper",{testId:this.$route.query.id}).then((function(e){console.log("res=>",e),200==e.data.code?(t.questions=e.data.data,console.log(e.data.data)):(console.log("错误代码："+e.data.code),console.log("错误提示："+e.data.msg))})).catch((function(t){console.log(t.data)}))},getscore:function(){var t=this;console.log(this.rs),o.a.post("/test/score",{result:this.rs}).then((function(e){console.log("res:",e),200===e.data.code?t.$store.dispatch("snackbar/openSnackbar",{msg:"您的分数为："+e.data.data.score+" / "+e.data.data.sumscore,color:"primary"}):console.log("错误代码：",e.data.code)})).catch((function(t){console.log("err=>",t)}))}}},l=r,u=(i("f2c0"),i("2877")),c=i("6544"),h=i.n(c),d=i("7496"),p=i("8336"),f=i("b0af"),g=i("a523"),v=i("5530"),m=(i("b0c0"),i("2c64"),i("ba87")),b=i("9d26"),y=i("c37a"),C=i("7e2b"),S=i("a9ad"),I=i("4e82"),D=i("5607"),k=i("2b0e"),V=k["a"].extend({name:"rippleable",directives:{ripple:D["a"]},props:{ripple:{type:[Boolean,Object],default:!0}},methods:{genRipple:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};return this.ripple?(t.staticClass="v-input--selection-controls__ripple",t.directives=t.directives||[],t.directives.push({name:"ripple",value:{center:!0}}),this.$createElement("div",t)):null}}}),$=i("7560"),M=(i("25f0"),i("4de4"),i("8547")),O=i("58df");function B(t){t.preventDefault()}var _=Object(O["a"])(y["a"],V,M["a"]).extend({name:"selectable",model:{prop:"inputValue",event:"change"},props:{id:String,inputValue:null,falseValue:null,trueValue:null,multiple:{type:Boolean,default:null},label:String},data:function(){return{hasColor:this.inputValue,lazyValue:this.inputValue}},computed:{computedColor:function(){if(this.isActive)return this.color?this.color:this.isDark&&!this.appIsDark?"white":"primary"},isMultiple:function(){return!0===this.multiple||null===this.multiple&&Array.isArray(this.internalValue)},isActive:function(){var t=this,e=this.value,i=this.internalValue;return this.isMultiple?!!Array.isArray(i)&&i.some((function(i){return t.valueComparator(i,e)})):void 0===this.trueValue||void 0===this.falseValue?e?this.valueComparator(e,i):Boolean(i):this.valueComparator(i,this.trueValue)},isDirty:function(){return this.isActive},rippleState:function(){return this.isDisabled||this.validationState?this.validationState:void 0}},watch:{inputValue:function(t){this.lazyValue=t,this.hasColor=t}},methods:{genLabel:function(){var t=y["a"].options.methods.genLabel.call(this);return t?(t.data.on={click:B},t):t},genInput:function(t,e){return this.$createElement("input",{attrs:Object.assign({"aria-checked":this.isActive.toString(),disabled:this.isDisabled,id:this.computedId,role:t,type:t},e),domProps:{value:this.value,checked:this.isActive},on:{blur:this.onBlur,change:this.onChange,focus:this.onFocus,keydown:this.onKeydown,click:B},ref:"input"})},onBlur:function(){this.isFocused=!1},onClick:function(t){this.onChange(),this.$emit("click",t)},onChange:function(){var t=this;if(this.isInteractive){var e=this.value,i=this.internalValue;if(this.isMultiple){Array.isArray(i)||(i=[]);var s=i.length;i=i.filter((function(i){return!t.valueComparator(i,e)})),i.length===s&&i.push(e)}else i=void 0!==this.trueValue&&void 0!==this.falseValue?this.valueComparator(i,this.trueValue)?this.falseValue:this.trueValue:e?this.valueComparator(i,e)?null:e:!i;this.validate(!0,i),this.internalValue=i,this.hasColor=i}},onFocus:function(){this.isFocused=!0},onKeydown:function(t){}}}),j=i("80d2"),A=i("d9f7"),w=Object(O["a"])(C["a"],S["a"],V,Object(I["a"])("radioGroup"),$["a"]),E=w.extend().extend({name:"v-radio",inheritAttrs:!1,props:{disabled:Boolean,id:String,label:String,name:String,offIcon:{type:String,default:"$radioOff"},onIcon:{type:String,default:"$radioOn"},readonly:Boolean,value:{default:null}},data:function(){return{isFocused:!1}},computed:{classes:function(){return Object(v["a"])(Object(v["a"])({"v-radio--is-disabled":this.isDisabled,"v-radio--is-focused":this.isFocused},this.themeClasses),this.groupClasses)},computedColor:function(){return _.options.computed.computedColor.call(this)},computedIcon:function(){return this.isActive?this.onIcon:this.offIcon},computedId:function(){return y["a"].options.computed.computedId.call(this)},hasLabel:y["a"].options.computed.hasLabel,hasState:function(){return(this.radioGroup||{}).hasState},isDisabled:function(){return this.disabled||!!this.radioGroup&&this.radioGroup.isDisabled},isReadonly:function(){return this.readonly||!!this.radioGroup&&this.radioGroup.isReadonly},computedName:function(){return this.name||!this.radioGroup?this.name:this.radioGroup.name||"radio-".concat(this.radioGroup._uid)},rippleState:function(){return _.options.computed.rippleState.call(this)},validationState:function(){return(this.radioGroup||{}).validationState||this.computedColor}},methods:{genInput:function(t){return _.options.methods.genInput.call(this,"radio",t)},genLabel:function(){return this.hasLabel?this.$createElement(m["a"],{on:{click:B},attrs:{for:this.computedId},props:{color:this.validationState,focused:this.hasState}},Object(j["p"])(this,"label")||this.label):null},genRadio:function(){return this.$createElement("div",{staticClass:"v-input--selection-controls__input"},[this.$createElement(b["a"],this.setTextColor(this.validationState,{props:{dense:this.radioGroup&&this.radioGroup.dense}}),this.computedIcon),this.genInput(Object(v["a"])({name:this.computedName,value:this.value},this.attrs$)),this.genRipple(this.setTextColor(this.rippleState))])},onFocus:function(t){this.isFocused=!0,this.$emit("focus",t)},onBlur:function(t){this.isFocused=!1,this.$emit("blur",t)},onChange:function(){this.isDisabled||this.isReadonly||this.isActive||this.toggle()},onKeydown:function(){}},render:function(t){var e={staticClass:"v-radio",class:this.classes,on:Object(A["c"])({click:this.onChange},this.listeners$)};return t("div",e,[this.genRadio(),this.genLabel()])}}),x=(i("a9e3"),i("ec29"),i("3d86"),i("604c")),F=Object(O["a"])(M["a"],x["a"],y["a"]),R=F.extend({name:"v-radio-group",provide:function(){return{radioGroup:this}},props:{column:{type:Boolean,default:!0},height:{type:[Number,String],default:"auto"},name:String,row:Boolean,value:null},computed:{classes:function(){return Object(v["a"])(Object(v["a"])({},y["a"].options.computed.classes.call(this)),{},{"v-input--selection-controls v-input--radio-group":!0,"v-input--radio-group--column":this.column&&!this.row,"v-input--radio-group--row":this.row})}},methods:{genDefaultSlot:function(){return this.$createElement("div",{staticClass:"v-input--radio-group__input",attrs:{id:this.id,role:"radiogroup","aria-labelledby":this.computedId}},y["a"].options.methods.genDefaultSlot.call(this))},genInputSlot:function(){var t=y["a"].options.methods.genInputSlot.call(this);return delete t.data.on.click,t},genLabel:function(){var t=y["a"].options.methods.genLabel.call(this);return t?(t.data.attrs.id=this.computedId,delete t.data.attrs.for,t.tag="legend",t):null},onClick:x["a"].options.methods.onClick}}),q=Object(u["a"])(l,s,n,!1,null,"924a9150",null);e["default"]=q.exports;h()(q,{VApp:d["a"],VBtn:p["a"],VCard:f["a"],VContainer:g["a"],VRadio:E,VRadioGroup:R})},"1b2c":function(t,e,i){},"2c64":function(t,e,i){},"38cb":function(t,e,i){"use strict";var s=i("53ca"),n=(i("a9e3"),i("fb6a"),i("a9ad")),a=i("7560"),o=i("3206"),r=i("80d2"),l=i("d9bd"),u=i("58df"),c=Object(u["a"])(n["a"],Object(o["a"])("form"),a["a"]);e["a"]=c.extend({name:"validatable",props:{disabled:Boolean,error:Boolean,errorCount:{type:[Number,String],default:1},errorMessages:{type:[String,Array],default:function(){return[]}},messages:{type:[String,Array],default:function(){return[]}},readonly:Boolean,rules:{type:Array,default:function(){return[]}},success:Boolean,successMessages:{type:[String,Array],default:function(){return[]}},validateOnBlur:Boolean,value:{required:!1}},data:function(){return{errorBucket:[],hasColor:!1,hasFocused:!1,hasInput:!1,isFocused:!1,isResetting:!1,lazyValue:this.value,valid:!1}},computed:{computedColor:function(){if(!this.isDisabled)return this.color?this.color:this.isDark&&!this.appIsDark?"white":"primary"},hasError:function(){return this.internalErrorMessages.length>0||this.errorBucket.length>0||this.error},hasSuccess:function(){return this.internalSuccessMessages.length>0||this.success},externalError:function(){return this.internalErrorMessages.length>0||this.error},hasMessages:function(){return this.validationTarget.length>0},hasState:function(){return!this.isDisabled&&(this.hasSuccess||this.shouldValidate&&this.hasError)},internalErrorMessages:function(){return this.genInternalMessages(this.errorMessages)},internalMessages:function(){return this.genInternalMessages(this.messages)},internalSuccessMessages:function(){return this.genInternalMessages(this.successMessages)},internalValue:{get:function(){return this.lazyValue},set:function(t){this.lazyValue=t,this.$emit("input",t)}},isDisabled:function(){return this.disabled||!!this.form&&this.form.disabled},isInteractive:function(){return!this.isDisabled&&!this.isReadonly},isReadonly:function(){return this.readonly||!!this.form&&this.form.readonly},shouldValidate:function(){return!!this.externalError||!this.isResetting&&(this.validateOnBlur?this.hasFocused&&!this.isFocused:this.hasInput||this.hasFocused)},validations:function(){return this.validationTarget.slice(0,Number(this.errorCount))},validationState:function(){if(!this.isDisabled)return this.hasError&&this.shouldValidate?"error":this.hasSuccess?"success":this.hasColor?this.computedColor:void 0},validationTarget:function(){return this.internalErrorMessages.length>0?this.internalErrorMessages:this.successMessages&&this.successMessages.length>0?this.internalSuccessMessages:this.messages&&this.messages.length>0?this.internalMessages:this.shouldValidate?this.errorBucket:[]}},watch:{rules:{handler:function(t,e){Object(r["g"])(t,e)||this.validate()},deep:!0},internalValue:function(){this.hasInput=!0,this.validateOnBlur||this.$nextTick(this.validate)},isFocused:function(t){t||this.isDisabled||(this.hasFocused=!0,this.validateOnBlur&&this.$nextTick(this.validate))},isResetting:function(){var t=this;setTimeout((function(){t.hasInput=!1,t.hasFocused=!1,t.isResetting=!1,t.validate()}),0)},hasError:function(t){this.shouldValidate&&this.$emit("update:error",t)},value:function(t){this.lazyValue=t}},beforeMount:function(){this.validate()},created:function(){this.form&&this.form.register(this)},beforeDestroy:function(){this.form&&this.form.unregister(this)},methods:{genInternalMessages:function(t){return t?Array.isArray(t)?t:[t]:[]},reset:function(){this.isResetting=!0,this.internalValue=Array.isArray(this.internalValue)?[]:null},resetValidation:function(){this.isResetting=!0},validate:function(){var t=arguments.length>0&&void 0!==arguments[0]&&arguments[0],e=arguments.length>1?arguments[1]:void 0,i=[];e=e||this.internalValue,t&&(this.hasInput=this.hasFocused=!0);for(var n=0;n<this.rules.length;n++){var a=this.rules[n],o="function"===typeof a?a(e):a;!1===o||"string"===typeof o?i.push(o||""):"boolean"!==typeof o&&Object(l["b"])("Rules should return a string or boolean, received '".concat(Object(s["a"])(o),"' instead"),this)}return this.errorBucket=i,this.valid=0===i.length,this.valid}}})},"3d86":function(t,e,i){},"551c":function(t,e,i){},8547:function(t,e,i){"use strict";var s=i("2b0e"),n=i("80d2");e["a"]=s["a"].extend({name:"comparable",props:{valueComparator:{type:Function,default:n["g"]}}})},"8ff2":function(t,e,i){},ba87:function(t,e,i){"use strict";var s=i("5530"),n=(i("a9e3"),i("1b2c"),i("a9ad")),a=i("7560"),o=i("58df"),r=i("80d2"),l=Object(o["a"])(a["a"]).extend({name:"v-label",functional:!0,props:{absolute:Boolean,color:{type:String,default:"primary"},disabled:Boolean,focused:Boolean,for:String,left:{type:[Number,String],default:0},right:{type:[Number,String],default:"auto"},value:Boolean},render:function(t,e){var i=e.children,o=e.listeners,l=e.props,u={staticClass:"v-label",class:Object(s["a"])({"v-label--active":l.value,"v-label--is-disabled":l.disabled},Object(a["b"])(e)),attrs:{for:l.for,"aria-hidden":!l.for},on:o,style:{left:Object(r["e"])(l.left),right:Object(r["e"])(l.right),position:l.absolute?"absolute":"relative"},ref:"label"};return t("label",n["a"].options.methods.setTextColor(l.focused&&l.color,u),i)}});e["a"]=l},c37a:function(t,e,i){"use strict";var s=i("5530"),n=(i("a9e3"),i("4de4"),i("d81d"),i("1276"),i("ac1f"),i("99af"),i("d191"),i("9d26")),a=i("ba87"),o=(i("8ff2"),i("a9ad")),r=i("7560"),l=i("58df"),u=i("80d2"),c=Object(l["a"])(o["a"],r["a"]).extend({name:"v-messages",props:{value:{type:Array,default:function(){return[]}}},methods:{genChildren:function(){return this.$createElement("transition-group",{staticClass:"v-messages__wrapper",attrs:{name:"message-transition",tag:"div"}},this.value.map(this.genMessage))},genMessage:function(t,e){return this.$createElement("div",{staticClass:"v-messages__message",key:e},Object(u["p"])(this,"default",{message:t,key:e})||[t])}},render:function(t){return t("div",this.setTextColor(this.color,{staticClass:"v-messages",class:this.themeClasses}),[this.genChildren()])}}),h=c,d=i("7e2b"),p=i("38cb"),f=i("d9f7"),g=Object(l["a"])(d["a"],p["a"]),v=g.extend().extend({name:"v-input",inheritAttrs:!1,props:{appendIcon:String,backgroundColor:{type:String,default:""},dense:Boolean,height:[Number,String],hideDetails:[Boolean,String],hint:String,id:String,label:String,loading:Boolean,persistentHint:Boolean,prependIcon:String,value:null},data:function(){return{lazyValue:this.value,hasMouseDown:!1}},computed:{classes:function(){return Object(s["a"])({"v-input--has-state":this.hasState,"v-input--hide-details":!this.showDetails,"v-input--is-label-active":this.isLabelActive,"v-input--is-dirty":this.isDirty,"v-input--is-disabled":this.isDisabled,"v-input--is-focused":this.isFocused,"v-input--is-loading":!1!==this.loading&&null!=this.loading,"v-input--is-readonly":this.isReadonly,"v-input--dense":this.dense},this.themeClasses)},computedId:function(){return this.id||"input-".concat(this._uid)},hasDetails:function(){return this.messagesToDisplay.length>0},hasHint:function(){return!this.hasMessages&&!!this.hint&&(this.persistentHint||this.isFocused)},hasLabel:function(){return!(!this.$slots.label&&!this.label)},internalValue:{get:function(){return this.lazyValue},set:function(t){this.lazyValue=t,this.$emit(this.$_modelEvent,t)}},isDirty:function(){return!!this.lazyValue},isLabelActive:function(){return this.isDirty},messagesToDisplay:function(){var t=this;return this.hasHint?[this.hint]:this.hasMessages?this.validations.map((function(e){if("string"===typeof e)return e;var i=e(t.internalValue);return"string"===typeof i?i:""})).filter((function(t){return""!==t})):[]},showDetails:function(){return!1===this.hideDetails||"auto"===this.hideDetails&&this.hasDetails}},watch:{value:function(t){this.lazyValue=t}},beforeCreate:function(){this.$_modelEvent=this.$options.model&&this.$options.model.event||"input"},methods:{genContent:function(){return[this.genPrependSlot(),this.genControl(),this.genAppendSlot()]},genControl:function(){return this.$createElement("div",{staticClass:"v-input__control"},[this.genInputSlot(),this.genMessages()])},genDefaultSlot:function(){return[this.genLabel(),this.$slots.default]},genIcon:function(t,e){var i=this,s=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{},a=this["".concat(t,"Icon")],o="click:".concat(Object(u["t"])(t)),r=!(!this.listeners$[o]&&!e),l=Object(f["a"])({attrs:{"aria-label":r?Object(u["t"])(t).split("-")[0]+" icon":void 0,color:this.validationState,dark:this.dark,disabled:this.isDisabled,light:this.light},on:r?{click:function(t){t.preventDefault(),t.stopPropagation(),i.$emit(o,t),e&&e(t)},mouseup:function(t){t.preventDefault(),t.stopPropagation()}}:void 0},s);return this.$createElement("div",{staticClass:"v-input__icon",class:t?"v-input__icon--".concat(Object(u["t"])(t)):void 0},[this.$createElement(n["a"],l,a)])},genInputSlot:function(){return this.$createElement("div",this.setBackgroundColor(this.backgroundColor,{staticClass:"v-input__slot",style:{height:Object(u["e"])(this.height)},on:{click:this.onClick,mousedown:this.onMouseDown,mouseup:this.onMouseUp},ref:"input-slot"}),[this.genDefaultSlot()])},genLabel:function(){return this.hasLabel?this.$createElement(a["a"],{props:{color:this.validationState,dark:this.dark,disabled:this.isDisabled,focused:this.hasState,for:this.computedId,light:this.light}},this.$slots.label||this.label):null},genMessages:function(){var t=this;return this.showDetails?this.$createElement(h,{props:{color:this.hasHint?"":this.validationState,dark:this.dark,light:this.light,value:this.messagesToDisplay},attrs:{role:this.hasMessages?"alert":null},scopedSlots:{default:function(e){return Object(u["p"])(t,"message",e)}}}):null},genSlot:function(t,e,i){if(!i.length)return null;var s="".concat(t,"-").concat(e);return this.$createElement("div",{staticClass:"v-input__".concat(s),ref:s},i)},genPrependSlot:function(){var t=[];return this.$slots.prepend?t.push(this.$slots.prepend):this.prependIcon&&t.push(this.genIcon("prepend")),this.genSlot("prepend","outer",t)},genAppendSlot:function(){var t=[];return this.$slots.append?t.push(this.$slots.append):this.appendIcon&&t.push(this.genIcon("append")),this.genSlot("append","outer",t)},onClick:function(t){this.$emit("click",t)},onMouseDown:function(t){this.hasMouseDown=!0,this.$emit("mousedown",t)},onMouseUp:function(t){this.hasMouseDown=!1,this.$emit("mouseup",t)}},render:function(t){return t("div",this.setTextColor(this.validationState,{staticClass:"v-input",class:this.classes}),this.genContent())}});e["a"]=v},d191:function(t,e,i){},ec29:function(t,e,i){},f2c0:function(t,e,i){"use strict";i("551c")}}]);
//# sourceMappingURL=chunk-30ffedc2.90f5b6b1.js.map