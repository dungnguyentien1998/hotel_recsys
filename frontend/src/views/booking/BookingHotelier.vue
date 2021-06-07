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
        <b-pagination
            v-if="filterBookings.length > perPage"
            v-model="currentPage"
            :per-page="perPage"
            :total-rows="rows"
            pills
            aria-controls="bookings-list"
        />
        <!--        <div>-->
        <!--            <b-button-->
        <!--                v-b-toggle.collapse-2-->
        <!--                variant="primary"-->
        <!--                class="btn-sm"-->
        <!--            >-->
        <!--                {{ $t('booking.booking.newTitle') }}-->
        <!--            </b-button>-->
        <!--            <b-collapse-->
        <!--                id="collapse-2"-->
        <!--                class="mt-2"-->
        <!--                :visible="visibleNewBookings()"-->
        <!--            >-->
        <!--                <b-card>-->
        <!--                    <b-list-group>-->
        <!--                        <b-list-group-item-->
        <!--                            v-for="booking in bookings"-->
        <!--                            :key="`${booking.uuid}`"-->
        <!--                            class="list-item"-->
        <!--                        >-->
        <!--                            <div>-->
        <!--                                <h5 class="m-0 font-weight-bolder">-->
        <!--                                    {{ $t('booking.booking.userName') }}: {{ booking.userName }}-->
        <!--                                </h5>-->
        <!--                                <p>-->
        <!--                                    &lt;!&ndash;                        <span class="font-weight-bolder">&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            {{ $t('booking.booking.userTel') }}:&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                        </span>&ndash;&gt;-->
        <!--                                    <img-->
        <!--                                        v-if="isNotNull(booking.userTel)"-->
        <!--                                        src="../../assets/phone.png"-->
        <!--                                        alt="phone"-->
        <!--                                        class="icon"-->
        <!--                                    >-->
        <!--                                    {{ booking.userTel }}-->
        <!--                                    <span-->
        <!--                                        v-if="isNotNull(booking.userTel)"-->
        <!--                                    >-->
        <!--                                        - -->
        <!--                                    </span>-->
        <!--                                    &lt;!&ndash;                        <span class="font-weight-bolder">&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            {{ $t('booking.booking.userEmail') }}:&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                        </span>&ndash;&gt;-->
        <!--                                    <img-->
        <!--                                        src="../../assets/email.png"-->
        <!--                                        alt="email"-->
        <!--                                        class="icon"-->
        <!--                                    >-->
        <!--                                    {{ booking.userEmail }}-->
        <!--                                </p>-->
        <!--                                <p>-->
        <!--                                    <span class="font-weight-bolder">-->
        <!--                                        {{ $t('booking.booking.code') }}:-->
        <!--                                    </span>-->
        <!--                                    {{ booking.code }}-->
        <!--                                </p>-->
        <!--                                <ul-->
        <!--                                    id="time"-->
        <!--                                    style="padding: 0; list-style-type: none"-->
        <!--                                >-->
        <!--                                    <li>-->
        <!--                                        <img-->
        <!--                                            src="../../assets/schedule.png"-->
        <!--                                            alt="Check in date"-->
        <!--                                            class="icon"-->
        <!--                                        >-->
        <!--                                        <span class="font-weight-bolder">-->
        <!--                                            {{ $t('booking.booking.checkIn') }}:-->
        <!--                                        </span>-->
        <!--                                        {{ toDate(booking.checkInTime) }}-->
        <!--                                    </li>-->
        <!--                                    <li>-->
        <!--                                        <img-->
        <!--                                            src="../../assets/schedule.png"-->
        <!--                                            alt="Check out date"-->
        <!--                                            class="icon"-->
        <!--                                        >-->
        <!--                                        <span class="font-weight-bolder">-->
        <!--                                            {{ $t('booking.booking.checkOut') }}:-->
        <!--                                        </span>-->
        <!--                                        {{ toDate(booking.checkOutTime) }}-->
        <!--                                    </li>-->
        <!--                                </ul>-->
        <!--                                <br>-->
        <!--                                <br>-->
        <!--                                <div>-->
        <!--                                    <b-button-->
        <!--                                        variant="primary"-->
        <!--                                        href="#"-->
        <!--                                        size="sm"-->
        <!--                                        @click="onHandle(booking.uuid)"-->
        <!--                                    >-->
        <!--                                        {{ $t('booking.booking.viewBtn') }}-->
        <!--                                    </b-button>-->
        <!--                                    &lt;!&ndash;                        <b-button&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            href="#"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            variant="danger"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            size="sm"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            @click="$bvModal.show(`modal-${booking.uuid}-delete`)"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                        >&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            {{ $t('booking.booking.cancelBtn') }}&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                        </b-button>&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                        <b-modal&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            :id="`modal-${booking.uuid}-delete`"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            :title="$t('booking.booking.cancelTitle')"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            size="lg"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            :ok-title="$t('button.submit')"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            :cancel-title="$t('button.unsubmit')"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            @ok="deleteBookingHotelier(booking.uuid)"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                        >&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            {{ $t('booking.booking.confirmDelete') }}&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                        </b-modal>&ndash;&gt;-->
        <!--                                </div>-->
        <!--                            </div>-->
        <!--                        </b-list-group-item>-->
        <!--                    </b-list-group>-->
        <!--                </b-card>-->
        <!--            </b-collapse>-->
        <!--        </div>-->
        <!--        <hr>-->
        <!--        <br>-->
        <!--        <h3>-->
        <!--            {{ $t('booking.booking.oldTitle') }}-->
        <!--        </h3>-->
        <!--        <div>-->
        <!--            <b-button-->
        <!--                v-b-toggle.collapse-3-->
        <!--                variant="success"-->
        <!--                class="btn-sm"-->
        <!--            >-->
        <!--                {{ $t('booking.booking.oldTitle') }}-->
        <!--            </b-button>-->
        <!--            <b-collapse-->
        <!--                id="collapse-3"-->
        <!--                class="mt-2"-->
        <!--                :visible="visibleOldBookings()"-->
        <!--            >-->
        <!--                <b-card>-->
        <!--                    <b-list-group>-->
        <!--                        <b-list-group-item-->
        <!--                            v-for="booking in getOldBookings()"-->
        <!--                            :key="`${booking.uuid}`"-->
        <!--                            class="list-item"-->
        <!--                        >-->
        <!--                            <div>-->
        <!--                                <h5 class="m-0 font-weight-bolder">-->
        <!--                                    {{ $t('booking.booking.userName') }}: {{ booking.userName || booking.user_name }}-->
        <!--                                </h5>-->
        <!--                                <p>-->
        <!--                                    &lt;!&ndash;                        <span class="font-weight-bolder">&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            {{ $t('booking.booking.userTel') }}:&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                        </span>&ndash;&gt;-->
        <!--                                    <img-->
        <!--                                        v-if="isNotNull(booking.userTel)"-->
        <!--                                        src="../../assets/phone.png"-->
        <!--                                        alt="phone"-->
        <!--                                        class="icon"-->
        <!--                                    >-->
        <!--                                    {{ booking.userTel || booking.user_tel }}-->
        <!--                                    <span-->
        <!--                                        v-if="isNotNull(booking.userTel)"-->
        <!--                                    >-->
        <!--                                        - -->
        <!--                                    </span>-->
        <!--                                    &lt;!&ndash;                        <span class="font-weight-bolder">&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            {{ $t('booking.booking.userEmail') }}:&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                        </span>&ndash;&gt;-->
        <!--                                    <img-->
        <!--                                        src="../../assets/email.png"-->
        <!--                                        alt="email"-->
        <!--                                        class="icon"-->
        <!--                                    >-->
        <!--                                    {{ booking.userEmail || booking.user_email }}-->
        <!--                                </p>-->
        <!--                                <p>-->
        <!--                                    <span class="font-weight-bolder">-->
        <!--                                        {{ $t('booking.booking.code') }}:-->
        <!--                                    </span>-->
        <!--                                    {{ booking.code }}-->
        <!--                                </p>-->
        <!--                                <ul-->
        <!--                                    id="time-1"-->
        <!--                                    style="padding: 0; list-style-type: none"-->
        <!--                                >-->
        <!--                                    <li>-->
        <!--                                        <img-->
        <!--                                            src="../../assets/schedule.png"-->
        <!--                                            alt="Check in date"-->
        <!--                                            class="icon"-->
        <!--                                        >-->
        <!--                                        <span class="font-weight-bolder">-->
        <!--                                            {{ $t('booking.booking.checkIn') }}:-->
        <!--                                        </span>-->
        <!--                                        {{ toDate(booking.checkInTime) }}-->
        <!--                                    </li>-->
        <!--                                    <li>-->
        <!--                                        <img-->
        <!--                                            src="../../assets/schedule.png"-->
        <!--                                            alt="Check out date"-->
        <!--                                            class="icon"-->
        <!--                                        >-->
        <!--                                        <span class="font-weight-bolder">-->
        <!--                                            {{ $t('booking.booking.checkOut') }}:-->
        <!--                                        </span>-->
        <!--                                        {{ toDate(booking.checkOutTime) }}-->
        <!--                                    </li>-->
        <!--                                </ul>-->
        <!--                                <br>-->
        <!--                                <br>-->
        <!--                                <div>-->
        <!--                                    <b-button-->
        <!--                                        variant="primary"-->
        <!--                                        href="#"-->
        <!--                                        size="sm"-->
        <!--                                        @click="onHandle(booking.uuid)"-->
        <!--                                    >-->
        <!--                                        {{ $t('booking.booking.viewBtn') }}-->
        <!--                                    </b-button>-->
        <!--                                    &lt;!&ndash;                        <b-button&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            href="#"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            variant="danger"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            size="sm"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            @click="$bvModal.show(`modal-${booking.uuid}-delete`)"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                        >&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            {{ $t('booking.booking.cancelBtn') }}&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                        </b-button>&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                        <b-modal&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            :id="`modal-${booking.uuid}-delete`"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            :title="$t('booking.booking.cancelTitle')"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            size="lg"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            :ok-title="$t('button.submit')"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            :cancel-title="$t('button.unsubmit')"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            @ok="deleteBookingHotelier(booking.uuid)"&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                        >&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                            {{ $t('booking.booking.confirmDelete') }}&ndash;&gt;-->
        <!--                                    &lt;!&ndash;                        </b-modal>&ndash;&gt;-->
        <!--                                </div>-->
        <!--                            </div>-->
        <!--                        </b-list-group-item>-->
        <!--                    </b-list-group>-->
        <!--                </b-card>-->
        <!--            </b-collapse>-->
        <!--        </div>-->
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
                code: null
            },
            filterBookings: [],
            currentPage: 1,
            perPage: 10,
            rows: 0,
        }
    },
    created() {
        this.$store.dispatch('booking/newListBookingsHotelier', this.$route.params.uuid)
            .then(() => {
                this.bookings = this.$store.getters['booking/bookings']
                this.filterBookings = this.bookings
                this.rows = this.filterBookings.length
                this.filterBookings.sort(function (a,b) {
                    return new Date(a.created) - new Date(b.created)
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

            this.rows = this.filterHotels.length
            // if (this.filterHotels.length === 0) {
            //     this.makeToast(this.$t('hotel.hotel.errors.search'), this.$t('hotel.hotel.noResult'))
            //     this.isSearch = true
            // }
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
            // localStorage.setItem("bookingId", booking_id)
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