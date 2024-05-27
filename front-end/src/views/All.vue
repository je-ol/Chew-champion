<template>
  <PostsList :posts="visiblePosts" @load-more="loadMorePosts" />
  <div v-if="loading" class="text-center mt-4">Loading more posts...</div>
  <CreateButton />
</template>

<script>
import PostsList from '../components/PostsList.vue';
import axios from '../axios';
import CreateButton from '../components/CreateButton.vue';
import { useAuthStore } from '../store/auth';

export default {
  name: 'All',
  components: {
    PostsList,
    CreateButton,
  },
  data() {
    return {
      posts: [], // All posts fetched from the server
      visiblePosts: [], // Posts currently visible to the user
      loading: false,
      limit: 4, // Number of posts to display per load
      currentOffset: 0, // Offset for simulating pagination
    };
  },
  async created() {
    await this.fetchAllPosts();
    this.loadMorePosts();
  },
  methods: {
    async fetchAllPosts() {
      this.loading = true;
      try {
        const response = await axios.get(`/posts/`, {
          headers: {
            Authorization: `token ${localStorage.getItem('token')}`,
          },
        });

        this.posts = response.data.reverse(); // Reverse to show newest posts first
        const postStore = useAuthStore();
        postStore.setPosts(this.posts);
      } catch (error) {
        console.error('Error fetching posts:', error);
      } finally {
        this.loading = false;
      }
    },
    loadMorePosts() {
      if (this.loading) return;

      const newPosts = this.posts.slice(this.currentOffset, this.currentOffset + this.limit);
      this.visiblePosts = [...this.visiblePosts, ...newPosts];
      this.currentOffset += this.limit;

      if (this.currentOffset >= this.posts.length) {
        this.loading = false; // No more posts to load
      }
    },
  },
};
</script>