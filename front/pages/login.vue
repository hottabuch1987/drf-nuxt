<template>
<main class="container mx-auto p-4 mt-12 bg-white flex flex-col items-center justify-center text-gray-700">
    <div class="w-10/12 sm:w-8/12 md:w-6/12 lg:w-5/12 xl:w-4/12 mb-4">
        <h1 class="text-4xl text-gray-400  font-semibold">Войти</h1>
    </div>
    <div class="w-10/12 sm:w-8/12 md:w-6/12 lg:w-5/12 xl:w-4/12 mb-6">
        <form class="space-y-6" v-on:submit.prevent="submitForm">
            <input type="email" v-model="form.email"  class="mb-4 p-2 appearance-none block w-full bg-gray-200 placeholder-gray-400 rounded border focus:border-teal-500"  placeholder="Email"/>
            <input type="password" v-model="form.password" class="mb-4 p-2 appearance-none block w-full bg-gray-200 placeholder-gray-400 rounded border focus:border-teal-500" placeholder="Пароль"/>

            <div class="flex items-center">
                <div class="w-1/2 flex items-center">
                
                    <input id="remember-me" type="checkbox" class="mt-1 mr-2" />
                    <label for="remember-me">Запомнить меня!</label>
                </div>


                <button  class="ml-auto w-1/2 bg-gray-800 text-white p-2 rounded font-semibold hover:bg-gray-900" tu>Отправить</button>

                <nuxt-link to="/signup"
                    class="rounded-md  to-emerald-400 px-3 py-1.5 font-dm text-sm font-medium shadow-md  transition-transform duration-200 ease-in-out hover:scale-[1.03]">Регистрация
                </nuxt-link>
                <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                            <!-- SPINER -->
                                <div role="status">
                                    <svg aria-hidden="true" class="inline w-11 h-11 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-green-500" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                                        <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
                                    </svg>
                                    <span class="sr-only"></span>
                                </div>
                            <!-- /SPINER -->
                        </div>
                </template>
            </div> 
        </form>
    </div>
</main>
</template>





<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    name: 'login',
    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                password: '',
            },
            errors: []
        }
    },
      mounted() {
        document.title = "Войти | Знакомства"

    },
    methods: {
        async submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Поле "E-mail" не может быть пусты!')
            }

            if (this.form.password === '') {
                this.errors.push('Поле "Пароль" не может быть пусты!')
            }

            if (this.errors.length === 0) {
                await axios
                    .post('/login/', this.form)
                    .then(response => {
                        this.userStore.setToken(response.data)
                        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    })
                    .catch(error => {
                        console.log('error', error)
                        this.errors.push('Электронная почта или пароль неверны! Или пользователь не активирован!')
                    })
            }
        
            if (this.errors.length === 0) {
                await axios
                    .get('/me/')
                    .then(response => {
                        this.userStore.setUserInfo(response.data)

                        this.$router.push('/account')
                        this.toastStore.showToast(5000, 'Вы вошли в систему!', 'bg-emerald-500');
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>
