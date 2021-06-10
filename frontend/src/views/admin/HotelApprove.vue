<template>
    <layout>
        <template #content>
            <div class="align-items-center d-flex">
                <h2 class="flex-grow-1">
                    {{ $t('hotel.hotel.searchHotel') }}
                </h2>
            </div>
            <br>
            <b-form>
                <b-form-group
                    id="name-group"
                    :label="$t('hotel.hotelForm.name')"
                    label-for="name"
                    label-cols-sm="2"
                    label-cols-lg="2"
                    content-cols-sm="4"
                    content-cols-lg="4"
                >
                    <b-form-input
                        v-model="$v.form.name.$model"
                        :placeholder="$t('hotel.hotelForm.namePlaceholder')"
                        list="name-list-id"
                        type="search"
                    />
                    <datalist id="name-list-id">
                        <option
                            v-for="hotel in hotels"
                            :key="hotel.uuid"
                        >
                            {{ hotel.name }}
                        </option>
                    </datalist>
                </b-form-group>
            </b-form>
            <div>
                <b-button
                    v-b-toggle.collapse-1
                    variant="secondary"
                    class="btn-sm"
                >
                    {{ $t('hotel.hotel.advancedSearch') }}
                </b-button>
                <button
                    class="btn btn-sm btn-primary"
                    type="button"
                    style="float: right; margin-right: 550px"
                    @click="onSubmit"
                >
                    {{ $t('hotel.hotel.searchBtn') }}
                    <font-awesome-icon
                        :icon="['fas', 'search']"
                    />
                </button>
                <b-collapse
                    id="collapse-1"
                    class="mt-2"
                >
                    <b-card>
                        <b-form>
                            <b-form-group
                                id="star-group"
                                :label="$t('hotel.hotelForm.star')"
                                label-for="star"
                                label-cols-sm="2"
                                label-cols-lg="2"
                                content-cols-sm="4"
                                content-cols-lg="4"
                            >
                                <b-form-rating
                                    v-model="$v.form.star.$model"
                                    variant="warning"
                                    size="sm"
                                    inline
                                    no-border
                                />
                            </b-form-group>
                            <b-form-group
                                id="city-group"
                                :label="$t('hotel.hotelForm.city')"
                                label-for="city"
                                label-cols-sm="2"
                                label-cols-lg="2"
                                content-cols-sm="4"
                                content-cols-lg="4"
                            >
                                <b-form-select
                                    id="city"
                                    v-model="$v.form.city.$model"
                                    :options="cities"
                                    @change="onChangeCity"
                                />
                            </b-form-group>
                            <b-form-group
                                id="district-group"
                                :label="$t('hotel.hotelForm.district')"
                                label-for="district"
                                label-cols-sm="2"
                                label-cols-lg="2"
                                content-cols-sm="4"
                                content-cols-lg="4"
                            >
                                <b-form-select
                                    id="district"
                                    v-model="$v.form.district.$model"
                                    :options="districts"
                                    @change="onChangeDistrict"
                                />
                            </b-form-group>
                            <b-form-group
                                id="ward-group"
                                :label="$t('hotel.hotelForm.ward')"
                                label-for="ward"
                                label-cols-sm="2"
                                label-cols-lg="2"
                                content-cols-sm="4"
                                content-cols-lg="4"
                            >
                                <b-form-select
                                    id="ward"
                                    v-model="$v.form.ward.$model"
                                    :options="wards"
                                />
                            </b-form-group>
                        </b-form>
                    </b-card>
                </b-collapse>
            </div>
            <br>
            <hr>
            <div class="align-items-center d-flex">
                <h2 class="flex-grow-1">
                    {{ $t('hotel.hotel.approveLabel') }}
                </h2>
            </div>
            <br>
            <div
                v-if="loading"
                class="loader"
            />
            <div
                id="hotels-list"
                :current-page="currentPage"
                :per-page="perPage"
                class="row"
            >
                <div
                    v-for="hotel in filterHotels.slice((currentPage-1)*perPage, (currentPage-1)*perPage+perPage)"
                    :key="hotel.uuid"
                    class="col-md-6 col-sm-12"
                    @dblclick="$router.push({name: 'adminHotelDetail', params: {uuid: hotel.uuid}})"
                >
                    <!--    Hotel info                -->
                    <b-card
                        img-top
                        class="mb-2 p-1"
                        tag="article"
                    >
                        <b-card-img
                            :src="hotelImage(hotel.image)"
                            class="mb-2"
                            style="height: 300px"
                        />
                        <b-card-title
                            :title="hotel.name"
                            title-tag="h2"
                            class="p-inline"
                        />
                        <p class="p-inline">
                            <b-form-rating
                                v-model="hotel.star"
                                variant="warning"
                                no-border
                                inline
                                readonly
                            />
                        </p>
                        <p
                            style="height: 48px; margin-bottom: 0"
                        >
                            <span class="font-weight-bolder">
                                {{ $t('hotel.hotel.address') }}
                            </span>
                            <span class="text-secondary">
                                {{ getAddress(hotel.address, hotel.ward, hotel.district, hotel.city) }}
                            </span>
                        </p>
                        <p>
                            <span class="font-weight-bolder">
                                {{ $t('hotel.hotel.ownerName') }}
                            </span>
                            <span class="text-secondary">
                                {{ hotel.ownerName }}
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
                    </b-card>
                </div>
            </div>
            <span
                v-if="filterHotels.length === 0 && isSearch"
                style="font-style: italic"
            >
                {{ $t('hotel.hotel.noResult') }}
            </span>
            <b-pagination
                v-if="filterHotels.length > perPage"
                v-model="currentPage"
                :per-page="perPage"
                :total-rows="rows"
                pills
                aria-controls="hotels-list"
            />
        </template>
    </layout>
</template>

<script>
import Layout from '@/components/layouts/Layout';
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin'
import addressMixin from '@/mixin/address-mixin'
import {getDistrictsByProvinceCode, getWardsByDistrictCode, getProvinces} from 'sub-vn';
import {library} from '@fortawesome/fontawesome-svg-core'
import {faSearch} from '@fortawesome/free-solid-svg-icons'
import json from '../../mixin/data/db_en.json'
import Pusher from 'pusher-js'
import ApproveForm from "@/views/admin/ApproveForm";
import camelcaseKeys from "camelcase-keys";
import dataUtil from "@/utils/data-view-utils"

library.add(faSearch)

export default {
    name: "HotelApprove",
    components: {Layout, ApproveForm},
    mixins: [validationMixin, formMixin, addressMixin, dataUtil],
    data: function () {
        return {
            // Amenities options
            options: ['fitness center', 'breakfast', 'free parking', 'swimming pool', 'bar', 'spa',
                'room service', 'non smoking icon'],
            // Hotel data
            hotels: [],
            // Hotel data for search form
            filterHotels: [],
            // Pagination data
            currentPage: 1,
            perPage: 6,
            rows: 0,
            // Search form data
            form: {
                name: null,
                amenities: [],
                city: null,
                district: null,
                ward: null,
                star: null
            },
            updateForm: {
                status: null
            },
            slide: 0,
            sliding: null,
            isSearch: false,
            loading: false
        }
    },
    computed: {
        availableOptions() {
            return this.options.filter(opt => this.form.amenities.indexOf(opt) === -1)
        },
    },
    validations: {
        form: {
            name: {

            },
            amenities: {

            },
            city: {

            },
            district: {

            },
            ward: {

            },
            star: {

            }
        }
    },
    created() {
        this.loading = true
        this.$store.dispatch('hotel/listHotels').then(() => {
            this.hotels = this.$store.getters['hotel/hotels']
            this.filterHotels = this.hotels
            this.rows = this.filterHotels.length
            this.filterHotels.sort(function (a,b) {
                return new Date(b.created) - new Date(a.created)
            })
            this.loading = false
            this.subscribe()
        })
    },
    methods: {
        getAddress: function (address, ward, district, city) {
            return this.getTransAddress(address, ward, district, city)
        },
        // Get hotel image
        hotelImage: function (uri) {
            return this.getHotelImage(uri)
        },
        getSrc: function (amenity) {
            return this.getImgSrc(amenity)
        },

        // Handle search function
        onSubmit: function () {
            this.filterHotels = this.hotels
            // Filter by name city district ward and amenities
            if (!!this.form.name) {
                this.filterHotels = this.filterHotels.filter(hotel =>
                    hotel.name.toLowerCase().indexOf(this.form.name.toLowerCase()) > -1
                )
            }
            if (!!this.form.city) {
                this.filterHotels = this.filterHotels.filter(hotel =>
                    hotel.city === getProvinces().filter(option => option.code === this.form.city)[0].name
                )
            }
            if (!!this.form.district) {
                this.filterHotels = this.filterHotels.filter(hotel =>
                    hotel.district === getDistrictsByProvinceCode(this.form.city).filter(option => option.code === this.form.district)[0].name
                )
            }
            if (!!this.form.ward) {
                this.filterHotels = this.filterHotels.filter(hotel =>
                    hotel.ward === getWardsByDistrictCode(this.form.district).filter(option => option.code === this.form.ward)[0].name
                )
            }
            if (!!this.form.amenities) {
                const amenities_list = this.form.amenities.map(amenity => amenity.toLowerCase())
                this.filterHotels = this.filterHotels.filter(hotel =>
                    amenities_list.every(amenity => hotel.amenities.includes(amenity))
                )
            }
            if (!!this.form.star) {
                this.filterHotels = this.filterHotels.filter(hotel =>
                    hotel.star === this.form.star
                )
            }
            this.form.star = null
            this.rows = this.filterHotels.length
            if (this.filterHotels.length === 0) {
                this.makeToast(this.$t('hotel.hotel.errors.search'), this.$t('hotel.hotel.noResult'))
                this.isSearch = true
            }
        },
        compare: function (a,b) {
            if (a.name < b.name) {
                return -1;
            }
            if (a.name > b.name) {
                return  1;
            }
            return 0;
        },
        subscribe() {
            let pusher = new Pusher('5d873d3e35474aa76004', {
                cluster: 'ap1'
            });
            pusher.subscribe('a_channel');
            pusher.bind('an_event', data => {
                data = camelcaseKeys(data, {deep: true})
                this.$store.commit('hotel/saveHotel', data)
            })
        }
    },
}
</script>

<style
    lang="scss"
    scoped
>
.card-img {
    object-fit: cover;
}
.required:before {
    content: " *";
    color: red;
}
.p-inline {
    display: inline-block;
}
.badge-size {
    font-size: 1em;
}
.icon {
    height: 30px;
    width: 30px;
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