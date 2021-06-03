<template>
    <Layout>
        <template #content>
            <div>
                <h3>
                    {{ $t('booking.booking.detail') }}
                </h3>
                <hr>
                <b-form>
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
                        <span class="font-weight-bolder">
                            {{ $t('booking.booking.totalPrice') }}: {{ totalPrice() }} VND
                        </span>
                        ({{ $t('booking.booking.description') }})
                    </div>
                    <br>
                    <!--                    <div>-->
                    <!--                        <b-form-group>-->
                    <!--                            <div-->
                    <!--                                v-for="(item, index) in getItem()"-->
                    <!--                                :key="`${item}-${index}`"-->
                    <!--                            >-->
                    <!--                                <label>-->
                    <!--                                    {{ item.type }}-->
                    <!--                                </label>-->
                    <!--                            </div>-->
                    <!--                        </b-form-group>-->
                    <!--                    </div>-->
                    <!--                    <div-->
                    <!--                        v-if="!showTableAfter()"-->
                    <!--                    >-->
                    <!--                        <hr>-->
                    <!--                        <h3>-->
                    <!--                            {{ $t('booking.bookingForm.title') }}-->
                    <!--                        </h3>-->
                    <!--                        <br>-->
                    <!--                        <ul style="padding: 0; list-style-type: none">-->
                    <!--                            <li-->
                    <!--                                v-for="(item, index) in getItem()"-->
                    <!--                                :key="`number-${index}`"-->
                    <!--                                style="list-style-type: none"-->
                    <!--                            >-->
                    <!--                                <span class="font-weight-bolder">-->
                    <!--                                    {{ $t('booking.bookingForm.roomType') }}-->
                    <!--                                </span>-->
                    <!--                                : {{ item.type }}-->
                    <!--                                - -->
                    <!--                                <span>-->
                    <!--                                    ({{ $t('booking.bookingForm.description') }}: {{ item.amount }})-->
                    <!--                                </span>-->
                    <!--                                <br>-->
                    <!--                                <b-form-group>-->
                    <!--                                    <b-form-checkbox-->
                    <!--                                        v-for="option in getAvailableOptions(item.room_number)"-->
                    <!--                                        :key="option.value"-->
                    <!--                                        v-model="room_numbers[getIndex(item.type)]"-->
                    <!--                                        :value="option.value"-->
                    <!--                                        :disabled="onDisable(room_numbers[getIndex(item.type)], item.amount, option)"-->
                    <!--                                        inline-->
                    <!--                                    >-->
                    <!--                                        {{ option.text }}-->
                    <!--                                    </b-form-checkbox>-->
                    <!--                                </b-form-group>-->
                    <!--                            </li>-->
                    <!--                        </ul>-->
                    <!--                    </div>-->
                    <div
                        v-if="!showTableAfter()"
                    >
                        <hr>
                        <h3>
                            {{ $t('booking.bookingForm.title') }}
                        </h3>
                        <br>
                        <b-table
                            id="arrange-table"
                            :items="getItem()"
                            :fields="arrange_fields"
                            :responsive="true"
                            hover
                            striped
                        >
                            <template
                                #cell(amount)="data"
                            >
                                {{ data.item.amount }} {{ $tc('hotel.hotel.room', data.item.amount) }}
                            </template>
                            <template
                                #cell(room_number)="data"
                            >
                                <b-form-group>
                                    <b-form-checkbox
                                        v-for="option in getAvailableOptions(data.item.room_number)"
                                        :key="option.value"
                                        v-model="room_numbers[getIndex(data.item.type)]"
                                        :value="option.value"
                                        :disabled="onDisable(room_numbers[getIndex(data.item.type)], data.item.amount, option.value)"
                                        inline
                                    >
                                        {{ option.text }}
                                    </b-form-checkbox>
                                </b-form-group>
                            </template>
                        </b-table>
                    </div>
                    <div
                        v-if="!showTableAfter()"
                    >
                        <button
                            class="btn btn-sm btn-success"
                            type="button"
                            @click="onSubmit"
                        >
                            {{ $t('hotel.hotel.submit') }}
                        </button>
                    </div>
                    <div
                        v-if="showTableAfter()"
                    >
                        <b-table
                            id="booking-table"
                            :items="getItem()"
                            :fields="arrange_fields_after"
                            :responsive="true"
                            hover
                            striped
                        >
                            <template
                                #cell(amenities)="data"
                            >
                                <ul style="padding: 0; list-style-type: none">
                                    <li
                                        v-for="(amenity, index) in data.item.amenities"
                                        :key="`${data.item.uuid}-amenity-${index}`"
                                    >
                                        <img
                                            :src="getSrc(amenity)"
                                            :alt="amenity"
                                            class="icon"
                                        >
                                        {{ amenity }}
                                    </li>
                                </ul>
                            </template>
                            <template
                                #cell(amount)="data"
                            >
                                {{ data.item.amount }} {{ $tc('hotel.hotel.room', data.item.amount) }}
                            </template>
                            <template
                                #cell(room_booked)="data"
                            >
                                <span>
                                    {{ $t('booking.bookingForm.room') }}
                                </span>
                                <ul style="padding: 0; list-style-type: none; display: inline">
                                    <li
                                        v-for="(number, index) in data.item.room_booked"
                                        :key="`number-${index}`"
                                        class="number"
                                    >
                                        {{ number }}
                                    </li>
                                </ul>
                            </template>
                        </b-table>
                    </div>
                    <!--                    <diuttonv-->
                    <!--                        v-if="showTableAfter()"-->
                    <!--                    >-->
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
                    <!--                    </div>-->
                </b-form>
            </div>
        </template>
    </Layout>
</template>

<script>
import Layout from "@/components/layouts/Layout";
import {faHotel, faMoneyBill} from '@fortawesome/free-solid-svg-icons'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faAddressBook, faCalendar, faMoneyBillAlt} from '@fortawesome/free-regular-svg-icons'
import formMixin from '@/mixin/form-mixin'
import {validationMixin} from "vuelidate";

library.add(faHotel)
library.add(faCalendar)
library.add(faAddressBook)
library.add(faMoneyBillAlt)

export default {
    name: "BookingHotelierDetail",
    components: {Layout},
    mixins: [validationMixin, formMixin],
    data: function () {
        const bookingId = this.$store.getters['booking/booking_id']
        return {
            types: [],
            booking_types: [],
            booking: this.$store.getters['booking/bookings'].filter(booking => (booking.uuid === bookingId))[0],
            room_numbers: [],
            form: {

            }
        }
    },
    computed: {
        fields: function() {
            return [
                {
                    key: 'type',
                    label: this.$t('booking.bookingForm.roomType'),
                },
                {
                    key: 'capacity',
                    label: this.$t('booking.bookingForm.capacity'),
                },
                {
                    key: 'price',
                    label: this.$t('booking.bookingForm.price'),
                },
                {
                    key: 'amenities',
                    label: this.$t('booking.bookingForm.amenities'),
                },
                {
                    key: 'amount',
                    label: this.$t('booking.bookingForm.rooms'),
                },
            ]
        },
        arrange_fields: function () {
            return [
                {
                    key: 'type',
                    label: this.$t('booking.bookingForm.roomType'),
                },
                {
                    key: 'amount',
                    label: this.$t('booking.bookingForm.rooms'),
                },
                {
                    key: 'room_number',
                    label: this.$t('booking.bookingForm.roomNumber'),
                }
            ]
        },
        arrange_fields_after: function () {
            return [
                {
                    key: 'type',
                    label: this.$t('booking.bookingForm.roomType'),
                },
                {
                    key: 'amount',
                    label: this.$t('booking.bookingForm.hotelierRooms'),
                },
                {
                    key: 'room_booked',
                    label: this.$t('booking.bookingForm.roomNumber'),
                }
            ]
        }
    },
    created() {
        this.$store.dispatch('type/listTypes', this.booking.hotelid)
            .then(() => {
                this.types = this.$store.getters['type/types']
            })
        this.$store.dispatch('booking/listTypes', {hotelId: this.$route.params.uuid, bookingId: this.booking.uuid})
            .then(() => {
                this.booking_types = this.$store.getters['booking/types']
                for (let i = 0; i < this.booking_types.length; i++) {
                    this.room_numbers.push([])
                }
            })
        this.$store.dispatch('booking/listBookingRooms', {hotelId: this.$route.params.uuid, bookingId: this.booking.uuid})
            .then(() => {
                this.booking_rooms = this.$store.getters['booking/booking_rooms']
            })
    },
    methods: {
        getSrc: function (amenity) {
            let images = require.context('../../assets/', false, /\.png$/)
            return images('./' + amenity + ".png")
        },
        hotelImage: function (uri) {
            return `${process.env.VUE_APP_PUBLIC_URL}${uri}`
        },
        showTableAfter: function() {
            const booking_rooms = this.$store.getters['booking/booking_rooms']
            return booking_rooms.length > 0;
        },
        getIndex: function(room_type) {
            let index = 0
            const types = this.$store.getters['booking/types']
            for (let i=0; i<types.length; i++) {
                if (types[i].roomType === room_type) {
                    return index
                }
                index = index + 1
            }
            return index
        },
        onDisable: function (room_numbers, amount, value) {
            return room_numbers.length >= amount && room_numbers.indexOf(value) === -1
        },
        toDate: function (datetime) {
            let date = new Date(datetime);
            return date.getDate() + "-" + (date.getMonth() + 1) + "-" + date.getFullYear();
        },
        onlyUnique: function (value, index, self) {
            return self.indexOf(value) === index
        },
        getAvailableOptions: function(room_number) {
            let options = []
            for (let i = 0; i < room_number.length; i++) {
                options.push({text: room_number[i], value: room_number[i]})
            }
            return options
        },
        getItem: function () {
            let temp = []
            for (let i = 0; i < this.booking_types.length; i++) {
                temp.push({'type': this.booking_types[i].roomType, 'room_number': this.booking_types[i].roomNumber,
                'amount': this.booking_types[i].amount, 'room_booked': this.booking_types[i].roomBooked})
            }
            return temp
        },
        totalPrice: function () {
            let total_price = 0
            const prices = this.booking.price
            for (const price in prices) {
                total_price += prices[price]
            }
            return total_price
        },
        isNotNull: function(tel) {
            return tel != null && tel !== "";
        },
        deleteBookingHotelier: function (uuid) {
            this.$store.dispatch('booking/resetStatus')
            this.$store.dispatch('booking/newDeleteBookingHotelier', {hotelId: this.$route.params.uuid, bookingId: uuid})
                .then(() => {
                    if (this.$store.getters['booking/status'] === 'FAILED') {
                        // Alert for failed api call
                        this.makeToast(this.$t('booking.booking.errors.title'), this.$t('booking.booking.errors.exceptionOccurred'))
                    } else {
                        this.$router.push({name: 'bookingsHotelier', params: {uuid: this.$route.params.uuid}})
                    }
                })
        },
        onSubmit: function () {
            const bookingId = this.booking.uuid
            let check_higher = ''
            let check_lower = ''
            for (let i = 0; i < this.booking_types.length; i++) {
                if (this.room_numbers[i].length > this.booking_types[i].amount) {
                    check_higher = this.booking_types[i].roomType
                    break
                }
                if (this.room_numbers[i].length < this.booking_types[i].amount) {
                    check_lower = this.booking_types[i].roomType
                    break
                }
            }
            if (check_higher !== '') {
                let failed_message = ''
                if (localStorage.getItem("language") === "en") {
                    failed_message = 'The number of ' + check_higher + ' rooms that you choose is greater than the number of rooms that customer books'
                } else {
                    failed_message = 'Số lượng phòng ' + check_higher + ' mà bạn chọn lớn hơn số lượng phòng mà khách hàng đặt'
                }
                this.makeToast(this.$t('booking.booking.errors.title'), failed_message)
            } else if (check_lower !== '') {
                let failed_message = ''
                if (localStorage.getItem("language") === "en") {
                    failed_message = 'The number of ' + check_lower + ' rooms that you choose is smaller than the number of rooms that customer books'
                } else {
                    failed_message = 'Số lượng phòng ' + check_higher + ' mà bạn chọn nhỏ hơn số lượng phòng mà khách hàng đặt'
                }
                this.makeToast(this.$t('booking.booking.errors.title'), failed_message)
            } else {
                let flat_room_numbers = []
                for (let i = 0; i < this.booking_types.length; i++) {
                    for (let j = 0; j < this.room_numbers[i].length; j++) {
                        flat_room_numbers.push(this.room_numbers[i][j])
                    }
                }
                if (flat_room_numbers.length === 0) {
                    this.makeToast(this.$t('booking.bookingForm.errors.createTitle'), this.$t('booking.bookingForm.errors.missing'))
                } else {
                    this.form.booking_id = bookingId
                    this.form.room_numbers = flat_room_numbers
                    this.form.hotelId = this.$route.params.uuid
                    this.$store.dispatch('booking/resetStatus')
                    this.$store.dispatch('booking/arrangeRoom', this.form).then(() => {
                        if (this.$store.getters['booking/status'] === 'FAILED') {
                            this.makeToast(this.$t('booking.booking.errors.title'), this.$t('booking.booking.errors.exceptionOccurred'))
                        } else {
                            // this.$router.push({name: 'bookingsHotelier', params: {uuid: this.$route.params.uuid}})
                            window.location.reload()
                        }
                    })
                }
            }
        }
    }
}
</script>

<style
    lang="scss"
    scoped
>
.p-inline {
    display: inline-block;
}
.u-inline {
    display: inline-block;
    padding: 0;
}
#time li {
    display: inline-block;
    list-style-type: none;
    float: left;
    margin: 0 10px 0 0;
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
li.number {
    list-style: none;
    //float: left;
    display: inline;
    padding: 0 5px;
    margin-bottom: 5px;
}
//li.number:nth-child(4n) {clear: left}
</style>