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
                        <b-img
                            :src="hotelImage(booking.image)"
                            style="float: right"
                            alt="image"
                            thumbnail
                            fluid
                        />
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
                            <span class="font-weight-bolder">
                                {{ $t('booking.booking.totalPrice') }}: {{ totalPrice() }} VND
                            </span>
                            ({{ $t('booking.booking.description') }})
                        </div>
                    </div>
                    <br>
                    <br>
                    <div>
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
                                <div class="test">
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
                                </div>
                            </template>
                            <template
                                #cell(amount)="data"
                            >
                                {{ data.item.amount }} {{ $tc('hotel.hotel.room', data.item.amount) }}
                            </template>
                        </b-table>
                    </div>
                </b-form>
            </div>
        </template>
    </Layout>
</template>

<script>
import {faHotel, faMoneyBill} from '@fortawesome/free-solid-svg-icons'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faAddressBook, faCalendar, faMoneyBillAlt} from '@fortawesome/free-regular-svg-icons'
import Layout from "@/components/layouts/Layout";
import dataUtil from "@/utils/data-view-utils"
import {validationMixin} from "vuelidate";

library.add(faHotel)
library.add(faCalendar)
library.add(faAddressBook)
library.add(faMoneyBillAlt)

export default {
    name: "BookingDetail",
    components: {Layout},
    mixins: [validationMixin, dataUtil],
    data: function () {
        return {
            types: [],
            booking: this.$store.getters['booking/bookings'].filter(booking => booking.uuid === this.$route.params.uuid)[0],
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
                    key: 'amenities',
                    label: this.$t('booking.bookingForm.amenities'),
                    thStyle: {width: '400px'}
                },
                {
                    key: 'amount',
                    label: this.$t('booking.bookingForm.rooms'),
                },
            ]
        }
    },
    created() {
        this.$store.dispatch('type/listTypes', this.booking.hotelid)
            .then(() => {
                this.types = this.$store.getters['type/types']
            })
    },
    methods: {
        getAddress: function (address, ward, district, city) {
            return this.getTransAddress(address, ward, district, city)
        },
        getSrc: function (amenity) {
            return this.getImgSrc(amenity)
        },
        hotelImage: function (uri) {
            return this.getHotelImage(uri)
        },
        toDate: function(datetime) {
            let date = new Date(datetime);
            return date.getDate() + "-" + (date.getMonth() + 1) + "-" + date.getFullYear();
        },
        testDetails: function() {
            const types = this.booking.roomType
            const amounts = this.booking.roomAmount
            let temp = []
            for (let j=0; j<types.length; j++) {

                let count = amounts[j]
                let price = 0
                let amenities = []
                for (let i=0; i< this.types.length; i++) {
                    if (this.types[i].name === types[j]) {
                        price = this.types[i].price
                        amenities = this.types[i].amenities
                        break
                    }
                }
                temp.push({'type' : types[j], 'amount': count, 'price': price, 'amenities': amenities})
            }
            return temp
        },
        totalPrice: function () {
            // let total_price = 0
            // const prices = this.booking.price
            //
            // for (let i=0; i< prices.length; i++) {
            //     total_price += prices[i]
            // }
            let total_price = this.booking.totalPrice
            return this.formatPrice(total_price)
        },
        formatPrice(price) {
            return this.getFormatPrice(price)
        },
        deleteBooking: function(uuid) {
            this.$store.dispatch('booking/resetStatus')
            this.$store.dispatch('booking/newDeleteBooking', uuid)
                .then(() => {
                    if (this.$store.getters['booking/status'] === 'FAILED') {
                        // Alert for failed api call
                        this.makeToast(this.$t('booking.booking.errors.title'), this.$t('booking.booking.errors.exceptionOccurred'))
                    } else {
                        this.$bvToast.toast(this.$t('booking.booking.success.deleteMessage'), {
                            title: this.$t('booking.booking.success.deleteTitle'),
                            autoHideDelay: 2000,
                            variant: 'success'
                        })
                        setTimeout(() => this.$router.push('/bookings'), 2000)
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

.test ul {
    display: flex;
    flex-wrap: wrap;
    padding-left: 0;
}
.test ul li {
    list-style: none;
    flex: 0 0 33.333333%;
}
</style>