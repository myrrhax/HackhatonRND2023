<template>
    <loading v-model:active='isLoading' :can-cancel="true" :on-cancel="onCancel" :is-full-page="true" />
    <drop-down v-if='!notFound && !noFaces && !image_url' @onSubmit="onSubmit" />
    <div class='flex justify-center' v-if='image_url'>
      <div>
        <span style='font-weight: bold;'>Загруженное фото:</span>
        <img :src='image_url' style='width: 250px; height: 250px;' />
      </div>
      <div>
        <span style='font-weight: bold;'>Найденное фото:</span>
        <img :src='photo_url' style='width: 250px; height: 250px;' />
      </div>
      <div class='tags'>
        <ul>
          <li v-for='tag in tags' :key=tag>
            <div class='rounded-full text-white bg-black' style='width: 100px; height: 100px;'>
              {{ tag }}
            </div>
          </li>
        </ul>
        <input v-if='currentUser' v-model='tag_name' @click='addTag' placeholder="Тэг" class='rounded-full text-white bg-black' style='width: 100px; height: 50;' />
      </div>
    </div>
    <div v-if='notFound'>
      <span><b>О таком человеке я слышу впервые, он был добавлен в мою базу данных!</b></span>
    </div>
    <button @click='tryAgain' v-if='notFound || noFaces || image_url' class='bg-black mt-2 rounded-3xl text-base text-white mr-7 w-28 h-10'>Ещё раз!</button>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import authHeader from '../services/auth-header'
import DropDown from '../components/DropDown.vue'
import loading from 'vue-loading-overlay'
import 'vue-loading-overlay/dist/css/index.css';

export default {
  name: 'SearchView',
  components: {
    DropDown, loading
  },
  data() {
    return {
      isLoading: false,
      image_url: null,
      photo_url: null,
      image_id: null,
      tags: null,
      tag_name: '',
      dragEntered: false,
      notFound: null,
      noFaces: null
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
    tryAgain() {
      this.isLoading= false
      this.image_url= null
      this.photo_url= null
      this.image_id= null
      this.tags= null
      this.tag_name= ''
      this.dragEntered= false
      this.notFound= null
      this.noFaces= null
    },
    async onSubmit(file) {
        await this.show(file)
    },
    previewFiles(event) {
      if (event.target.files) {
        this.image = event.target.files[0]
      }
    },
    onCancel() {
      this.$router.push('/search')
    },
    async show(image) {
      var interpolateUrl = require('interpolate-url');
      let bodyFormData = new FormData();
      bodyFormData.append('file', image);
      this.isLoading = true;
      try {
        const response = await axios({method: 'post', url:'http://localhost:8000/image/search', data: bodyFormData, headers: {'Content-Type': 'multipart/form-data'}})
        const index = response.data.match_index
        if (index) {
          const reader = new FileReader()
          reader.onload = e => {
            this.image_url = e.target.result
          }
          reader.readAsDataURL(image)
          console.log(this.addTagimage_url)
          this.image_id = index
          this.photo_url = interpolateUrl('http://localhost:8000/image/:id', {id: index})
          const tagsUrl = interpolateUrl('http://localhost:8000/image/tags/:id', {id: index})
          const tagResposne = await axios.get(tagsUrl)
          this.tags = tagResposne.data.tags
        } else if (response.data.status_code === 400) {
          this.noFaces = true
        }
      } catch(err) {
        this.notFound = true
      }
      this.isLoading = false;
    },
    async addTag() {
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
    },
    onDragEnter(e) {
        e.preventDefault()
        this.dragEntered = true;
    },
    onDragLeave(e) {
        e.preventDefault()
        this.dragEntered = false;
    },
    onFileDrop(e) {
        e.preventDefault()
        let files = [...e.dataTransfer.files]
        console.log(files)
    }
  }
}
</script>
