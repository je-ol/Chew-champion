<template>
    <div id="container" 
    class="flex flex-row w-[100%] h-[100%] justify-center gap-[2%] mt-[80px] md:mt-[40px]">
        <p v-if="!this.user" class="m-auto text-center">Login or register to have full access to the blog!</p>
        <div v-else="this.user" id="content" class="grid grid-cols-3 grid-rows-3 gap-3  w-[70%] h-[30%]  my-10 rounded-3xl">
            <div
                v-for="(post, index) in posts.slice(0, 5)"
                :key="index"
                :style="{ backgroundImage: `url(${post.image_url})` }"
                class="flex flex-col justify-end bg-cover bg-center rounded-sm transition-transform duration-300 ease-in-out hover:scale-105 hover:bg-black/20 shadow-lg"
                :class="{ 'hover:bg-black/30': true }">
                <router-link :to="`/${post.post}`">
                    <div class="px-2 bg-black/50">
                        <h1 v-if="post.title.length > 34" class=" text-lg text-[#F1F2F6] font-semibold">{{ post.title.slice(0, 34) }}...</h1>
                        <h1 v-else="" class=" text-lg text-[#F1F2F6] font-semibold">{{ post.title }}</h1>
                        <p class=" text-white/90">{{ post.content.slice(0, 38) }}...</p>
                    </div>
                </router-link>
            </div>
        </div>
        <div id="side-section"
        class="flex flex-col items-center w-[20%] h-[80%] my-10 rounded-3xl text-black/60">
            <div class="flex flex-col items-center w-[80%] h-[400px] md:h-[260px] mt-[30px] md:mt-0 text-center " >
                <h2 class="text-xl md:text-sm font-bold">About Chew Champion</h2>
                <div class="flex w-[120px] h-[116px] md:w-[64px] md:h-[60px] bg-slate-500/20 rounded-full my-4 md:my-0" >
                    <img src="../assets/burger.png" alt=""
                class="w-[80px] h-[80px] md:w-[42px] md:h-[42px] m-auto">
                </div>
                <p class="mb-4 md:text-xs"><!-- Chew Champion is a fun blog about anything related to competitive eating, as well as eating challenges.  -->
                    Are you a fan of the sport or a competitor yourself? Then you're more than welcome to join and share your experiences or opinions with our community! </p>
            </div>
            <hr class="border-black w-[80%]">
            <div class="flex flex-col justify-around h-[140px] my-4 ">
                <h3 class="font-bold">DON'T MISS OUT NEW POSTS!</h3>
                <input type="email" placeholder="Your email address"
                class="pl-2 h-[30px] rounded-md">
                <button class="special-btn h-[30px] bg-[#27187ee2] rounded-sm text-white font-black text-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.9)]">SUBSCRIBE</button>
            </div>
        </div>    
        <CreateButton />
    </div>

</template>
<script>
import axios from '../axios';
import { computed } from 'vue';
import { useAuthStore } from '../store/auth';
import CreateButton from '../components/CreateButton.vue';

export default {
    name: 'MainPage',
    components: {
        CreateButton
    },
    setup() {
        const authStore = useAuthStore();
        const user = computed(() => authStore.user);
        return { authStore, user };
    },
    data() {
        return {
            posts: []
        }
    },
    created() {
        this.fetchPosts();
    },
    methods: {
        async fetchPosts() {
            try {
            const response = await axios.get('posts/', {
                headers: {
                Authorization: `token ${localStorage.getItem('token')}`
                }
            });
            this.posts = response.data.reverse(); // display newest posts first
            } catch (error) {
            console.error('Error fetching posts:', error);
            }
        }
    }
}
</script>