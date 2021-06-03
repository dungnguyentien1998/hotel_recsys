<template>
    <b-form>
        <b-form-group
            id="type-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('type.typeForm.roomType') }}</label>
                <b-form-input
                    id="type"
                    v-model="$v.form.room_type.$model"
                    class="form-control col-sm-9"
                    :state="validateState('room_type')"
                    :placeholder="$t('type.typeForm.roomTypePlaceholder')"
                    type="text"
                />
            </div>
        </b-form-group>
        <b-form-group
            id="capacity-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('type.typeForm.capacity') }}</label>
                <b-form-input
                    id="capacity"
                    v-model="$v.form.capacity.$model"
                    class="form-control col-sm-9"
                    :state="validateState('capacity')"
                    :placeholder="$t('type.typeForm.capacityPlaceholder')"
                    type="text"
                />
            </div>
        </b-form-group>
        <b-form-group
            id="children-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('type.typeForm.children') }}</label>
                <b-form-input
                    id="children"
                    v-model="$v.form.children_number.$model"
                    class="form-control col-sm-9"
                    :state="validateState('children')"
                    :placeholder="$t('type.typeForm.childrenPlaceholder')"
                    type="text"
                />
            </div>
        </b-form-group>
        <b-form-group
            id="price-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('type.typeForm.price') }}</label>
                <b-form-input
                    id="price"
                    v-model="$v.form.price.$model"
                    class="form-control col-sm-9"
                    :state="validateState('price')"
                    :placeholder="$t('type.typeForm.pricePlaceholder')"
                    type="text"
                />
            </div>
        </b-form-group>
        <b-form-group
            id="area-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('type.typeForm.area') }}</label>
                <b-form-input
                    id="area"
                    v-model="$v.form.area.$model"
                    class="form-control col-sm-9"
                    :state="validateState('area')"
                    :placeholder="$t('type.typeForm.areaPlaceholder')"
                    type="text"
                />
            </div>
        </b-form-group>
        <b-form-group
            id="amenities-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('type.typeForm.amenities') }}</label>
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
                                    {{ $t('type.typeForm.amenitiesPlaceholder') }}
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
            {{ typeExist ? $t('type.typeForm.updateBtn') : $t('type.typeForm.createBtn') }}
        </button>
    </b-form>
</template>

<script>
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin'
import {required, numeric} from 'vuelidate/lib/validators';

export default {
    name: "TypeForm",
    mixins: [validationMixin, formMixin],
    props: {
        type: {
            type: Object,
            default: () => {
                return null
            }
        }
    },
    data: function () {
        return {
            // Room amenities options
            options: ['personal care', 'coffee kit', 'tissue box', 'bathrobes', 'wifi'],
            form: !!this.type ? {
                room_type: this.type.roomType,
                capacity: this.type.capacity,
                children_number: this.type.childrenNumber,
                price: this.type.price,
                area: this.type.area,
                amenities: this.type.amenities
            } : {
                room_type: null,
                capacity: null,
                children_number: null,
                price: null,
                area: null,
                amenities: [],
            }
        }
    },
    computed: {
        typeExist() {
            return !!this.type
        },
        // Get amenities options
        availableOptions() {
            return this.options.filter(opt => this.form.amenities.indexOf(opt) === -1)
        },
    },
    validations: {
        form: {
            room_type: {
                required
            },
            capacity: {
                required,
                numeric
            },
            children_number: {
                required,
                numeric
            },
            price: {
                required,
                numeric
            },
            area: {
                required,
                numeric
            },
            amenities: {
                required
            },
        }
    },
    methods: {
        onSubmit: function () {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validation
                this.makeToast(this.$t('type.typeForm.errors.title'), this.$t('type.typeForm.errors.missing'))
            } else {
                this.form.amenities = this.form.amenities.map(amenity => amenity.toLowerCase())
                // Handle update form
                this.$store.dispatch('type/resetStatus')
                if (this.typeExist) {
                    this.form.hotelId = this.$route.params.uuid
                    this.form.typeId = this.type.uuid
                    this.$store.dispatch('type/updateType', this.form).then(() => {
                        if (this.$store.getters['type/status'] === 'FAILED') {
                            // Alert for failed api calls
                            this.makeToast(this.$t('type.typeForm.errors.updateTitle'), this.$t('type.typeForm.errors.exceptionOccurred'))
                        } else {
                            this.$bvToast.toast(this.$t('type.typeForm.success.updateMessage'), {
                                title: this.$t('type.typeForm.success.updateTitle'),
                                autoHideDelay: 2000,
                                variant: 'success'
                            })
                            // this.$bvModal.hide(`modal-${this.type.uuid}-update`)
                            setTimeout(location.reload.bind(location), 2000)
                        }
                    })
                } else {
                    // Handle create form
                    this.form.hotelId = this.$route.params.uuid
                    this.$store.dispatch('type/createType', this.form)
                        .then(() => {
                            if (this.$store.getters['type/status'] === 'FAILED') {
                                // Alert for failed api calls
                                this.makeToast(this.$t('type.typeForm.errors.createTitle'), this.$t('type.typeForm.errors.exceptionOccurred'))
                            } else {
                                this.$bvToast.toast(this.$t('type.typeForm.success.message'), {
                                    title: this.$t('type.typeForm.success.title'),
                                    autoHideDelay: 2000,
                                    variant: 'success'
                                })
                                // this.$bvModal.hide(`modal-create`)
                                setTimeout(location.reload.bind(location), 2000)
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