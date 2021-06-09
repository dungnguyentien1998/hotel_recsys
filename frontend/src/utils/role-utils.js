export default {
    methods: {
        roleHotelier: function () {
            return (this.$store.getters['user/user'].role === 'hotelier')
        },
        roleUser: function () {
            return (this.$store.getters['user/user'].role === 'user')
        },
        roleAdmin: function () {
            return (this.$store.getters['user/user'].role === 'admin')
        },
    }
}