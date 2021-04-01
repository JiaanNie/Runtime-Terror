<template>
  <q-page padding>
    <q-list bordered padding>
      <q-expansion-item expand-separator icon="fas fa-folder-open" v-for="(ids, label) in getSortedImages" :key="label" :label="label">
        <q-card>
          <q-card-section>
            <div class="q-gutter-lg row items-start justify-evenly">
                <q-img contain v-for= "id in ids" :key=id :src="URL+'image/'+id" style="height: 140px; max-width: 150px" class="shadow-7"/>
            </div>
          </q-card-section>
        </q-card>
      </q-expansion-item>
    </q-list>
    <q-page-sticky position="bottom-right" :offset="[18, 18]">
        <q-btn v-if="!isNormalView" fab icon="fas fa-th" color="accent" class="shadow-7" @click= "normalView">
          <q-tooltip content-class="bg-indigo" :offset="[10, 10]">
            Normal View
          </q-tooltip>
        </q-btn>
    </q-page-sticky>
  </q-page>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  data () {
    return {
      isNormalView: false
    }
  },
  methods: {
    normalView () {
      this.$router.push('/HomePage')
    }
  },
  computed: {
    ...mapGetters({ getSortedImages: 'imageURLs/getSortedImages' }),
    ...mapGetters({ URL: 'env/getHostURL' })
  }
}
</script>

<style >
.q-field__control-container div {
  color: transparent;
}
</style>
