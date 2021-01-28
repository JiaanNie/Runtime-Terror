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
      axios.get(localUrl + 'image/3').then(function (res) {
        document.getElementById('ItemPreview').src = localUrl + 'image/3'
      })
    }
  }
}
</script>
