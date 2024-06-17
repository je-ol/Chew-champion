<template>
    <div class="flex w-[100%] h-[40%] bg-black/5">
        <div class="flex flex-col w-[25%] h-[100%] items-center justify-center gap-1 px-16 rounded-lg ">
            <img :src="getAvatarUrl(userProfile?.id)" alt="" class="w-[100px] h-[100px] md:w-[80px] md:h-[70px] border-white border-4 rounded-full">
            <h1 class="text-2xl md:text-sm font-bold"> {{ userProfile?.username }}</h1>
            <p class="md:text-xs">Joined </p>
            <p class="md:text-xs">23 Sep 2033</p>
        </div>
        <div class="flex flex-col items-start w-[100%] h-[100%] gap-4 py-6 px-16 ">
            <h2 class="text-xl font-bold ">About {{ userProfile?.username }}</h2>
            <div class="flex justify-start gap-16 w-[80%] text-2xl">
                <div class="flex flex-col">
                    <p>Posts</p>
                    <p>{{ posts.length }}</p>
                </div>                                                   
                <div class="flex flex-col">
                    <p>Liked</p>
                    <p>{{ likedPosts.length }}</p>
                </div>                  
            </div>
            
        </div>
    </div>
</template>
<script>
import axios from '../axios';
import { getAvatarUrl } from '../utils/getAvatars.js';

export default {
    name: 'ProfileAbout',
    props: {
        userProfile: {
            type: Object,
        },
        posts: {
            type: Array,
        },
    },
    data() {
        return {
            likedPosts: [],
        };
    },
    watch: {
        userProfile() {
            this.fetchLikedPosts();
        },
    },
    methods: {
        async fetchLikedPosts() {
            if(this.userProfile) {
                try {
                    const response = await axios.get(`likes/?user_id=${this.userProfile.id}`, {
                        headers: {
                            Authorization: `token ${localStorage.getItem('token')}`
                        }
                    });
                    this.likedPosts = response.data;
                } catch (error) {
                    console.error(error);
                
                }
            }
        },
        getAvatarUrl,
    }
}
</script>