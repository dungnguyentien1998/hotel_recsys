<template>
    <layout>
        <template #content>
            <b-card
                title="Card Title"
                no-body
            >
                <b-card-header
                    header-tag="nav"
                >
                    <!--      Tabs for hotelier              -->
                    <b-nav
                        v-if="roleHotelier"
                        tabs
                        card-header
                    >
                        <b-nav-item
                            :to="{name: 'detail'}"
                            class="b-nav-item"
                            exact-active-class="active"
                        >
                            {{ $t('hotel.hotelDetail.title') }}
                        </b-nav-item>
                        <b-nav-item
                            :to="{name: 'types'}"
                            class="b-nav-item"
                            exact-active-class="active"
                        >
                            {{ $t('hotel.hotelDetail.types') }}
                        </b-nav-item>
                        <b-nav-item
                            :to="{name: 'rooms'}"
                            class="b-nav-item"
                            exact-active-class="active"
                        >
                            {{ $t('hotel.hotelDetail.rooms') }}
                        </b-nav-item>
                        <b-nav-item
                            :to="{name: 'reviews'}"
                            class="b-nav-item"
                            exact-active-class="active"
                        >
                            {{ $t('hotel.hotelDetail.reviews') }}
                        </b-nav-item>
                        <b-nav-item
                            :to="{name: 'complaints'}"
                            class="b-nav-item"
                            exact-active-class="active"
                        >
                            {{ $t('hotel.hotelDetail.complaints') }}
                        </b-nav-item>
                        <b-nav-item
                            :to="{name: 'bookingsHotelier'}"
                            class="b-nav-item"
                            exact-active-class="active"
                        >
                            {{ $t('hotel.hotelDetail.bookings') }}
                        </b-nav-item>
                    </b-nav>
                    <!--      Tabs for user              -->
                    <b-nav
                        v-else
                        tabs
                        card-header
                    >
                        <b-nav-item
                            :to="{name: 'createFavorite'}"
                            class="b-nav-item"
                            exact-active-class="active"
                        >
                            {{ $t('hotel.hotelDetail.title') }}
                        </b-nav-item>
                        <!--                        <b-nav-item-->
                        <!--                            :to="{name: 'dashboardTypes'}"-->
                        <!--                            class="b-nav-item"-->
                        <!--                            exact-active-class="active"-->
                        <!--                        >-->
                        <!--                            {{ $t('hotel.hotelDetail.types') }}-->
                        <!--                        </b-nav-item>-->
                        <b-nav-item
                            :to="{name: 'dashboardRooms'}"
                            class="b-nav-item"
                            exact-active-class="active"
                        >
                            {{ $t('hotel.hotelDetail.rooms') }}
                        </b-nav-item>
                        <b-nav-item
                            :to="{name: 'dashboardReviews'}"
                            class="b-nav-item"
                            exact-active-class="active"
                        >
                            {{ $t('hotel.hotelDetail.reviews') }}
                        </b-nav-item>
                        <b-nav-item
                            :to="{name: 'dashboardComplaints'}"
                            class="b-nav-item"
                            exact-active-class="active"
                        >
                            {{ $t('hotel.hotelDetail.createComplaint') }}
                        </b-nav-item>
                        <b-nav-item
                            :to="{name: 'dashboardBookings'}"
                            class="b-nav-item"
                            exact-active-class="active"
                        >
                            {{ $t('hotel.hotelDetail.booking') }}
                        </b-nav-item>
                    </b-nav>
                </b-card-header>

                <b-card-body>
                    <router-view />
                </b-card-body>
            </b-card>
        </template>
    </layout>
</template>

<script>
import Layout from '@/components/layouts/Layout';

export default {
    name: "HotelDetail",
    components: {Layout},
    computed: {
        // Check if role hotelier
        roleHotelier: function () {
            return (this.$store.getters['user/user'].role === 'hotelier')
        }
    }
}
</script>

<style scoped>
.b-nav-item {
    color: #1a2795;
    font-weight: bolder;
}
</style>