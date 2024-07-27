
<template>

<div class="container mx-auto p4-10">
    <div class="max-w-md mx-auto bg-white rounded-lg overflow-hidden md:max-w-xl">
        <div class="md:flex">
            <div class="w-full px-6 py-8 md:p-8">
                <h2 class="text-2xl font-bold text-gray-800">Редактировать профиль </h2>
                
                <form @submit.prevent="submitForm" class="mt-6">
                    <div class="mb-6">
                        <label class="block text-gray-800 font-bold mb-2" for="password">
                            Новый пароль
                        </label>
                        <input type="password" id="password" v-model="formData.password" required  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"  placeholder="Введите новый пароль">
                    </div>
                 
                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" :key="error">{{ error }}</p>
                        </div>
                    </template>
                    <button class="bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
                        Изменить
                    </button>
                    <p class="mt-4 text-gray-600">
                    <nuxt-link class="text-red-500 hover:underline" :to="{'name': 'edit-account'}">Изменить профиль
                    </nuxt-link>
                    </p>
                </form>
            </div>
        </div>
    </div>
</div>

</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router';
import { useToastStore } from '@/stores/toast'
import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const toastStore = useToastStore();
        const userStore = useUserStore();
        const router = useRouter();
        const formData = reactive({ password: '' }); 
        const errors = ref([]); 
        const submitForm = () => {
            errors.value = [];

            if (formData.password.trim() === '') {
                errors.value.push('Введите пароль!');
            } else if (formData.password.length < 6) {
                errors.value.push('Пароль должен содержать минимум 6 символов.');
            }

            if (errors.value.length === 0) {
                let requestData = {
                    password: formData.password
                };

                axios.post('/change-password/', requestData)
                    .then(response => {
                        if (response.data.message === 'Password updated successfully') {
                            toastStore.showToast(5000, 'Пароль успешно обновлен!', 'bg-emerald-500');
                            router.push({ name: 'account' });
                            
                        } else {
                            errors.value.push('Произошла ошибка при обновлении пароля.');
                        }
                    })
                    .catch(error => {
                        console.error('Ошибка при обновлении пароля:', error);
                        errors.value.push('Произошла ошибка при обновлении пароля.');
                    });
            }
        };

        return { formData, errors, submitForm };
    }

}

</script>
