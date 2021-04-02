<template>
  <div class="body">
  <el-breadcrumb separator-class="el-icon-arrow-right">
  <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
  <el-breadcrumb-item>病种管理</el-breadcrumb-item>
  <el-breadcrumb-item>病种增加</el-breadcrumb-item>
</el-breadcrumb>
<div class="main">
<el-collapse v-model="activeNames"  accordion @change="handleChange">
  <el-collapse-item title="传染病" name="1">
  <el-tag
  :key="tag"
  v-for="tag in dynamicTags"
  closable
  :disable-transitions="false"
  @close="handleClose(tag)">
  {{tag}}
</el-tag>
<el-input
  class="input-new-tag"
  v-if="inputVisible"
  v-model="inputValue"
  ref="saveTagInput"
  @keyup.enter.native="handleInputConfirm"
  @blur="handleInputConfirm"
>
</el-input>
<el-button v-else class="button-new-tag"   @click="showInput">+ New Tag</el-button>
  </el-collapse-item>
  <el-collapse-item title="寄生虫病" name="2">
    <el-tag
  :key="tag"
  v-for="tag in dynamicTags"
  closable
  :disable-transitions="false"
  @close="handleClose(tag)">
  {{tag}}
</el-tag>
<el-input
  class="input-new-tag"
  v-if="inputVisible"
  v-model="inputValue"
  type="success"
  ref="saveTagInput"
   
  @keyup.enter.native="handleInputConfirm"
  @blur="handleInputConfirm"
>
</el-input>
<el-button v-else class="button-new-tag"   @click="showInput">+ New Tag</el-button>
  </el-collapse-item>
  <el-collapse-item title="内科" name="3">
    <el-tag
  :key="tag"
  v-for="tag in dynamicTags"
  closable
  :disable-transitions="false"
  @close="handleClose(tag)">
  {{tag}}
</el-tag>
<el-input
  class="input-new-tag"
  v-if="inputVisible"
  v-model="inputValue"
  ref="saveTagInput"
   
  @keyup.enter.native="handleInputConfirm"
  @blur="handleInputConfirm"
>
</el-input>
<el-button v-else class="button-new-tag"   @click="showInput">+ New Tag</el-button>
  </el-collapse-item>
  <el-collapse-item title="神经科" name="4">
   <el-tag
  :key="tag"
  v-for="tag in dynamicTags"
  closable
  :disable-transitions="false"
  @close="handleClose(tag)">
  {{tag}}
</el-tag>
<el-input
  class="input-new-tag"
  v-if="inputVisible"
  v-model="inputValue"
  ref="saveTagInput"
   
  @keyup.enter.native="handleInputConfirm"
  @blur="handleInputConfirm"
>
</el-input>
<el-button v-else class="button-new-tag"   @click="showInput">+ New Tag</el-button>
  </el-collapse-item>
  <el-collapse-item title="常用手术" name="5">
    <el-tag
  :key="tag"
  v-for="tag in dynamicTags"
  closable
  :disable-transitions="false"
  @close="handleClose(tag)">
  {{tag}}
</el-tag>
<el-input
  class="input-new-tag"
  v-if="inputVisible"
  v-model="inputValue"
  ref="saveTagInput"
   
  @keyup.enter.native="handleInputConfirm"
  @blur="handleInputConfirm"
>
</el-input>
<el-button v-else class="button-new-tag"   @click="showInput">+ New Tag</el-button>
  </el-collapse-item>
  <el-collapse-item title="免疫" name="6">
    <el-tag
  :key="tag"
  v-for="tag in dynamicTags"
  closable
  :disable-transitions="false"
  @close="handleClose(tag)">
  {{tag}}
</el-tag>
<el-input
  class="input-new-tag"
  v-if="inputVisible"
  v-model="inputValue"
  ref="saveTagInput"
   
  @keyup.enter.native="handleInputConfirm"
  @blur="handleInputConfirm"
>
</el-input>
<el-button v-else class="button-new-tag"   @click="showInput">+ New Tag</el-button>
  </el-collapse-item>
</el-collapse>
</div> 
  </div>
</template>

<script>
  export default {
    data() {
      return {
        activeNames: ['1'],
        dynamicTags: ['病种一', '病种二', '病种三'],
        inputVisible: false,
        inputValue: '',
     
      };
    },
    methods: {
        handleChange(val) {
        console.log(val);
      },
       handleClose(tag) {
        this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
      },

      showInput() {
        this.inputVisible = true;
        this.$nextTick(_ => {
          this.$refs.saveTagInput.$refs.input.focus();
        });
      },

      handleInputConfirm() {
        let inputValue = this.inputValue;
        if (inputValue) {
          this.dynamicTags.push(inputValue);
        }
        this.inputVisible = false;
        this.inputValue = '';
      }
    },
  };
</script>

<style>
.body{
    height: 100%;
}
  .main{
      padding-top: 3%;
      padding-left: 2%;
      margin-top:3%;
      border-radius: 4%;
      background-color: #fff;
      width: 98%;
      height: 80%;
  }
  .el-tag + .el-tag {
    margin-left: 10px;
  }
  .button-new-tag {
    margin-left: 10px;
    height: 32px;
    line-height: 30px;
    padding-top: 0;
    padding-bottom: 0;
  }
  .input-new-tag {
    width: 90px;
    margin-left: 10px;
    vertical-align: bottom;
  }
.el-collapse-item__header {
    color: #303133!important;
    font-weight:550!important;
    font-size: 16px!important;
  }
</style>