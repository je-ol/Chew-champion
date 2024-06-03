<template>
  <div id="postpage-container" v-if="post" class="flex justify-evenly w-[100%] mt-[80px] py-8">
    <div id="posts-container" class="flex flex-col items-center w-[60%] rounded-3xl text-black/80">
      <div class="flex flex-col w-[100%] gap-2 mx-4 bg-black/10 rounded-sm shadow-md">
        <img v-if="post.image_url" :src="post.image_url" alt="" class="w-[100%] h-[500px] object-cover rounded-t-sm">
        <div class="flex self-end m-4">
          <!-- LIKE -->
          <div class="flex items-center mr-6 text-2xl font-bold">
            <Like :postId="post.post" />
          </div>
          <div v-if="user?.id === post.user" class="flex">
            <img src="../assets/edit.png" title="edit" class="mr-4 cursor-pointer w-[42px] h-[42px] bg-[#ff9602]/80 rounded-full p-2 border-2 border-white" @click="toggleEdit">
            <img src="../assets/delete.png" title="delete" class="mr-4 cursor-pointer w-[42px] h-[42px] bg-[#ba2222]/80 rounded-full p-2 border-2 border-white" @click="deletePost">
          </div>
        </div>
        <div v-if="isEditing" class="flex flex-col w-[90%] gap-4 m-4 px-4 text-black/80">
          <input v-model="editedTitle" type="text" class="w-full border p-2" placeholder="Edit title">
          <textarea v-model="editedContent" class="w-full border p-2" placeholder="Edit content"></textarea>
          <div class="flex gap-2">
            <button @click="saveEdit" class=" bg-[#758bfd] px-4 py-2 rounded-sm text-white">Save</button>
            <button @click="toggleEdit" class=" bg-gray-500 text-white px-4 py-2 rounded-sm">Cancel</button>
          </div>
        </div>
        <div v-else class="flex flex-col w-[90%] gap-4 mx-4 px-4 text-black/80">
          <h2 class="text-3xl font-bold">{{ post.title }}</h2>
          <div v-html="renderContent(post.content)" class="text-lg"></div>
          <p class="font-bold my-4">{{ new Date(post.date).toLocaleString('es-ES') }}</p>
        </div>
        <CommentSection :post="post" />
      </div>
    </div>
    <div class="side-container flex flex-col w-[20%] gap-2">
      <Author :post="post" />
      <hr class="border-black w-[80%] mx-auto mt-1">
      <ReadMore :post="post" :key="post.post" />
    </div>
  </div>
  <CreateButton />
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import axios from '../axios';
import Like from '../components/Like.vue';
import { useAuthStore } from '../store/auth';
import ReadMore from '../components/ReadMore.vue';
import Author from '../components/Author.vue';
import { timeAgo } from '../utils/timeAgo.js';
import CommentSection from '../components/CommentSection.vue';
import CreateButton from '../components/CreateButton.vue';

export default {
  name: 'SinglePost',
  components: {
    Like,
    ReadMore,
    Author,
    CommentSection,
    CreateButton,
  },
  methods: {
    timeAgo,
    renderContent(content) {
      return content.replace(/\n/g, '<br>');
    },
  },
  setup() {
    const { user } = useAuthStore();
    const route = useRoute();
    const post = ref(null);
    const isEditing = ref(false);
    const editedTitle = ref('');
    const editedContent = ref('');
    const posts = ref([]);

    const fetchPost = async () => {
      try {
        const response = await axios.get(`/posts/${route.params.post}/`, {
          headers: {
            Authorization: `token ${localStorage.getItem('token')}`,
          },
        });
        post.value = response.data;
        editedTitle.value = response.data.title;
        editedContent.value = response.data.content;
      } catch (error) {
        console.error('Failed to fetch post:', error);
      }
    };

    const toggleEdit = () => {
      isEditing.value = !isEditing.value;
    };

    const saveEdit = async () => {
      try {
        const response = await axios.put(
          `/posts/${post.value.post}/`,
          {
            title: editedTitle.value,
            content: editedContent.value,
          },
          {
            headers: {
              Authorization: `token ${localStorage.getItem('token')}`,
            },
          }
        );
        post.value = response.data;
        isEditing.value = false;
      } catch (error) {
        console.error('Failed to save post:', error);
      }
    };

    const deletePost = async () => {
      if (confirm('Are you sure you want to delete this post?')) {
        try {
          await axios.delete(`/posts/${post.value.post}/`, {
            headers: {
              Authorization: `token ${localStorage.getItem('token')}`,
            },
          });
        } catch (error) {
          console.error('Failed to delete post:', error);
        }
      }
    };

    onMounted(() => {
      fetchPost();
    });

    watch(route, () => {
      fetchPost();
    });

    return {
      post,
      isEditing,
      editedTitle,
      editedContent,
      toggleEdit,
      saveEdit,
      deletePost,
      posts,
      user,
    };
  },
};
</script>