<template>
  <div id="postpage-container" v-if="post" class="flex justify-evenly w-[100%] mt-[80px] py-8">
    <div id="posts-container" class="flex flex-col items-center w-[60%] rounded-3xl text-black/80">
      <div class="flex flex-col w-[100%] gap-2 mx-4 bg-black/10">
        <img v-if="post.image_url" :src="post.image_url" alt="" class="w-[100%] h-[500px] object-cover rounded-t-sm">
        <img v-if="!post.image_url" src="../assets/bearded.jpg" alt="" class="w-[100%] h-[500px] object-cover rounded-t-sm">
        
        
        <div class="flex self-end mx-4">
          <!-- LIKE -->
          <div class="flex items-center mr-6 text-2xl font-bold">
            <Like :postId="post.post" />
          </div>

          <div v-if="post.user == user?.id" class="flex">
            <img src="../assets/edit.png" title="edit" class="mr-4 cursor-pointer w-[48px] h-[48px] bg-[#ea8b1f]/80 rounded-full p-2 border-2 border-white" @click="toggleEdit">
            <img src="../assets/delete.png" title="delete" class="mr-4 cursor-pointer w-[48px] h-[48px] bg-[#ba2222]/80 rounded-full p-2 border-2 border-white" @click="deletePost">
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
          <h2 class="text-2xl font-bold"> {{ post.title }}</h2>
          <p class="text-lg"> {{ post.content }}</p>
          <p class="font-bold"> {{ new Date(post.date).toLocaleString('es-ES') }}</p>
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
                  <p :title="new Date(comment.date).toLocaleString('es-ES')"  > {{ timeAgo(comment.date) }}</p>
                </div>
              </div>
            </div>
            <div v-else>
              <input v-model="comment.editedContent" type="text" class="w-full border p-2" placeholder="Edit comment">
              <div class="flex gap-2 justify-end mt-2">
                <button @click="saveCommentEdit(comment)" class="bg-[#758bfd] px-4 py-2 rounded-sm text-white">Save</button>
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
    <div class="side-container flex flex-col w-[20%]  gap-2">
      <router-link :to="`/profile${post.user}`">
        <div id="author-container" class="flex justify-around h-[100%] w-[100%]  p-5 rounded-3xl text-black/60">
          <div>
            <img src="/src/assets/avatar-01.png" alt="" class="h-[100px] w-[100px] rounded-full border-solid border-white border-[4px]">
          </div>
          <div>
            <h3 class="text-lg font-semibold mt-2">Written by {{ post.username }}</h3>
            <p :title="new Date(post.date).toLocaleString('es-ES')"  > {{ timeAgo(post.date) }}</p>
            <button class="bg-[#758bfd] font-bold text-sm mt-1 px-2 py-1 rounded-sm text-white">Visit profile</button>
          </div>
        </div>
      <hr class="border-black w-[80%] mx-auto mt-1 ">
      </router-link>
      <div id="posts-cards" class="flex flex-col items-center p-5 rounded-3xl gap-5 text-black/60 my-4">
        <h2 class="text-xl font-bold">READ MORE</h2>
        
          <div v-for="(post, index) in posts.slice(0, 4)" :key="index" class="h-[250px] w-[80%] bg-black/10">
            <router-link :to="`/${post.post}`">
              <img :src=post.image_url alt="" class="object-cover h-[70%] w-[100%]">
              <h3> {{ post.title }}</h3>
              <p> {{ post.content.slice(0, 25) }}...</p>        
            </router-link>
          </div>

      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import axios from '../axios';
import Like from '../components/Like.vue';
import { useAuthStore } from '../store/auth';

export default {
  name: 'SinglePost',
  components: {
    Like,
  },
  props: {
  },
  setup(props) {
    const { user } = useAuthStore();
    const route = useRoute();
    const post = ref(null);
    const comments = ref([]);
    const isEditing = ref(false);
    const editedTitle = ref('');
    const editedContent = ref('');
    const newComment = ref('');
    const posts = ref([]);

    const fetchPost = async () => {
      console.log(user)
      try {
        const response = await axios.get(`/posts/${route.params.post}/`, {
          headers: {
            Authorization: `token ${localStorage.getItem('token')}`
          }
        });
        post.value = response.data;
        editedTitle.value = response.data.title;
        editedContent.value = response.data.content;
        // Fetch posts after post data is set
        await fetchPosts();
      } catch (error) {
        console.error('Failed to fetch post:', error);
      }
    };

    const fetchComments = async () => {
      try {
        const response = await axios.get('comments/', {
          headers: {
            Authorization: `token ${localStorage.getItem('token')}`
          }
        });
        comments.value = response.data;
      } catch (error) {
        console.error('Failed to fetch comments:', error);
      }
    };

    const fetchPosts = async () => {
      try {
        const response = await axios.get('/posts/', {
          headers: {
            Authorization: `token ${localStorage.getItem('token')}`
          }
        });
        const allPosts = response.data.reverse();
        // Check if post.value is not null before filtering
        if (post.value) {
          const filteredPosts = allPosts.filter(singlePost => singlePost.post !== post.value.post);
          posts.value = filteredPosts;
        }
      } catch (error) {
        console.error('Failed to fetch posts:', error);
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
        const response = await axios.put(`/posts/${post.value.post}/`, 
        {
          title: editedTitle.value,
          content: editedContent.value,
        }, {
          headers: {
            Authorization: `token ${localStorage.getItem('token')}`
          },
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
          await axios.delete(`/posts/${post.value.post}/`, {
            headers: {
              Authorization: `token ${localStorage.getItem('token')}`
            }
          });
        } catch (error) {
          console.error('Failed to delete post:', error);
        }
      }
    };

    const sendComment = async () => {
      try {
        await axios.post('comments/', 
          {
            content: newComment.value,
            post_id: post.value.post,
          },
          {
            headers: {
              Authorization: `token ${localStorage.getItem('token')}`
            }
          }
        );
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
        await axios.put(`comments/${comment.comment}/`, 
          {
            content: comment.editedContent,
          }, 
          {
            headers: {
              Authorization: `token ${localStorage.getItem('token')}`
            }
          }
        );
        comment.content = comment.editedContent;
        comment.isEditing = false;
      } catch (error) {
        console.error('Failed to save comment:', error);
      }
    };

    const deleteComment = async (commentID) => {
      if (confirm('Are you sure you want to delete this comment?')) {
        try {
          await axios.delete(`comments/${commentID}/`, {
            headers: {
              Authorization: `token ${localStorage.getItem('token')}`
            }
          });
          fetchComments();
        } catch (error) {
          console.error('Failed to delete comment:', error);
        }
      }
    };

    const timeAgo = (timestamp) => {
      const date = new Date(timestamp);
      const now = new Date();
      const diffInMs = now - date;
      const diffInSeconds = Math.floor(diffInMs / 1000);
      const diffInMinutes = Math.floor(diffInSeconds / 60);
      const diffInHours = Math.floor(diffInMinutes / 60);
      const diffInDays = Math.floor(diffInHours / 24);

      if (diffInSeconds < 60) {
        return diffInSeconds === 1 ? '1 second ago' : `${diffInSeconds} seconds ago`;
      } else if (diffInMinutes < 60) {
        return diffInMinutes === 1 ? '1 minute ago' : `${diffInMinutes} minutes ago`;
      } else if (diffInHours < 24) {
        return diffInHours === 1 ? '1 hour ago' : `${diffInHours} hours ago`;
      } else {
        return diffInDays === 1 ? '1 day ago' : `${diffInDays} days ago`;
      }
    };

    onMounted(() => {
      fetchPost();
      fetchComments();
    });

    watch(route, () => {
      fetchPost();
      fetchComments();
    });

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
      fetchPosts,
      posts,
      timeAgo,
      user,
    };
  }
};
</script>
