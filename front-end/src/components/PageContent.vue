<template>
  <main class="w-[100%] h-[100%] flex bg-[#f0f0f0]">
    <div class="m-auto h-[717px] flex flex-col justify-center"
    v-if="page"> {{ console.log(page) }}
      <h1 class="text-2xl font-bold">{{ page.pageTitle }}</h1>
      <p>{{ page.pageContent }} </p>
      <!-- <p>{{ $route.params.index }}</p> -->
    </div>
  </main>
</template>

<script>
export default {
  created() {
    this.page = this.$pages.getSinglePage(this.$route.params.index);
  },
  data() {
    return {
      page: null
    };
  }
/*   name: "PageContent",
  props: {
    page: Object,
  }, */
};
</script>
