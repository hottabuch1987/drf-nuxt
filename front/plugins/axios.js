import axios from "axios"

export default defineNuxtPlugin((NuxtApp) => {

    axios.defaults.baseURL = 'http://127.0.0.1:8000/api/v1'
    axios.defaults.withCredentials = true;
    

    return {
        provide: { 
            axios: axios
        },
    }
})