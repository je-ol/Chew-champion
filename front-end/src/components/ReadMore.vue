<template>
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
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import axios from '../axios';

export default {
    name: 'ReadMore',
    props: {
        post: {
            type: Object,
            required: true
        }
    },
    setup(props) {
        const posts = ref([]);

        const fetchPosts = async () => {
            try {
                const response = await axios.get('/posts/', {
                    headers: {
                        Authorization: `token ${localStorage.getItem('token')}`
                    }
                });
                const allPosts = response.data.reverse();
                // Check if props.post is defined before filtering
                if (props.post) {
                    const filteredPosts = allPosts.filter(singlePost => singlePost.post !== props.post.post);
                    posts.value = filteredPosts;
                }
            } catch (error) {
                console.error('Failed to fetch posts:', error);
            }
        };

        onMounted(() => {
            fetchPosts();
        });

        watch(() => [props.post, props.post.post], () => {
            fetchPosts();
        });

        return { posts };
    }
};
</script>
