<template>
    <div class="w-[70vw] h-[70vh] flex flex-col mx-auto mt-[7%] rounded-3xl">
        <ProfileAbout :userProfile="userProfile" :posts="posts" />
        <ProfilePosts :posts="posts" />
    </div>
</template>

<script>
import { ref, onMounted, watch, nextTick } from 'vue';
import { useRoute } from 'vue-router';
import axios from '../axios';
import ProfileAbout from '../components/ProfileAbout.vue';
import ProfilePosts from '../components/ProfilePosts.vue';
import { useAuthStore } from '../store/auth';

export default {
    name: 'Profile',
    components: {
        ProfileAbout,
        ProfilePosts
    },
    setup() {
        const { user } = useAuthStore();
        const route = useRoute();

        const posts = ref([]);
        const userProfile = ref(JSON.parse(sessionStorage.getItem('userProfile')) || null);

        const fetchAllUsers = async () => {
            const response = await axios.get('users/', {
                headers: {
                    Authorization: `token ${localStorage.getItem('token')}`
                }
            });
            const allUsers = response.data;

            if (route.params.user) {
                const matchedUser = allUsers.find(singleuser => singleuser.id == route.params.user);
                if (matchedUser) {
                    userProfile.value = matchedUser;
                    // Save userProfile to sessionStorage
                    sessionStorage.setItem('userProfile', JSON.stringify(userProfile.value));
                }
            } else {
                userProfile.value = user;
                sessionStorage.setItem('userProfile', JSON.stringify(user));
            }
        };

        const fetchPosts = async () => {
            const response = await axios.get('posts/', {
                headers: {
                    Authorization: `token ${localStorage.getItem('token')}`
                }
            });
            const allPosts = response.data;
            posts.value = allPosts.filter(singlePost => singlePost.user == userProfile.value.id);
        };

        onMounted(async () => {
            await fetchAllUsers();
            await fetchPosts();
        });

        watch(route, async () => {
            await fetchAllUsers();
            await fetchPosts();
            await nextTick();
        });

        return { posts, userProfile, user };
    }
};
</script>

