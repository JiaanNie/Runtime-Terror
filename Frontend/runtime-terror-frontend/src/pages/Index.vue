<template>
  <q-page padding>
    <div class="q-gutter-lg row items-start justify-evenly">
        <q-file standout bottom-slots ref="file" color="grey" style="color: grey-4; height: 140px; max-width: 150px; color:transparent; " v-model="filesImages" multiple accept=".jpg, image/*" @input="uploadImages(filesImages)" >
            <q-icon name="add_a_photo" class="absolute-center" style="height: 140px; font-size: 2em; color: #BCAAA4"/>
        </q-file>
        <q-img contain v-for= "item in getImagesURL" :key=item.id :src=item.url style="height: 140px; max-width: 150px" class="shadow-7" @click="showImage(item.url)">
            <q-icon v-if="!item.favorite" name="favorite_border" clickable @click="setFavorite(item)" class="absolute-bottom-right" style="font-size: 3.5em;"/>
            <q-icon v-if="item.favorite" clickable @click="setFavorite(item)" name="favorite" class="absolute-bottom-right" style="font-size: 3.5em; color: red"/>
        </q-img>
    </div>
    <q-page-sticky position="bottom-right" :offset="[18, 18]">
        <q-btn v-if="isNormalView" fab icon="fas fa-sort" color="accent" class="shadow-7" @click= "sortView">
          <q-tooltip content-class="bg-indigo" :offset="[10, 10]">
            Sorted View
          </q-tooltip>
        </q-btn>
    </q-page-sticky>
    <q-dialog v-model="isFullSize">
      <q-card class="fixed-center" style="width:100%; height:60%">
        <q-img class="fixed-center" :src="selectedURL"></q-img>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import axios from 'axios'
import { saveAs } from 'file-saver'
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'PageIndex',
  data () {
    return {
      tab: 'albums',
      filesImages: null,
      urls: [],
      isDoneUploading: false,
      ready: false,
      progress: 0,
      isQuery: false,
      isDone: 1,
      isNormalView: true,
      isFullSize: false,
      selectedURL: ''

    }
  },
  created: function () {
    // loading images from the db into the app fetch all the url for display each image on the app
    this.fetchAllImagesURL()
  },
  methods: {
    uploadImages (filesImages) {
      var vm = this
      var headers = {
        user: this.getUserUUID
      }
      for (var i = 0; i < filesImages.length; i++) {
        var reader = new FileReader()
        var fd = new FormData()
        reader.readAsDataURL(filesImages[i])
        reader.onload = function (e) {
          vm.urls.push(e.target.result)
        }
        fd.append('img', filesImages[i])
        fd.append('label', 'Unknown')
        console.log('google vision: ', this.getGoogleVisionModel)
        axios.post(this.URL + 'image', fd, { headers: headers, params: { GoogleVisionModel: this.getGoogleVisionModel } }).then(function (res) {
          vm.fetchAllImagesURL()
          vm.fetchAllLabels()
        })
      }
      vm.isDoneUploading = true
    },
    showImage (url) {
      this.isFullSize = true
      this.selectedURL = url
    },
    sortImages () {
      var vm = this
      this.ready = true
      setTimeout(() => { vm.isQuery = true }, 2000)
    },
    getZip () {
      axios.get(this.URL + 'sort', { headers: { user: this.getUserUUID }, responseType: 'blob' }).then(function (res) {
        saveAs(res.data)
      })
    },
    ...mapActions({ fetchAllImagesURL: 'imageURLs/fetchAllImagesURL' }),
    ...mapActions({ fetchFavoriteImagesURL: 'imageURLs/fetchFavoriteImagesURL' }),
    ...mapActions({ fetchAllLabels: 'imageURLs/fetchAllLabels' }),
    ...mapActions({ fetchSortedImages: 'imageURLs/fetchSortedImages' }),
    setFavorite (imageDetails) {
      axios.put(this.URL + '/favorite/' + imageDetails.id).then((res) => {
        this.fetchAllImagesURL()
      })
    },
    sortView () {
      this.isNormalView = false
      this.fetchSortedImages()
      this.$router.push('/SortedView')
      console.log('sort view')
    }
  },
  computed: {
    ...mapGetters({ getImagesURL: 'imageURLs/getImagesURL' }),
    ...mapGetters({ getFavoriteImagesURL: 'imageURLs/getFavoriteImagesURL' }),
    ...mapGetters({ getUserUUID: 'user/getUserUUID' }),
    ...mapGetters({ getGoogleVisionModel: 'user/getGoogleVisionModel' }),
    ...mapGetters({ URL: 'env/getHostURL' })
  }
}
</script>

<style >
.q-field__control-container div {
  color: transparent;
}
</style>
