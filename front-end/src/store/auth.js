// store/auth.js
import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || '',
  }),
  actions: {
    async getUser() {
      if (!this.token) {
        this.user = null;
        return;
      }
      try {
        const response = await axios.get('/users/current_user/', {
          headers: {
            'Authorization': 'token ' + this.token,
          },
        });
        this.user = response.data;
      } catch (error) {
        console.error('Failed to fetch user:', error);
        this.user = null;
      }
    },
    setToken(token) {
      this.token = token;
      localStorage.setItem('token', token);
    },
  },
});
