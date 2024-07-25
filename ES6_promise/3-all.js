import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()]).then((values) => {
    let response = '';
    values.map((value) => {
      if (value.body) {
        response = `${response + value.body} `;
      } else {
        response = `${response + value.firstName} ${value.lastName}`;
      }
      return response;
    });
    console.log(response);
  }).catch(() => {
    console.log('Signup system offline');
  });
}
