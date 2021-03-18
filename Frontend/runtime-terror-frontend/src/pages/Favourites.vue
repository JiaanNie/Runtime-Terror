<template>
  <q-page padding>
    <div class="q-gutter-lg row items-start justify-evenly">
      <q-img v-for= "item in getFavoriteImagesURL" :key=item.url :src=item.url style="height: 140px; max-width: 150px" class="shadow-7">
         <q-icon v-if="!item.favorite" name="favorite_border" clickable @click="setFavorite(item)" class="absolute-bottom-right" style="font-size: 3.5em;"/>
         <q-icon v-if="item.favorite" name="favorite" clickable @click="setFavorite(item)" class="absolute-bottom-right" style="font-size: 3.5em; color: red; border-color: black;"/>
      </q-img>
    </div>
  </q-page>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import axios from 'axios'
const URL = 'http://localhost:5000/'
export default {
  name: 'Favourites',
  data () {
    return {
    }
  },
  created: function () {
    // loading images from the db into the app fetch all the url for display each image on the app
    this.fetchFavoriteImagesURL()
  },
  methods: {
    ...mapActions({ fetchFavoriteImagesURL: 'imageURLs/fetchFavoriteImagesURL' }),
    setFavorite (imageDetails) {
      console.log(imageDetails)
      axios.put(URL + '/favorite/' + imageDetails.id).then((res) => {
        this.fetchFavoriteImagesURL()
      })
    }
  },
  computed: {
    ...mapGetters({ getFavoriteImagesURL: 'imageURLs/getFavoriteImagesURL' })
  }
}
</script>
