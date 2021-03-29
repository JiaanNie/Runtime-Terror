import axios from 'axios'
const URL = 'http://localhost:5000/'
export function login (state, credential) {
  axios.post(URL + 'login', { email: credential.email, password: credential.password }).then((res) => {
    if (res.data === 404) {
      console.log('invaild credential')
    } else {
      console.log(res.data)
      state.commit('updateUserUUID', res.data.uuid)
      state.commit('updateLoginState', true)
      state.commit('updateUserEmail', res.data.email)
      this.$router.push('/HomePage')
    }
  })
}
export function logout (state) {
  state.commit('updateUserUUID', '')
  state.commit('updateLoginState', false)
  this.$router.push('/')
}

export function signUp (state, credential) {
  axios.post(URL + 'signup', { email: credential.email, password: credential.password }).then((res) => {
    console.log(res)
  })
}

export function setGoogleVersionModel (state, setting) {
  state.commit('updateGoogleVersionModelStatus', setting)
}
