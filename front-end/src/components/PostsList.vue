<template>
  <div id="list-container" class="flex w-[100%] h-[100%] mt-[80px] pt-[34px] gap-[3%] justify-center">
    <div id="posts-container" class="flex flex-col items-center w-[70%] gap-1 rounded-3xl">
      <div v-for="(post, index) in posts" :key="index" class="flex flex-col w-[90%] gap-1 bg-black/10 rounded-sm my-6" :class="{ 'hover:bg-black/30': true }">
        <img :src="post.image_url" alt="" class="w-[100%] h-[500px] object-cover rounded-t-sm">
        <div class="flex flex-col w-[80%] gap-2 m-4 px-2 text-black/80">
          <h2 class="text-2xl font-bold">{{ post.title }}</h2>
          <p class="text-md">{{ post.content.slice(0, 250) }}...</p>
          <router-link :to="`/${post.post}`" class="text-blue-500">
            <button class="bg-[#758bfd] px-4 py-2 rounded-sm font-bold text-white">GO TO POST</button>
          </router-link>
        </div>
      </div>
      <div ref="loadMoreTrigger"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostsList',
  props: {
    posts: {
      type: Array,
      required: true
    }
  },
  mounted() {
    this.createObserver();
  },
  methods: {
    createObserver() {
      const options = {
        root: null,
        rootMargin: '0px',
        threshold: 1.0
      };
      const observer = new IntersectionObserver(this.handleIntersect, options);
      observer.observe(this.$refs.loadMoreTrigger);
    },
    handleIntersect(entries) {
      if (entries[0].isIntersecting) {
        this.$emit('load-more');
      }
    }
  }
};
</script>
