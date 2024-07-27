<template>
<div class="max-w-sm mx-auto overflow-hidden bg-white rounded-lg shadow-lg hover:shadow-blue-400">
  <div class="relative">
    <img :src="userStore.user.avatar" class="mb-6 rounded-full">
  </div>
  <div class="px-6 py-4">
    <div class="text-xl font-semibold text-gray-800">{{ userStore.user.username }}</div>
    <p class="text-gray-600">{{ userStore.user.email }} </p>
    <p class="text-gray-600">{{ userStore.user.first_name  }} </p>
    <p class="text-gray-600">{{ userStore.user.last_name  }} </p>
    <p class="text-gray-600">{{ userStore.user.bio  }} </p>
  </div>
  <div class="px-6 py-4">
    <span class="inline-block px-2 py-1 font-semibold text-teal-900 bg-teal-200 rounded-full">
      <nuxt-link :to="{'name': 'edit-account'}">Редактировать
      </nuxt-link>
    </span>
    <span class="inline-block px-2 py-1 font-semibold text-indigo-900 bg-indigo-200 rounded-full">
      <nuxt-link :to="{'name': 'edit-password'}">Изменить пароль
      </nuxt-link> 
    </span>
    <span @click="deleteUser" class="inline-block px-2 py-1 font-semibold text-purple-900 bg-purple-200 rounded-full">Удалить </span>
  </div>

  <div class="px-6 py-4">
    <button @click="logout" class="text-blue-500 hover:underline">Выйти</button>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    name: 'account',

    setup(context) {
        const userStore = useUserStore()
        const toastStore = useToastStore()
        const router = useRouter();
        const logout = () => {
            userStore.removeToken() // Очистка данных пользователя из хранилища
            toastStore.showToast(5000, 'Вы вышли из системы успешно', 'bg-green-500')
            router.push({ name: 'login' });
          
        }
        const deleteUser = () => {
          if (confirm('Вы уверены, что хотите удалить свою учетную запись?')) {
            axios
              .delete('/delete-user/')
              .then(response => {
                toastStore.showToast(5000, 'Пользователь успешно удален', 'bg-green-500');
                logout(); 
              })
              .catch(error => {
                toastStore.showToast(5000, 'Ошибка при удалении пользователя', 'bg-red-500');
                console.error(error);
              });
          }
        };
            
        return {
            userStore,
            toastStore,
            logout,
            deleteUser
      
        }
    },

    mounted() {  
        document.title = "Мой профиль"

    },
    
}
</script>