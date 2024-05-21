<template>
  <PostsList :posts="posts" @load-more="loadMorePosts" />
  <CreateButton />
</template>

<script>
import PostsList from '../components/PostsList.vue';
import CreateButton from '../components/CreateButton.vue';
import axios from '../axios';

export default {
  name: 'All',
  components: {
    PostsList,
    CreateButton
  },
  data() {
    return {
      posts: [],
      page: 1,
      limit: 5,
      loading: false,
      allPostsLoaded: false
    };
  },
  async created() {
    await this.loadMorePosts();
  },
  methods: {
    async loadMorePosts() {
      if (this.loading || this.allPostsLoaded) return;
      this.loading = true;
      try {
        const response = await axios.get(`https://jsonplaceholder.typicode.com/posts?_page=${this.page}&_limit=${this.limit}`);
        if (response.data.length < this.limit) {
          this.allPostsLoaded = true;
        }
        this.posts = [...this.posts, ...response.data];
        this.page++;
      } catch (error) {
        console.error('Error fetching posts:', error);
      }
      this.loading = false;
    }
  }
};
</script>
