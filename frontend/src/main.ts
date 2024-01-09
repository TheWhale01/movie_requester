import('./assets/css/main.css');

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faSearch, faCircleCheck, faCheck } from '@fortawesome/free-solid-svg-icons';
import Notifications from '@kyvg/vue3-notification';

library.add(faSearch);
library.add(faCircleCheck);
library.add(faCheck);

const app = createApp(App)

app.component('font-awesome-icon', FontAwesomeIcon);
app.use(router)
app.use(Notifications);

app.mount('#app')
