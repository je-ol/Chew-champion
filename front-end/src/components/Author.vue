<template>
    <router-link :to="`/profile${post.user}`">
        <div id="author-container" class="flex justify-around items-center h-[100%] w-[100%] p-5 md:p-1 rounded-3xl text-black/60">
            <div>
                <img :src="getAvatarUrl(post.user)" alt="" class="h-[100px] md:h-[80px] w-[100px] md:w-[80px] rounded-full border-solid border-white border-[4px]">
            </div>
            <div class="flex flex-col w-[120px]">
                <h3 class="text-lg md:text-sm font-semibold mt-2">Written by {{ post.username }}</h3>
                <p :title="new Date(post.date).toLocaleString('es-ES')"  class="md:text-sm" > {{ timeAgo(post.date) }}</p>
                <button class="bg-[#758bfd] font-bold text-sm md:text-xs mt-1  py-1 rounded-sm text-white">Visit profile</button>
            </div>
        </div>
    </router-link>
</template>

<script>
import { timeAgo } from '../utils/timeAgo.js';
import { getAvatarUrl } from '../utils/getAvatars.js';

    export default {
        name: 'Author',
        props: {
            post: {
                type: Object,
            }
        },
        methods: {
        timeAgo,
        getAvatarUrl
        }
    }
</script>