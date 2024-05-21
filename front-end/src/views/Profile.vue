<template>
    <div class="w-[70vw] h-[70vh] flex flex-col mx-auto mt-[7%] rounded-3xl">
        <div class="flex w-[100%] h-[50%]">
            <div class="flex flex-col w-[25%] h-[100%] items-center gap-2 py-6 px-16 bg-black/5 rounded-lg ">
                <img src="../assets/avatar-01.png" alt="" class="border-white border-4 rounded-full">
                <h1 class="text-3xl font-bold"> {{ user.username }}</h1>
                <p>Joined </p>
                <p>23 Sep 2033</p>
            </div>
            <div class="flex flex-col items-start w-[100%] h-[100%] gap-4 py-6 px-16 bg-black/5">
                <h2 class="text-xl font-bold">About {{ user.username }}</h2>
                <div class="flex justify-between w-[80%] text-2xl">
                    <div class="flex flex-col">
                        <p>Posts</p>
                        <p>0</p>
                    </div>                  
                    <div class="flex flex-col">
                        <p>Followers</p>
                        <p>0</p>
                    </div>                  
                    <div class="flex flex-col">
                        <p>Following</p>
                        <p>0</p>
                    </div>                                   
                    <div class="flex flex-col">
                        <p>Liked</p>
                        <p>0</p>
                    </div>                  
                </div>

            </div>
        </div>
        <div class="h-[50%] w-[100%] flex flex-col justify-end">
            <h2 class="text-xl font-bold m-4">POSTS</h2>
            <div class="flex items-center justify-between mx-2 mb-8 text-black/60">
                <div v-for="(post, index) in posts.slice(0, 5)" :key="index" class="h-[200px] w-[19%] bg-black/10 rounded-sm">
                    <img src="../assets/bearded.jpg" alt="">
                    <h3> {{ post.title }}</h3>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useAuthStore } from '../store/auth';
import axios from '../axios';

export default {
    name: 'Profile',
    props: {
        user: {
            type: Object,
        },
        otherUserID: {
            type: Number,
        }
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
            const response = await axios.get('https://jsonplaceholder.typicode.com/posts');
            this.posts = response.data;
            console.log("Fetching posts...");
        },

        async fetchUser() {
            if (this.otherUserID) {
            const response = await axios.get(`https://jsonplaceholder.typicode.com/users/${this.otherUserID}`);
            this.user = response.data;
            }
            return
        }
    },
}
</script>
