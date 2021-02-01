<template>
  <q-page class="bg-blue-grey-2" padding>
  <div class="q-gutter-lg row items-start">
      <q-file standout bottom-slots
      color="grey"
      style="max-width: 150px"
      bg-color="blue-grey-3"
      v-model="filesImages"
      multiple
       accept=".jpg, image/*"
        @rejected="onRejected">
         <template v-slot:prepend>
          <q-icon name="add"/>
        </template>
      </q-file>
        </div>
          </div>
          </div>

  </q-page>
</template>

<script>
import axios from 'axios'
// import JSZip from 'jszip'
import { saveAs } from 'file-saver'
export default {
  name: 'PageIndex'
}
</script>
<script>
export default {
  data () {
    return {
      tab: 'albums'
    }
  }
}
</script>
<script>
export default {
  data () {
    return {
      filesImages: null
    }
  },

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
    onRejected (rejectedEntries) {
      // Notify plugin needs to be installed
      // https://quasar.dev/quasar-plugins/notify#Installation
      this.$q.notify({
        type: 'negative',
        message: `${rejectedEntries.length} file(s) did not pass validation constraints`
      })
    }
  }
}
</script>

<style lang="sass" scoped>
.row > div
  padding: 10px 15px
  background: white
.row + .row
  margin-top: 1rem
</style>
