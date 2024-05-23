<template>
    <div id="posts-cards" class="flex flex-col items-center h-[80%] w-[20%] bg-black/10 p-5 rounded-3xl gap-5 text-black/60 my-10">
      <h2 class="text-xl font-bold">READ MORE</h2>
      <div v-for="(post, index) in posts" :key="index" class="h-[250px] w-[80%] bg-black/10"></div>
    </div>
</template>

<script>
export default {
    name: 'ReadMore',
    props: {
        posts: {
            type: array,
        },
    },
}
</script>