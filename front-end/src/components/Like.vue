<template>
    <div> {{ likes }}</div>
</template>
<script>
import axios from '../axios';
export default {
    name: 'Like',
    props: {
        

    },
    created() {
        this.fetchLikes();
    },
    data() {
        return {
            likes: 0
        }
    },
    methods: {
        async fetchLikes() {
            const response = await axios.get(`/likes/`, {
                headers: {
                    Authorization: `token ${localStorage.getItem('token')}`
                },
            });
            const allLikes = response.data;
            allLikes.forEach(like => {
                if (this.postId === like.post) {
                    this.likes = like.count;
                }
                
            });

        },

        /* async likePost() {
            if (this.isLiked) {
                this.likeCount -= 1;
            } else {
                this.likeCount += 1;
            }
            this.isLiked = !this.isLiked;
            await this.$emit('like', this.postId, this.isLiked);
        } */
    }
}
</script>