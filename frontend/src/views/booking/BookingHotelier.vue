<template>
    <div>
        <!--        <h3>-->
        <!--            {{ $t('booking.booking.newTitle') }}-->
        <!--        </h3>-->
        <div>
            <b-button
                v-b-toggle.collapse-2
                variant="primary"
                class="btn-sm"
            >
                {{ $t('booking.booking.newTitle') }}
            </b-button>
            <b-collapse
                id="collapse-2"
                class="mt-2"
                :visible="visibleNewBookings()"
            >
                <b-card>
                    <b-list-group>
                        <b-list-group-item
                            v-for="booking in new_bookings"
                            :key="`${booking.uuid}`"
                            class="list-item"
                        >
                            <div>
                                <h5 class="m-0 font-weight-bolder">
                                    {{ $t('booking.booking.userName') }}: {{ booking.userName }}
                                </h5>
                                <p>
                                    <!--                        <span class="font-weight-bolder">-->
                                    <!--                            {{ $t('booking.booking.userTel') }}:-->
                                    <!--                        </span>-->
                                    <img
                                        v-if="isNotNull(booking.userTel)"
                                        src="../../assets/phone.png"
                                        alt="phone"
                                        class="icon"
                                    >
                                    {{ booking.userTel }}
                                    <span
                                        v-if="isNotNull(booking.userTel)"
                                    >
                                        -
                                    </span>
                                    <!--                        <span class="font-weight-bolder">-->
                                    <!--                            {{ $t('booking.booking.userEmail') }}:-->
                                    <!--                        </span>-->
                                    <img
                                        src="../../assets/email.png"
                                        alt="email"
                                        class="icon"
                                    >
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
                                    <!--                        <b-button-->
                                    <!--                            href="#"-->
                                    <!--                            variant="danger"-->
                                    <!--                            size="sm"-->
                                    <!--                            @click="$bvModal.show(`modal-${booking.uuid}-delete`)"-->
                                    <!--                        >-->
                                    <!--                            {{ $t('booking.booking.cancelBtn') }}-->
                                    <!--                        </b-button>-->
                                    <!--                        <b-modal-->
                                    <!--                            :id="`modal-${booking.uuid}-delete`"-->
                                    <!--                            :title="$t('booking.booking.cancelTitle')"-->
                                    <!--                            size="lg"-->
                                    <!--                            :ok-title="$t('button.submit')"-->
                                    <!--                            :cancel-title="$t('button.unsubmit')"-->
                                    <!--                            @ok="deleteBookingHotelier(booking.uuid)"-->
                                    <!--                        >-->
                                    <!--                            {{ $t('booking.booking.confirmDelete') }}-->
                                    <!--                        </b-modal>-->
                                </div>
                            </div>
                        </b-list-group-item>
                    </b-list-group>
                </b-card>
            </b-collapse>
        </div>
        <hr>
        <br>
        <!--        <h3>-->
        <!--            {{ $t('booking.booking.oldTitle') }}-->
        <!--        </h3>-->
        <div>
            <b-button
                v-b-toggle.collapse-3
                variant="success"
                class="btn-sm"
            >
                {{ $t('booking.booking.oldTitle') }}
            </b-button>
            <b-collapse
                id="collapse-3"
                class="mt-2"
                :visible="visibleOldBookings()"
            >
                <b-card>
                    <b-list-group>
                        <b-list-group-item
                            v-for="booking in getOldBookings()"
                            :key="`${booking.uuid}`"
                            class="list-item"
                        >
                            <div>
                                <h5 class="m-0 font-weight-bolder">
                                    {{ $t('booking.booking.userName') }}: {{ booking.userName }}
                                </h5>
                                <p>
                                    <!--                        <span class="font-weight-bolder">-->
                                    <!--                            {{ $t('booking.booking.userTel') }}:-->
                                    <!--                        </span>-->
                                    <img
                                        v-if="isNotNull(booking.userTel)"
                                        src="../../assets/phone.png"
                                        alt="phone"
                                        class="icon"
                                    >
                                    {{ booking.userTel }}
                                    <span
                                        v-if="isNotNull(booking.userTel)"
                                    >
                                        -
                                    </span>
                                    <!--                        <span class="font-weight-bolder">-->
                                    <!--                            {{ $t('booking.booking.userEmail') }}:-->
                                    <!--                        </span>-->
                                    <img
                                        src="../../assets/email.png"
                                        alt="email"
                                        class="icon"
                                    >
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
                                    id="time-1"
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
                                    <!--                        <b-button-->
                                    <!--                            href="#"-->
                                    <!--                            variant="danger"-->
                                    <!--                            size="sm"-->
                                    <!--                            @click="$bvModal.show(`modal-${booking.uuid}-delete`)"-->
                                    <!--                        >-->
                                    <!--                            {{ $t('booking.booking.cancelBtn') }}-->
                                    <!--                        </b-button>-->
                                    <!--                        <b-modal-->
                                    <!--                            :id="`modal-${booking.uuid}-delete`"-->
                                    <!--                            :title="$t('booking.booking.cancelTitle')"-->
                                    <!--                            size="lg"-->
                                    <!--                            :ok-title="$t('button.submit')"-->
                                    <!--                            :cancel-title="$t('button.unsubmit')"-->
                                    <!--                            @ok="deleteBookingHotelier(booking.uuid)"-->
                                    <!--                        >-->
                                    <!--                            {{ $t('booking.booking.confirmDelete') }}-->
                                    <!--                        </b-modal>-->
                                </div>
                            </div>
                        </b-list-group-item>
                    </b-list-group>
                </b-card>
            </b-collapse>
        </div>
    </div>
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
            new_bookings: []
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
        this.$store.dispatch('booking/listNewBookings', this.$route.params.uuid)
            .then(() => {
                this.new_bookings = this.$store.getters['booking/new_bookings']
                this.new_bookings.sort(function (a,b) {
                    return new Date(a.created) - new Date(b.created)
                })
            })
    },
    methods: {
        visibleNewBookings(){
            return this.new_bookings.length > 0;
        },
        visibleOldBookings(){
            const old_bookings = this.getOldBookings()
            return old_bookings.length > 0;
        },
        // Get date from datetime
        toDate: function (datetime) {
            let date = new Date(datetime);
            return date.getDate() + "-" + (date.getMonth() + 1) + "-" + date.getFullYear();
        },
        onHandle: function(booking_id) {
            localStorage.setItem("bookingId", booking_id)
            this.$store.commit('booking/setBookingId', booking_id)
            this.$router.push({name: 'bookingsHotelierDetail', params: {uuid: this.$route.params.uuid}})
        },
        IsNotArrange: function (uuid) {
            this.$store.dispatch('booking/listBookingRooms', {hotelId: this.$route.params.uuid, bookingId: uuid})
                .then(() => {
                    const booking_rooms = this.$store.getters['booking/booking_rooms']
                    return booking_rooms.length === 0;
                })
        },
        getOldBookings: function () {
            let bookings = this.$store.getters['booking/bookings']
            let new_bookings = this.$store.getters['booking/new_bookings']
            let old_bookings = bookings.filter(o => !new_bookings.some(i => i.uuid === o.uuid))
            old_bookings.sort(function (a,b) {
                return new Date(a.created) - new Date(b.created)
            })
            return old_bookings
        },
        isNotNull: function(tel) {
            return tel != null && tel !== "";
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
    height: 210px;
    border-radius: 10px;
}
#time li {
    display: inline;
    list-style-type: none;
    float: left;
    margin: 0 10px 0 0;
}
#time-1 li {
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