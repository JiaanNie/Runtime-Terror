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
export default {
  name: 'PageIndex',
  methods: {
    test () {
      const localUrl = 'http://localhost:5000/'
      // let aws_url  = 'http://ec2-3-97-34-208.ca-central-1.compute.amazonaws.com:5000/'
      axios.get(localUrl + 'sort').then(function (res) {
        var fileURL = window.URL.createObjectURL(new Blob([res.data]))
        var fileLink = document.createElement('a')
        fileLink.href = fileURL
        fileLink.setAttribute('download', 'result.zip')
        document.body.appendChild(fileLink)
        fileLink.click()
      })
    }
  }
}
</script>
