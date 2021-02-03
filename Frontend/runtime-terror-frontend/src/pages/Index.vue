<template>
  <q-page class="bg-grey-2" padding>
    <div class="q-gutter-lg row items-start justify-evenly">
        <q-file standout bottom-slots ref="email" color="grey" style="color: grey-4 height: 140px; max-width: 150px" bg-color="grey-4" v-model="filesImages" multiple accept=".jpg, image/*" @input="uploadImages(filesImages)" >
            <q-icon name="add_a_photo" class="absolute-center" style="height: 140px; font-size: 2em; color: #BCAAA4"/>
        </q-file>
        <q-img v-for= "item in urls" :key=item :src=item style="height: 140px; max-width: 150px"/>
    </div>
  </q-page>
</template>

<script>
import axios from 'axios'
// // import JSZip from 'jszip'
// import { saveAs } from 'file-saver'
const URL = 'http://ec2-3-97-34-208.ca-central-1.compute.amazonaws.com:5000/'
// const URL = 'http://localhost:5000/'
export default {
  name: 'PageIndex',
  data () {
    return {
      tab: 'albums',
      filesImages: null,
      urls: []
    }
  },
  methods: {
    uploadImages (filesImages) {
      var vm = this
      for (var i = 0; i < filesImages.length; i++) {
        var reader = new FileReader()
        var fd = new FormData()
        reader.readAsDataURL(filesImages[i])
        reader.onload = function (e) {
          vm.urls.push(e.target.result)
        }
        fd.append('img', filesImages[i])
        fd.append('label', 'test')
        axios.post(URL + 'image', fd).then(res => { console.log(res) })
      }
    }
  }
}
</script>

<style lang="scss" scoped>
div[class="relative-position"] {
  height: 140px !important;
}
</style>
