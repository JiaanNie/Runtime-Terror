<template>
  <q-page padding>
    <div class="q-pa-md" style="max-width: 100%">
      <q-list bordered padding>
        <q-item-label header>User Controls</q-item-label>
        <q-separator spaced />
        <q-item-label header>Notifications</q-item-label>
        <q-item tag="label" v-ripple>
          <q-item-section>
            <q-item-label>Dark mode</q-item-label>
          </q-item-section>
          <q-item-section side >
            <q-toggle color="blue" v-model="notif1" val="battery" @input="toggle"/>
          </q-item-section>
        </q-item>
        <q-separator spaced />
        <q-item-label header>About</q-item-label>
          <q-expansion-item expand-separator label="About Album Organizer"/>
          <q-expansion-item expand-separator label="Help & Support"/>
          <q-expansion-item expand-separator label="Privacy Policy"/>
      </q-list>
    </div>
  </q-page>
</template>

<script>
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
    }
  }
}
</script>
