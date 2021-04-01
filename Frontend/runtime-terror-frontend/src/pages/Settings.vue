<template>
  <q-page padding>
    <div class="q-pa-md" style="max-width: 100%">
      <q-list bordered padding>
        <q-item-label header>Account Info</q-item-label>
        <q-item>
          <q-item-section>
            <q-item-label>User Email</q-item-label>
          </q-item-section>
          <q-item-section side >
            <q-input :placeholder="this.getUserEmail" readonly/>
          </q-item-section>
        </q-item>
        <!-- <q-item v-ripple>
          <q-item-section>
            <q-item-label>Enable Google Vision</q-item-label>
          </q-item-section>
          <q-item-section side >
            <q-toggle color="blue" v-model="getGoogleVisionModel" @input="setGoogleVisionModel(!getGoogleVisionModel)"/>
          </q-item-section>
        </q-item> -->
        <q-item v-ripple>
          <q-item-section>
            <q-item-label>Log Out</q-item-label>
          </q-item-section>
          <q-item-section side >
            <q-icon name="fas fa-sign-out-alt" @click="logout"/>
          </q-item-section>
        </q-item>
        <q-separator spaced />
        <q-item-label header>Application Settings</q-item-label>
        <q-item v-ripple>
          <q-item-section>
            <q-item-label>Dark mode</q-item-label>
          </q-item-section>
          <q-item-section side >
            <q-toggle color="blue" v-model="this.$q.dark.isActive" val="battery" @input="toggle"/>
          </q-item-section>
        </q-item>
        <q-item v-ripple>
          <q-item-section>
            <q-item-label>Export Sorted Images</q-item-label>
          </q-item-section>
          <q-item-section side >
            <q-icon name="fas fa-download"  @click="exportImages"/>
          </q-item-section>
        </q-item>
        <q-separator spaced />
        <q-item-label header>About</q-item-label>
          <q-expansion-item expand-separator label="About Album Organizer">
            <q-card>
              <q-card-section>
                In modern society, travelers have a lot of photos that they have taken over the years on their vacations. Having so many fond memories compounding in their photo albums gets overwhelming over time.
                Where was this photo taken? Why was this structure so important at the time? what can I do to organize my collections? We would like to create an product that is cross platforms allow users feed their images and automatically help them tag them and organize it into different folders
              </q-card-section>
            </q-card>
          </q-expansion-item>
          <q-expansion-item expand-separator label="Help & Support">
            <q-card>
              <q-card-section>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, eius reprehenderit eos corrupti
                commodi magni quaerat ex numquam, dolorum officiis modi facere maiores architecto suscipit iste
                eveniet doloribus ullam aliquid.
              </q-card-section>
            </q-card>
          </q-expansion-item>
          <q-expansion-item expand-separator label="Privacy Policy">
            <q-card>
              <q-card-section>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, eius reprehenderit eos corrupti
                commodi magni quaerat ex numquam, dolorum officiis modi facere maiores architecto suscipit iste
                eveniet doloribus ullam aliquid.
              </q-card-section>
            </q-card>
          </q-expansion-item>
      </q-list>
    </div>
  </q-page>
</template>

<script>
import { colors } from 'quasar'
import { mapGetters, mapActions } from 'vuex'
import axios from 'axios'
import { saveAs } from 'file-saver'
export default {
  name: 'Settings',
  data () {
    return {
      notif1: true
    }
  },
  methods: {
    toggle () {
      this.$q.dark.toggle()
      if (this.$q.dark.isActive === true) {
        colors.setBrand('primary', '#332940')
      } else {
        colors.setBrand('primary', '#1976D2')
      }
    },
    logout () {
      this.$router.push('/')
    },
    ...mapActions({ setGoogleVersionModel: 'user/setGoogleVersionModel' }),
    exportImages () {
      axios.get(this.URL + 'sort', { headers: { user: this.getUserUUID }, responseType: 'blob' }).then(function (res) {
        saveAs(res.data)
      })
    }
  },
  computed: {
    ...mapGetters({ getGoogleVersionModel: 'user/getGoogleVersionModel' }),
    ...mapGetters({ getUserUUID: 'user/getUserUUID' }),
    ...mapGetters({ getUserEmail: 'user/getUserEmail' }),
    ...mapGetters({ URL: 'env/getHostURL' })
  }
}
</script>
