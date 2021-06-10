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
                    <div>
                        <span class="font-weight-bolder">
                            {{ $t('hotel.hotel.amenities') }}
                        </span>
                        <div class="test">
                            <ul
                                style="padding: 0; list-style-type: none"
                            >
                                <li
                                    v-for="(amenity, index) in hotel.amenities"
                                    :key="`${hotel.uuid}-amenity-${index}`"
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
                    </div>
                    <p>
                        <span class="font-weight-bolder">
                            {{ $t('hotel.hotel.ownerName') }}
                        </span>
                        <span>
                            {{ hotel.ownerName }}
                        </span>
                    </p>
                    <!--                    <p>-->
                    <!--                        <img-->
                    <!--                            src="../../assets/phone.png"-->
                    <!--                            alt="phone"-->
                    <!--                            class="icon"-->
                    <!--                            style="height:20px; width:20px"-->
                    <!--                        >-->
                    <!--                        <span>-->
                    <!--                            {{ hotel.ownerTel }}-->
                    <!--                        </span>-->
                    <!--                        - -->
                    <!--                        <img-->
                    <!--                            src="../../assets/email.png"-->
                    <!--                            alt="email"-->
                    <!--                            class="icon"-->
                    <!--                            style="height:20px; width:20px"-->
                    <!--                        >-->
                    <!--                        <span>-->
                    <!--                            {{ hotel.ownerEmail }}-->
                    <!--                        </span>-->
                    <!--                    </p>-->
                    <p>
                        <span class="font-weight-bolder">
                            {{ $t('hotel.hotel.contact') }}
                        </span>
                        <img
                            src="../../assets/phone.png"
                            alt="phone"
                            class="icon"
                            style="height:20px; width:20px"
                        >
                        <span>
                            {{ hotel.tel }}
                        </span>
                        -
                        <img
                            src="../../assets/email.png"
                            alt="email"
                            class="icon"
                            style="height:20px; width:20px"
                        >
                        <span>
                            {{ hotel.email }}
                        </span>
                    </p>
                    <div class="mt-2">
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
import dataUtil from "@/utils/data-view-utils"
import {validationMixin} from "vuelidate";

export default {
    name: "HotelApproveDetail",
    components: {Layout, ApproveForm},
    mixins: [validationMixin, dataUtil],
    data: function () {
        return {
            updateForm: {
                status: null
            },
            hotel: this.$store.getters['hotel/hotels'].filter(hotel => hotel.uuid === this.$route.params.uuid)[0],
        }
    },
    methods: {
        getAddress: function (address, ward, district, city) {
            return this.getTransAddress(address, ward, district, city)
        },
        hotelImage: function (uri) {
            return this.getHotelImage(uri)
        },
        getSrc: function (amenity) {
            return this.getImgSrc(amenity)
        },
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


.test ul {
    display: flex;
    flex-wrap: wrap;
    padding-left: 0;
}
.test ul li {
    list-style: none;
    flex: 0 0 20%;
}

</style>