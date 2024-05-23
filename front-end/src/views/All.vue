<template>
  <PostsList :posts="posts" :limit="limit" v-if="posts.length" @load-more="loadMorePosts" />
  <div v-else class="text-center">Loading posts...</div>
  <CreateButton />
  <div v-if="loading" class="text-center mt-4">Loading more posts...</div>
</template>

<script>
import PostsList from '../components/PostsList.vue';
import CreateButton from '../components/CreateButton.vue';
import axios from '../axios';

export default {
  name: 'All',
  components: {
    PostsList,
    CreateButton,
  },
  data() {
    return {
      posts: [],
      loading: false,
      allPostsLoaded: false,
      offset: 0, // Tracks the offset for fetching the next set of posts
      limit: 4, // Number of posts to fetch in each request
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
        const response = await axios.get(`/posts/`, {
          headers: {
            Authorization: `token ${localStorage.getItem('token')}`,
          },
          params: {
            offset: this.offset,
            limit: this.limit,
          },
        });

        // Check if the response data has any length
        this.hasMoreToLoad = response.data.length > 0;

        // Update the posts array only if there's new data
        if (this.hasMoreToLoad) {
          const combinedPosts = [...this.posts, ...response.data];
          this.posts = combinedPosts.reverse(); // Reverse the array to display newest posts first
          this.offset += this.limit; // Update offset for next request
        } else {
          this.allPostsLoaded = true;
        }
      } catch (error) {
        console.error('Error fetching posts:', error);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>