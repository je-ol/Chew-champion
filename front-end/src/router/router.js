import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../views/MainPage.vue'
import LogIn from '../views/LogIn.vue'
import Register from '../views/Register.vue'
import Profile from '../views/Profile.vue'
import All from '../views/All.vue'
import Feed from '../views/Feed.vue'
import Feasters from '../views/Feasters.vue'
import Fans from '../views/Fans.vue'
import NewPost from '../views/NewPost.vue'
import SinglePost from '../views/SinglePost.vue'

const routes = [
    {path: '/', component: MainPage, meta: {title: 'Main Page'}},
    {path: '/login', component: LogIn, meta: {title: 'Login'}},
    {path: '/register', component: Register, meta: {title: 'Register'}},
    {path: '/profile', component: Profile, meta: {title: 'Profile'}},
    {path: '/all', component: All, meta: {title: 'All'}},
    {path: '/feed', component: Feed, meta: {title: 'Feed'}},
    {path: '/feasters', component: Feasters, meta: {title: 'Feasters'}},
    {path: '/fans', component: Fans, meta: {title: 'Fans'}},
    {path: '/new-post', component: NewPost, meta: {title: 'New post'}},

    {path: '/profile:user', component: Profile, meta: {title: 'Profile'}},
    {path: '/:post', component: SinglePost, meta: {title: 'Post'}},


]

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | Chew Champion`;
    next()
})

export default router