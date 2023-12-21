import('./assets/css/main.css');

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faSearch, faCircleCheck } from '@fortawesome/free-solid-svg-icons';

library.add(faSearch);
library.add(faCircleCheck);

const app = createApp(App)

app.component('font-awesome-icon', FontAwesomeIcon);
app.use(router)

app.mount('#app')
