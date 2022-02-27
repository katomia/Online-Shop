<template>
  <div>
    <el-row>
      <el-col :span="8" v-for="(g, i) in goods" :key="i">
        <el-card :body-style="{ padding: '4px' }">
          <img :src="imgSrc(g)" class="image" />
          <div style="padding: 14px">
            <span
              >{{ g.name }} {{ g.price }}￥ 打折后{{
                (g.price * g.discount).toFixed(2)
              }}￥</span
            >
            <div class="bottom clearfix">
              <span class="desc">{{ g.description }}</span>
              <el-button type="text" class="button" @click="addToCart(g)"
                >加购</el-button
              >
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-badge :value="goodsNumber" class="item">
      <el-button
        @click="drawer = true"
        type="primary"
        style="margin-left: 16px"
      >
        购物车
      </el-button>
    </el-badge>

    <el-drawer title="购物车" :visible.sync="drawer" :direction="direction">
      <el-table :data="cartData" style="width: 100%">
        <el-table-column prop="name" label="名称" width="100">
        </el-table-column>
        <el-table-column prop="price" label="价格" width="100">
        </el-table-column>
        <el-table-column prop="number" label="数量"> </el-table-column>
      </el-table>
      <span>总价：{{ this.totalPrice }}</span>
      <el-button @click="clearCart"> 清空 </el-button>
      <el-button @click="placeOrder"> 下单 </el-button>
    </el-drawer>
  </div>
</template>

<style>
.desc {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}
</style>

<script>
import axios from "axios";
export default {
  data() {
    return {
      goods: [],
      currentDate: new Date(),
      cartData: [],
      drawer: false,
      direction: "rtl",
      goodsNumber: 0,
      totalPrice: 0,
    };
  },
  methods: {
    async getGoods() {
      try {
        console.log("try get goods");
        const response = await axios.get("http://127.0.0.1:5000/getGoods");
        this.goods = response.data.goods;
        this.$notify({
          title: "成功",
          message: "查询商品成功",
          type: "success",
        });
      } catch (error) {
        console.log("查询失败");
        this.$notify.error({
          title: "失败",
          message: "查询商品失败",
        });
      }
    },
    imgSrc(item) {
      return require("../assets/goods/" + item.picture);
    },
    addToCart(goods) {
      this.$notify({
        title: "成功",
        message: "加购成功",
        type: "success",
      });
      this.goodsNumber++;
      let p = Number((goods.price * goods.discount).toFixed(2));
      this.totalPrice += p;
      for (const g of this.cartData) {
        if (g.name == goods.name) {
          g.number++;
          return;
        }
      }
      this.cartData.push({ name: goods.name, price: p, number: 1 });
    },
    clearCart() {
      this.cartData = [];
      this.goodsNumber = 0;
      this.totalPrice = 0;
    },
    async placeOrder() {
      let trading=[];
      for (const c of this.cartData) {
        trading.push({name:c.name,number:c.number})
      }
      try {
        console.log("try get goods");
        const response = await axios.post("http://127.0.0.1:5000/placeOrder",{
          count:this.goodsNumber,
          amount:this.totalPrice,
          c_name:this.$root.userName,
          trading:trading
        });
        console.log(response.data)
        this.$notify({
          title: "成功",
          message: "下单成功",
          type: "success",
        });
      } catch (error) {
        console.log("下单失败");
        this.$notify.error({
          title: "失败",
          message: "下单失败",
        });
      }
    },
  },
  created: function () {
    this.getGoods();
  },
};
</script>