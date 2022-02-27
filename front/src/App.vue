<template>
  <div id="app">
  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b"
    router
  >
    <el-menu-item index="/">主页</el-menu-item>
    <el-menu-item index="/goods">商品一览</el-menu-item>
    <el-menu-item index="/orders" >订单管理</el-menu-item>
    <el-menu-item index="/payment" >付款记录</el-menu-item>
    <el-menu-item index="/userInfo" >用户信息</el-menu-item>
    <el-menu-item index="/about" >about</el-menu-item>
    <font color="red">{{this.$root.userName}}</font>
  </el-menu>
  <router-view></router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: "1",
      activeIndex2: "1",
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>

<style>
  #app{
    width:100%;
    height:100%;
    background-color: #f5f5f5;
  }
  html,body{
    width:100%;
    height:100%;
  }
</style>    