<template>
  <q-page padding>
    <div class="q-pa-md" style="max-width: 100%">
      <q-list bordered padding>
        <q-item-label header>User Controls</q-item-label>
        <q-separator spaced />
        <q-item tag="label" v-ripple>
          <q-item-section>
            <q-item-label>Dark mode</q-item-label>
          </q-item-section>
          <q-item-section side >
            <q-toggle color="blue" v-model="notif1" val="battery" @input="toggle"/>
          </q-item-section>
        </q-item>
        <q-item tag="lable" v-ripple>
          <q-item-section>
            <q-item-label>Clear Database</q-item-label>
          </q-item-section>
          <q-item-section side >
            <q-toggle color="blue" v-model="notif1" val="battery" @input="toggle"/>
          </q-item-section>
        </q-item>
        <q-item tag="label" v-ripple>
          <q-item-section>
            <q-item-label @click="logout">Log Out</q-item-label>
          </q-item-section>
        </q-item>
        <q-separator spaced />
        <q-item-label header>About</q-item-label>
          <q-expansion-item expand-separator label="About Album Organizer">
            <q-card>
              <q-card-section>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, eius reprehenderit eos corrupti
                commodi magni quaerat ex numquam, dolorum officiis modi facere maiores architecto suscipit iste
                eveniet doloribus ullam aliquid.
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
export default {
  name: 'Settings',
  data () {
    return {
      notif1: true,
      notif2: true
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
    }
  }
}
</script>
