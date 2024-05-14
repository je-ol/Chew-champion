import { createApp } from 'vue'
import App from './App.vue'
import router from './router.js'
import './index.css'
import $pages from './data.js'

const app = createApp(App)
app.use(router);

app.config.globalProperties.$pages = $pages;

app.mount('#app');
