<template>
    <div>
         <el-form ref="form" :model="login_form" action="/login" method="POST">
          <el-form-item>
            <el-input id="username" v-model="login_form.user_name" prefix-icon="el-icon-user"></el-input>
          </el-form-item>
          <el-form-item>
            <el-input id="password" v-model="login_form.user_password" prefix-icon="el-icon-lock" show-password></el-input>
          </el-form-item>
             <el-button type="submit">提交</el-button>
        </el-form>
    </div>
</template>
<script>
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
    }
  }
</script>