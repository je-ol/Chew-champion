<template>
    <div class="h-[60%] w-[100%] flex flex-col justify-evenly">
        <h2 class="text-xl font-bold ml-2">POSTS</h2>
        <div class="flex items-center justify-start gap-4 mx-2 mb-8 text-black/60 ">
            <div v-for="(post, index) in posts.reverse().slice(0, 5)" :key="index" class="h-[100%] w-[19%] bg-black/10 rounded-sm">
                <img :src=post.image_url alt="" class="object-cover h-[70%] w-[100%]">
                <h3> {{ post.title }}</h3>
                <p class="text-sm"> {{ post.content.slice(0, 25) }}...</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProfilePosts',
    props: {
        posts: {
            type: Array,
        },
    },
}
</script>