<template>
    <b-form>
        <b-form-group
            id="title-group"
        >
            <label class="required">{{ $t('review.reviewForm.title') }}</label>
            <b-form-input
                id="title"
                v-model="$v.form.title.$model"
                :state="validateState('title')"
                :placeholder="$t('review.reviewForm.titlePlaceholder')"
                type="text"
            />
        </b-form-group>
        <b-form-group
            id="content-group"
        >
            <label class="required">{{ $t('review.reviewForm.content') }}</label>
            <!--            <b-form-input-->
            <!--                id="content"-->
            <!--                v-model="$v.form.content.$model"-->
            <!--                :state="validateState('content')"-->
            <!--                :placeholder="$t('review.reviewForm.contentPlaceholder')"-->
            <!--                type="text"-->
            <!--            />-->
            <b-form-textarea
                id="content"
                v-model="$v.form.content.$model"
                :state="validateState('content')"
                :placeholder="$t('review.reviewForm.contentPlaceholder')"
                rows="3"
                max-rows="6"
                type="text"
            />
        </b-form-group>
        <b-form-group
            id="rating-group"
        >
            <label class="required">{{ $t('review.reviewForm.rating') }}</label>
            <span style="margin: 0 10px" />
            <b-form-rating
                v-model="$v.form.rating.$model"
                class="pl-0"
                variant="primary"
                size="sm"
                no-border
                style="width: 100px"
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
    name: "ReviewForm",
    mixins: [validationMixin, formMixin],
    data: function() {
        return {
            // Form data
            form: {
                title: null,
                content: null,
                rating: null
            }
        }
    },
    // Form validate
    validations: {
        form: {
            title: {
                required
            },
            content: {
                required
            },
            rating :{
                required
            }
        }
    },
    methods: {
        resetForm: function () {
            this.form = {
                title: '',
                content: '',
                rating: null
            }
        },
        // Handle create review
        onSubmit: function () {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validate
                this.makeToast(this.$t('review.reviewForm.errors.createTitle'), this.$t('review.reviewForm.errors.missing'))
            } else {
                this.form.hotelId = this.$route.params.uuid
                this.$store.dispatch('review/resetStatus')
                this.$store.dispatch('review/createReview', this.form)
                    .then(() => {
                        if (this.$store.getters['review/status'] === 'FAILED') {
                            // Alert for failed created api
                            this.makeToast(this.$t('review.reviewForm.errors.createTitle'), this.$t('review.reviewForm.errors.exceptionOccurred'))
                        } else {
                            // Alert for success created
                            this.$bvToast.toast(this.$t('review.reviewForm.success.message'), {
                                title: this.$t('review.reviewForm.success.title'),
                                autoHideDelay: 2000,
                                variant: 'success'
                            })
                            setTimeout(location.reload.bind(location), 2000)
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