<template>
    <div class="flex flex-col w-[100%] self-start bg-white p-8 gap-2">
        <h3 class="text-xl font-semibold">Comments</h3>
        <!-- Display all the comments -->
        <div v-for="(comment, index) in filteredComments" :key="index" class="flex flex-col bg-slate-500/20 p-2 rounded-md">
            <div v-if="!comment.isEditing">
                <p> {{ comment.content }}</p>
                <div class="flex justify-between items-center">
                    <p class="font-bold"> {{ comment.username }}</p>
                    
                    <div class="flex items-center">
                        <div v-if="user.id === comment.user" class="flex">
                            <img src="../assets/edit-comment.png" alt="" class="mr-1 cursor-pointer w-[32px] h-[32px] bg-[#ff9602] rounded-full p-1 border-2 border-white" @click="toggleCommentEdit(comment)">
                            <img src="../assets/delete.png" class="mr-4 cursor-pointer w-[32px] h-[32px] bg-[#ba2222] rounded-full p-1 border-2 border-white" @click="deleteComment(comment.comment)">
                        </div>
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
            <input type="text" class="w-[85%] h-[50px] px-2 border-2 border-gray-500/20 rounded-md" placeholder="Write a new comment..." v-model="newComment" @keydown.enter="sendComment">
            <button class="w-[14%] h-[100%] bg-[#758bfd] px-4 py-2 rounded-md font-bold text-white" @click="sendComment">COMMENT</button>
        </div>
    </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import { useAuthStore } from '../store/auth';
import axios from '../axios';
import { useRoute } from 'vue-router';
import { timeAgo } from '../utils/timeAgo.js';

    export default {
        name: "CommentSection",
        props: {
            post: {
                type: Object,
            }
        },
        methods: {
            timeAgo
        },
        setup(props) {
            const { user } = useAuthStore();
            const route = useRoute();
            const comments = ref([]);
            const isEditing = ref(false);
            const newComment = ref('');
            const editedContent = ref('');

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

            const filteredComments = computed(() => {
            return comments.value.filter(comment => comment.post === props.post.post);
            });

            const sendComment = async () => {
                 try {
                    await axios.post('comments/', 
                    {
                        content: newComment.value,
                        post_id: props.post.post,
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

            onMounted(() => {
                fetchComments();
            });

            watch(route, () => {
                fetchComments();
            });

            return {
                user,
                newComment,
                comments,
                filteredComments,
                sendComment,
                toggleCommentEdit,
                saveCommentEdit,
                deleteComment
            }

        }
    };
</script>