<template>
    <b-form>
        <b-form-group
            id="name-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('hotel.hotelForm.name') }}</label>
                <b-form-input
                    id="name"
                    v-model="$v.form.name.$model"
                    class="form-control col-sm-9"
                    :state="validateState('name')"
                    :placeholder="$t('hotel.hotelForm.namePlaceholder')"
                    type="text"
                />
            </div>
        </b-form-group>
        <b-form-group
            id="star-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('hotel.hotelForm.star') }}</label>
                <b-form-rating
                    v-model="$v.form.star.$model"
                    :state="validateState('star')"
                    class="form-control col-sm-3"
                    variant="warning"
                    size="sm"
                    inline
                    no-border
                />
            </div>
        </b-form-group>
        <b-form-group
            id="city-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('hotel.hotelForm.city') }}</label>
                <b-form-select
                    id="city"
                    v-model="$v.form.city.$model"
                    class="form-control col-sm-9"
                    :options="cities"
                    :state="validateState('city')"
                    @change="onChangeCity"
                />
            </div>
        </b-form-group>
        <b-form-group
            id="district-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('hotel.hotelForm.district') }}</label>
                <b-form-select
                    id="district"
                    v-model="$v.form.district.$model"
                    class="form-control col-sm-9"
                    :options="districts"
                    :state="validateState('district')"
                    @change="onChangeDistrict"
                />
            </div>
        </b-form-group>
        <b-form-group
            id="ward-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('hotel.hotelForm.ward') }}</label>
                <b-form-select
                    id="ward"
                    v-model="$v.form.ward.$model"
                    class="form-control col-sm-9"
                    :options="wards"
                    :state="validateState('ward')"
                />
            </div>
        </b-form-group>
        <b-form-group
            id="address-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('hotel.hotelForm.address') }}</label>
                <b-form-input
                    id="address"
                    v-model="$v.form.address.$model"
                    class="form-control col-sm-9"
                    :state="validateState('address')"
                    :placeholder="$t('hotel.hotelForm.addressPlaceholder')"
                    type="text"
                />
            </div>
        </b-form-group>
        <b-form-group
            id="image-group"
            class="col-12"
        >
            <div class="form-row">
                <label
                    class="col-sm-3 col-form-label"
                    :class="[{'required': !hotelExist}]"
                >
                    {{ $t('hotel.hotelForm.image') }}</label>
                <b-form-file
                    v-model="$v.form.image.$model"
                    class="form-control col-sm-9"
                    :placeholder="$t('hotel.hotelForm.imagePlaceholder')"
                    :drop-placeholder="$t('hotel.hotelForm.imageDropPlaceholder')"
                />
            </div>
        </b-form-group>
        <b-form-group
            id="amenities-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('hotel.hotelForm.amenities') }}</label>
                <b-form-tags
                    id="amenities"
                    v-model="form.amenities"
                    class="form-control col-sm-9"
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
            </div>
        </b-form-group>
        <button
            class="btn btn-sm btn-primary"
            type="button"
            @click="onSubmit"
        >
            {{ hotelExist ? $t('hotel.hotelForm.updateBtn') : $t('hotel.hotelForm.createBtn') }}
        </button>
    </b-form>
</template>

<script>
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin'
import addressMixin from '@/mixin/address-mixin'
import {required} from 'vuelidate/lib/validators';
import {getDistrictsByProvinceCode, getWardsByDistrictCode, getProvinces} from 'sub-vn';
import json from '../mixin/data/db_en.json'

export default {
    name: "HotelForm",
    mixins: [validationMixin, formMixin, addressMixin],
    props: {
        // Hotel data
        hotel: {
            type: Object,
            default: () => {
                return null
            }
        }
    },
    data: function () {
        let city_code = null
        let district_code = null
        let ward_code = null
        if (!!this.hotel) {
            city_code = getProvinces().filter(option => option.name === this.hotel.city)[0].code
            district_code = getDistrictsByProvinceCode(city_code).filter(option => option.name === this.hotel.district)[0].code
            ward_code = getWardsByDistrictCode(district_code).filter(option => option.name === this.hotel.ward)[0].code
        }
        return {
            // Amenities options
            options: ['fitness center', 'breakfast', 'free parking', 'swimming pool', 'bar', 'spa',
                'room service', 'non smoking icon'],
            // Hotel form data
            form: !!this.hotel ? {
                name: this.hotel.name,
                star: this.hotel.star,
                city: city_code,
                district: district_code,
                ward: ward_code,
                address: this.hotel.address,
                image: null,
                amenities: this.hotel.amenities,
            } : {
                name: null,
                star: null,
                address: null,
                image: null,
                amenities: [],
            },
        }
    },
    computed: {
        // Check if hotel already existed
        hotelExist() {
            return !!this.hotel
        },
        // Get amenities options
        availableOptions() {
            return this.options.filter(opt => this.form.amenities.indexOf(opt) === -1)
        }
    },
    // Form validation
    validations: {
        form: {
            name: {
                required
            },
            star: {
                required
            },
            city: {
                required,
            },
            district: {
                required,
            },
            ward: {
                required,
            },
            address: {
                required,
            },
            image: {

            },
            amenities: {
                required
            },
        }
    },
    created() {
        if (this.hotelExist) {
            const dists = json.district
            this.districts = [
                {value: null, text: '-----'},
                ...getDistrictsByProvinceCode(this.form.city).map(district => {
                    let trans_text = district.name
                    if (localStorage.getItem("language") === "en") {
                        let dist = dists.filter(option => option.idDistrict === district.code)[0]
                        trans_text = dist.name
                    }
                    return {value: district.code, text: trans_text}
                })
            ]
            const communes = json.commune
            this.wards = [
                {value: null, text: '-----'},
                ...getWardsByDistrictCode(this.form.district).map(ward => {
                    let trans_text = ward.name
                    if (localStorage.getItem("language") === "en") {
                        let commune = communes.filter(option => option.idCoummune === ward.code)[0]
                        trans_text = commune.name
                    }
                    return {value: ward.code, text: trans_text}
                })
            ]
        }
    },
    methods: {
        resetForm: function () {
            this.form = {
                name: null,
                star: null,
                city: null,
                district: null,
                ward: null,
                address: null,
                image: null,
                amenities: [],
            }
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
        // Handle create/update hotel
        onSubmit: function () {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validation
                this.makeToast(this.$t('hotel.hotelForm.errors.title'), this.$t('hotel.hotelForm.errors.missing'))
            } else
            if (!this.hotelExist && this.form.image == null) {
                this.makeToast(this.$t('hotel.hotelForm.errors.title'), this.$t('hotel.hotelForm.errors.missing'))
            } else
            {
                this.form.amenities = this.form.amenities.map(amenity => amenity.toLowerCase())
                if (!isNaN(this.form.city) && !isNaN(this.form.district) && !isNaN(this.form.ward)) {
                    const city_code = this.form.city
                    const district_code = this.form.district
                    this.form.city = this.citiesOptions().filter(option => option.code === this.form.city)[0].name
                    this.form.district = this.districtsOptions(city_code).filter(option => option.code === this.form.district)[0].name
                    this.form.ward = this.wardsOptions(district_code).filter(option => option.code === this.form.ward)[0].name
                }
                // const city_code = this.form.city
                // const district_code = this.form.district
                // this.form.city = this.citiesOptions().filter(option => option.code === this.form.city)[0].name
                // this.form.district = this.districtsOptions(city_code).filter(option => option.code === this.form.district)[0].name
                // this.form.ward = this.wardsOptions(district_code).filter(option => option.code === this.form.ward)[0].name
                // Handle update form
                this.$store.dispatch('hotel/resetStatus')
                if (this.hotelExist) {
                    this.form.uuid = this.hotel.uuid
                    this.$store.dispatch('hotel/updateHotel', this.form).then(() => {
                        if (this.$store.getters['hotel/status'] === 'FAILED') {
                            // Alert for failed api calls
                            this.makeToast(this.$t('hotel.hotelForm.errors.updateTitle'),
                                this.$t('hotel.hotelForm.errors.exceptionOccurred'))
                        } else {
                            this.$bvToast.toast(this.$t('hotel.hotelForm.success.updateMessage'), {
                                title: this.$t('hotel.hotelForm.success.updateTitle'),
                                autoHideDelay: 2000,
                                variant: 'success'
                            })
                            // this.$bvModal.hide(`modal-${this.hotel.uuid}-update`)
                            setTimeout(location.reload.bind(location), 2000)
                        }
                    })
                } else {
                    // Handle create form
                    this.$store.dispatch('hotel/createHotel', this.form)
                        .then(() => {
                            if (this.$store.getters['hotel/status'] === 'FAILED') {
                                // Alert for failed api calls
                                this.makeToast(this.$t('hotel.hotelForm.errors.createTitle'),
                                    this.$t('hotel.hotelForm.errors.exceptionOccurred'))
                            } else {
                                this.$bvToast.toast(this.$t('hotel.hotelForm.success.message'), {
                                    title: this.$t('hotel.hotelForm.success.title'),
                                    autoHideDelay: 2000,
                                    variant: 'success'
                                })
                                setTimeout(() => this.$bvModal.hide(`modal-create`), 2000)
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
.required:after {
    content: " *";
    color: red;
}
</style>