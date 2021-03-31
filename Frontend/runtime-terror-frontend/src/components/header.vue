<template>
  <q-header elevated
  class="bg-primary text-white shadow-2">
    <q-toolbar>
      <q-toolbar-title @click="homePage()">
        Albums
      </q-toolbar-title>
      <q-btn v-if="!isReady" dense flat>
         <i class="fa fa-search" aria-hidden="true" style="font-size: 20px;" @click="isReady = true"></i>
      </q-btn>
      <q-input v-if="isReady" dark dense standout v-model="text" input-class="text-right" class="q-ml-md" style="max-width: 190px" @keyup.enter="searchImages(text)">
        <template v-slot:append>
          <q-icon v-if="text === ''" name="search"/>
          <q-icon v-else name="clear" class="cursor-pointer" @click="isReady=false; text = ''" />
        </template>
      </q-input>
      <q-btn-dropdown dense flat dropdown-icon="filter_alt">
        <q-list>
          <q-item v-for= "label in getLabels" :key=label clickable v-close-popup @click="filterImagesByLabel(label)">
            <q-item-section>
              <q-item-label>{{label}}</q-item-label>
            </q-item-section>
          </q-item>
      </q-list>
    </q-btn-dropdown>
      <q-btn dense flat to="/Settings">
        <i class="fas fa-cog" aria-hidden="true" style="font-size: 20px;"></i>
      </q-btn>
    </q-toolbar>
  </q-header>
</template>
<script>
// import axios from 'axios'
import { mapGetters, mapActions } from 'vuex'
// const URL = 'http://ec2-3-97-34-208.ca-central-1.compute.amazonaws.com:5000/'
// const URL = 'http://localhost:5000/'
export default {
  data () {
    return {
      isReady: false,
      showLabels: false,
      text: '',
      dropdown: false
    }
  },
  created: function () {
    this.fetchAllLabels()
  },
  methods: {
    ...mapActions({ filterImagesByLabel: 'imageURLs/filterImagesByLabel' }),
    ...mapActions({ searchImages: 'imageURLs/searchImages' }),
    ...mapActions({ fetchAllLabels: 'imageURLs/fetchAllLabels' }),
    homePage () {
      this.$router.push('/HomePage')
    }
  },
  computed: {
    ...mapGetters({ getImagesURL: 'imageURLs/getImagesURL' }),
    ...mapGetters({ getLabels: 'imageURLs/getLabels' })
  }
}
</script>
