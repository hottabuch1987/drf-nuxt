import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore({
    id: 'user',

    state: () => ({
        user: {
            isAuthenticated: false,
            id: null,
            username: null,
            email: null,
            access: null,
            refresh: null,
            avatar: null,
            first_name: null,
            last_name: null,
            bio: null,
            phone: null,
           

        }
    }),

    actions: {
        initStore() {
            console.log('initStore', localStorage.getItem('user.access'))

            if (localStorage.getItem('user.access')) {
                console.log('User has access!')

                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.id = localStorage.getItem('user.id')
                this.user.username = localStorage.getItem('user.username')
                this.user.email = localStorage.getItem('user.email')
                this.user.first_name = localStorage.getItem('user.first_name')
                this.user.last_name = localStorage.getItem('user.last_name')
                this.user.bio = localStorage.getItem('user.bio')
                this.user.phone = localStorage.getItem('user.phone')
                this.user.avatar = localStorage.getItem('user.avatar')
                this.user.isAuthenticated = true

                this.refreshToken()
                
                console.log('Initialized user:', this.user)
            }
        },

        setToken(data) {
            console.log('setToken', data)

            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)

            console.log('user.access: ', localStorage.getItem('user.access'))
        },

        removeToken() {
            console.log('removeToken')

            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = null
            this.user.username = null
            this.user.email = null
            this.user.first_name = null
            this.user.last_name = null
            this.user.bio = null
            this.user.phone = null
            this.user.avatar = null

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.username', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.first_name', '')
            localStorage.setItem('user.last_name', '')
            localStorage.setItem('user.bio', '')
            localStorage.setItem('user.phone', '')
            localStorage.setItem('user.avatar', '')
        },

        setUserInfo(user) {
          console.log('setUserInfo', user);

          if (user && user.id) {
              this.user.id = user.id;
          }
      
          // Проверка и установка других свойств
      
            console.log('User', this.user);
         

          
            this.user.username = user.username
            this.user.email = user.email
            this.user.first_name = user.first_name
            this.user.last_name = user.last_name
            this.user.bio = user.bio
            this.user.phone = user.phone
       
            this.user.avatar = user.avatar

            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.username', this.user.username)
            localStorage.setItem('user.email', this.user.email)
            localStorage.setItem('user.first_name', this.user.first_name)
            localStorage.setItem('user.last_name', this.user.last_name)
            localStorage.setItem('user.bio', this.user.bio)
            localStorage.setItem('user.phone', this.user.phone)
            localStorage.setItem('user.avatar', this.user.avatar)

            console.log('User', this.user)
        },

        refreshToken() {
            axios.post('/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    this.user.access = response.data.access

                    localStorage.setItem('user.access', response.data.access)

                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error)=>{
                    console.log(error)

                    this.removeToken()
                })
        },
        setAvatar(avatarUrl) {

            this.user.avatar = avatarUrl;
    
            // Сохранение значения аватара в локальное хранилище
    
            localStorage.setItem('user.avatar', avatarUrl);
    
        }
    },
    
})