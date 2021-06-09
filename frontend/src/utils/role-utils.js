export default {
    methods: {
        getRoleHotelier: function () {
            return (this.$store.getters['user/user'].role === 'hotelier')
        },
        getRoleUser: function () {
            return (this.$store.getters['user/user'].role === 'user')
        },
        getRoleAdmin: function () {
            return (this.$store.getters['user/user'].role === 'admin')
        },
    }
}