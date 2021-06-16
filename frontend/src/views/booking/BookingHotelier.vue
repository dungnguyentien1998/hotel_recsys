<template>
    <div>
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
                            type="search"
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
                            type="search"
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
                            type="search"
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
                            type="search"
                        />
                    </b-form-group>
                    <!--                    <b-form-group>-->
                    <!--                        <label class="required">{{ $t('booking.booking.status') }}: </label>-->
                    <!--                        <b-form-radio-group-->
                    <!--                            v-model="$v.form.is_processed.$model"-->
                    <!--                        >-->
                    <!--                            <b-form-radio value="yes">-->
                    <!--                                {{ $t('booking.booking.processed') }}-->
                    <!--                            </b-form-radio>-->
                    <!--                            <b-form-radio value="no">-->
                    <!--                                {{ $t('booking.booking.notProcess') }}-->
                    <!--                            </b-form-radio>-->
                    <!--                        </b-form-radio-group>-->
                    <!--                    </b-form-group>-->
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
                v-for="booking in filterBookings"
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
            v-if="rows > perPage"
            v-model="currentPage"
            :per-page="perPage"
            :total-rows="rows"
            pills
            aria-controls="bookings-list"
            @change="handlePageChange"
        />
    </div>
</template>

<script>
import {faHotel, faMoneyBill} from '@fortawesome/free-solid-svg-icons'
import {faSearch} from '@fortawesome/free-solid-svg-icons'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faAddressBook, faCalendar, faMoneyBillAlt} from '@fortawesome/free-regular-svg-icons'
import {validationMixin} from "vuelidate";
import roleUtil from "@/utils/role-utils"
import dataUtil from "@/utils/data-view-utils"
import formMixin from '@/mixin/form-mixin'
import addressMixin from '@/mixin/address-mixin'
import Pusher from "pusher-js";
import camelcaseKeys from "camelcase-keys";

library.add(faHotel)
library.add(faCalendar)
library.add(faAddressBook)
library.add(faMoneyBillAlt)
library.add(faSearch)

export default {
    name: "BookingHotelier",
    mixins: [validationMixin, formMixin, addressMixin, roleUtil, dataUtil],
    data: function () {
        return {
            // Booking data
            bookings: [],
            new_bookings: [],
            form: {
                user_name: this.$store.getters['booking/user_name'],
                user_tel: this.$store.getters['booking/user_tel'],
                user_email: this.$store.getters['booking/user_email'],
                code: this.$store.getters['booking/code'],
                is_processed: this.$store.getters['booking/is_processed'],
            },
            filterBookings: [],
            currentPage: this.$store.getters['booking/page'],
            perPage: 10,
            rows: 0,
            loading: false,
            isSearch: false,
            uuids: []
        }
    },
    created() {
        this.retrieveBookings()
        this.subscribe_booking()
        this.$store.dispatch('booking/listUuids', this.$route.params.uuid).then(() => {
            this.uuids = this.$store.getters['booking/uuids']
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
            is_processed: {

            }
        }
    },
    methods: {
        getRequestParams(currentPage, perPage, user_name, user_tel, user_email, code, is_processed) {
            let params = []
            if (currentPage) {
                params["page"] = currentPage
                this.$store.commit('booking/setPage', currentPage)
            } else {
                if (this.isSearch || this.$store.getters['booking/is_search']) {
                    params["page"] = this.$store.getters['booking/page']
                }
            }
            if (perPage) {
                params["per_page"] = perPage
            }
            if (user_name) {
                params["user_name"] = user_name
                this.$store.commit('booking/setUserName', user_name)
            } else {
                this.$store.commit('booking/setUserName', user_name)
                if (this.isSearch || this.$store.getters['booking/is_search']) {
                    params["user_name"] = null
                }
            }
            if (user_tel) {
                params["user_tel"] = user_tel
                this.$store.commit('booking/setUserTel', user_tel)
            } else {
                this.$store.commit('booking/setUserTel', user_tel)
                if (this.isSearch || this.$store.getters['booking/is_search']) {
                    params["user_tel"] = null
                }
            }
            if (user_email) {
                params["user_email"] = user_email
                this.$store.commit('booking/setUserEmail', user_email)
            } else {
                this.$store.commit('booking/setUserEmail', user_email)
                if (this.isSearch || this.$store.getters['booking/is_search']) {
                    params["user_email"] = null
                }
            }
            if (code) {
                params["code"] = code
                this.$store.commit('booking/setCode', code)
            } else {
                this.$store.commit('booking/setCode', code)
                if (this.isSearch || this.$store.getters['booking/is_search']) {
                    params["code"] = null
                }
            }
            if (is_processed) {
                params["is_processed"] = is_processed
                this.$store.commit('booking/setIsProcessed', is_processed)
            } else {
                this.$store.commit('booking/setIsProcessed', is_processed)
                if (this.isSearch || this.$store.getters['booking/is_search']) {
                    params["is_processed"] = null
                }
            }
            return params
        },
        retrieveBookings() {
            const params = this.getRequestParams(this.currentPage, this.perPage, this.form.user_name, this.form.user_tel,
                this.form.user_email, this.form.code, this.form.is_processed)
            params["hotelId"] = this.$route.params.uuid
            this.loading = true
            this.$store.dispatch('booking/newListBookingsHotelier', params)
                .then(() => {
                    this.bookings = this.$store.getters['booking/bookings']
                    this.filterBookings = this.bookings
                    this.rows = this.$store.getters['booking/count']
                    this.loading = false
                })
        },
        handlePageChange(value) {
            this.currentPage = value
            this.retrieveBookings()
        },
        onSubmit: function () {
            this.isSearch = true
            this.$store.commit('booking/setIsSearch', true)
            this.currentPage = 1
            this.retrieveBookings()
        },
        isArrange(roomNumber) {
            return roomNumber.length > 0;
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
        },
        subscribe_booking() {
            let pusher = new Pusher('5d873d3e35474aa76004', {
                cluster: 'ap1'
            });
            pusher.subscribe('a_channel');
            pusher.bind('an_event_3', data => {
                let user = this.$store.getters['user/user']
                if (user.role === 'hotelier' && user.uuid === data.booking.hotel_owner_id) {
                    data = camelcaseKeys(data, {deep: true})
                    let new_uuid = data.booking.uuid
                    let check = true
                    let uuids = this.$store.getters['booking/uuids']
                    for (let i=0; i<uuids.length; i++) {
                        if (uuids[i] === new_uuid) {
                            check = false
                            break
                        }
                    }
                    if (check === true) {
                        this.$store.commit('booking/saveBooking', data)
                        this.$store.commit('booking/saveNewBooking', data)
                    }
                    this.$store.commit('booking/saveUuid', data.booking.uuid)
                }
            })
        },
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