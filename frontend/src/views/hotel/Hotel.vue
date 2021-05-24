<template>
    <layout>
        <template #content>
            <div class="align-items-center d-flex">
                <h2 class="flex-grow-1">
                    {{ roleUser ? $t('hotel.hotel.searchHotel') : $t('hotel.hotel.title') }}
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
                    label-cols-sm="4"
                    label-cols-lg="3"
                    content-cols-sm="7"
                    content-cols-lg="7"
                >
                    <b-form-input
                        id="name"
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
                                label-cols-sm="4"
                                label-cols-lg="3"
                                content-cols-sm="7"
                                content-cols-lg="7"
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
                                label-cols-sm="4"
                                label-cols-lg="3"
                                content-cols-sm="7"
                                content-cols-lg="7"
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
                                label-cols-sm="4"
                                label-cols-lg="3"
                                content-cols-sm="7"
                                content-cols-lg="7"
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
                                label-cols-sm="4"
                                label-cols-lg="3"
                                content-cols-sm="7"
                                content-cols-lg="7"
                            >
                                <b-form-select
                                    id="ward"
                                    v-model="$v.form.ward.$model"
                                    :options="wards"
                                />
                            </b-form-group>
                            <b-form-group
                                id="amenities-group"
                                :label="$t('hotel.hotelForm.amenities')"
                                label-for="amenities"
                                label-cols-sm="4"
                                label-cols-lg="3"
                                content-cols-sm="7"
                                content-cols-lg="7"
                            >
                                <b-form-tags
                                    id="amenities"
                                    v-model="form.amenities"
                                    add-on-change
                                    no-outer-focus
                                    size="lg"
                                >
                                    <template #default="{ tags, inputAttrs, inputHandlers, disabled, removeTag }">
                                        <ul
                                            v-if="tags.length > 0"
                                            class="mb-2 list-inline d-inline-block"
                                        >
                                            <li
                                                v-for="tag in tags"
                                                :key="tag"
                                                class="list-inline-item"
                                            >
                                                <b-form-tag
                                                    :title="tag"
                                                    variant="success"
                                                    :disabled="disabled"
                                                    @remove="removeTag(tag)"
                                                >
                                                    {{ tag }}
                                                </b-form-tag>
                                            </li>
                                        </ul>
                                        <b-form-select
                                            v-bind="inputAttrs"
                                            :options="availableOptions"
                                            :disabled="disabled || availableOptions.length === 0"
                                            v-on="inputHandlers"
                                        >
                                            <template #first>
                                                <option
                                                    value=""
                                                    disabled
                                                >
                                                    {{ $t('hotel.hotelForm.amenitiesPlaceholder') }}
                                                </option>
                                            </template>
                                        </b-form-select>
                                    </template>
                                </b-form-tags>
                            </b-form-group>
                        </b-form>
                    </b-card>
                </b-collapse>
            </div>
            <br>
            <button
                v-if="roleUser"
                class="btn btn-sm btn-primary"
                type="button"
                @click="onSubmit"
            >
                {{ $t('hotel.hotel.searchBtn') }}
                <font-awesome-icon
                    :icon="['fas', 'search']"
                />
            </button>
            <hr>
            <div class="align-items-center d-flex">
                <h2 class="flex-grow-1">
                    {{ roleUser ? $t('hotel.hotel.title') : '' }}
                </h2>
            </div>
            <br>
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
                            :height="300"
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
                        <p>
                            <span class="font-weight-bolder">
                                {{ $t('hotel.hotel.address') }}
                            </span>
                            <span class="text-secondary">
                                {{ getAddress(hotel.address, hotel.ward, hotel.district, hotel.city) }}
                            </span>
                        </p>
                        <b-badge
                            v-if="roleHotelier"
                            variant="primary"
                        >
                            {{ hotel.numRooms }} {{ $tc('hotel.hotel.room', hotel.numRooms) }}
                        </b-badge>
                        <b-badge
                            v-if="roleHotelier"
                            class="mx-2"
                            variant="success"
                        >
                            {{ hotel.numReviews }} {{ $tc('hotel.hotel.review', hotel.numReviews) }}
                        </b-badge>
                        <b-badge
                            v-if="roleHotelier"
                            variant="danger"
                        >
                            {{ hotel.numComplaints }} {{ $tc('hotel.hotel.complaint', hotel.numComplaints) }}
                        </b-badge>
                        <div class="mt-2">
                            <b-button
                                v-if="roleHotelier"
                                variant="primary"
                                href="#"
                                size="sm"
                                style="width: 80px"
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
                                style="width: 80px"
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
            <b-pagination
                v-model="currentPage"
                :per-page="perPage"
                :total-rows="rows"
                aria-controls="hotels-list"
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

library.add(faSearch)

export default {
    name: "Hotel",
    components: {HotelForm, Layout},
    mixins: [validationMixin, formMixin, addressMixin],
    data: function () {
        return {
            // Amenities options
            options: ['fitness center', 'free breakfast', 'free parking', 'swimming pool'],
            hotels: [],
            filterHotels: [],

            currentPage: 1,
            perPage: 6,

            recommendationsLogin: [],
            form: {
                name: null,
                amenities: [],
                city: null,
                district: null,
                ward: null,
                star: null
            },
            slide: 0,
            sliding: null
        }
    },
    computed: {
        availableOptions() {
            return this.options.filter(opt => this.form.amenities.indexOf(opt) === -1)
        },
        // Check if role hotelier
        roleHotelier: function () {
            return (this.$store.getters['user/user'].role === 'hotelier')
        },
        // Check if role user
        roleUser: function () {
            return (this.$store.getters['user/user'].role === 'user')
        },
        // Get row for hotel list
        rows: function () {
            return this.hotels.length
            // return this.filterHotels.length
        },
    },
    // Form validation
    validations: {
        form: {
            name: {
                // required
            },
            amenities: {
                // required
            },
            city: {
                // required,
            },
            district: {
                // required,
            },
            ward: {
                // required,
            },
            star: {

            }
        }
    },
    created() {
        this.$store.dispatch('hotel/listHotels').then(() => {
            this.hotels = this.$store.getters['hotel/hotels']
            this.filterHotels = this.hotels
            this.filterHotels.sort(function (a, b){
                return a.name.localeCompare(b.name) || b.star - a.star
            })
        })
        this.$store.dispatch('recommendation/listRecommendationsLogin').then(() => {
            this.recommendationsLogin = this.$store.getters['recommendation/recommendationsLogin']
            this.recommendationsLogin.sort(this.compare)
        })
    },
    methods: {
        getAddress: function (address, ward, district, city) {
            if (address == null || address === "") {
                return ward + ", " + district + ", " + city
            } else {
                return address + ", " + ward + ", " + district + ", " + city
            }
        },
        // Get hotel image
        hotelImage: function (uri) {
            return `${process.env.VUE_APP_PUBLIC_URL}${uri}`
        },
        // Get cities
        citiesOptions: function() {
            return getProvinces()
        },
        // Get districts from city
        districtsOptions: function(code) {
            return getDistrictsByProvinceCode(code)
        },
        // Get wards from district
        wardsOptions: function(code) {
            return getWardsByDistrictCode(code)
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
                    hotel.city === this.citiesOptions().filter(option => option.code === this.form.city)[0].name
                )
            }
            if (!!this.form.district) {
                this.filterHotels = this.filterHotels.filter(hotel =>
                    hotel.district === this.districtsOptions(this.form.city).filter(option => option.code === this.form.district)[0].name
                )
            }
            if (!!this.form.ward) {
                this.filterHotels = this.filterHotels.filter(hotel =>
                    hotel.ward === this.wardsOptions(this.form.district).filter(option => option.code === this.form.ward)[0].name
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
        compareStar: function(a,b) {
            if (a.star < b.star) {
                return 1;
            }
            if (a.star > b.star) {
                return  -1;
            }
            return 0;
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
</style>