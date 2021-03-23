import axios from 'axios'
const URL = 'http://localhost:5000/'
export function login (state, email, password) {
  console.log(email, password)
  axios.post(URL + 'login', { email: 'exmaple1@gmail.com', password: 'abc1234' }).then((res) => {
    console.log(res)
  })
}
export function logout (state) {

}
