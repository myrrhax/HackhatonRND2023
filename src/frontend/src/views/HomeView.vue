<template>
  <div class='photo' v-if=photo_url>
    <img :src='photo_url'>
    <ul class='tags'>
      <li v-for='tag in tags' :key="tag">
        {{ tag }}
      </li>
    </ul>
    <div v-if='currentUser'>
      <input type='text' v-model='tag_name' />
      <button @click='addTag'>Добавить тэг</button>
    </div>
  </div>
  <div class='container' v-else>
    <b>Найдите человека по фотографии: </b>
    <div>
      <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="file_input">Upload file</label>
      <input @change="previewFiles" class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="file_input" type="file">
    </div>
    <button @click='show' v-if='image'>Найти человека</button>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import authHeader from '../services/auth-header'

export default {
  name: 'HomeView',
  data() {
    return {
      image: null,
      photo_url: null,
      image_id: null,
      tags: null,
      tag_name: ''
    }
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user 
    }
  },
  mounted() {

  }, 
  methods: {
    previewFiles(event) {
      if (event.target.files) {
        this.image = event.target.files[0]
      }
    },
    async show() {
      var interpolateUrl = require('interpolate-url');
      let bodyFormData = new FormData();
      bodyFormData.append('file', this.image);
      const response = await axios({method: 'post', url:'http://localhost:8000/image/search', data: bodyFormData, headers: {'Content-Type': 'multipart/form-data'}})
      if (response.data) {
        const index = response.data.match_index
        this.image_id = index
        this.photo_url = interpolateUrl('http://localhost:8000/image/:id', {id: index})
        const tagsUrl = interpolateUrl('http://localhost:8000/image/tags/:id', {id: index})
        const tagResposne = await axios.get(tagsUrl)
        this.tags = tagResposne.data.tags
      }
    },
    async addTag() {
      console.log(authHeader())
      if (this.tag_name !== '') {
        this.tags.push(this.tag_name)
        console.log({
          id: this.image_id,
          tags: this.tags
        })
        const response = await axios.patch('http://localhost:8000/image', {
          id: this.image_id,
          tags: this.tags
        }, { headers: authHeader() })
        console.log(response)
      }
    }
  }
}
</script>
