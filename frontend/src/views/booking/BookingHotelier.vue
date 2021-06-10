<template>
    <div>
        <!--        <h3>-->
        <!--            {{ $t('booking.booking.newTitle') }}-->
        <!--        </h3>-->
        <b-button
            v-b-toggle.collapse-1
            variant="secondary"
            class="btn-sm"
        >
            {{ $t('booking.booking.search') }}
        </b-button>
        <b-collapse
            id="collapse-1"
            class="mt-2"
        >
            <b-card>
                <b-form>
                    <b-form-group
                        id="name-group"
                        :label="$t('booking.booking.customerName')"
                        label-for="name"
                        label-cols-sm="3"
                        label-cols-lg="3"
                        content-cols-sm="5"
                        content-cols-lg="5"
                    >
                        <b-form-input
                            v-model="$v.form.user_name.$model"
                            :placeholder="$t('booking.booking.customerNamePlaceholder')"
                            type="text"
                        />
                    </b-form-group>
                    <b-form-group
                        id="tel-group"
                        :label="$t('booking.booking.customerTel')"
                        label-for="tel"
                        label-cols-sm="3"
                        label-cols-lg="3"
                        content-cols-sm="5"
                        content-cols-lg="5"
                    >
                        <b-form-input
                            v-model="$v.form.user_tel.$model"
                            :placeholder="$t('booking.booking.customerTelPlaceholder')"
                            type="text"
                        />
                    </b-form-group>
                    <b-form-group
                        id="email-group"
                        :label="$t('booking.booking.customerEmail')"
                        label-for="email"
                        label-cols-sm="3"
                        label-cols-lg="3"
                        content-cols-sm="5"
                        content-cols-lg="5"
                    >
                        <b-form-input
                            v-model="$v.form.user_email.$model"
                            :placeholder="$t('booking.booking.customerEmailPlaceholder')"
                            type="text"
                        />
                    </b-form-group>
                    <b-form-group
                        id="code-group"
                        :label="$t('booking.booking.bookingCode')"
                        label-for="code"
                        label-cols-sm="3"
                        label-cols-lg="3"
                        content-cols-sm="5"
                        content-cols-lg="5"
                    >
                        <b-form-input
                            v-model="$v.form.code.$model"
                            :placeholder="$t('booking.booking.bookingCodePlaceholder')"
                            type="text"
                        />
                    </b-form-group>
                    <b-form-group>
                        <label class="required">{{ $t('booking.booking.status') }}: </label>
                        <b-form-radio-group
                            v-model="$v.form.status.$model"
                        >
                            <b-form-radio value="yes">
                                {{ $t('booking.booking.processed') }}
                            </b-form-radio>
                            <b-form-radio value="no">
                                {{ $t('booking.booking.notProcess') }}
                            </b-form-radio>
                        </b-form-radio-group>
                    </b-form-group>
                </b-form>
                <button
                    class="btn btn-sm btn-primary"
                    type="button"
                    @click="onSubmit"
                >
                    {{ $t('hotel.hotel.searchBtn') }}
                    <font-awesome-icon
                        :icon="['fas', 'search']"
                    />
                </button>
            </b-card>
        </b-collapse>
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
                v-for="booking in filterBookings.slice((currentPage-1)*perPage, (currentPage-1)*perPage+perPage)"
                :key="`${booking.uuid}`"
                class="list-item"
            >
                <div>
                    <span
                        v-if="isArrange(booking.roomNumber)"
                        class="position-absolute"
                        style="right: 20px; color: #de0404"
                    >
                        {{ $t('booking.booking.isArranged') }}
                    </span>
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
                    </div>
                </div>
            </b-list-group-item>
        </b-list-group>
        <br>
        <span
            v-if="bookings.length === 0"
            style="font-style: italic"
        >
            {{ $t('booking.booking.noBooking') }}
        </span>
        <b-pagination
            v-if="filterBookings.length > perPage"
            v-model="currentPage"
            :per-page="perPage"
            :total-rows="rows"
            pills
            aria-controls="bookings-list"
        />
    </div>
</template>

<script>
import {faHotel, faMoneyBill} from '@fortawesome/free-solid-svg-icons'
import {faSearch} from '@fortawesome/free-solid-svg-icons'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faAddressBook, faCalendar, faMoneyBillAlt} from '@fortawesome/free-regular-svg-icons'

library.add(faHotel)
library.add(faCalendar)
library.add(faAddressBook)
library.add(faMoneyBillAlt)
library.add(faSearch)

export default {
    name: "BookingHotelier",
    data: function () {
        return {
            // Booking data
            bookings: [],
            new_bookings: [],
            form: {
                user_name: null,
                user_tel: null,
                user_email: null,
                code: null,
                status: null,
            },
            filterBookings: [],
            currentPage: 1,
            perPage: 10,
            rows: 0,
            loading: false
        }
    },
    created() {
        this.loading = true
        this.$store.dispatch('booking/newListBookingsHotelier', this.$route.params.uuid)
            .then(() => {
                this.bookings = this.$store.getters['booking/bookings']
                this.filterBookings = this.bookings
                this.rows = this.filterBookings.length
                this.filterBookings.sort(function (a,b) {
                    return new Date(a.created) - new Date(b.created)
                })
                this.loading = false
            })
        this.$store.dispatch('booking/listNewBookings', this.$route.params.uuid)
            .then(() => {
                this.new_bookings = this.$store.getters['booking/new_bookings']
                this.new_bookings.sort(function (a,b) {
                    return new Date(a.created) - new Date(b.created)
                })
            })
    },
    validations: {
        form: {
            user_name: {

            },
            user_tel: {

            },
            user_email: {

            },
            code: {

            },
            status: {

            }
        }
    },
    methods: {
        onSubmit: function () {
            this.filterBookings = this.bookings

            if (!!this.form.user_name) {
                this.filterBookings = this.filterBookings.filter(booking =>
                    booking.userName.toLowerCase().indexOf(this.form.user_name.toLowerCase()) > -1
                )
            }
            if (!!this.form.user_tel) {
                this.filterBookings = this.filterBookings.filter(booking =>
                    booking.userTel.toLowerCase().indexOf(this.form.user_tel.toLowerCase()) > -1
                )
            }
            if (!!this.form.user_email) {
                this.filterBookings = this.filterBookings.filter(booking =>
                    booking.userEmail.toLowerCase().indexOf(this.form.user_email.toLowerCase()) > -1
                )
            }
            if (!!this.form.code) {
                this.filterBookings = this.filterBookings.filter(booking =>
                    booking.code.toLowerCase().indexOf(this.form.code.toLowerCase()) > -1
                )
            }

            this.rows = this.filterBookings.length
            if (this.filterBookings.length === 0) {
                this.makeToast(this.$t('booking.booking.errors.search'), this.$t('booking.booking.noResultSearch'))
                this.isSearch = true
            }
        },
        isArrange(roomNumber) {
            return roomNumber.length > 0;
        },
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