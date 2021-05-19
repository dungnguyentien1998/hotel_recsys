<template>
    <layout>
        <template #content>
            <div>
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
                                src="../../assets/phone.png"
                                alt="phone"
                                class="icon"
                            >
                            {{ booking.userTel }}
                            -
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
                    <div
                        v-if="!showTableAfter()"
                    >
                        <b-table
                            id="arrange-table"
                            :items="getItem()"
                            :fields="arrange_fields"
                            :responsive="true"
                            hover
                            striped
                        >
                            <template
                                #cell(room_number)="data"
                            >
                                <b-form-checkbox-group
                                    v-model="room_numbers[getIndex(data.item.type)]"
                                    :options="getAvailableOptions(data.item.room_number)"
                                    class="mb-3"
                                    :disabled="onDisable(room_numbers[getIndex(data.item.type)], data.item.amount)"
                                ></b-form-checkbox-group>
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
                            {{ $t('booking.bookingForm.submit') }}
                        </button>
                    </div>
                    <div
                        v-if="showTableAfter()"
                    >
                        <b-table
                            id="booking-table"
                            :items="testDetails()"
                            :fields="fields"
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
                            <!--                            <template-->
                            <!--                                #cell(room_number)="data"-->
                            <!--                            >-->
                            <!--                                <ul style="padding: 0; list-style-type: none">-->
                            <!--                                    <li-->
                            <!--                                        v-for="(number, index) in data.item.room_number"-->
                            <!--                                        :key="`${data.item.uuid}-number-${index}`"-->
                            <!--                                        class="number"-->
                            <!--                                    >-->
                            <!--                                        {{ number }}-->
                            <!--                                    </li>-->
                            <!--                                </ul>-->
                            <!--                            </template>-->
                        </b-table>
                    </div>
                    <!--                    <div-->
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
    </layout>
</template>

<script>
import Layout from "@/components/layouts/Layout";
import {faHotel, faMoneyBill} from '@fortawesome/free-solid-svg-icons'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faAddressBook, faCalendar, faMoneyBillAlt} from '@fortawesome/free-regular-svg-icons'
import formMixin from '@/mixin/form-mixin'
import booking from "../../store/modules/booking/booking";
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
        // const created = localStorage.getItem("created")
        // const userId = localStorage.getItem("userId")
        const bookingId = localStorage.getItem("bookingId")
        const types = this.$store.getters['booking/types']
        let room_numbers = []
        for (let i = 0; i < types.length; i++) {
            room_numbers.push([])
        }
        return {
            types: [],
            booking_types: [],
            booking: this.$store.getters['booking/bookings'].filter(booking => (booking.uuid === bookingId))[0],
            room_numbers: room_numbers,
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
                // {
                //     key: 'room_number',
                //     label: this.$t('booking.bookingForm.roomNumber'),
                // }
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
        onDisable: function (room_numbers, amount) {
            const temp1 = room_numbers
            const temp2 = amount
            // return room_numbers.length >= amount
            return false
        },
        onHandle: function (checked, amount) {
            const temp = checked
            const number = amount
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
                'amount': this.booking_types[i].amount})
            }
            return temp
        },
        testDetails: function () {
            const types = this.booking.roomType
            // const numbers = this.booking.roomNumber
            let unique_types = types.filter(this.onlyUnique)
            let temp = []
            for (let j = 0; j < unique_types.length; j++) {
                let count = 0
                for (let i = 0; i < types.length; i++) {
                    if (types[i] === unique_types[j]) {
                        count += 1
                    }
                }
                // let room_numbers = []
                // for (let i = 0; i < numbers.length; i++) {
                //     if (types[i] === unique_types[j]) {
                //         room_numbers.push(numbers[i])
                //     }
                // }
                let capacity = 0
                let price = 0
                let amenities = []
                for (let option in this.types) {
                    if (this.types[option].roomType === unique_types[j]) {
                        capacity = this.types[option].capacity
                        price = this.types[option].price
                        amenities = this.types[option].amenities
                        break
                    }
                }
                temp.push({
                    'type': unique_types[j], 'amount': count, 'capacity': capacity, 'price': price,
                    'amenities': amenities
                })
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
            let check = true
            for (let i = 0; i < this.booking_types.length; i++) {
                if (this.room_numbers[i].length > this.booking_types[i].amount) {
                    check = false
                    break
                }
            }
            if (check === false) {
                this.makeToast(this.$t('booking.booking.errors.title'), this.$t('booking.booking.errors.exceptionOccurred'))
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
    display: inline;
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
    float: left;
    padding: 0 10px;
    margin-bottom: 5px;
}
li.number:nth-child(odd) {clear: left}
</style>