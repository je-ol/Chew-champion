<template>
    <router-link :to="`/profile${post.user}`">
        <div id="author-container" class="flex justify-around items-center h-[100%] w-[100%] p-5 rounded-3xl text-black/60">
            <div>
                <img :src="getAvatarUrl(post.user)" alt="" class="h-[100px] w-[100px] rounded-full border-solid border-white border-[4px]">
            </div>
            <div class="flex flex-col w-[120px]">
                <h3 class="text-lg font-semibold mt-2">Written by {{ post.username }}</h3>
                <p :title="new Date(post.date).toLocaleString('es-ES')"  > {{ timeAgo(post.date) }}</p>
                <button class="bg-[#758bfd] font-bold text-sm mt-1 px-2 py-1 rounded-sm text-white">Visit profile</button>
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