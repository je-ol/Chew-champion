import axios from 'axios';

axios.defaults.baseURL = 'https://chew-champion-ea4753cf27e6.herokuapp.com/';
/* axios.defaults.headers.common['Authorization'] = 'token ' + localStorage.getItem('token'); */

export default axios;