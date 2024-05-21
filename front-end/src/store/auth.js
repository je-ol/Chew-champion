import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore("auth", {
    state: () => ({
        authUser: null
    }),
    getters: {
        user: (state) => state.authUser
    },
    actions: {
        getToken() {
            return localStorage.getItem('token');
        },
        getUser() {
            const localUser = localStorage.getItem('user');
            this.authUser = localUser ? JSON.parse(localUser) : null;
        }
    }
});
