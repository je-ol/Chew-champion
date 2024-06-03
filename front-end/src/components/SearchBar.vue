<template>
    <div>
      <form @submit.prevent="handleSearch" class="text-black">
        <input type="text" v-model="search" placeholder="Search posts..."
        class="w-[260px] h-[40px] rounded-md p-4">
      </form>
    </div>
  </template>
  
  <script>
  import axios from '../axios';
  import { useAuthStore } from '../store/auth';

  
  export default {
    name: 'SearchBar',
    data() {
      return {
        search: '',
        posts: [],
      };
    },
    methods: {
      async fetchAllPosts() {
        try {
          const response = await axios.get('/posts/', {
            headers: {
              Authorization: `token ${localStorage.getItem('token')}`,
            },
          });
          this.posts = response.data.reverse(); // Reverse to show newest posts first
        } catch (error) {
          console.error('Error fetching posts:', error);
        }
      },
      handleSearch() {
        const filteredPosts = this.posts.filter(post =>
          post.title.toLowerCase().includes(this.search.toLowerCase())
        );
        const postStore = useAuthStore();
        postStore.setPosts(filteredPosts);
        this.$router.push({ name: 'PostList' });
        this.search = '';
      },
    },
    async created() {
      await this.fetchAllPosts();
    },
  };
  </script>
