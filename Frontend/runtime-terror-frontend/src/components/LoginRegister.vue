<template>
     <q-form
        @submit="onSubmit"
        class="q-gutter-md"
     >
        <q-input
            filled
            v-if="tab == 'register'"
            v-model="formData.name"
            label="Name"
        />

        <q-input
            filled
            v-model="formData.email"
            type="email"
            label="Email"
            lazy-rules
        />
        <q-input
            filled
            v-model="formData.password"
            :type="formData.isPwd ? 'password' : 'text'"
            label="Password">
            <template v-slot:append>
                <q-icon
                    :name="formData.isPwd ? 'visibility_off' : 'visibility'"
                    class="cursor-pointer"
                    @click="formData.isPwd = !formData.isPwd"
                />
            </template>
        </q-input>

        <div class="row">
           <q-space/>
            <q-btn
            :label="tab"
            type="submit"
            color="primary"/>
        </div>
    </q-form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  props: ['tab'],
  data () {
    return {
      formData: {
        name: '',
        email: '',
        password: '',
        isPwd: true
      }
    }
  },
  computed: {
    ...mapGetters({ getUserUUID: 'user/getUserUUID' }),
    ...mapGetters({ getLoginStatus: 'user/getLoginState' })
  },
  methods: {
    ...mapActions({ login: 'user/login' }),
    ...mapActions({ logout: 'user/logout' }),
    ...mapActions({ signup: 'user/signUp' }),
    onSubmit () {
      var credential = {}
      if (this.tab === 'login') {
        credential.email = this.formData.email
        credential.password = this.formData.password
        this.login(credential)
      } else {
        credential.email = this.formData.email
        credential.password = this.formData.password
        this.signup(credential)
      }
    }
  }
}
</script>
