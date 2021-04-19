<template>
<div> 
<div> 
      <el-breadcrumb separator-class="el-icon-arrow-right">
  <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
  <el-breadcrumb-item>基本结构与功能管理</el-breadcrumb-item>
  <el-breadcrumb-item>科室管理</el-breadcrumb-item>
  
</el-breadcrumb>
</div>
<div style="margin-top:2%">
  <el-table
    :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
    style="width: 100%  ">
    <el-table-column
      label="日期"
      prop="date">
    </el-table-column>
    <el-table-column
      label="科室名称"
      prop="name">
    </el-table-column>
  
      <template slot="header"  slot-scope="{}">
            <el-button type="success" size="small" @click="add">增加</el-button>
      </template>
    <el-table-column
      align="right">
      <template slot="header"  slot-scope="{}">
            <el-button type="success" size="small" @click="add">增加</el-button>
        <el-input
          v-model="search"
          size="mini"
          placeholder="输入关键字搜索"/>
      </template>
  
      <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
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
      }
    },
    methods: {
      handleEdit(index, row) {
        console.log(index, row);
      },
      handleDelete(index, row) {
        console.log(index, row);
      }
    },
  }
</script>