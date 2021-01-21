<template>
  <q-page class="flex flex-center">
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-full.svg"
    >
    <q-btn color="primary" label="click me" @click=test />
  </q-page>
</template>

<script>
import axios from 'axios'
export default {
  name: 'PageIndex',
  methods: {
    test () {
      axios.get('http://ec2-3-97-34-208.ca-central-1.compute.amazonaws.com:5000/book').then(function (res) {
        console.log(res)
      })
    }
  }
}
</script>
