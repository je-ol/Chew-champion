<template>
  <div id="postpage-container" v-if="post" class="flex w-[100%] justify-start mt-[80px]">
    <div id="posts-container" class="flex flex-col items-center w-[74vw] p-8 rounded-3xl text-black/80">
      <div class="flex flex-col w-[80%] gap-2 m-4 bg-black/10">
        <img v-if="post.image_url" :src="post.image_url" alt="" class="w-[100%] h-[500px] object-cover rounded-t-sm">
        <img v-if="!post.image_url" src="../assets/bearded.jpg" alt="" class="w-[100%] h-[500px] object-cover rounded-t-sm">
        
        <div v-if="post.user === user.id" class="flex self-end mx-4">
          <img src="../assets/edit.png" class="mr-4 cursor-pointer w-[48px] h-[48px] bg-[#ea8b1f]/80 rounded-full p-2 border-2 border-white" @click="toggleEdit">
          <img src="../assets/delete.png" class="mr-4 cursor-pointer w-[48px] h-[48px] bg-[#ba2222]/80 rounded-full p-2 border-2 border-white" @click="deletePost">
        </div>
        
        <div v-if="isEditing" class="flex flex-col w-[90%] gap-4 m-4 px-4 text-black/80">
          <input v-model="editedTitle" type="text" class="w-full border p-2" placeholder="Edit title">
          <textarea v-model="editedContent" class="w-full border p-2" placeholder="Edit content"></textarea>
          <button @click="saveEdit" class="self-end bg-blue-500 text-white px-4 py-2 rounded">Save</button>
          <button @click="toggleEdit" class="self-end bg-gray-500 text-white px-4 py-2 rounded">Cancel</button>
        </div>

        <div v-else class="flex flex-col w-[90%] gap-4 mx-4 px-4 text-black/80">
          <h2 class="text-2xl font-bold"> {{ post.title }}</h2>
          <p class="text-lg"> {{ post.content }}</p>
        </div>

        <div class="flex flex-col w-[100%] self-start bg-white p-8 gap-2">
          <h3 class="text-xl font-semibold">Comments</h3>
          <!-- Display all the comments -->
          <div v-for="(comment, index) in filteredComments" :key="index" class="flex flex-col bg-slate-500/20 p-2 rounded-md">
            <div v-if="!comment.isEditing">
              <p> {{ comment.content }}</p>
              <div class="flex justify-between">
                <p class="font-bold"> {{ comment.username }}</p>
                <div class="flex items-center">
                  <img src="../assets/edit-comment.png" alt="" class="mr-1 cursor-pointer w-[32px] h-[32px] bg-[#ea8b1f] rounded-full p-1 border-2 border-white" @click="toggleCommentEdit(comment)">
                  <img src="../assets/delete.png" class="mr-4 cursor-pointer w-[32px] h-[32px] bg-[#ba2222] rounded-full p-1 border-2 border-white" @click="deleteComment(comment.comment)">
                  <p class="font-bold"> {{ new Date(comment.date).toLocaleString('es-ES') }}</p>
                </div>
              </div>
            </div>
            <div v-else>
              <input v-model="comment.editedContent" type="text" class="w-full border p-2" placeholder="Edit comment">
              <div class="flex justify-end">
                <button @click="saveCommentEdit(comment)" class="bg-blue-500 text-white px-4 py-2 rounded mr-2">Save</button>
                <button @click="toggleCommentEdit(comment)" class="bg-gray-500 text-white px-4 py-2 rounded">Cancel</button>
              </div>
            </div>
          </div>
          <!-- Create a new comment -->
          <div class="new-comment flex justify-between my-4">
            <input type="text" class="w-[85%] h-[50px] px-2 border-2 border-gray-500/20 rounded-md" placeholder="Write a new comment..." v-model="newComment">
            <button class="w-[14%] h-[100%] bg-[#758bfd] px-4 py-2 rounded-md font-bold text-white" @click="sendComment">COMMENT</button>
          </div>
        </div>
      </div>
    </div>

    <router-link :to="`/profile${post.user}`">
      <div id="author-container" class="flex flex-col items-center h-[70vh] fixed right-[100px] top-[14%] w-[20vw] bg-black/10 p-5 rounded-3xl" :otherUserID="post.user">
        <div></div>
        <img src="/src/assets/avatar-01.png" alt="" class="h-[160px] w-[160px] rounded-full border-solid border-white border-[4px]">
        <h3 class="text-xl font-bold mt-2">Written by {{ post.username }}</h3>
      </div>
    </router-link>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from '../axios';

export default {
  name: 'SinglePost',
  props: {
    user: {
      type: Object,
    }
  },
  setup(props) {
    const route = useRoute();
    const post = ref(null);
    const comments = ref([]);
    const isEditing = ref(false);
    const editedTitle = ref('');
    const editedContent = ref('');
    const newComment = ref('');

    const fetchPost = async () => {
      try {
        const response = await axios.get(`/posts/${route.params.post}/`);
        post.value = response.data;
        editedTitle.value = response.data.title;
        editedContent.value = response.data.content;
      } catch (error) {
        console.error('Failed to fetch post:', error);
      }
    };

    const fetchComments = async () => {
      try {
        const response = await axios.get(`comments/`);
        comments.value = response.data;
      } catch (error) {
        console.error('Failed to fetch comments:', error);
      }
    };

    const filteredComments = computed(() => {
      return comments.value.filter(comment => comment.post === post.value.post);
    });

    const toggleEdit = () => {
      isEditing.value = !isEditing.value;
    };

    const saveEdit = async () => {
      try {
        const response = await axios.put(`/posts/${post.value.post}/`, {
          title: editedTitle.value,
          content: editedContent.value,
        });
        post.value = response.data;
        isEditing.value = false;
      } catch (error) {
        console.error('Failed to save post:', error);
      }
    };

    const deletePost = async () => {
      if (confirm('Are you sure you want to delete this post?')) {
        try {
          await axios.delete(`/posts/${post.value.post}/`);
          post.value = null;
        } catch (error) {
          console.error('Failed to delete post:', error);
        }
      } 
    };

    const sendComment = async () => {
      try {
        await axios.post(`comments/`, {
          content: newComment.value,
          post_id: post.value.post,
        });
        newComment.value = '';
        fetchComments();
      } catch (error) {
        console.error('Failed to send comment:', error);
      }
    };

    const toggleCommentEdit = (comment) => {
      comment.isEditing = !comment.isEditing;
      comment.editedContent = comment.content;
    };

    const saveCommentEdit = async (comment) => {
      try {
        await axios.put(`comments/${comment.comment}/`, {
          content: comment.editedContent,
        });
        comment.content = comment.editedContent;
        comment.isEditing = false;
      } catch (error) {
        console.error('Failed to save comment:', error);
      }
    };

    const deleteComment = async (commentID) => {
      if (confirm('Are you sure you want to delete this comment?')) {
        try {
          await axios.delete(`comments/${commentID}/`);
          fetchComments();
        } catch (error) {
          console.error('Failed to delete comment:', error);
        }
      }
    };

    onMounted(fetchPost);
    onMounted(fetchComments);

    return {
      post,
      comments,
      filteredComments,
      isEditing,
      editedTitle,
      editedContent,
      newComment,
      toggleEdit,
      saveEdit,
      deletePost,
      sendComment,
      toggleCommentEdit,
      saveCommentEdit,
      deleteComment,
    };
  }
};
</script>