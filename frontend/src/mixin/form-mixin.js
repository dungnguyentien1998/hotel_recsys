export default {
    methods: {
        makeToast: function (title, msg) {
            this.$bvToast.toast(msg, {
                title: title,
                autoHideDelay: 5000,
                variant: 'danger'
            })
        },
        validateState: function (name) {
            const {$dirty, $error} = this.$v.form[name];
            return $dirty ? !$error : null;
        }
    }
}