<template>
  <q-page class="bg-grey-2" padding>
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
  </q-page>
</template>

<script>
// import axios from 'axios'
// // import JSZip from 'jszip'
// import { saveAs } from 'file-saver'
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
}
</script>

<style lang="sass" scoped>
.row > div
  padding: 10px 15px
  background: white
.row + .row
  margin-top: 1rem
</style>
