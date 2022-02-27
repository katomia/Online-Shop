<template>
  <el-container>
    <el-main>
      <HelloWorld msg="你好" />
      <el-tabs v-model="activeName">
        <el-tab-pane label="登录" name="login">
          <el-form ref="loginForm" :model="loginForm" label-width="80px">
            <el-form-item label="账号">
              <el-input v-model="loginForm.name"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="pass">
              <el-input
                type="password"
                v-model="loginForm.pass"
                autocomplete="off"
              ></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="loginSubmit">登录</el-button>
              <el-button>取消</el-button>
            </el-form-item>
          </el-form>
        </el-tab-pane>
        <el-tab-pane label="注册" name="signup">
                    <el-form
            :model="ruleForm"
            status-icon
            :rules="rules"
            ref="ruleForm"
            label-width="100px"
            class="demo-ruleForm"
          >
            <el-form-item label="账号" prop="name">
              <el-input v-model="ruleForm.name"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="pass">
              <el-input
                type="password"
                v-model="ruleForm.pass"
                autocomplete="off"
              ></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="checkPass">
              <el-input
                type="password"
                v-model="ruleForm.checkPass"
                autocomplete="off"
              ></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="signupSubmit('ruleForm')"
                >注册</el-button
              >
              <el-button @click="resetForm('ruleForm')">重置</el-button>
            </el-form-item>
          </el-form>
        </el-tab-pane>
      </el-tabs>
    </el-main>
  </el-container>
</template>


<script>
import axios from "axios";
import HelloWorld from "@/components/HelloWorld.vue";
export default {
  name: "Home",
  components: { HelloWorld },
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.ruleForm.checkPass !== "") {
          this.$refs.ruleForm.validateField("checkPass");
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.ruleForm.pass) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };
    return {
      ruleForm: {
        name: "",
        pass: "",
        checkPass: "",
      },
      loginForm: {
        name: "",
        pass: "",
      },
      rules: {
        name: [
          { required: true, message: "请输入账号", trigger: "blur" },
          {
            min: 3,
            max: 10,
            message: "长度在 3 到 10 个字符",
            trigger: "blur",
          },
        ],
        pass: [{ validator: validatePass, trigger: "blur" }],
        checkPass: [{ validator: validatePass2, trigger: "blur" }],
      },
      activeName: "login",
    };
  },
  methods: {
    async signup(name, pass) {
      try {
        console.log("post data");
        const response = await axios.post("http://127.0.0.1:5000/signup", {
          name: name,
          pass: pass,
        });
        console.log("response:" + response);
        this.$notify({
          title: "成功",
          message: "注册成功",
          type: "success",
        });
      } catch (error) {
        console.log("发送失败");
        this.$notify.error({
          title: "失败",
          message: "注册失败",
        });
      }
    },
    async login(name, pass) {
      try {
        const response = await axios.post("http://127.0.0.1:5000/login", {
          name: name,
          pass: pass,
        });
        console.log(response.data.state);
        
        if (response.data.state === "false") {
          this.$notify.error({
            title: "失败",
            message: "用户名和或密码错误",
          });
        } else {
          this.$root.userName=name;
          console.log(this.userName);
          this.$notify({
            title: "成功",
            message: "登录成功",
            type: "success",
          });
        }
      } catch (error) {
        console.log("发送失败");
        this.$notify.error({
          title: "失败",
          message: "登录失败",
        });
      }
    },
    signupSubmit(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          console.log("submit!");
          this.signup(this.ruleForm.name, this.ruleForm.pass);
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    loginSubmit() {
      this.login(this.loginForm.name, this.loginForm.pass);
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
  },
};
</script>

<style scoped>
.el-main {
  max-width: 500px;
  color: #333;
  text-align: center;
  line-height: 160px;
  margin: auto;
}
</style>