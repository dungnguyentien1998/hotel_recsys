<template>
    <layout>
        <template #content>
            <div class="align-items-center d-flex">
                <h2 class="flex-grow-1">
                    {{ roleUser ? $t('hotel.hotel.searchHotel') : $t('hotel.hotel.myHotel') }}
                </h2>
                <b-button
                    v-if="roleHotelier"
                    variant="success"
                    size="sm"
                    @click="$bvModal.show('modal-create')"
                >
                    {{ $t('hotel.hotel.createBtn') }}
                </b-button>
            </div>
            <br>
            <b-form
                v-if="roleUser"
            >
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
                            v-for="(name, index) in names"
                            :key="`${name}-${index}`"
                        >
                            {{ name }}
                        </option>
                    </datalist>
                </b-form-group>
            </b-form>
            <div
                v-if="roleUser"
            >
                <b-button
                    v-b-toggle.collapse-1
                    variant="secondary"
                    class="btn-sm"
                >
                    {{ $t('hotel.hotel.advancedSearch') }}
                </b-button>
                <button
                    v-if="roleUser"
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
                                    show-clear
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
                    {{ roleUser ? $t('hotel.hotel.title') : '' }}
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
                    v-for="hotel in filterHotels"
                    :key="hotel.uuid"
                    class="col-md-6 col-sm-12"
                    @dblclick="onHandle(hotel.uuid)"
                >
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
                        <p>
                            <span class="font-weight-bolder">
                                {{ $t('hotel.hotel.rating') }}:
                            </span>
                            <b-badge
                                pill
                                variant="info"
                                class="badge-size"
                            >
                                {{ hotel.rating }} / 5
                            </b-badge>
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
                        <!--                        <b-badge-->
                        <!--                            v-if="roleHotelier"-->
                        <!--                            variant="primary"-->
                        <!--                        >-->
                        <!--                            {{ hotel.numNewBookings }} {{ $tc('hotel.hotel.new_bookings', hotel.numNewBookings) }}-->
                        <!--                        </b-badge>-->
                        <!--                        <b-badge-->
                        <!--                            v-if="roleHotelier"-->
                        <!--                            class="mx-2"-->
                        <!--                            variant="success"-->
                        <!--                        >-->
                        <!--                            {{ hotel.numReviews }} {{ $tc('hotel.hotel.review', hotel.numReviews) }}-->
                        <!--                        </b-badge>-->
                        <!--                        <b-badge-->
                        <!--                            v-if="roleHotelier"-->
                        <!--                            variant="danger"-->
                        <!--                        >-->
                        <!--                            {{ hotel.numComplaints }} {{ $tc('hotel.hotel.complaint', hotel.numComplaints) }}-->
                        <!--                        </b-badge>-->
                        <div class="mt-2">
                            <b-button
                                v-if="roleHotelier"
                                variant="primary"
                                href="#"
                                size="sm"
                                style="width: 90px"
                                @click="$bvModal.show(`modal-${hotel.uuid}-update`)"
                            >
                                {{ $t('hotel.hotel.updateBtn') }}
                            </b-button>
                            <b-button
                                v-if="roleHotelier"
                                class="ml-2"
                                variant="danger"
                                href="#"
                                size="sm"
                                style="width: 90px"
                                @click="$bvModal.show(`modal-${hotel.uuid}-delete`)"
                            >
                                {{ $t('hotel.hotel.deleteBtn') }}
                            </b-button>
                        </div>
                        <b-modal
                            :id="`modal-${hotel.uuid}-update`"
                            :title="$t('hotel.hotel.updateTitle')"
                            size="lg"
                            hide-footer
                        >
                            <hotel-form :hotel="hotel" />
                        </b-modal>
                        <b-modal
                            :id="`modal-${hotel.uuid}-delete`"
                            :title="$t('hotel.hotel.deleteTitle')"
                            size="lg"
                            button-size="sm"
                            :ok-title="$t('button.submit')"
                            :cancel-title="$t('button.unsubmit')"
                            @ok="deleteHotel(hotel.uuid)"
                        >
                            {{ $t('hotel.hotel.confirmDelete') }}
                        </b-modal>
                    </b-card>
                </div>
            </div>
            <span
                v-if="filterHotels.length === 0 && roleHotelier && !loading"
                style="font-style: italic"
            >
                {{ $t('hotel.hotel.noHotel') }}
            </span>
            <span
                v-if="filterHotels.length === 0 && !roleHotelier && isSearch"
                style="font-style: italic"
            >
                {{ $t('hotel.hotel.noResult') }}
            </span>
            <b-pagination
                v-if="rows > perPage"
                v-model="currentPage"
                :per-page="perPage"
                :total-rows="rows"
                pills
                aria-controls="hotels-list"
                @change="handlePageChange"
            />
            <hr
                v-if="roleUser"
            >
            <div
                v-if="roleUser"
                class="align-items-center d-flex"
            >
                <h2 class="flex-grow-1">
                    {{ (recommendationsLogin.length > 0) ? $t('hotel.hotel.recommended') : '' }}
                </h2>
            </div>
            <br>
            <div
                v-if="roleUser"
                class="row"
            >
                <div
                    v-for="recommendation in recommendationsLogin"
                    :key="recommendation.uuid"
                    class="col-md-4 col-sm-10"
                    @dblclick="$router.push({name: 'createFavorite', params: {uuid: recommendation.uuid}})"
                >
                    <b-card
                        img-top
                        class="mb-2 p-1"
                        tag="article"
                        style="height: 505px"
                    >
                        <b-card-img
                            :src="hotelImage(recommendation.image)"
                            class="mb-2"
                            :height="200"
                            :width="200"
                        />
                        <b-card-title
                            :title="recommendation.name"
                            title-tag="h2"
                            class="p-inline"
                        />
                        <p>
                            <b-form-rating
                                v-model="recommendation.star"
                                variant="warning"
                                no-border
                                inline
                                readonly
                            />
                        </p>
                        <p>
                            <span class="font-weight-bolder">
                                {{ $t('hotel.hotel.rating') }}:
                            </span>
                            <b-badge
                                pill
                                variant="info"
                                class="badge-size"
                            >
                                {{ recommendation.rating }} / 5
                            </b-badge>
                        </p>
                        <p>
                            <span class="font-weight-bolder">
                                {{ $t('hotel.hotel.address') }}
                            </span>
                            <span class="text-secondary">
                                {{ getAddress(recommendation.address, recommendation.ward, recommendation.district, recommendation.city) }}
                            </span>
                        </p>
                    </b-card>
                </div>
            </div>
            <b-modal
                id="modal-create"
                :title="$t('hotel.hotel.createTitle')"
                size="lg"
                hide-footer
            >
                <hotel-form />
            </b-modal>
        </template>
    </layout>
</template>

<script>
import Layout from '@/components/layouts/Layout';
import HotelForm from '@/components/HotelForm';
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin'
import addressMixin from '@/mixin/address-mixin'
import {getDistrictsByProvinceCode, getWardsByDistrictCode, getProvinces} from 'sub-vn';
import {Carousel, Slide} from 'vue-carousel'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faSearch} from '@fortawesome/free-solid-svg-icons'
import json from '../../mixin/trans/db_en.json'
import Pusher from "pusher-js";
import camelcaseKeys from "camelcase-keys";
import roleUtil from "@/utils/role-utils"
import dataUtil from "@/utils/data-view-utils"

library.add(faSearch)

export default {
    name: "Hotel",
    components: {HotelForm, Layout},
    mixins: [validationMixin, formMixin, addressMixin, roleUtil, dataUtil],
    data: function () {
        return {
            // Amenities options
            options: ['fitness center', 'breakfast', 'free parking', 'swimming pool', 'bar', 'spa',
                'room service', 'non smoking room'],
            hotels: [],
            filterHotels: [],

            currentPage: this.$store.getters['hotel/page'],
            perPage: 6,
            rows: 0,
            recommendationsLogin: [],
            form: {
                name: this.$store.getters['hotel/name'],
                amenities: [],
                city: this.$store.getters['hotel/city'],
                district: this.$store.getters['hotel/district'],
                ward: this.$store.getters['hotel/ward'],
                star: this.$store.getters['hotel/star']
            },
            slide: 0,
            sliding: null,
            isSearch: false,
            loading: false,
            names: [],
            uuids: []
        }
    },
    computed: {
        availableOptions() {
            return this.options.filter(opt => this.form.amenities.indexOf(opt) === -1)
        },
        roleHotelier: function () {
            return this.getRoleHotelier()
        },
        roleUser: function () {
            return this.getRoleUser()
        },
    },
    // Form validation
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
        this.retrieveHotels()
        if (this.isSearch || this.$store.getters['hotel/is_search']) {
            const dists = json.district
            this.districts = [
                {value: null, text: '-----'},
                ...getDistrictsByProvinceCode(this.form.city).map(district => {
                    let trans_text = district.name
                    if (localStorage.getItem("language") === "en") {
                        let dist = dists.filter(option => option.idDistrict === district.code)[0]
                        if (dist) {
                            trans_text = dist.name
                        } else {
                            trans_text = ''
                        }
                        trans_text = dist.name
                    }
                    if (trans_text !== '') {
                        return {value: district.code, text: trans_text}
                    }
                }).filter(temp => temp !== undefined)
            ]
            const communes = json.commune
            this.wards = [
                {value: null, text: '-----'},
                ...getWardsByDistrictCode(this.form.district).map(ward => {
                    let trans_text = ward.name
                    if (localStorage.getItem("language") === "en") {
                        let commune = communes.filter(option => option.idCoummune === ward.code)[0]
                        if (commune) {
                            trans_text = commune.name
                        } else {
                            trans_text = ''
                        }
                    }
                    if (trans_text !== '') {
                        return {value: ward.code, text: trans_text}
                    }
                }).filter(temp => temp !== undefined)
            ]
        }
        if (this.$store.getters['user/user'].role === 'user') {
            this.$store.dispatch('recommendation/listRecommendationsLogin').then(() => {
                this.recommendationsLogin = this.$store.getters['recommendation/recommendationsLogin']
                this.recommendationsLogin.sort(this.compare)
            })
            this.$store.dispatch('hotel/listNames').then(() => {
                this.names = this.$store.getters['hotel/names']
                this.names.sort()
            })
        }
        this.$store.dispatch('hotel/notifyHotels')
            .then(() => {
                let count = this.$store.getters['hotel/notify_hotels'].length
                this.$store.commit('hotel/setOldHotelierCount', count)
                this.subscribe()
            })
        this.$store.dispatch('hotel/listUuids').then(() => {
            this.uuids = this.$store.getters['hotel/uuids']
        })
        // let user = this.$store.getters['user/user']
        // if (user.role === 'hotelier') {
        //     this.subscribe_review()
        //     this.subscribe_complaint()
        //     this.subscribe_booking()
        // }
        this.subscribe_user()
    },
    methods: {
        getRequestParams(currentPage, perPage, name, city, district, ward, star) {
            let params = []
            if (currentPage) {
                params["page"] = currentPage
                this.$store.commit('hotel/setPage', currentPage)
            } else {
                if (this.isSearch || this.$store.getters['hotel/is_search']) {
                    params["page"] = this.$store.getters['hotel/page']
                }
            }
            if (perPage) {
                params["per_page"] = perPage
            }
            if (name) {
                params["name"] = name
                this.$store.commit('hotel/setName', name)
            } else {
                this.$store.commit('hotel/setName', name)
                if (this.isSearch || this.$store.getters['hotel/is_search']) {
                    params["name"] = null
                }
            }
            if (city) {
                const city_name = getProvinces().filter(option => option.code === city)[0].name
                params["city"] = city_name
                this.$store.commit('hotel/setCity', city)
            } else {
                this.$store.commit('hotel/setCity', city)
                if (this.isSearch || this.$store.getters['hotel/is_search']) {
                    params["city"] = null
                }
            }
            if (district) {
                const district_name = getDistrictsByProvinceCode(city).filter(option => option.code === district)[0].name
                params["district"] = district_name
                this.$store.commit('hotel/setDistrict', district)
            } else {
                this.$store.commit('hotel/setDistrict', district)
                if (this.isSearch || this.$store.getters['hotel/is_search']) {
                    params["district"] = null
                }
            }
            if (ward) {
                const ward_name = getWardsByDistrictCode(district).filter(option => option.code === ward)[0].name
                params["ward"] = ward_name
                this.$store.commit('hotel/setWard', ward)
            } else {
                this.$store.commit('hotel/setWard', ward)
                if (this.isSearch || this.$store.getters['hotel/is_search']) {
                    params["ward"] = null
                }
            }
            if (star) {
                params["star"] = star
                this.$store.commit('hotel/setStar', star)
            } else {
                this.$store.commit('hotel/setStar', star)
                if (this.isSearch || this.$store.getters['hotel/is_search']) {
                    params["star"] = null
                }
            }
            return params
        },
        retrieveHotels() {
            const params = this.getRequestParams(this.currentPage, this.perPage, this.form.name, this.form.city,
                this.form.district, this.form.ward, this.form.star)
            this.loading = true
            this.$store.dispatch('hotel/listHotels', params).then(() => {
                this.hotels = this.$store.getters['hotel/hotels']
                this.filterHotels = this.hotels
                this.rows = this.$store.getters['hotel/count']
                this.loading = false
            })
        },
        handlePageChange(value) {
            this.currentPage = value
            this.retrieveHotels()
        },
        getAddress: function (address, ward, district, city) {
            return this.getTransAddress(address, ward, district, city)
        },
        // Get hotel image
        hotelImage: function (uri) {
            return this.getHotelImage(uri)
        },
        // Handle search function
        onSubmit: function () {
            this.isSearch = true
            this.$store.commit('hotel/setIsSearch', true)
            this.currentPage = 1
            this.retrieveHotels()
        },
        // Handle router based on role
        onHandle: function (uuid) {
            if (this.roleHotelier === true) {
                this.$router.push({name: 'detail', params: {uuid: uuid}})
            } else if (this.roleUser === true) {
                this.$router.push({name: 'createFavorite', params: {uuid: uuid}})
            }
        },
        // Handle delete hotel
        deleteHotel: function (uuid) {
            this.$store.dispatch('hotel/resetStatus')
            this.$store.dispatch('hotel/deleteHotel', uuid)
                .then(() => {
                    if (this.$store.getters['hotel/status'] === 'FAILED') {
                        // Alert for failed api call
                        this.makeToast(this.$t('hotel.hotel.errors.title'), this.$t('hotel.hotel.errors.exceptionOccurred'))
                    } else {
                        window.location.reload()
                    }
                })
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
            pusher.subscribe('a_channel_1');
            pusher.bind('an_event_1', data => {
                data = camelcaseKeys(data, {deep: true})
                let user_id = this.$store.getters['user/user'].uuid
                let owner_id = data.hotel.user
                if (user_id === owner_id) {
                    let new_uuid = data.hotel.uuid
                    let check = true
                    let notify_hotels = this.$store.getters['hotel/notify_hotels']
                    for (let i=0; i<notify_hotels.length; i++) {
                        let uuid = notify_hotels[i].uuid
                        if (uuid === new_uuid) {
                            check = false
                            break
                        }
                    }
                    if (check === true) {
                        this.$store.commit('hotel/saveNotifyHotel', data)
                    }
                    // this.$store.commit('hotel/saveNotifyHotel', data)
                    if (data.hotel.status === 'active') {
                        let new_uuid = data.hotel.uuid
                        let check = true
                        let hotels = this.$store.getters['hotel/hotels']
                        for (let i=0; i<hotels.length; i++) {
                            let uuid = hotels[i].uuid
                            if (uuid === new_uuid) {
                                check = false
                                break
                            }
                        }
                        if (check === true) {
                            this.$store.commit('hotel/saveHotel', data)
                        }
                        // this.$store.commit('hotel/saveHotel', data)
                    }
                }
                let user = this.$store.getters['user/user']
                if (user.role === 'user') {
                    if (data.hotel.status === 'active') {
                        let new_uuid = data.hotel.uuid
                        let check = true
                        // let hotels = this.$store.getters['hotel/hotels']
                        let uuids = this.$store.getters['hotel/uuids']
                        for (let i=0; i<uuids.length; i++) {
                            // let uuid = hotels[i].uuid
                            if (uuids[i] === new_uuid) {
                                check = false
                                break
                            }
                        }
                        if (check === true) {
                            this.$store.commit('hotel/saveHotel', data)
                        }
                        this.$store.commit('hotel/saveUuid', data.hotel.uuid)
                        // this.$store.commit('hotel/saveHotel', data)
                    }
                }
                let count = this.$store.getters['hotel/notify_hotels'].length
                let old_count = this.$store.getters['hotel/old_count_hotelier']
                this.$store.commit('hotel/setHotelierCount', count - old_count)
            })
        },
        subscribe_review() {
            let pusher = new Pusher('5d873d3e35474aa76004', {
                cluster: 'ap1'
            });
            pusher.subscribe('a_channel');
            pusher.bind('an_event_1', data => {
                let user = this.$store.getters['user/user']
                if (user.role === 'hotelier' && user.uuid === data.review.owner_id) {
                    this.$store.commit('review/saveReview', data)
                    this.$store.commit('review/saveNewReview', data)
                    this.$store.commit('review/saveNewCount')
                }
            })
        },
        subscribe_complaint() {
            let pusher = new Pusher('5d873d3e35474aa76004', {
                cluster: 'ap1'
            });
            pusher.subscribe('a_channel');
            pusher.bind('an_event_2', data => {
                let user = this.$store.getters['user/user']
                if (user.role === 'hotelier' && user.uuid === data.complaint.owner_id) {
                    this.$store.commit('complaint/saveComplaint', data)
                    this.$store.commit('complaint/saveNewComplaint', data)
                    this.$store.commit('complaint/saveNewCount')
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
                    this.$store.commit('booking/saveBooking', data)
                    this.$store.commit('booking/saveNewBooking', data)
                }
            })
        },
        subscribe_user() {
            let pusher = new Pusher('5d873d3e35474aa76004', {
                cluster: 'ap1'
            });
            pusher.subscribe('a_channel_1');
            pusher.bind('an_event_2', data => {
                let user = this.$store.getters['user/user']
                if (user.uuid === data.user.uuid) {
                    this.$store.dispatch('user/logout')
                    this.$router.push('/login')
                }
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