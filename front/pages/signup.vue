<template>
<main class="container mx-auto p-4 mt-12 bg-white flex flex-col items-center justify-center text-gray-700">
    <div class="w-10/12 sm:w-8/12 md:w-6/12 lg:w-5/12 xl:w-4/12 mb-4">
        <h1 class="text-4xl text-gray-400  font-semibold">Регистрация</h1>
    </div>
    <div class="w-10/12 sm:w-8/12 md:w-6/12 lg:w-5/12 xl:w-4/12 mb-6">
    <form class="space-y-6" v-on:submit.prevent="submitForm">
        <input class="mb-4 p-2 appearance-none block w-full bg-gray-200 placeholder-gray-400 rounded border focus:border-teal-500" type="text" v-model="form.username" placeholder="Логин"/>
        <input class="mb-4 p-2 appearance-none block w-full bg-gray-200 placeholder-gray-400 rounded border focus:border-teal-500" type="email" v-model="form.email" placeholder="Email"/>
        <input class="mb-4 p-2 appearance-none block w-full bg-gray-200 placeholder-gray-400 rounded border focus:border-teal-500" type="password" v-model="form.password" placeholder="Пароль"/>
        <div class="flex items-center">
           

            <button class="ml-auto w-1/2 bg-gray-800 text-white p-2 rounded font-semibold hover:bg-gray-900" >Отправить</button>
            <nuxt-link :to="{'name': 'login'}"
                class="rounded-md  to-emerald-400 px-3 py-1.5 font-dm text-sm font-medium shadow-md  transition-transform duration-200 ease-in-out hover:scale-[1.03]">Войти
            </nuxt-link>
            
        </div>
                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
            </template>
    </form>
    </div>
</main>
</template>
<script>
import axios from 'axios'
import { useToastStore } from '@/stores/toast'

export default {
    name: 'signup',
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                username: '',
                password: '',
      
            },
            errors: [],
        }
    },
    mounted() {
        document.title = "Регистрация | Знакомства"

    },


    methods: {
        async submitForm() {
            this.errors = [];

            if (this.form.email === '') {
                this.errors.push('Поле "E-mail" не может быть пустым');
            }

            if (this.form.username === '') {
                this.errors.push('Поле "Имя" не может быть пустым');
            }

            if (this.form.password === '') {
                this.errors.push('Поле "Пароль" не может быть пустым');
            }

            if (this.errors.length === 0) {
                try {
                    const response = await axios.post('create/', this.form);
                    if (response.status === 201) {
                        this.toastStore.showToast(5000, 'Пользователь зарегистрирован. Пожалуйста, войдите в систему!.', 'bg-emerald-500');
                        this.$router.push({ path: '/login' }); // Перенаправление на страницу логина
                    } else {
                        const data = response.data;
                        if (data && data.message) {
                            this.errors.push(data.message);
                        }
                        this.toastStore.showToast(5000, 'Что-то пошло не так. Пожалуйста, попробуйте еще раз.', 'bg-red-300');
                    }
                } catch (error) {
                    console.error('Error submitting registration form:', error);
                    this.toastStore.showToast(5000, 'Что-то пошло не так. Пожалуйста, попробуйте еще раз.', 'bg-red-300');
                }
            }
        }
    }
}
</script>