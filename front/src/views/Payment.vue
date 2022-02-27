<template>
    <div>
    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="id" label="编号" width="150"> </el-table-column>
      <el-table-column prop="time" label="日期" width="150"> </el-table-column>
      <el-table-column prop="o_id" label="订单编号" width="150"> </el-table-column>
      <el-table-column prop="amount" label="总额" width="150"></el-table-column>
      <el-table-column prop="state" label="状态"> </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      tableData: [],
    };
  },
  methods: {
    async getPayment() {
      try {
        console.log("try to get payment");
        const response = await axios.post("http://127.0.0.1:5000/getPayment", {
          c_name: this.$root.userName,
        });
        this.tableData = response.data.payment;
        this.$notify({
          title: "成功",
          message: "查询付款成功",
          type: "success",
        });
      } catch (error) {
        console.log("查询失败");
        this.$notify.error({
          title: "失败",
          message: "查询付款失败",
        });
      }
    },
  },
  created: function () {
    this.getPayment();
  },
};
</script>

<style>

</style>