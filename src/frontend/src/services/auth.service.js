import axios from 'axios'

const API_URL = 'http://localhost:8000/user/'

class AuthService {
    async login(user) {
        const response = await axios.post(API_URL + 'login', {
            name: user.name,
            password: user.password,
        });
        if (response.data.token) {
            localStorage.setItem('user', JSON.stringify(response.data));
        }

        return response.data;
    }

    async register(user) {
        const response = await axios.post(API_URL + 'register', {
            name: user.name,
            password: user.password
        });
        if (response.data.token) {
            localStorage.setItem('user', JSON.stringify(response.data));
        }

        return response.data;
    }

    logout() {
        localStorage.removeItem('user');
    }
}

export default new AuthService();