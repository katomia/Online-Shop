<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <!-- <el-button @click="buttondown">默认按钮</el-button> -->
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  methods:{
    buttondown(){
      this.$notify.error({
        title: '失败',
        message: '登录失败'
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
