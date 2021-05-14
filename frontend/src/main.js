import Vue from 'vue'
import App from "@/App"
import Router from "vue-router"
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'
import responsive from 'vue-responsive';
import Vuelidate from 'vuelidate'
import 'v-contextmenu/dist/index.css'
import {sync} from 'vuex-router-sync'
import VueMoment from 'vue-moment'
import {store} from '@/store/store'
import router from '@/router'
import i18n from '@/lang/i18n';
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
import contentmenu from 'v-contextmenu'
import VueCarousel from 'vue-carousel'
import Autocomplete from 'vuejs-auto-complete'


// Disable production warning when run in development mode
Vue.config.productionTip = false;
const originalPush = Router.prototype.push;
// Define router push function
Router.prototype.push = function push(location, onResolve, onReject) {
    if (onResolve || onReject) return originalPush.call(this, location, onResolve, onReject);
    return originalPush.call(this, location).catch(err => err)
};
const unsync = sync(store, router)
unsync()

// Define vue component FontAwesomeIcon
Vue.component('FontAwesomeIcon', FontAwesomeIcon)
// Import plugins
Vue.use(Router)
Vue.use(BootstrapVue)
Vue.use(contentmenu)
Vue.use(VueMoment)
Vue.use(IconsPlugin)
Vue.use(responsive)
Vue.use(Vuelidate)
Vue.use(VueCarousel)
Vue.use(Autocomplete)

// Create Vue instance for App
new Vue({
    render: h => h(App),
    router,
    i18n,
    store
}).$mount('#app')
