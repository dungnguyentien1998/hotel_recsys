<template>
    <b-form>
        <b-form-group>
            <label class="required">Approve or reject this request</label>
            <b-form-radio-group
                v-model="$v.form.status.$model"
                :state="validateState('status')"
            >
                <b-form-radio value="active">
                    Activate
                </b-form-radio>
                <b-form-radio value="reject">
                    Reject
                </b-form-radio>
            </b-form-radio-group>
        </b-form-group>
        <b-form-group>
            <label class="required">{{ $t('review.reviewForm.content') }}</label>
            <b-form-textarea
                v-model="$v.form.reject_reason.$model"
                :state="validateState('reject_reason')"
                :placeholder="$t('review.reviewForm.contentPlaceholder')"
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
            {{ $t('review.reviewForm.submitBtn') }}
        </button>
    </b-form>
</template>

<script>
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin'
import {required} from 'vuelidate/lib/validators';

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
                    // this.$bvModal.hide(`modal-create`)
                    setTimeout(location.reload.bind(location), 2000)
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