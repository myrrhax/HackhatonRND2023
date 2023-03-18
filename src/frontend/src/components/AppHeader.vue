<template>
  <div class='wrapper' style="width: 100%;height: 50px;background-color: green;">
    
    <div class='auth' v-if='!currentUser'>
        <button @click='login'>Войти</button>
        <button @click='registration'>Регистрация</button>
    </div>
    <div v-else>
        <button @click='logout'>Выйти</button>
    </div>
  </div>
</template>

<script>
export default {
    name: 'AppHeader',
    props: {
        showAuth: Boolean
    },
    computed:{
        currentUser() {
            console.log(this.$store.state.auth.user )
            return this.$store.state.auth.user 
        }
    },
    methods: {
        async login() {
            
        },
        async registration() {
            
        },
        async logout(){
            this.$store.dispatch('auth/logout')
        }
    }
}
</script>

<style>

</style>