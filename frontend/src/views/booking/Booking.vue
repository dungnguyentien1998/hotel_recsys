<template>
    <Layout>
        <template #content>
            <div class="align-items-center d-flex">
                <h2 class="flex-grow-1">
                    {{ $t('booking.booking.title') }}
                </h2>
            </div>
            <br>
            <!--   Booking list         -->
            <b-list-group>
                <b-list-group-item
                    v-for="booking in bookings"
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
                            {{ booking.address }}
                        </p>
                        <p>
                            <span class="font-weight-bolder">
                                {{ $t('booking.booking.code') }}:
                            </span>
                            {{ booking.code }}
                        </p>
                        <!--                        <p class="p-inline">-->
                        <!--                            <span class="font-weight-bolder">-->
                        <!--                                {{ $t('booking.booking.roomNumber') }}:-->
                        <!--                            </span>-->
                        <!--                        </p>-->
                        <!--                        <ul class="u-inline">-->
                        <!--                            <li-->
                        <!--                                v-for="number in booking.roomNumber"-->
                        <!--                                :key="number"-->
                        <!--                                style="display: inline-block; margin: 5px; text-align: left"-->
                        <!--                            >-->
                        <!--                                {{ number }}-->
                        <!--                            </li>-->
                        <!--                        </ul>-->
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
                            <!--                            <b-button-->
                            <!--                                href="#"-->
                            <!--                                variant="danger"-->
                            <!--                                size="sm"-->
                            <!--                                @click="$bvModal.show(`modal-${booking.uuid}-delete`)"-->
                            <!--                            >-->
                            <!--                                {{ $t('booking.booking.cancelBtn') }}-->
                            <!--                            </b-button>-->
                            <!--                            <b-modal-->
                            <!--                                :id="`modal-${booking.uuid}-delete`"-->
                            <!--                                :title="$t('booking.booking.cancelTitle')"-->
                            <!--                                size="lg"-->
                            <!--                                :ok-title="$t('button.submit')"-->
                            <!--                                :cancel-title="$t('button.unsubmit')"-->
                            <!--                                @ok="deleteBooking(booking.uuid)"-->
                            <!--                            >-->
                            <!--                                {{ $t('booking.booking.confirmDelete') }}-->
                            <!--                            </b-modal>-->
                            <!--                            <b-modal-->
                            <!--                                :id="`modal-${booking.created}-view`"-->
                            <!--                                title="View booking"-->
                            <!--                                size="lg"-->
                            <!--                                hide-footer-->
                            <!--                            >-->
                            <!--                                <booking-detail :booking="booking" />-->
                            <!--                            </b-modal>-->
                        </div>
                    </div>
                </b-list-group-item>
            </b-list-group>
        </template>
    </Layout>
</template>

<script>
import Layout from "@/components/layouts/Layout";
import {faHotel, faMoneyBill} from '@fortawesome/free-solid-svg-icons'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faAddressBook, faCalendar, faMoneyBillAlt} from '@fortawesome/free-regular-svg-icons'
import BookingDetail from "@/views/booking/BookingDetail";

library.add(faHotel)
library.add(faCalendar)
library.add(faAddressBook)
library.add(faMoneyBillAlt)

export default {
    name: "Booking",
    components: {Layout},
    data: function () {
        return {
            // Booking data
            bookings: [],
        }
    },
    created() {
        this.$store.dispatch('booking/newListBookings')
            .then(() => {
                this.bookings = this.$store.getters['booking/bookings']
                this.bookings.sort(function (a,b) {
                    return new Date(b.created) - new Date(a.created)
                })
            })
    },
    methods: {
        hotelImage: function (uri) {
            return `${process.env.VUE_APP_PUBLIC_URL}${uri}`
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
</style>