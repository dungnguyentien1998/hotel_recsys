<template>
    <b-form>
        <b-form-group
            id="type-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('room.roomForm.roomType') }}</label>
                <b-form-select
                    id="type"
                    v-model="$v.form.room_type.$model"
                    class="form-control col-sm-9"
                    :options="typeOptions"
                    :state="validateState('room_type')"
                />
            </div>
        </b-form-group>
        <b-form-group
            v-if="roomExist"
            id="number-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('room.roomForm.roomNumber') }}</label>
                <b-form-input
                    id="number"
                    v-model="$v.form.room_number.$model"
                    class="form-control col-sm-9"
                    :state="validateState('room_number')"
                    :placeholder="$t('room.roomForm.roomNumberPlaceholder')"
                    type="text"
                />
            </div>
        </b-form-group>
        <b-form-group
            v-if="!roomExist"
            id="room-numbers-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('room.roomForm.roomNumbers') }}</label>
                <b-form-tags
                    v-model="form.room_numbers"
                    input-id="tags"
                    tag-variant="success"
                    class="form-control col-sm-9"
                    :input-attrs="{ 'aria-describedby': 'tags-remove-on-delete-help' }"
                    :placeholder="$t('room.roomForm.roomNumbersPlaceholder')"
                    remove-on-delete
                />
            </div>
        </b-form-group>
        <b-form-group
            v-if="roomExist"
            id="image-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="col-sm-3 col-form-label">{{ $t('room.roomForm.image') }}</label>
                <b-form-file
                    id="image"
                    v-model="$v.form.image.$model"
                    class="form-control col-sm-9"
                    :state="validateState('image')"
                    :placeholder="$t('hotel.hotelForm.imagePlaceholder')"
                    :drop-placeholder="$t('hotel.hotelForm.imageDropPlaceholder')"
                />
            </div>
        </b-form-group>
        <div>
            <b-form-group
                v-if="!roomExist"
                class="col-12"
            >
                <div
                    v-for="(room_number, index) in form.room_numbers"
                    :key="`${room_number}-${index}`"
                    class="form-row"
                >
                    <label class="required col-sm-3 col-form-label">
                        {{ $t('room.roomForm.images') }} {{ room_number }}:
                    </label>
                    <b-form-file
                        v-model="form.images[index]"
                        class="form-control col-sm-9"
                        :placeholder="$t('hotel.hotelForm.imagePlaceholder')"
                        :drop-placeholder="$t('hotel.hotelForm.imageDropPlaceholder')"
                    />
                    <br><br>
                </div>
            </b-form-group>
        </div>
        <button
            class="btn btn-sm btn-primary"
            type="button"
            @click="onSubmit"
        >
            {{ roomExist ? $t('room.roomForm.updateBtn') : $t('room.roomForm.createBtn') }}
        </button>
    </b-form>
</template>

<script>
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin'
import {required, numeric} from 'vuelidate/lib/validators';


export default {
    name: "RoomForm",
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
        return {
            // Room form data
            form: !!this.room ? {
                room_number: this.room.roomNumber,
                image: null,
                images: null,
                room_numbers: this.room.room_numbers,
                room_type: this.room.roomType
            } : {
                room_number: null,
                image: null,
                images: [],
                room_numbers: [],
                room_type: null
            }
        }
    },
    computed: {
        // Check if room already existed
        roomExist() {
            return !!this.room
        },
        typeOptions() {
            let opts = []
            const types = this.$store.getters['type/types']
            opts.push({value: null, text: '-----'})
            for (let option in this.$store.getters['type/types']) {
                const room_type = types[option].roomType
                opts.push({value: room_type, text: room_type})
            }
            return opts
        }
    },
    // Form validation
    validations: {
        form: {
            room_number: {
                required,
                numeric
            },
            image: {
                // required
            },
            images: {
                required
            },
            room_numbers: {
                required
            },
            room_type: {
                required
            }
        }
    },
    methods: {
        // Handle create/update room
        onSubmit: function () {
            this.$v.form.$touch();
            if (this.$v.form.$anyError || this.form.room_type == null) {
                // Alert for form validation
                this.makeToast(this.$t('room.roomForm.errors.title'), this.$t('room.roomForm.errors.missing'))
            } else {
                // Handle update form
                this.$store.dispatch('room/resetStatus')
                if (this.roomExist) {
                    if (this.form.room_number == null || this.form.room_number === '') {
                        this.makeToast(this.$t('room.roomForm.errors.updateTitle'), this.$t('room.roomForm.errors.missing'))
                    } else {
                        this.form.hotelId = this.$route.params.uuid
                        this.form.roomId = this.room.uuid
                        // if (this.form.room_number === this.room.roomNumber) {
                        //     this.form.room_number = null
                        // }
                        this.$store.dispatch('room/updateRoom', this.form).then(() => {
                            if (this.$store.getters['room/status'] === 'FAILED') {
                                // Alert for failed api calls
                                this.makeToast(this.$t('room.roomForm.errors.updateTitle'),
                                    this.$t('room.roomForm.errors.exceptionOccurred'))
                            } else {
                                this.$bvToast.toast(this.$t('room.roomForm.success.updateMessage'), {
                                    title: this.$t('room.roomForm.success.updateTitle'),
                                    autoHideDelay: 2000,
                                    variant: 'success'
                                })
                                // this.$bvModal.hide(`modal-${this.room.uuid}-update`)
                                setTimeout(location.reload.bind(location), 2000)
                            }
                        })
                    }
                } else {
                    // Handle create form
                    if (this.form.room_numbers.length === 0 || this.form.images.length === 0) {
                        this.makeToast(this.$t('room.roomForm.errors.createTitle'), this.$t('room.roomForm.errors.missing'))
                    } else {
                        this.form.hotelId = this.$route.params.uuid
                        this.$store.dispatch('room/createRoom', this.form)
                            .then(() => {
                                if (this.$store.getters['room/status'] === 'FAILED') {
                                    let message = this.$store.getters['room/message']
                                    if (localStorage.getItem("language") === "en") {
                                        message = "Room number " + message + " already existed"
                                    } else {
                                        message = "Số phòng " + message + " đã tồn tại"
                                    }
                                    // Alert for failed api calls
                                    this.makeToast(this.$t('room.roomForm.errors.createTitle'), message)
                                } else {
                                    this.$bvToast.toast(this.$t('room.roomForm.success.message'), {
                                        title: this.$t('room.roomForm.success.title'),
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