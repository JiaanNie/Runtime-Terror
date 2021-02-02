<template>
  <q-page class="bg-grey-2" padding>
    <div class="q-gutter-lg row items-start">
        <q-file standout bottom-slots color="grey" style="max-width: 150px" bg-color="grey-4" v-model="filesImages" multiple accept=".jpg, image/*" @input="uploadImages(filesImages)" >
            <q-icon name="add" class="absolute-center" style="font-size: 2em; color: #BCAAA4"/>
        </q-file>
    </div>
  </q-page>
</template>

<script>
import axios from 'axios'
// // import JSZip from 'jszip'
// import { saveAs } from 'file-saver'
const AWS_URL = 'http://ec2-3-97-34-208.ca-central-1.compute.amazonaws.com:5000/'
export default {
  name: 'PageIndex',
  data () {
    return {
      tab: 'albums',
      filesImages: null
    }
  },
  methods: {
    uploadImages (filesImages) {
      // var fr = new FileReader()
      var fd = new FormData()
      for (var i = 0; i < filesImages.length; i++) {
        fd.append('img', filesImages[i])
        fd.append('label', 'test')
      }
      console.log(fd.getHeaders)
      axios.post(AWS_URL + 'image', fd).then(res => { console.log(res) })
      // axios({ method: 'post', url: AWS_URL + 'image', data: fd, headers: { 'Content-Type': 'multipart/form-data' } }).then(function (response) {
      //   // handle success
      //   console.log(response)
      // })
      //   .catch(function (response) {
      //   // handle error
      //     for (var pair of fd.entries()) {
      //       console.log(pair[0] + ', ' + pair[1])
      //     }
      //     console.log(response)
      //   })
    }
  }
}
</script>

<style lang="sass" scoped>
.row > div
  padding: 10px 15px
  background: white
.row + .row
  margin-top: 1rem
</style>
