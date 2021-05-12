<template>
    <b-form>
        <!--  Booking check in date      -->
        <b-form-group
            id="checkin-group"
            label="Check in date"
            label-for="check_in"
        >
            <b-form-datepicker
                id="check_in"
                v-model="$v.form.check_in_time.$model"
                :state="validateState('check_in_time')"
                :min="first"
                placeholder="Select check in date"
            />
        </b-form-group>
        <!--  Booking check out date      -->
        <b-form-group
            id="checkout-group"
            label="Check out date"
            label-for="check_out"
        >
            <b-form-datepicker
                id="check_out"
                v-model="$v.form.check_out_time.$model"
                :state="validateState('check_out_time')"
                :min="last"
                placeholder="Select check out date"
            />
        </b-form-group>
        <!--  Booking room number      -->
        <b-form-group
            id="room-number-group"
            label="Room number"
            label-for="room_number"
        >
            <b-form-input
                id="room_number"
                :value="room.roomNumber"
                type="text"
                disabled
            />
        </b-form-group>
        <!--  Booking price      -->
        <b-form-group
            id="price-group"
            label="Price per night"
            label-for="price"
        >
            <b-form-input
                id="price"
                :value="room.price"
                type="text"
                disabled
            />
        </b-form-group>
        <!--  Booking room amenities      -->
        <b-form-group
            id="amenities-group"
            label="Amenities"
            label-for="amenities"
        >
            <b-list-group>
                <b-list-group-item
                    v-for="(amenity, index) in room.amenities"
                    :key="`${room.uuid}-amenity-${index}`"
                >
                    {{ amenity }}
                </b-list-group-item>
            </b-list-group>
        </b-form-group>
        <button
            class="btn btn-primary"
            type="button"
            @click="onSubmit"
        >
            Submit
        </button>
    </b-form>
</template>

<script>
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin'
import {required} from 'vuelidate/lib/validators';


export default {
    name: "BookingForm",
    mixins: [validationMixin, formMixin],
    props: {
        // Room data
        room: {
            type: Object,
            default: () => {
                return null
            }
        }
    },
    data: function () {
        const now = new Date()
        const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
        const minDate = new Date(today)
        minDate.setDate(minDate.getDate() + 1)

        return {
            // Form data
            form : {
                check_in_time: null,
                check_out_time: null,
            },
            first: minDate,
            last: minDate
        }
    },
    // Form validation
    validations: {
        form: {
            check_in_time: {
                required
            },
            check_out_time: {
                required
            }
        }
    },
    methods: {
        // Parse date string to right format
        convertDate: function(date_string) {
            let date = new Date(date_string)
            let format_date = date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate() + " " +
                date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
            return format_date;
        },
        // Handle booking
        onSubmit: function() {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validation
                this.makeToast('Booking failed', 'Invalid data')
            } else if (Date.parse(this.form.check_in_time) >= Date.parse(this.form.check_out_time)) {
                // Alert if check in greater than check out
                this.makeToast('Booking failed', 'Check out time must be after')
            } else {
                this.form.room_id = this.room.uuid
                this.form.check_in_time = this.convertDate(this.form.check_in_time)
                this.form.check_out_time = this.convertDate(this.form.check_out_time)
                // Handle create booking
                this.$store.dispatch('booking/resetStatus')
                this.$store.dispatch('booking/createBooking', this.form).then(() => {
                    if (this.$store.getters['booking/status'] === 'FAILED') {
                        // Alert for failed api calls
                        this.makeToast('Booking failed', 'Invalid data')
                    } else {
                        // Alert for success
                        this.$bvToast.toast('You have made booking', {
                            title: 'Booking success',
                            autoHideDelay: 5000,
                            variant: 'success'
                        })
                        this.$bvModal.hide(`modal-${this.room.uuid}-booking`)
                    }
                })
            }
        }
    }
}
</script>

<style scoped>

</style>