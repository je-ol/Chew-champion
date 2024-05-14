import { createRouter, createWebHistory } from 'vue-router'
import PageContent from './components/PageContent.vue'
import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'

const routes = [
    {path: '/:index?', component: PageContent},
    {path: '/login', component: LogIn},
    {path: '/register', component: SignUp}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router