/* eslint-disable */
<template>
  <div class="body">
      <el-breadcrumb separator-class="el-icon-arrow-right">
  <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
  <el-breadcrumb-item>病种管理</el-breadcrumb-item>
  <el-breadcrumb-item>病种编辑</el-breadcrumb-item>
</el-breadcrumb>

<div class="main">
     <el-table
    :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
    style="width: 100%">
    <el-table-column
      label="分类"
      prop="date">
    </el-table-column>
    <el-table-column
      label="病种"
      prop="date">
    </el-table-column>
    <el-table-column
      label="病例数"
      prop="name">
    </el-table-column>
    <el-table-column
      align="right">
      <template slot="header" >

        <el-input
          v-model="search"
          size="mini"
          placeholder="输入关键字搜索"/>
      </template>
      <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleEdit(scope.$index, scope.row)">查看</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
</div>
  </div>
</template>
<script>
  export default {
    data() {
      return {
         tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄'
        }, {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄'
        }],
        search: ''
      };
    },
    methods: {
         handleEdit(index, row) {
        console.log(index, row);
      },
      handleDelete(index, row) {
        console.log(index, row);
      }
    },
  };
</script>

<style scoped>
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
</style>