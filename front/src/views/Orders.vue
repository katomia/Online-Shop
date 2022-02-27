  <template>
  <div>
    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="id" label="编号" width="150"> </el-table-column>
      <el-table-column prop="time" label="日期" width="150"> </el-table-column>
      <el-table-column prop="count" label="数量" width="150"> </el-table-column>
      <el-table-column prop="amount" label="总额" width="150"></el-table-column>
      <el-table-column prop="state" label="状态"> </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="mini" @click="handlePay(scope.row)">付款</el-button>
        </template>
      </el-table-column>
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
    async handlePay(row) {
      if (row.state != 0) {
        this.$notify.error({
          title: "失败",
          message: "已付款",
        });
        return
      }
      try {
        console.log("try to pay");
        console.log(row);
        const response = await axios.post("http://127.0.0.1:5000/pay", {
          o_id: row.id,
          amount: row.amount,
        });
        console.log(response.data);
        row.state = 1;
        this.$notify({
          title: "成功",
          message: "付款成功",
          type: "success",
        });
      } catch (error) {
        console.log("付款失败");
        this.$notify.error({
          title: "失败",
          message: "付款失败",
        });
      }
    },
    async getOrders() {
      try {
        console.log("try to get orders");
        const response = await axios.post("http://127.0.0.1:5000/getOrders", {
          c_name: this.$root.userName,
        });
        this.tableData = response.data.orders;
        this.$notify({
          title: "成功",
          message: "查询订单成功",
          type: "success",
        });
      } catch (error) {
        console.log("查询失败");
        this.$notify.error({
          title: "失败",
          message: "查询订单失败",
        });
      }
    },
  },
  created: function () {
    this.getOrders();
  },
};
</script>

<style>
</style>