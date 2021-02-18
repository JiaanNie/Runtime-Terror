<template>
  <q-page padding>
    <q-img v-for= "item in getFavoriteImagesURL" :key=item.url :src=item.url style="height: 140px; max-width: 150px" class="shadow-7">
       <q-icon v-if="!item.favorite" name="favorite_border" clickable @click="setFavorite(item)" class="absolute-bottom-right" style="font-size: 1.5em; color: #1976D2"/>
       <q-icon v-if="item.favorite" name="favorite" clickable @click="setFavorite(item)" class="absolute-bottom-right" style="font-size: 1.5em; color: red"/>
    </q-img>
  </q-page>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
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
    ...mapActions({ fetchFavoriteImagesURL: 'imageURLs/fetchFavoriteImagesURL' })
  },
  computed: {
    ...mapGetters({ getFavoriteImagesURL: 'imageURLs/getFavoriteImagesURL' })
  }
}
</script>
