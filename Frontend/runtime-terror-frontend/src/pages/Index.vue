<template>
  <q-page class="flex flex-center">
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-full.svg"
    >
    <q-btn color="primary" label="click me" @click=test />
    <img id="ItemPreview" src="">
  </q-page>
</template>

<script>
import axios from 'axios'
// import JSZip from 'jszip'
import { saveAs } from 'file-saver'
export default {
  name: 'PageIndex',
  methods: {
    test () {
      const localUrl = 'http://localhost:5000/'
      // let aws_url  = 'http://ec2-3-97-34-208.ca-central-1.compute.amazonaws.com:5000/'
      axios.get(localUrl + 'sort', { responseType: 'blob' }).then(function (res) {
        // var blob = new Blob([res.data], { type: 'application/x-zip-compressed' })
        saveAs(res.data, 'test.zip')
        // console.log(typeof (res.data))
        // // console.log(JSZip.loadAsync(res.data))
        // var blob = new Blob([res.data], { type: 'application/x-zip-compressed' })
        // console.log(typeof (blob))
        // JSZip.loadAsync(blob, { base64: true }).then(function (zipFile) {
        //   saveAs(zipFile, 'result.zip')
        // })
        // console.log(blob)
        // // var fileLink = document.createElement('a')
        // // fileLink.href = fileURL
        // // fileLink.setAttribute('download', 'result.zip')
        // saveAs(zip_file, 'result.zip')
        // // document.body.appendChild(fileLink)
        // // fileLink.click()
      })
    }
  }
}
</script>
