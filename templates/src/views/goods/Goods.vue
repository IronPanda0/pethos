<template>
<div>
  <div class="navig">
      <el-breadcrumb separator-class="el-icon-arrow-right">
  <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
  <el-breadcrumb-item>病例分布</el-breadcrumb-item>
  <el-breadcrumb-item>病例列表</el-breadcrumb-item>
</el-breadcrumb>
  </div>
   
  <!-- <el-checkbox :indeterminate="isIndeterminate" v-model="checkAll" @change="handleCheckAllChange">全选</el-checkbox> -->
  <!-- <div style="margin: 15px 0;"></div> -->
 <div class="topchoose">
    <el-checkbox-group v-model="checkedCities" @change="handleCheckedCitiesChange">
    <el-checkbox v-for="city in cities" :label="city" :key="city">{{city}}</el-checkbox>
  </el-checkbox-group>
 </div>

  <el-row :gutter="20" v-infinite-scroll="load">
    <el-col
      :xs="24" :md="8"  :lg="6"
      v-for="(goods, index) in goods_data"
      :key="index"
      style="margin-top: 10px"
    >
 
      <el-card shadow="never">
        <div slot="header">
          <span>{{ goods.goods_title }}</span>
         <div class="changeStyle">
            <el-tag :type="goods.goods_surplus_num < 10 ? 'danger' : 'success'"
            >学习者{{ goods.goods_surplus_num }}</el-tag
          >
         </div>
        </div>
        <div>
          <!-- <el-popover
            placement="top-start"
            title="来源"
            trigger="hover"
            :content="goods.goods_adress"
          > -->
            <el-image slot="reference" :src="goods.goods_src"></el-image>
          <!-- </el-popover> -->
        </div>
        <div align="center">
          <!-- <el-button
            size="small"
            type="danger"
            round
            icon="el-icon-shopping-cart-2"
            >{{ goods.goods_price }}</el-button
          > -->
               <el-button
            size="small"
            type="success"
            plain
            style="margin-top: 10px;width:30%"
            icon="el-icon-s-management"
            ></el-button
          >
             <el-button
            size="small"
            type="success"
            plain
            style="margin-top: 10px;width:30%"
            icon="el-icon-s-open"
            ></el-button
          >
             <el-button
            size="small"
            type="danger"
            plain
            style="margin-top: 10px;width:30%"
            icon="el-icon-delete-solid"
            ></el-button
          >
        </div>
      </el-card>
    </el-col>
  </el-row>
</div>
  
</template>
<script>
 const cityOptions = ['传染病', '寄生虫病', '内科','外产科疾病','常用手术','免疫'];
export default {
  data() {
    return {
        checkAll: false,
        checkedCities: ['上海', '北京'],
        cities: cityOptions,
        isIndeterminate: true,
      goods_data: [],
    };
  },
  methods: {
    create_goods_data() {
      var goods = new Array();
      for (let index = 0; index < 50; index++) {
        goods[index] = {
          id: index,
          goods_title:
            parseInt(Math.random() * 2, 10) + 1 == 1 ? "病例一" : "病例二",
          goods_src:
            "https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg",
          goods_adress: "病例来源于医疗网站，无反馈",
          goods_surplus_num: parseInt(
            Math.random() * (1000 - 100 + 1) + 100,
            10
          ),
          goods_price: parseInt(Math.random() * (1000 - 100 + 1) + 100, 10),
        };
      }
      this.goods_data = goods;
      // console.log(goods)
    },
    load() {
      var goods = new Array();
      for (let index = 0; index < 50; index++) {
        goods = {
          id: index,
          goods_title:
            parseInt(Math.random() * 2, 10) + 1 == 1 ? "病例一" : "病例二",
          goods_src:
            "https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg",
          goods_adress: "该病例来源于医疗网站，无反馈",
          goods_surplus_num: parseInt(
            Math.random() * (1000 - 100 + 1) + 100,
            10
          ),
          goods_price: parseInt(Math.random() * (1000 - 100 + 1) + 100, 10),
        };
        this.goods_data.splice( this.goods_data.length,0,goods)
      }
      this.$message('生成数据成功')
      console.log(this.goods_data)
    },
      handleCheckAllChange(val) {
        this.checkedCities = val ? cityOptions : [];
        this.isIndeterminate = false;
      },
      handleCheckedCitiesChange(value) {
        let checkedCount = value.length;
        this.checkAll = checkedCount === this.cities.length;
        this.isIndeterminate = checkedCount > 0 && checkedCount < this.cities.length;
      }
  },
  mounted() {
    this.create_goods_data();
  },
};
</script>
<style scoped>
.navig{
  padding-bottom: 2%;
}
.changeStyle{
  float:right;
}
.topchoose{
  background-color: #fff;
  padding: 1%;
  border-radius: 3%;
}
</style>