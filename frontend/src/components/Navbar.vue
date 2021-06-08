<template>
    <div>
        <b-navbar
            toggleable="lg"
            style="height: 60px"
            variant="light"
            type="light"
            :sticky="true"
        >
            <b-navbar-brand
                v-if="loggedIn"
                :href="dashboard"
            >
                <img
                    src="../assets/hotel.png"
                    alt="hotel"
                    class="icon"
                >
                Hotels
            </b-navbar-brand>

            <b-navbar-brand
                v-if="!loggedIn"
                href="/login"
            >
                <img
                    src="../assets/hotel.png"
                    alt="hotel"
                    class="icon"
                >
                Hotels
            </b-navbar-brand>

            <b-navbar-toggle target="nav-collapse" />

            <b-collapse
                id="nav-collapse"
                is-nav
            >
                <b-navbar-nav>
                    <b-nav-item
                        v-if="loggedIn && roleUser"
                        id="favorite"
                        style="margin:5px; font-weight: bold"
                        href="/favorites"
                        :active="$route.path === '/favorites'"
                    >
                        {{ $t('navbar.favorite') }}
                    </b-nav-item>
                    <b-nav-item
                        v-if="loggedIn && roleUser"
                        id="booking"
                        style="margin:5px; font-weight: bold"
                        href="/bookings"
                        :active="$route.path === '/bookings'"
                    >
                        {{ $t('navbar.booking') }}
                    </b-nav-item>
                    <!--                    <b-nav-item-->
                    <!--                        v-if="loggedIn && roleUser"-->
                    <!--                        id="reply"-->
                    <!--                        style="margin:5px; font-weight: bold"-->
                    <!--                        href="/replys"-->
                    <!--                    >-->
                    <!--                        {{ $t('navbar.reply') }}-->
                    <!--                    </b-nav-item>-->
                    <b-nav-item
                        v-if="loggedIn && roleHotelier"
                        id="notification"
                        style="margin:5px; font-weight: bold"
                        href="/notification/hotels"
                        :active="$route.path === '/notification/hotels'"
                    >
                        {{ $t('navbar.notification') }}
                        <b-badge
                            v-if="notify_count>0"
                            variant="primary"
                        >
                            {{ notify_count }}
                        </b-badge>
                    </b-nav-item>
                    <b-nav-item
                        v-if="loggedIn && roleAdmin"
                        id="user"
                        style="margin:5px; font-weight: bold"
                        href="/admin/users"
                        :active="$route.path === '/admin/users'"
                    >
                        {{ $t('navbar.user') }}
                    </b-nav-item>
                    <b-nav-item
                        v-if="loggedIn && roleAdmin"
                        id="hotel"
                        style="margin:5px; font-weight: bold"
                        href="/admin/hotels"
                        :active="$route.path === '/admin/hotels'"
                    >
                        {{ $t('navbar.hotel') }}
                        <b-badge
                            v-if="count>0"
                            variant="primary"
                        >
                            {{ count }}
                        </b-badge>
                    </b-nav-item>
                </b-navbar-nav>

                <b-navbar-nav class="ml-auto align-items-center">
                    <b-nav-item-dropdown
                        :text="$t('navbar.languages')"
                        class="nav-lang"
                        right
                    >
                        <b-dropdown-item
                            :active="isEn"
                            @click="localeToEn"
                        >
                            {{ $t('navbar.en') }}
                        </b-dropdown-item>

                        <b-dropdown-item
                            :active="isVi"
                            @click="localeToVi"
                        >
                            {{ $t('navbar.vi') }}
                        </b-dropdown-item>
                    </b-nav-item-dropdown>

                    <b-nav-item-dropdown
                        v-if="loggedIn"
                        class="nav-avatar"
                        right
                    >
                        <template #button-content>
                            <b-avatar
                                variant="info"
                                :src="avatar"
                            />
                        </template>

                        <b-dropdown-item
                            href="/profile"
                        >
                            {{ $t('navbar.profile') }}
                        </b-dropdown-item>
                        <b-dropdown-item
                            href="/change-password"
                        >
                            {{ $t('navbar.changePassword') }}
                        </b-dropdown-item>

                        <b-dropdown-item
                            href="#"
                            @click="logout"
                        >
                            {{ $t('navbar.logout') }}
                        </b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
import {faHotel} from '@fortawesome/free-solid-svg-icons'
import {library} from '@fortawesome/fontawesome-svg-core'

library.add(faHotel)

export default {
    name: "Navbar",
    computed: {
        count: function () {
            return this.$store.getters['hotel/hotels'].length
        },
        notify_count: function() {
            return this.$store.getters['hotel/count_hotelier']
        },
        // Check if user logged in
        loggedIn: function () {
            return !!localStorage.getItem('token')
        },
        // Get user avatar
        avatar: function () {
            return `${process.env.VUE_APP_PUBLIC_URL}${this.$store.getters['user/user'].image}`
        },
        // Check if role hotelier
        roleHotelier: function () {
            return (this.$store.getters['user/user'].role === 'hotelier')
        },
        // Check if role user
        roleUser: function () {
            return (this.$store.getters['user/user'].role === 'user')
        },
        roleAdmin: function () {
            return (this.$store.getters['user/user'].role === 'admin')
        },
        // Select url based on user role
        dashboard: function () {
            if (this.$store.getters['user/user'] !== null) {
                if (this.roleHotelier === true) {
                    return '/hotels'
                } else if (this.roleUser === true) {
                    return '/dashboard/hotels'
                } else {
                    return '/admin/users'
                }
            } else {
                return '#'
            }
        },
        isVi: function () {
            return (this.$i18n.locale === 'vi')
        },
        isEn: function () {
            return (this.$i18n.locale === 'en')
        },
    },
    beforeCreate() {
        if (localStorage.getItem("language") === null) {
            localStorage.setItem("language", "vi")
        }
    },
    created() {

    },
    methods: {
        // Change to vietnamese
        localeToVi: function () {
            this.$i18n.locale = 'vi'
            localStorage.setItem("language", "vi")
            window.location.reload()
        },
        // Change to english
        localeToEn: function () {
            this.$i18n.locale = 'en'
            localStorage.setItem("language", "en")
            window.location.reload()
        },
        // Logout function
        logout: function () {
            this.$store.dispatch('user/logout')
            this.$router.push('/login')
        }
    }
}
</script>

<style
    lang="scss"
    scoped
>
#favorite :hover{
    color: #1a2795;
    font-weight: bolder;
}
#booking :hover{
    color: #1a2795;
    font-weight: bolder;
}
.selected {
    color: red;
}
.icon {
    height: 20px;
    width: 20px;
}
</style>