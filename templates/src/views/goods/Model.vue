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
         
          </el-form-item>
 <el-form-item label="所属病种">
       
 </el-form-item>

            <el-form-item label="检查项目">
            
          </el-form-item>
          <el-form-item label="详细介绍">
  

<div class="ProcessOne" v-for="(item) in viewArr" :key="item">
   <el-divider  style="width:60%;"><span style="color:#909399">{{item.name}}</span></el-divider>
   <el-form-item label="" style="width:60%">
    <div class="block">
    <span class="demonstration"></span>
    <el-image :src="src"  ></el-image>
  </div>
 <div class="Setfloat">
   <span>在此处请用一段文字，对于该流程进行的操作进行详细地解释。</span>
  </div>
          </el-form-item>
</div>
 </el-form-item>
          
         
         <el-form-item label="宠物心率">
           
          </el-form-item>

          <el-form-item label="宠物体温">
           
          </el-form-item>
          <el-form-item label="宠物脉搏">
           
          </el-form-item>

        </el-form>
       
      </div>
    </el-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
       
        value: '',
        desc:[{name:"1"},{name:'2'},{name:'3'}],
        src: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
      viewArr:[{name:'临床症状'},{name:'检查过程及结果'},{name:'诊断结果'},{name:'治疗方案'}],
      title: "病例",
      textarea: '',
      form: {
        goods_title: "病例名称（不超过八个字）",
        goods_type: "",
        goods_check:"",
        goods_desc: "",
        goods_price:"",
        goods_pic1: "",
        goods_pic2: "",
        goods_pic3: "",
        goods_desc1:"",
        goods_desc2:"",
        goods_desc3:"",
        goods_heart:"",
        goods_temp:"",
        goods_hand:""
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