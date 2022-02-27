<template>
  <div>
    <span>id:{{ userInfo.id }}</span> <br>
    <span>name:{{ userInfo.name }}</span><br>
    <span>pass:{{ userInfo.pass }}</span>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      userInfo: {},
    };
  },
  methods: {
    async getUserInfo() {
      try {
        console.log("try to get UserInfo");
        const response = await axios.post("http://127.0.0.1:5000/getUserInfo", {
          c_name: this.$root.userName,
        });
        this.userInfo = response.data.userInfo;
        console.log(this.userInfo)
        this.$notify({
          title: "成功",
          message: "查询信息成功",
          type: "success",
        });
      } catch (error) {
        this.$notify.error({
          title: "失败",
          message: "查询信息失败",
        });
      }
    },
  },
  created: function () {
    this.getUserInfo();
  },
};
</script>

<style>
</style>