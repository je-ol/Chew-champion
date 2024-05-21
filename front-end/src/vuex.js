import { createStore } from 'vuex';

export default createStore({
  state: {
    user: '',
  },
  getters: {
  
  },
  mutations: {
    login(state, email) {
        state.user = user;
        localStorage.setItem('user', user);
        alert('User logged in - from vuex');
    },
    logout(state) {
        state.user = '';
        localStorage.removeItem('user');
        alert('User logged out - from vuex');
    },
    initializeStore(state) {
        if(localStorage.getItem('user')) {
            state.user = localStorage.getItem('user');
        }
    }
  },
  actions: {

  },
});

