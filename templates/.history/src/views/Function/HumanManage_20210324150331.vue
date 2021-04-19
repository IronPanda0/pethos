<template>
    <div>
        <div style="font-size: 30px;color: salmon">表格案例</div>
    <!--按钮、表格-->
    <el-card class="box-card">
      <el-button type="success" size="small" @click="add">增加</el-button>
      <el-table :data="tableData" stripe>
        <el-table-column prop="date" label="日期" align="center">
        </el-table-column>
        <el-table-column prop="name" label="姓名" align="center">
        </el-table-column>
        <el-table-column prop="address" label="地址" align="center">
        </el-table-column>
        <el-table-column prop="age" label="年龄" align="center">
        </el-table-column>
        <el-table-column label="操作" fixed="right" align="center">
          <template slot-scope="scope">
            <el-button type="primary" size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button type="danger" size="small" @click="remove(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    <!--弹窗-->
    <el-dialog :title="dialogTitle" width="50%" :visible.sync="iconFormVisible">
      <el-form :inline="true" :model="userInfo" class="demo-form-inline">
        <el-form-item label="姓名">
          <el-input v-model="userInfo.name" placeholder="姓名"></el-input>
        </el-form-item>
        <el-form-item label="日期">
          <el-input v-model="userInfo.date" placeholder="日期"></el-input>
        </el-form-item>
        <el-form-item label="地址">
          <el-input v-model="userInfo.address" placeholder="地址"></el-input>
        </el-form-item>
        <el-form-item label="年龄">
          <el-input v-model="userInfo.age" placeholder="年龄"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="iconFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitUser()">确 定</el-button>
      </div>
    </el-dialog>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                columns: [{
                        name: "用户名",
                        prop: "name",
                    },
                    {
                        name: "电话号码",
                        prop: "phone",
                    },
                    {
                        name: "年龄",
                        prop: "age",
                    },
                ],
                data: [{
                        name: "小明",
                        phone: "123456",
                        age: 12,
                    },
                    {
                        name: "小龙",
                        phone: "123456",
                        age: 12,
                    },
                    {
                        name: "小李",
                        phone: "123456",
                        age: 12,
                    },
                    {
                        name: "小陈",
                        phone: "123456",
                        age: 12,
                    },
                    {
                        name: "李白",
                        phone: "123456",
                        age: 12,
                    },
                    {
                        name: "张三",
                        phone: "123456",
                        age: 12,
                    },
                ],
            };
        },
        methods: {
            edit(index) {
                this.$message.success('编辑' + this.data[index].name)
            },
            remove(index) {
                this.$message.error('删除' + this.data[index].name)
            }
        }
    };
</script>