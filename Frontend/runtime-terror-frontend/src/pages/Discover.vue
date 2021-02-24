<template>
  <q-page padding class="absolute-center">
    <q-card inline style="width: 375px; heigh: 400px;">
      <q-img :src="photoReference" :ratio="4/3"/>
      <q-card-section>
        {{locationName}}
      </q-card-section>
      <q-card-section style="height: 300px">
        <p class="text-faded">lat: {{lat}}</p>
        <p class="text-faded">long: {{long}}</p>
      </q-card-section>
      <q-separator />
      <q-card-actions>
        <q-btn flat round icon="explore" />
        <q-btn flat @click="fetchPlaceDetails">
          DISCOVER A PLACE
        </q-btn>
      </q-card-actions>
    </q-card>
</q-page>
</template>

<script>
import axios from 'axios'
const URL = 'http://localhost:5000/'
import secret from 'src/keys'
const key = secret.google_place
const GOOGLEPhotoBASE = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference='
const GOOGLEKEY = `&key=${key}`
export default {
  name: 'Discover',
  data () {
    return {
      photoReference: '',
      locationName: '',
      lat: '',
      long: ''
    }
  },
  created: function () {
    this.fetchPlaceDetails()
  },
  methods: {
    fetchPlaceDetails () {
      var vm = this
      axios.get(URL + 'places').then(function (res) {
        vm.photoReference = GOOGLEPhotoBASE + res.data.photo_reference + GOOGLEKEY
        vm.locationName = res.data.name
        vm.long = res.data.location.lng
        vm.lat = res.data.location.lat
      })
    }
  }
}
</script>
