<template>
    <layout>
        <template #content>
            <div>
                <b-form>
                    <h3 class="p-inline">
                        <span class="font-weight-bolder">
                            {{ hotel.name }}
                        </span>
                    </h3>
                    <p class="p-inline">
                        <b-form-rating
                            :value="hotel.star"
                            variant="warning"
                            no-border
                            inline
                            readonly
                        />
                    </p>
                    <b-form-group
                        id="image-group"
                        label=""
                        label-for="image"
                    >
                        <b-card-img
                            :src="hotelImage(hotel.image)"
                        />
                    </b-form-group>
                    <p>
                        <span class="font-weight-bolder">
                            {{ $t('hotel.hotel.address') }}
                        </span>
                        <span>
                            {{ getAddress(hotel.address, hotel.ward, hotel.district, hotel.city) }}
                        </span>
                    </p>
                    <p>
                        <span class="font-weight-bolder">
                            {{ $t('hotel.hotel.amenities') }}
                        </span>
                        <b-list-group horizontal="md">
                            <b-list-group-item
                                v-for="(amenity, index) in hotel.amenities"
                                :key="`${hotel.uuid}-amenity-${index}`"
                                style="margin: 5px; border: none"
                            >
                                <img
                                    :src="getSrc(amenity)"
                                    :alt="amenity"
                                    class="icon"
                                >
                                {{ amenity }}
                            </b-list-group-item>
                        </b-list-group>
                    </p>
                    <p>
                        <span class="font-weight-bolder">
                            {{ $t('hotel.hotel.ownerName') }}
                        </span>
                        <span>
                            {{ hotel.ownerName }}
                        </span>
                    </p>
                    <p>
                        <!--                        <span class="font-weight-bolder">-->
                        <!--                            {{ $t('hotel.hotel.ownerTel') }}-->
                        <!--                        </span>-->
                        <img
                            src="../../assets/phone.png"
                            alt="phone"
                            class="icon"
                            style="height:20px; width:20px"
                        >
                        <span>
                            {{ hotel.ownerTel }}
                        </span>
                        -
                        <!--                        <span class="font-weight-bolder">-->
                        <!--                            {{ $t('hotel.hotel.ownerEmail') }}-->
                        <!--                        </span>-->
                        <img
                            src="../../assets/email.png"
                            alt="email"
                            class="icon"
                            style="height:20px; width:20px"
                        >
                        <span>
                            {{ hotel.ownerEmail }}
                        </span>
                    </p>
                    <div class="mt-2">
                        <!--                        <b-button-->
                        <!--                            :disabled="hotel.isActive === true"-->
                        <!--                            variant="success"-->
                        <!--                            href="#"-->
                        <!--                            size="sm"-->
                        <!--                            @click="$bvModal.show(`modal-${hotel.uuid}-approve`)"-->
                        <!--                        >-->
                        <!--                            {{ $t('hotel.hotel.approveBtn') }}-->
                        <!--                        </b-button>-->
                        <b-button
                            :disabled="hotel.status === 'active'"
                            variant="success"
                            href="#"
                            size="sm"
                            @click="$bvModal.show(`modal-${hotel.uuid}-approve`)"
                        >
                            {{ $t('hotel.hotel.approveBtn') }}
                        </b-button>
                    </div>
                    <b-modal
                        :id="`modal-${hotel.uuid}-approve`"
                        :title="$t('hotel.hotel.approveTitle')"
                        size="lg"
                        hide-footer
                    >
                        <approve-form :hotel="hotel" />
                    </b-modal>
                </b-form>
                <hr>
                <br>
            </div>
        </template>
    </layout>
</template>

<script>
import Layout from "@/components/layouts/Layout";
import json from '../../mixin/data/db_en.json'
import {getDistrictsByProvinceCode, getWardsByDistrictCode, getProvinces} from 'sub-vn';
import ApproveForm from "@/views/admin/ApproveForm";

export default {
    name: "FormDetail",
    components: {Layout, ApproveForm},
    // props: {
    //     // Hotel data
    //     hotel: {
    //         type: Object,
    //         default: () => {
    //             return null
    //         }
    //     }
    // },
    data: function () {
        return {
            updateForm: {
                // is_active: null,
                status: null
            },
            hotel: this.$store.getters['hotel/hotels'].filter(hotel => hotel.uuid === this.$route.params.uuid)[0],
        }
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
        getSrc: function (amenity) {
            let images = require.context('../../assets/', false, /\.png$/)
            return images('./' + amenity + ".png")
        },
        // approveHotel: function (uuid) {
        //     this.$store.dispatch('hotel/resetStatus')
        //     // this.updateForm.is_active = true
        //     this.updateForm.status = "active"
        //     this.updateForm.uuid = uuid
        //     this.$store.dispatch('hotel/approveHotel', this.updateForm).then(() => {
        //         if (this.$store.getters['hotel/status'] === 'FAILED') {
        //             // Alert for failed api calls
        //             this.makeToast(this.$t('hotel.hotel.errors.approveTitle'), this.$t('hotel.hotel.errors.exceptionOccurred'))
        //         } else {
        //             // window.location.reload()
        //             // this.$router.push('/admin/hotels')
        //             this.$bvToast.toast(this.$t('hotel.hotel.success.approveMessage'), {
        //                 title: this.$t('hotel.hotel.success.approveTitle'),
        //                 autoHideDelay: 2000,
        //                 variant: 'success'
        //             })
        //             setTimeout(() => this.$router.push('/admin/hotels'), 2000)
        //         }
        //     })
        // },
        // // Handle delete hotel
        // rejectHotel: function (uuid) {
        //     this.$store.dispatch('hotel/resetStatus')
        //     this.$store.dispatch('hotel/deleteHotel', uuid)
        //         .then(() => {
        //             if (this.$store.getters['hotel/status'] === 'FAILED') {
        //                 // Alert for failed api call
        //                 this.makeToast(this.$t('hotel.hotel.errors.rejectTitle'), this.$t('hotel.hotel.errors.exceptionOccurred'))
        //             } else {
        //                 this.$bvToast.toast(this.$t('hotel.hotel.success.rejectMessage'), {
        //                     title: this.$t('hotel.hotel.success.rejectTitle'),
        //                     autoHideDelay: 2000,
        //                     variant: 'success'
        //                 })
        //                 setTimeout(() => this.$router.push('/admin/hotels'), 2000)
        //             }
        //         })
        // },
    }
}
</script>

<style
    lang="scss"
    scoped
>
.card-img {
    height: 50%;
    width: 50%;
    object-fit: cover;
}
.icon {
    height: 30px;
    width: 30px;
}
.p-inline {
    display: inline-block;
}
</style>