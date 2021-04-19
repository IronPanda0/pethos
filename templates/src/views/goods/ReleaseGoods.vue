<template>
  <div>
  <div class="navig">
      <el-breadcrumb separator-class="el-icon-arrow-right">
  <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
  <el-breadcrumb-item>病例分布</el-breadcrumb-item>
  <el-breadcrumb-item>发布病例</el-breadcrumb-item>
</el-breadcrumb>
  </div>
    <el-card shadow="never">
      <div slot="header">
        <span>{{ title }}</span>
      </div>
      <div>
        <el-form size="small"  ref="form" :model="form" label-width="80px">
          <el-form-item label="病例名称">
            <el-input
            style="width:60%"
              v-model="form.goods_title"
              placeholder="请输入内容"
            ></el-input>
          </el-form-item>
 <el-form-item label="所属病种">
          <el-select v-model="value"  style="width:60%" clearable placeholder="请选择病种">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
 </el-form-item>

            <el-form-item label="检查项目">
            <el-input
            style="width:60%"
              v-model="form.goods_check"
              placeholder="请输入内容"
            ></el-input>
          </el-form-item>
          <el-form-item label="详细介绍">
  <el-input
  type="textarea"
  style="width:60%"
 :autosize="{ minRows: 4, maxRows: 6}"
  placeholder="请输入内容"
  v-model="textarea"
  maxlength="100"
  show-word-limit>
</el-input>

<div class="ProcessOne" v-for="(item) in viewArr" :key="item">
   <el-divider  style="width:60%;"><span style="color:#909399">{{item.name}}</span></el-divider>
   <el-form-item label="" style="width:60%">
          <el-upload
  class="upload-demo"
  action="https://jsonplaceholder.typicode.com/posts/"
  :on-preview="handlePreview"
  :on-remove="handleRemove"
  :file-list="fileList"
  list-type="picture">
  <el-button size="small" type="success">图片上传</el-button>
  <div slot="tip" class="el-upload__tip">上传jpg/png文件，且不超过500kb</div>
</el-upload>
 <div class="Setfloat">
   <span class="el-upload__tip">上传文字描述</span> 
     <div class="white"></div>
      <el-input
  type="textarea"
  style="width:100%"
 :autosize="{ minRows: 9, maxRows: 10}"
  placeholder="请输入内容"
  v-model="textarea"
  maxlength="100"
  show-word-limit>
</el-input>
  </div>
          </el-form-item>
</div>
 </el-form-item>
          
         
         <el-form-item label="宠物心率">
            <el-input
            style="width:60%"
              v-model="form.goods_check"
              placeholder="请输入内容"
            ></el-input>
          </el-form-item>

          <el-form-item label="宠物体温">
            <el-input
            style="width:60%"
              v-model="form.goods_check"
              placeholder="请输入内容"
            ></el-input>
          </el-form-item>
          <el-form-item label="宠物脉搏">
            <el-input
            style="width:60%"
              v-model="form.goods_check"
              placeholder="请输入内容"
            ></el-input>
          </el-form-item>

        </el-form>
        <div align="right">
          <el-button type="success">确认发布</el-button>
        </div>
      </div>
    </el-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
        options: [{
          value: '选项1',
          label: '传染病'
        }, {
          value: '选项2',
          label: '寄生虫病'
        }, {
          value: '选项3',
          label: '内科'
        }, {
          value: '选项4',
          label: '外产科疾病'
        }, {
          value: '选项5',
          label: '常用手术'
        }, {
          value: '选项6',
          label: '免疫'
        }],
        value: '',
        desc:[{name:"1"},{name:'2'},{name:'3'}],
      fileList: [{name: 'food.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'}, {name: 'food2.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'}],
      viewArr:[{name:'临床症状'},{name:'检查过程及结果'},{name:'诊断结果'},{name:'治疗方案'}],
      title: "病例",
      textarea: '',
      form: {
        goods_title: "",
        goods_adress: "",
        goods_check:"",
        goods_surplus_num: 0,
        goods_price: 0,
        goods_src: "",
        goods_desc1:"",
        goods_desc2:"",
        goods_desc3:""
      },
    };
  },
  methods: {
     handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePreview(file) {
        console.log(file);
      },
    image_change(file) {
      this.form.goods_src=URL.createObjectURL(file.raw)
      console.log(file);
      this.$message.success("上传图片成功");
    },
  },
};
</script>
<style scoped>
.white{
  height:6px;
}
.navig{
  padding-bottom: 3%;
}
.ProcessOne{
position: relative;
  margin-top: 4%;
  width:60%
}
.Setfloat{
  position: absolute;
    right: -60%;
    top: 15%;
    width:55%;
}
</style>