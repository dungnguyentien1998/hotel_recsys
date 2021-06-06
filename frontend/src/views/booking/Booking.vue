<template>
    <Layout>
        <template #content>
            <div class="align-items-center d-flex">
                <h2 class="flex-grow-1">
                    {{ $t('booking.booking.title') }}
                </h2>
            </div>
            <hr>
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
import json from '../../mixin/data/db_en.json'
import {getDistrictsByProvinceCode, getWardsByDistrictCode, getProvinces} from 'sub-vn';

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
            currentPage: 1,
            perPage: 10,
            rows: 0,
        }
    },
    created() {
        this.$store.dispatch('booking/newListBookings')
            .then(() => {
                this.bookings = this.$store.getters['booking/bookings']
                this.rows = this.bookings.length
                this.bookings.sort(function (a,b) {
                    return new Date(b.created) - new Date(a.created)
                })
            })
    },
    methods: {
        getAddress: function (address, ward, district, city) {
            let city_en = city
            let district_en = district
            let ward_en = ward
            if (localStorage.getItem("language") === "en") {
                let city_code = getProvinces().filter(option => option.name === city)[0].code
                const provinces = json.province
                city_en = provinces.filter(option => option.idProvince === city_code)[0].name
                let district_code = getDistrictsByProvinceCode(city_code).filter(option => option.name === district)[0].code
                const dists = json.district
                district_en = dists.filter(option => option.idDistrict === district_code)[0].name
                let ward_code = getWardsByDistrictCode(district_code).filter(option => option.name === ward)[0].code
                const communes = json.commune
                ward_en = communes.filter(option => option.idCoummune === ward_code)[0].name
            }
            if (address == null || address === "") {
                return ward_en + ", " + district_en + ", " + city_en
            } else {
                return address + ", " + ward_en + ", " + district_en + ", " + city_en
            }
            // if (address == null || address === "") {
            //     return ward + ", " + district + ", " + city
            // } else {
            //     return address + ", " + ward + ", " + district + ", " + city
            // }
        },
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