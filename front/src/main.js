import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import router from './router'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  data() {
    return {
      userName:'游客'
    }
  },
  router,
}).$mount('#app')
