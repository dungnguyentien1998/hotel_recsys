<template>
    <b-form>
        <b-form-group
            id="title-group"
        >
            <label class="required">{{ $t('complaint.complaintForm.title') }}</label>
            <b-form-input
                id="title"
                v-model="$v.form.title.$model"
                :state="validateState('title')"
                :placeholder="$t('complaint.complaintForm.titlePlaceHolder')"
                type="text"
            />
        </b-form-group>
        <b-form-group
            id="content-group"
        >
            <label class="required">{{ $t('complaint.complaintForm.content') }}</label>
            <b-form-textarea
                id="content"
                v-model="$v.form.content.$model"
                :state="validateState('content')"
                :placeholder="$t('complaint.complaintForm.contentPlaceHolder')"
                rows="3"
                max-rows="6"
                type="text"
            />
        </b-form-group>
        <b-form-group
            id="image-group"
        >
            <label>{{ $t('complaint.complaintForm.image') }}</label>
            <b-form-file
                id="image"
                v-model="$v.form.image.$model"
                :placeholder="$t('hotel.hotelForm.imagePlaceholder')"
                :drop-placeholder="$t('hotel.hotelForm.imageDropPlaceholder')"
            />
        </b-form-group>
        <button
            class="btn btn-sm btn-success"
            type="button"
            @click="onSubmit"
        >
            {{ $t('complaint.complaintForm.submit') }}
        </button>
    </b-form>
</template>

<script>
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin';
import {required} from 'vuelidate/lib/validators';

export default {
    name: "ComplaintForm",
    mixins: [validationMixin, formMixin],
    data: function() {
        return {
            // Form data
            form: {
                title: null,
                content: null,
                image: null
            }
        }
    },
    // Form validation
    validations: {
        form: {
            title: {
                required
            },
            content: {
                required
            },
            image :{

            }
        }
    },
    methods: {
        resetForm: function () {
            this.form = {
                title: '',
                content: '',
                image: null
            }
        },
        // Handle create complaint
        onSubmit: function () {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validation
                this.makeToast(this.$t('complaint.complaintForm.errors.createTitle'), this.$t('complaint.complaintForm.errors.missing'))
            } else {
                if (this.form.image == null) {
                    delete this.form.image
                }
                this.form.hotelId = this.$route.params.uuid
                this.$store.dispatch('complaint/resetStatus')
                this.$store.dispatch('complaint/createComplaint', this.form)
                    .then(() => {
                        if (this.$store.getters['complaint/status'] === 'FAILED') {
                            // Alert for failed api call
                            this.makeToast(this.$t('complaint.complaintForm.errors.createTitle'), this.$t('complaint.complaintForm.errors.exceptionOccurred'))
                        } else {
                            // Alert for success
                            this.$bvToast.toast(this.$t('complaint.complaintForm.success.message'), {
                                title: this.$t('complaint.complaintForm.success.title'),
                                autoHideDelay: 5000,
                                variant: 'success'
                            })
                            this.resetForm()
                        }
                    })
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