<template>
    <b-form>
        <b-form-group
            id="name-group"
            class="col-12"
            style="padding: 0"
        >
            <div>
                <span class="font-weight-bolder">
                    {{ $t('hotel.hotel.name') }}:
                </span>
                <span>
                    {{ hotel.name }}
                </span>
            </div>
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
                {{ $t('hotel.hotel.ownerName') }}
            </span>
            <span>
                {{ hotel.ownerName }}
            </span>
        </p>
        <b-form-group>
            <label class="required">{{ $t('hotel.hotel.approveChoice') }}: </label>
            <b-form-radio-group
                v-model="$v.form.status.$model"
                :state="validateState('status')"
            >
                <b-form-radio value="active">
                    {{ $t('hotel.hotel.approveBtn') }}
                </b-form-radio>
                <b-form-radio value="reject">
                    {{ $t('hotel.hotel.rejectBtn') }}
                </b-form-radio>
            </b-form-radio-group>
        </b-form-group>
        <b-form-group>
            <label class="required">{{ $t('hotel.hotel.reason') }}: </label>
            <b-form-textarea
                v-model="$v.form.reject_reason.$model"
                :state="validateState('reject_reason')"
                rows="3"
                max-rows="6"
                type="text"
            />
        </b-form-group>
        <button
            class="btn btn-sm btn-success"
            type="button"
            @click="onSubmit"
        >
            {{ $t('hotel.hotel.submit') }}
        </button>
    </b-form>
</template>

<script>
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin'
import {required} from 'vuelidate/lib/validators';
import {getDistrictsByProvinceCode, getProvinces, getWardsByDistrictCode} from "sub-vn";
import json from "../../mixin/data/db_en.json";

export default {
    name: "ApproveForm",
    mixins: [validationMixin, formMixin],
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
        return {
            form: {
                status: null,
                reject_reason: null,
            }
        }
    },
    validations: {
        form: {
            status: {
                required
            },
            reject_reason: {
                required
            },
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
        onSubmit: function () {
            this.$store.dispatch('hotel/resetStatus')
            this.form.uuid = this.hotel.uuid
            this.$store.dispatch('hotel/approveHotel', this.form).then(() => {
                if (this.$store.getters['hotel/status'] === 'FAILED') {
                    // Alert for failed api calls
                    this.makeToast(this.$t('hotel.hotel.errors.approveTitle'), this.$t('hotel.hotel.errors.exceptionOccurred'))
                } else {
                    if (this.form.status === "active") {
                        this.$bvToast.toast(this.$t('hotel.hotel.success.approveMessage'), {
                            title: this.$t('hotel.hotel.success.approveTitle'),
                            autoHideDelay: 2000,
                            variant: 'success'
                        })
                    } else {
                        this.$bvToast.toast(this.$t('hotel.hotel.success.rejectMessage'), {
                            title: this.$t('hotel.hotel.success.rejectTitle'),
                            autoHideDelay: 2000,
                            variant: 'success'
                        })
                    }
                    const path = this.$route.path
                    if (path === '/admin/hotels') {
                        setTimeout(location.reload.bind(location), 2000)
                    } else {
                        setTimeout(() => this.$router.push('/admin/hotels'), 2000)
                    }
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
.required:after {
    content: " *";
    color: red;
}
</style>