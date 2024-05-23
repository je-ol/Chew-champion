<template>
    <div class="w-[70vw] h-[70vh] flex flex-col mx-auto mt-[7%] rounded-3xl">
<!--         {{ user }}
        {{ userProfile }} -->
        <ProfileAbout :userProfile="userProfile" :posts="posts" />

        <ProfilePosts :posts="posts" />
    </div>
</template>

<script>
import ProfileAbout from '../components/ProfileAbout.vue';
import ProfilePosts from '../components/ProfilePosts.vue';
import { useAuthStore } from '../store/auth';
import axios from '../axios';

export default {
    name: 'Profile',
    components: {
        ProfileAbout,
        ProfilePosts
    },
    setup() {
        const { user } = useAuthStore();
        return { user };
    },
    data() {
        return {
            posts: [],
            userProfile: this.user
        }
    },
    created() {
        this.fetchAllUsers();
        this.fetchPosts();
    },
    computed: {
        userId() {
            return this.$route.params.user;
        },
    },
    methods: {
        async fetchAllUsers() {
            const response = await axios.get('users/', {
                headers: {
                    Authorization: `token ${localStorage.getItem('token')}`
                }
            });
            const allUsers = response.data;
            allUsers.forEach(singleuser => {
                if (singleuser.id == this.userId) {
                    this.userProfile = singleuser;
                }
                console.log(this.userProfile)
            });
        },

        async fetchPosts() {
            const response = await axios.get('posts/', {
                headers: {
                    Authorization: `token ${localStorage.getItem('token')}`
                }
            });
            const allPosts = response.data;
            allPosts.forEach(singlePost => {
                if (singlePost.user == this.userProfile.id) {
                    this.posts.push(singlePost);
                }
            });
        },
    },
}
</script>
