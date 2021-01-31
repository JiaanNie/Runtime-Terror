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
 