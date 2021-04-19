<template>
  <!-- 登录页面 -->
  <div id="login">
    <div id="form_space">
      <div align="center">
        <h1>{{ login_title }}</h1>
        <p>{{ login_adress }}</p>
      </div>
      <div style="padding: 20px">
        <el-form ref="form" :model="login_form" action="/login" method="POST">
          <el-form-item>
            <el-input id="username" v-model="login_form.user_name" prefix-icon="el-icon-user"></el-input>
          </el-form-item>
          <el-form-item>
            <el-input id="password" v-model="login_form.user_password" prefix-icon="el-icon-lock" show-password></el-input>
          </el-form-item>
          <el-form-item>
          </el-form-item>

          <el-form-item align="center">
            <el-button type="primary" icon="el-icon-right" @click="login()">登录</el-button>
          </el-form-item>

          <el-form-item>
            <el-link type="danger" style="float: left" @click="to('/register')">注册</el-link>
            <el-link type="primary" style="float: right" @click="to('/forget/password')">找回密码？</el-link>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>
<script>
  import exios from "@/eui/unit/axios/exios";
import axios from 'axios';
import qs from 'qs';
  export default {
    data() {
      return {
        login_title: "PetHospitalAdmin",
        login_adress: "PetHospitalAdmin欢迎你",
        login_form: {
          user_name: "PetHospitalAdmin",
          user_password: "12453",
        },
        remember_password: false,
      };
    },
    methods: {
      login() {
        // axios.post("/login",qs.stringify({
        //   login_form:this.login_form
        // })
        // ).then((res) => {
        //    console.log('res=>',res);   
        //   this.$message.success("登录成功"); //登录提示
        // });
        // this.$router.push("/home");
        this.intial_aside_menu();
      },
      intial_aside_menu() {
        const aslide_menu = [
          {
            name: "主页",
            icon: "fa fa-home",
            name_show: false,
            menu_item: [{
              path: "/home",
              label: "主页",
              label_icon: "fa fa-home",
              label_show: false,
              vist: true
            }, ],
          }
          // ,
          // {
          //   name: "PetHospitalAdmin内置工具",
          //   icon: "fa fa-briefcase",
          //   name_show: true,
          //   menu_item: [{
          //       path: "/eui/tinymce",
          //       label: "Tinymce富文本编辑器",
          //       label_icon: "fa fa-text-width",
          //       label_show: true,
          //       vist: true
          //     },
          //     {
          //       path: "/eui/icon",
          //       label: "图标选择器",
          //       label_icon: "fa fa-openid",
          //       label_show: true,
          //       vist: true
          //     },
          //   ],
          // },
          // {
          //   name: "PetHospitalAdmin表格",
          //   icon: "fa fa-table",
          //   name_show: true,
          //   menu_item: [{
          //       path: "/eui/table",
          //       label: "Eui表格",
          //       label_icon: "fa fa-table",
          //       label_show: true,
          //       vist: true
          //     },
          //     {
          //       path: "/eui/table/out",
          //       label: "Eui表格导出excel",
          //       label_icon: "fa fa-table",
          //       label_show: true,
          //       vist: true
          //     },
          //     {
          //       path: "/table/exios",
          //       label: "表格支持exios",
          //       label_icon: "fa fa-table",
          //       label_show: true,
          //       vist: true
          //     },
          //   ],
          // }
          // ,
          // {
          //   name: "Echarts图表",
          //   icon: "fa fa-area-chart",
          //   name_show: true,
          //   menu_item: [{
          //       path: "/echarts/bar",
          //       label: "柱状图",
          //       label_icon: "fa fa-bar-chart",
          //       label_show: true,
          //       vist: true
          //     },
          //     {
          //       path: "/echarts/line",
          //       label: "折线图",
          //       label_icon: "fa fa-line-chart",
          //       label_show: true,
          //       vist: true
          //     },
          //     {
          //       path: "/echarts/map",
          //       label: "中国地图",
          //       label_icon: "fa fa-map-marker",
          //       label_show: true,
          //       vist: true
          //     },
          //   ],
          // }
          ,
          // {
          //   name: "常用页面",
          //   icon: "fa fa-clone",
          //   name_show: true,
          //   menu_item: [{
          //       path: "/page/eui",
          //       label: "Eui主页",
          //       label_icon: "fa fa-list-alt",
          //       label_show: true,
          //       vist: true
          //     },
          //     {
          //       path: "/page/warning",
          //       label: "404",
          //       label_icon: "fa fa-warning",
          //       label_show: true,
          //       vist: true
          //     },
          //     {
          //       path: "/page/error",
          //       label: "500",
          //       label_icon: "fa fa-window-close",
          //       label_show: true,
          //       vist: true
          //     },
          //   ],
          // },
          {
            name: "病种管理",
            icon: "el-icon-s-help",
            name_show: true,
            menu_item: [{
                path: "/disease/add",
                label: "病种增加",
                label_icon: "fa fa-edit",
                label_show: true,
                vist: true
              },
              {
                path: "/disease/edit",
                label: "病种编辑",
                label_icon: "fa fa-flag",
                label_show: true,
                vist: true
              },
            ],
          },
          {
            name: "病例发布",
            icon: "el-icon-message-solid",
            name_show: true,
            menu_item: [{
                path: "/apply/goods",
                label: "病例列表",
                label_icon: "fa fa-list",
                label_show: true,
                vist: true
              },
              {
                path: "/apply/goods/model",
                label: "病例模板",
                label_icon: "fa fa-anchor",
                label_show: true,
                vist: true
              },
              {
                path: "/apply/goods/release",
                label: "发布病例",
                label_icon: "fa fa-edit",
                label_show: true,
                vist: true
              },
              
            ],
          },
            {
          name: "测试管理",
          icon: "el-icon-s-claim",
          name_show: true,
          menu_item: [
            {
              path: "/test/test",
              label: "题库管理",
              label_icon: "fa fa-clipboard",
              label_show: true,
              vist: true,
            },
            {
              path: "/test/paper",
              label: "试卷管理",
              label_icon: "fa fa-book",
              label_show: true,
              vist: true,
            },
            {
              path: "/test/exam",
              label: "考试管理",
              label_icon: "fa fa-calendar-check-o",
              label_show: true,
              vist: true,
            },
          ],
        },
        {
          name: "职能学习管理",
          icon: "el-icon-s-custom",
          name_show: true,
          menu_item: [
            {
              path: "/RolePlay",
              label: "学习列表",
              label_icon: "fa fa-code-fork",
              label_show: true,
              vist: true,
            },
          ],
        },
             {
            name: "基本结构管理",
            icon: "el-icon-menu",
            name_show: true,
            menu_item: [
            
              {
                path: "/Function/OfficeManage",
                label: "科室管理",
                label_icon: "fa fa-cubes",
                label_show: true,
                vist: true
              },
              {
                path: "/Function/HumanManage",
                label: "人员管理",
                label_icon: "fa fa-drivers-license",
                label_show: true,
                vist: true
              },
                {
                path: "/Function/DrugManage",
                label: "药品管理",
                label_icon: "	fa fa-dropbox",
                label_show: true,
                vist: true
              },
              {
                path: "/Function/FileManage",
                label: "档案管理",
                label_icon: "fa fa-expeditedssl",
                label_show: true,
                vist: true
              },
              {
                path: "/Function/PayManage",
                label: "收费管理",
                label_icon: "fa fa-fax",
                label_show: true,
                vist: true
              },
              {
                path: "/Function/LabProjectManage",
                label: "化验项目管理",
                label_icon: "fa fa-eyedropper",
                label_show: true,
                vist: true
              },
               {
                path: "/Function/VaccineManage",
                label: "疫苗管理",
                label_icon: "fa fa-medkit",
                label_show: true,
                vist: true
              },
               {
                path: "/Function/ClinicManage",
                label: "住院管理",
                label_icon: "fa fa-home",
                label_show: true,
                vist: true
              },
            ],
          },
          {
            name: "设置",
            icon: "el-icon-s-tools",
            name_show: true,
            menu_item: [{
                path: "/setting/power",
                label: "管理员权限管理",
                label_icon: "fa fa-key",
                label_show: true,
                vist: true
              },
              {
                path: "/setting/AdminSure",
                label: "管理员管理",
                label_icon: "fa fa-id-badge",
                label_show: true,
                vist: true
              },
              {
                path: "/setting/web",
                label: "网站基础设置",
                label_icon: "fa fa-institution",
                label_show: true,
                vist: true
              },
              {
                path: "/setting/email",
                label: "邮箱设置",
                label_icon: "fa fa-location-arrow",
                label_show: true,
                vist: true
              },
            ],
          },
          {
            name: "个人设置",
            icon: "el-icon-s-check",
            name_show: true,
            menu_item: [{
                path: "/setting/user",
                label: "个人设置",
                label_icon: "fa fa-user",
                label_show: true,
                vist: true
              },
              {
                path: "/setting/password",
                label: "密码设置",
                label_icon: "fa fa-bullseye",
                label_show: true,
                vist: true
              },
            ],
          }
          // ,
          // {
          //   name: "Socket组件",
          //   icon: "fa fa-link",
          //   name_show: true,
          //   menu_item: [{
          //     path: "/scoket",
          //     label: "客服",
          //     label_icon: "fa fa-users",
          //     label_show: true,
          //     vist: true
          //   }, ],
          // },
          // {
          //   name: "访问日志",
          //   icon: "fa fa-link",
          //   name_show: true,
          //   menu_item: [{
          //     path: "/log",
          //     label: "PetHospital-Admin访问日志",
          //     label_icon: "fa fa-users",
          //     label_show: true,
          //     vist: true
          //   }, ],
          // },
        ];
        sessionStorage.setItem("aslide_menu", JSON.stringify(aslide_menu)); //用sessionStorage储存左侧菜单
        this.$router.push("/home"); //成功后跳转到主页
      },
      to(link) {
        this.$router.push(link);
      },
    },
  };
</script>
<style scoped>
  #form_space {
    border-radius: 10px;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
    height: 400px;
    width: 400px;
  }
</style>