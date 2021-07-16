import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((repsonse) => {
      response[1].value = `Error: ${response[1].reason.message}`;
      delete response[1].reason;
      return response;
    });

}
// return an array with the following structure:
//[
//    {
//      status: status_of_the_promise,
//      value: value or error returned by the Promise
//    },
//    ...
//  ]
