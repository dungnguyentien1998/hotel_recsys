<template>
    <b-list-group>
        <b-list-group-item
            v-for="booking in bookings"
            :key="`${booking.uuid}`"
            class="list-item"
        >
            <div>
                <h5 class="m-0 font-weight-bolder">
                    {{ $t('booking.booking.userName') }}: {{ booking.userName }}
                </h5>
                <p>
                    <span class="font-weight-bolder">
                        {{ $t('booking.booking.userTel') }}:
                    </span>
                    {{ booking.userTel }}
                    -
                    <span class="font-weight-bolder">
                        {{ $t('booking.booking.userEmail') }}:
                    </span>
                    {{ booking.userEmail }}
                </p>
                <p>
                    <span class="font-weight-bolder">
                        {{ $t('booking.booking.code') }}:
                    </span>
                    {{ booking.code }}
                </p>
                <!--                <p-->
                <!--                    class="p-inline"-->
                <!--                >-->
                <!--                    <span class="font-weight-bolder">-->
                <!--                        {{ $t('booking.booking.roomNumber') }}:-->
                <!--                    </span>-->
                <!--                </p>-->
                <!--                <ul class="u-inline">-->
                <!--                    <li-->
                <!--                        v-for="number in booking.roomNumber"-->
                <!--                        :key="number"-->
                <!--                        style="display: inline-block; margin: 5px; text-align: left"-->
                <!--                    >-->
                <!--                        {{ number }}-->
                <!--                    </li>-->
                <!--                </ul>-->
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
                    <b-button
                        href="#"
                        variant="danger"
                        size="sm"
                        @click="$bvModal.show(`modal-${booking.uuid}-delete`)"
                    >
                        {{ $t('booking.booking.cancelBtn') }}
                    </b-button>
                    <b-modal
                        :id="`modal-${booking.uuid}-delete`"
                        :title="$t('booking.booking.cancelTitle')"
                        size="lg"
                        :ok-title="$t('button.submit')"
                        :cancel-title="$t('button.unsubmit')"
                        @ok="deleteBookingHotelier(booking.uuid)"
                    >
                        {{ $t('booking.booking.confirmDelete') }}
                    </b-modal>
                </div>
            </div>
        </b-list-group-item>
    </b-list-group>
</template>

<script>
import {faHotel, faMoneyBill} from '@fortawesome/free-solid-svg-icons'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faAddressBook, faCalendar, faMoneyBillAlt} from '@fortawesome/free-regular-svg-icons'

library.add(faHotel)
library.add(faCalendar)
library.add(faAddressBook)
library.add(faMoneyBillAlt)

export default {
    name: "BookingHotelier",
    data: function () {
        return {
            // Booking data
            bookings: [],
            // form: {
            //     userId: null,
            //     created: null
            // }
        }
    },
    created() {
        this.$store.dispatch('booking/newListBookingsHotelier', this.$route.params.uuid)
            .then(() => {
                this.bookings = this.$store.getters['booking/bookings']
                this.bookings.sort(function (a,b) {
                    return new Date(b.created) - new Date(a.created)
                })
            })
    },
    methods: {
        // Get date from datetime
        toDate: function (datetime) {
            let date = new Date(datetime);
            return date.getDate() + "-" + (date.getMonth() + 1) + "-" + date.getFullYear();
        },
        onHandle: function(booking_id) {
            // localStorage.setItem("created", created)
            // localStorage.setItem("userId", userId)
            localStorage.setItem("bookingId", booking_id)
            this.$router.push({name: 'bookingsHotelierDetail', params: {uuid: this.$route.params.uuid}})
        },
        deleteBookingHotelier: function(uuid) {
            this.$store.dispatch('booking/resetStatus')
            this.$store.dispatch('booking/newDeleteBookingHotelier', {hotelId: this.$route.params.uuid, bookingId: uuid})
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
    height: 250px;
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
.icon {
    height: 20px;
    width: 20px;
}
</style>