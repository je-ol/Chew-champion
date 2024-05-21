import axios from 'axios';

axios.defaults.baseURL = 'https://chew-champion-43c72340b77a.herokuapp.com/';
axios.defaults.headers.common['Authorization'] = 'token ' + localStorage.getItem('token');

export default axios;