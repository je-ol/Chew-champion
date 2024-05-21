import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import router from './router/router.js';
import { createPinia } from 'pinia';
/* import { QuillEditor } from '@vueup/vue-quill' */


const pinia = createPinia();

const app = createApp(App);
/* app.component('QuillEditor', QuillEditor) */
app.use(router);
app.use(pinia);

app.mount('#app');
