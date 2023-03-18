<template>
  <div class='wrapper-wrap'>
    <form>
        <div class="mb-6">
            <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Логин</label>
            <input v-model='name' type="name" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
        </div>
        <div class="mb-6">
            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Пароль</label>
            <input v-model='password' type="password" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
        </div>
        <button @click="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      password: ''
    }
  },
  mounted() {
    if (this.currentUser) {
      this.$router.push('/')
    }
  },
  computed:{
    currentUser() {
      return this.$store.state.auth.user
    }
  },
  methods: {
    async submit() {
      if (this.name && this.password) {
        const response = await this.$store.dispatch('auth/register', {
          name: this.name,
          password: this.password
        });
        console.log(response)
        this.$router.push('/');
      }
    }
  }
}
</script>

<style>

</style>