<template>
  <q-page class="bg-grey-2" padding>
    <div class="q-gutter-lg row items-start justify-evenly">
        <q-file standout bottom-slots color="grey" style="height: 140px; max-width: 150px" bg-color="grey-4" v-model="filesImages" multiple accept=".jpg, image/*" @input="uploadImages(filesImages)" >
            <q-icon name="add_a_photo" class="absolute-center" style="height: 140px; font-size: 2em; color: #BCAAA4"/>
        </q-file>
        <q-img v-for= "(item, i) in urls" :key=i :src=item.image style="height: 140px; max-width: 150px"/>
    </div>
  </q-page>
</template>

<script>
import axios from 'axios'
import EventBus from '../event-bus'
// // import JSZip from 'jszip'
// import { saveAs } from 'file-saver'
const AWS_URL = 'http://ec2-3-97-34-208.ca-central-1.compute.amazonaws.com:5000/'
export default {
  name: 'PageIndex',
  data () {
    return {
      tab: 'albums',
      filesImages: null,
      imageSourceArray: [
        { name: 'one', image: 'https://placeimg.com/500/300/nature' },
        { name: 'two', image: 'https://placeimg.com/500/300/nature' },
        { name: 'three', image: 'https://placeimg.com/500/300/nature' },
        { name: 'four', image: 'https://placeimg.com/500/300/nature' }
      ],
      urls: [
        { name: 'one', image: 'https://placeimg.com/500/300/nature' },
        { name: 'two', image: 'https://placeimg.com/500/300/nature' },
        { name: 'three', image: 'https://placeimg.com/500/300/nature' },
        { name: 'four', image: 'https://placeimg.com/500/300/nature' }
      ]
    }
  },
  created () {
    EventBus.$on('ALBUM_SEARCH', (value) => {
      if (value === '' || value === null) {
        this.urls = this.imageSourceArray
        return
      }
      console.log('triggered', value)
      var a = this.imageSourceArray
      console.log('urls', a)
      this.urls = a.filter(function (obj) {
        return obj.name === value
      })
    })
  },
  methods: {
    uploadImages (filesImages) {
      var fd = new FormData()
      for (var i = 0; i < filesImages.length; i++) {
        fd.append('img', filesImages[i])
        fd.append('label', 'test')
      }
      axios.post(AWS_URL + 'image', fd).then(res => { console.log(res) })
    }
  }
}
</script>

<style lang="scss" scoped>
div[class="relative-position"] {
  height: 140px !important;
}
</style>
