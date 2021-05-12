// Handle form validation
export default {
    methods: {
        // Make alert
        makeToast: function (title, msg) {
            this.$bvToast.toast(msg, {
                title: title,
                autoHideDelay: 5000,
                variant: 'danger'
            })
        },
        // Handle form state
        validateState: function (name) {
            const {$dirty, $error} = this.$v.form[name];
            return $dirty ? !$error : null;
        }
    }
}