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
// import axios from 'axios'
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
      var fr = new FileReader()

      console.log(fr)
      for (var i = 0; i < filesImages.length; i++) {
        console.log(filesImages[i])
        fr.readAsArrayBuffer(filesImages[i])
        console.log(fr)
        console.log(AWS_URL)
      }
      fr.onloadend = function () {
        console.log(fr.result)
        var bytes = new Uint8Array(fr.result)
        console.log(bytes)
      }
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
