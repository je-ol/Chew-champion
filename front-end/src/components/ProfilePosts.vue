<template>
    <div class="h-[60%] w-[100%] flex flex-col justify-center">
        <h2 class="text-xl font-bold ml-2">POSTS</h2>
        <div class="flex items-center justify-start gap-4 mx-2 mb-8 text-black/60 ">
            
            <div v-for="(post, index) in posts.reverse().slice(0, 5)" :key="index" class="h-[100%] w-[19%] bg-black/10 rounded-sm transition-transform duration-300 ease-in-out hover:scale-105 hover:bg-black/20 shadow-lg">
                <router-link :to="`/${post.post}`">
                    <img :src=post.image_url alt="" class="object-cover h-[70%] w-[100%]">
                    <h3 v-if="post.title.length > 16" class="text-lg font-bold mx-2">{{ post.title.slice(0, 16) }}...</h3>
          <h3 v-else="" class="text-lg font-bold mx-2">{{ post.title.slice(0, 20) }}</h3>
          <p class="mx-2 text-sm">{{ post.content.slice(0, 22) }}...</p>
                </router-link>
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