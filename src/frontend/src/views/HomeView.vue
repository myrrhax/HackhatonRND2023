<template>
  <div class='container'>
    HELLO WORLD!
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  computed: {
    currentUser() {
      return this.$store.state.auth.user 
    }
  },
  mounted() {

  }
}
</script>
