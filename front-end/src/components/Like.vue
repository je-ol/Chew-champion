<template>
    <img 
        src="../assets/heart.png" 
        alt="Like button" 
        class="mr-4 cursor-pointer w-[42px] h-[42px] bg-[#F1F2F6]/80 rounded-full p-1 border-2 border-white"
        @click="likePost"
      />
      <span>{{ likes }}</span>
  </template>
  
  <script>
  import axios from '../axios';
  
  export default {
    name: 'Like',
    props: {
      postId: {
        type: Number,
        required: true
      }
    },
    data() {
      return {
        likes: 0,
        isLiked: false,
      };
    },
    async mounted() {
      await this.fetchLikes();
    },
    watch: {
      postId() {
        this.fetchLikes();
      }
    },
    methods: {
      async fetchLikes() {
        try {
          const response = await axios.get(`/likes/`, {
            headers: {
              Authorization: `token ${localStorage.getItem('token')}`
            }
          });
          console.log(response.data);
          const allLikes = response.data;
          this.likes = allLikes.filter(like => like.post === this.postId).length;
        } catch (error) {
          console.error('Error fetching likes:', error);
        }
      },
      async likePost() {
        if (this.isLiked) {
          alert('You have already liked this post');
          return;
        }
  
        try {
          await axios.post(`/posts/${this.postId}/like/`, {}, {
            headers: {
              Authorization: `token ${localStorage.getItem('token')}`
            }
          });
          this.likes += 1;
          this.isLiked = true;
          this.$emit('like', this.postId, this.isLiked);
        } catch (error) {
          console.error('Error liking post:', error);
        }
      }
    }
  };
  </script>
  
  