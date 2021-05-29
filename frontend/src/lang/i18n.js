import VueI18n from 'vue-i18n'
import Vue from 'vue'
import vi from '@/lang/locales/vi';
import en from '@/lang/locales/en';

Vue.use(VueI18n)

// Internationalization function
const i18n = new VueI18n({
    locale: localStorage.getItem("language"),
    fallbackLocale: 'vi',
    messages: {
        en: en,
        vi: vi
    }
})

export default i18n
