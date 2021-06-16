<template>
    <Layout>
        <template #content>
            <div class="align-items-center d-flex">
                <h2 class="flex-grow-1">
                    {{ $t('booking.booking.title') }}
                </h2>
            </div>
            <hr>
            <div
                v-if="loading"
                class="loader"
            />
            <b-list-group
                id="bookings-list"
                :current-page="currentPage"
                :per-page="perPage"
            >
                <b-list-group-item
                    v-for="booking in bookings.slice((currentPage-1)*perPage, (currentPage-1)*perPage+perPage)"
                    :key="booking.uuid"
                    class="list-item"
                >
                    <div>
                        <b-img
                            :src="hotelImage(booking.image)"
                            style="float: right"
                            alt="image"
                            thumbnail
                            fluid
                        />
                    </div>
                    <div>
                        <h5 class="m-0 font-weight-bolder">
                            <img
                                src="../../assets/hotel_icon.png"
                                alt="hotel"
                                class="icon"
                            >
                            {{ $t('booking.booking.hotelName') }}: {{ booking.hotelName }}
                        </h5>
                        <p>
                            <img
                                src="../../assets/map.png"
                                alt="address"
                                class="icon"
                            >
                            <span class="font-weight-bolder">
                                {{ $t('booking.booking.address') }}:
                            </span>
                            {{ getAddress(booking.address, booking.ward, booking.district, booking.city) }}
                        </p>
                        <ul
                            id="time"
                            style="padding: 0; list-style-type: none"
                        >
                            <li>
                                <img
                                    src="../../assets/schedule.png"
                                    alt="Check in date"
                                    class="icon"
                                >
                                <span class="font-weight-bolder">
                                    {{ $t('booking.booking.checkIn') }}:
                                </span>
                                {{ toDate(booking.checkInTime) }}
                            </li>
                            <li>
                                <img
                                    src="../../assets/schedule.png"
                                    alt="Check out date"
                                    class="icon"
                                >
                                <span class="font-weight-bolder">
                                    {{ $t('booking.booking.checkOut') }}:
                                </span>
                                {{ toDate(booking.checkOutTime) }}
                            </li>
                        </ul>
                        <br>
                        <p>
                            <span class="font-weight-bolder">
                                {{ $t('booking.booking.code') }}:
                            </span>
                            {{ booking.code }}
                        </p>
                        <br>
                        <div>
                            <b-button
                                variant="primary"
                                href="#"
                                size="sm"
                                @click="onHandle(booking.uuid)"
                            >
                                {{ $t('booking.booking.viewBtn') }}
                            </b-button>
                        </div>
                    </div>
                </b-list-group-item>
            </b-list-group>
            <br>
            <span
                v-if="bookings.length === 0"
                style="font-style: italic"
            >
                {{ $t('booking.booking.noResult') }}
            </span>
            <b-pagination
                v-if="bookings.length > perPage"
                v-model="currentPage"
                :per-page="perPage"
                :total-rows="rows"
                pills
                aria-controls="bookings-list"
            />
        </template>
    </Layout>
</template>

<script>
import Layout from "@/components/layouts/Layout";
import {faHotel, faMoneyBill} from '@fortawesome/free-solid-svg-icons'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faAddressBook, faCalendar, faMoneyBillAlt} from '@fortawesome/free-regular-svg-icons'
import dataUtil from "@/utils/data-view-utils"
import {validationMixin} from "vuelidate";

library.add(faHotel)
library.add(faCalendar)
library.add(faAddressBook)
library.add(faMoneyBillAlt)

export default {
    name: "Booking",
    components: {Layout},
    mixins: [validationMixin, dataUtil],
    data: function () {
        return {
            // Booking data
            bookings: [],
            currentPage: 1,
            perPage: 10,
            rows: 0,
            loading: false
        }
    },
    created() {
        this.loading = true
        this.$store.dispatch('booking/newListBookings')
            .then(() => {
                this.bookings = this.$store.getters['booking/bookings']
                this.rows = this.bookings.length
                this.bookings.sort(function (a,b) {
                    return new Date(b.created) - new Date(a.created)
                })
                this.loading = false
            })
    },
    methods: {
        getAddress: function (address, ward, district, city) {
            return this.getTransAddress(address, ward, district, city)
        },
        hotelImage: function (uri) {
            return this.getHotelImage(uri)
        },
        // Get date from datetime
        toDate: function(datetime) {
            let date = new Date(datetime);
            return date.getDate() + "-" + (date.getMonth() + 1) + "-" + date.getFullYear();
        },
        onHandle: function(uuid) {
            this.$router.push({name: 'bookingsDetail', params: {uuid: uuid}})
        },
        deleteBooking: function(uuid) {
            this.$store.dispatch('booking/resetStatus')
            this.$store.dispatch('booking/newDeleteBooking', uuid)
                .then(() => {
                    if (this.$store.getters['booking/status'] === 'FAILED') {
                        // Alert for failed api call
                        this.makeToast(this.$t('booking.booking.errors.title'), this.$t('booking.booking.errors.exceptionOccurred'))
                    } else {
                        window.location.reload()
                    }
                })
        }
    }
}
</script>

<style
    lang="scss"
    scoped
>
.list-item {
    margin: 10px 0;
    height: 225px;
    border-radius: 10px;
}
#time li {
    display: inline;
    list-style-type: none;
    float: left;
    margin: 0 10px 0 0;
}
.p-inline {
    display: inline-block;
}
.u-inline {
    display: inline-block;
    padding: 0;
}
.img-thumbnail {
    object-fit: cover;
    height: 200px;
    width: 200px;
}
.icon {
    height: 20px;
    width: 20px;
}
.loader{
    position: absolute;
    top:0;
    right:0;
    width:100%;
    height:100%;
    background-color:#eceaea;
    background-image: url('../../assets/Spinner-3.gif');
    background-size: 50px;
    background-repeat:no-repeat;
    background-position:center;
    z-index:10000000;
    opacity: 0.4;
    filter: alpha(opacity=40);
}
</style>