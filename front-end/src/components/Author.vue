<template>
    <router-link :to="`/profile${post.user}`">
        <div id="author-container" class="flex justify-around h-[100%] w-[100%]  p-5 rounded-3xl text-black/60">
            <div>
            <img src="/src/assets/avatar-01.png" alt="" class="h-[100px] w-[100px] rounded-full border-solid border-white border-[4px]">
            </div>
            <div>
            <h3 class="text-lg font-semibold mt-2">Written by {{ post.username }}</h3>
            <p :title="new Date(post.date).toLocaleString('es-ES')"  > {{ timeAgo(post.date) }}</p>
            <button class="bg-[#758bfd] font-bold text-sm mt-1 px-2 py-1 rounded-sm text-white">Visit profile</button>
            </div>
        </div>
    </router-link>
</template>

<script>
import { timeAgo } from '../utils/timeAgo.js';

    export default {
        name: 'Author',
        props: {
            post: {
                type: Object,
            }
        },
        methods: {
        timeAgo
        }
    }
</script>