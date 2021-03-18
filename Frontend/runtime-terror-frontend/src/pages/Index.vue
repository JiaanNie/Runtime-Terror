<template>
  <q-page padding>
    <div class="q-gutter-lg row items-start justify-evenly">
        <q-file standout bottom-slots ref="file" color="grey" style="color: grey-4; height: 140px; max-width: 150px; color:transparent; " v-model="filesImages" multiple accept=".jpg, image/*" @input="uploadImages(filesImages)" >
            <q-icon name="add_a_photo" class="absolute-center" style="height: 140px; font-size: 2em; color: #BCAAA4"/>
        </q-file>
        <q-img contain v-for= "item in getImagesURL" :key=item.url :src=item.url style="height: 140px; max-width: 150px" class="shadow-7">
            <q-icon v-if="!item.favorite" name="favorite_border" clickable @click="setFavorite(item)" class="absolute-bottom-right" style="font-size: 3.5em;"/>
            <q-icon v-if="item.favorite" clickable @click="setFavorite(item)" name="favorite" class="absolute-bottom-right" style="font-size: 3.5em; color: red"/>
        </q-img>
    </div>
    <q-page-sticky position="bottom-right" :offset="[18, 18]">
        <q-btn v-if="isDoneUploading" fab icon="done" color="accent" class="shadow-7" @click= "sortImages" />
    </q-page-sticky>
    <q-dialog v-model="ready">
      <q-card style="max-width: 1500px;width:1400px;height:160px">
        <q-card-section>
          <div class="text-h6">Sorting Images</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          <q-linear-progress query class="q-mt-md" v-if="!isQuery" />
          <q-linear-progress class="q-mt-md" :value="isDone" v-if="isQuery"/>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Donwload Zip" color="primary" v-close-popup @click="getZip"/>
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import axios from 'axios'
import { saveAs } from 'file-saver'
import { mapGetters, mapActions } from 'vuex'
// const URL = 'http://ec2-3-97-34-208.ca-central-1.compute.amazonaws.com:5000/'
const URL = 'http://localhost:5000/'
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
      isDone: 1

    }
  },
  created: function () {
    // loading images from the db into the app fetch all the url for display each image on the app
    this.fetchAllImagesURL()
  },
  methods: {
    uploadImages (filesImages) {
      var vm = this
      for (var i = 0; i < filesImages.length; i++) {
        var reader = new FileReader()
        var fd = new FormData()
        reader.readAsDataURL(filesImages[i])
        reader.onload = function (e) {
          vm.urls.push(e.target.result)
        }
        fd.append('img', filesImages[i])
        fd.append('label', 'Unknown')
        axios.post(URL + 'image', fd).then(function (res) {
          vm.fetchAllImagesURL()
          vm.fetchAllLabels()
        })
      }
      vm.isDoneUploading = true
    },
    sortImages () {
      var vm = this
      this.ready = true
      setTimeout(() => { vm.isQuery = true }, 2000)
    },
    getZip () {
      axios.get(URL + 'sort', { responseType: 'blob' }).then(function (res) {
        saveAs(res.data)
      })
    },
    ...mapActions({ fetchAllImagesURL: 'imageURLs/fetchAllImagesURL' }),
    ...mapActions({ fetchFavoriteImagesURL: 'imageURLs/fetchFavoriteImagesURL' }),
    ...mapActions({ fetchAllLabels: 'imageURLs/fetchAllLabels' }),
    setFavorite (imageDetails) {
      axios.put(URL + '/favorite/' + imageDetails.id).then((res) => {
        this.fetchAllImagesURL()
      })
    }
  },
  computed: {
    ...mapGetters({ getImagesURL: 'imageURLs/getImagesURL' }),
    ...mapGetters({ getFavoriteImagesURL: 'imageURLs/getFavoriteImagesURL' })
  }
}
</script>

<style >
.q-field__control-container div {
  color: transparent;
}
</style>
