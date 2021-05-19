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
                    label-cols-sm="4"
                    label-cols-lg="3"
                    content-cols-sm="7"
                    content-cols-lg="7"
                >
                    <b-form-input
                        id="name"
                        v-model="$v.form.name.$model"
                        :placeholder="$t('hotel.hotelForm.namePlaceholder')"
                        type="text"
                    />
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
                    {{ $t('hotel.hotel.approveLabel') }}
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
                        <!--                        <p>-->
                        <!--                            <span class="font-weight-bolder">-->
                        <!--                                {{ $t('hotel.hotel.amenities') }}-->
                        <!--                            </span>-->
                        <!--                            <b-list-group horizontal="md">-->
                        <!--                                <b-list-group-item-->
                        <!--                                    v-for="(amenity, index) in hotel.amenities"-->
                        <!--                                    :key="`${hotel.uuid}-amenity-${index}`"-->
                        <!--                                    style="border: none"-->
                        <!--                                >-->
                        <!--                                    <img-->
                        <!--                                        :src="getSrc(amenity)"-->
                        <!--                                        :alt="amenity"-->
                        <!--                                        class="icon"-->
                        <!--                                    >-->
                        <!--                                    <span style="display: inline-block">-->
                        <!--                                        {{ amenity }}-->
                        <!--                                    </span>-->
                        <!--                                </b-list-group-item>-->
                        <!--                            </b-list-group>-->
                        <!--                        </p>-->
                        <div class="mt-2">
                            <b-button
                                :disabled="hotel.isActive === true"
                                variant="success"
                                href="#"
                                size="sm"
                                @click="$bvModal.show(`modal-${hotel.uuid}-approve`)"
                            >
                                {{ $t('hotel.hotel.approveBtn') }}
                            </b-button>

                            <b-button
                                :disabled="hotel.isActive === true"
                                class="ml-2"
                                variant="danger"
                                href="#"
                                size="sm"
                                @click="$bvModal.show(`modal-${hotel.uuid}-reject`)"
                            >
                                {{ $t('hotel.hotel.rejectBtn') }}
                            </b-button>
                            <!--                            <b-button-->
                            <!--                                class="ml-2"-->
                            <!--                                variant="primary"-->
                            <!--                                href="#"-->
                            <!--                                size="sm"-->
                            <!--                                @click="$bvModal.show(`modal-${hotel.uuid}-view`)"-->
                            <!--                            >-->
                            <!--                                View-->
                            <!--                            </b-button>-->
                        </div>

                        <b-modal
                            :id="`modal-${hotel.uuid}-approve`"
                            :title="$t('hotel.hotel.approveTitle')"
                            size="lg"
                            :ok-title="$t('button.submit')"
                            :cancel-title="$t('button.unsubmit')"
                            @ok="approveHotel(hotel.uuid)"
                        >
                            {{ $t('hotel.hotel.confirmApprove') }}
                        </b-modal>

                        <b-modal
                            :id="`modal-${hotel.uuid}-reject`"
                            :title="$t('hotel.hotel.rejectTitle')"
                            size="lg"
                            :ok-title="$t('button.submit')"
                            :cancel-title="$t('button.unsubmit')"
                            @ok="rejectHotel(hotel.uuid)"
                        >
                            {{ $t('hotel.hotel.confirmReject') }}
                        </b-modal>
                        <!--                        <b-modal-->
                        <!--                            :id="`modal-${hotel.uuid}-view`"-->
                        <!--                            title="View hotel"-->
                        <!--                            size="lg"-->
                        <!--                            hide-footer-->
                        <!--                        >-->
                        <!--                            <form-detail :hotel="hotel" />-->
                        <!--                        </b-modal>-->
                    </b-card>
                </div>
            </div>
            <b-pagination
                v-model="currentPage"
                :per-page="perPage"
                :total-rows="rows"
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
import FormDetail from "@/views/admin/FormDetail";
import {library} from '@fortawesome/fontawesome-svg-core'
import {faSearch} from '@fortawesome/free-solid-svg-icons'

library.add(faSearch)

export default {
    name: "Hotel",
    components: {Layout},
    mixins: [validationMixin, formMixin, addressMixin],
    data: function () {
        return {
            // Amenities options
            options: ['fitness center', 'free breakfast', 'free parking', 'swimming pool'],
            // Hotel data
            hotels: [],
            // Hotel data for search form
            filterHotels: [],
            // Pagination data
            currentPage: 1,
            perPage: 6,
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
                is_active: null
            },
            slide: 0,
            sliding: null
        }
    },
    computed: {
        // Get amenities options
        availableOptions() {
            // return this.options.filter(opt => this.form.amenities.indexOf(opt.toLowerCase()) === -1)
            return this.options.filter(opt => this.form.amenities.indexOf(opt) === -1)
        },
        // Get row for hotel list
        rows: function () {
            return this.hotels.length
        },
    },
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
        // Get hotel and recommendation list
        this.$store.dispatch('hotel/listHotels').then(() => {
            this.hotels = this.$store.getters['hotel/hotels']
            this.hotels.sort(this.compare)
            this.filterHotels = this.hotels
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
        getSrc: function (amenity) {
            let images = require.context('../../assets/', false, /\.png$/)
            return images('./' + amenity + ".png")
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
        approveHotel: function (uuid) {
            this.$store.dispatch('hotel/resetStatus')
            this.updateForm.is_active = true
            this.updateForm.uuid = uuid
            this.$store.dispatch('hotel/approveHotel', this.updateForm).then(() => {
                if (this.$store.getters['hotel/status'] === 'FAILED') {
                    // Alert for failed api calls
                    this.makeToast(this.$t('hotel.hotel.errors.approveTitle'), this.$t('hotel.hotel.errors.exceptionOccurred'))
                } else {
                    // window.location.reload()
                    this.$bvToast.toast(this.$t('hotel.hotel.success.approveMessage'), {
                        title: this.$t('hotel.hotel.success.approveTitle'),
                        autoHideDelay: 2000,
                        variant: 'success'
                    })
                    // this.$bvModal.hide(`modal-create`)
                    setTimeout(location.reload.bind(location), 2000)
                }
            })
        },
        // Handle delete hotel
        rejectHotel: function (uuid) {
            this.$store.dispatch('hotel/resetStatus')
            this.$store.dispatch('hotel/deleteHotel', uuid)
                .then(() => {
                    if (this.$store.getters['hotel/status'] === 'FAILED') {
                        // Alert for failed api call
                        this.makeToast(this.$t('hotel.hotel.errors.rejectTitle'), this.$t('hotel.hotel.errors.exceptionOccurred'))
                    } else {
                        // window.location.reload()
                        this.$bvToast.toast(this.$t('hotel.hotel.success.rejectMessage'), {
                            title: this.$t('hotel.hotel.success.rejectTitle'),
                            autoHideDelay: 2000,
                            variant: 'success'
                        })
                        // this.$bvModal.hide(`modal-create`)
                        setTimeout(location.reload.bind(location), 2000)
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
</style>