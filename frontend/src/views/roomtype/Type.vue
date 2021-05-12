<template>
    <div>
        <div>
            <b-button
                v-if="roleHotelier"
                variant="success"
                size="sm"
                @click="$bvModal.show('modal-create')"
            >
                {{ $t('type.type.createBtn') }}
            </b-button>
        </div>
        <br>
        <b-list-group>
            <b-list-group-item
                v-for="type in types"
                :key="type.uuid"
                class="list-item"
            >
                <div>
                    <button
                        v-if="roleHotelier"
                        href="#"
                        style="right: 110px"
                        class="btn btn-primary position-absolute"
                        @click="$bvModal.show(`modal-${type.uuid}-update`)"
                    >
                        {{ $t('type.type.updateBtn') }}
                    </button>
                    <b-modal
                        :id="`modal-${type.uuid}-update`"
                        title="Update room"
                        size="lg"
                        hide-footer
                    >
                        <type-form :type="type" />
                    </b-modal>
                    <b-button
                        v-if="roleHotelier"
                        href="#"
                        style="right: 20px; width: 80px"
                        variant="danger"
                        class="position-absolute"
                        @click="$bvModal.show(`modal-${type.uuid}-delete`)"
                    >
                        {{ $t('type.type.deleteBtn') }}
                    </b-button>
                    <b-modal
                        :id="`modal-${type.uuid}-delete`"
                        :title="$t('type.type.deleteTitle')"
                        size="lg"
                        :ok-title="$t('button.submit')"
                        :cancel-title="$t('button.unsubmit')"
                        @ok="deleteType(type.uuid)"
                    >
                        {{ $t('type.type.confirmDelete') }}
                    </b-modal>
                </div>
                <div>
                    <h4>
                        <span class="font-weight-bolder">
                            {{ $t('type.type.roomType') }}:
                        </span>
                        <span class="text-secondary">
                            {{ type.roomType }}
                        </span>
                    </h4>

                    <p class="p-inline">
                        <span class="font-weight-bolder">
                            {{ $t('type.type.capacity') }}:
                        </span>
                        <span class="text-secondary">
                            {{ type.capacity }}
                        </span>
                    </p>

                    <p
                        class="p-inline"
                        style="margin: 20px"
                    >
                        <span class="font-weight-bolder">
                            {{ $t('type.type.price') }}:
                        </span>
                        <span class="text-secondary">
                            {{ type.price }} VND
                        </span>
                    </p>

                    <p>
                        <span class="font-weight-bolder">
                            {{ $t('hotel.hotel.amenities') }}
                        </span>
                        <b-list-group horizontal="md">
                            <b-list-group-item
                                v-for="(amenity, index) in type.amenities"
                                :key="`${type.uuid}-amenity-${index}`"
                                style="margin: 5px; border: none"
                            >
                                <img
                                    :src="getSrc(amenity)"
                                    :alt="amenity"
                                    class="icon"
                                >
                                {{ amenity }}
                            </b-list-group-item>
                        </b-list-group>
                    </p>
                </div>
            </b-list-group-item>
        </b-list-group>
        <b-modal
            id="modal-create"
            :title="$t('type.type.createTitle')"
            size="lg"
            hide-footer
        >
            <type-form />
        </b-modal>
    </div>
</template>

<script>
import TypeForm from '@/components/TypeForm';
import formMixin from '@/mixin/form-mixin'

export default {
    name: "Type",
    components: {TypeForm},
    data: function () {
        return {
            types: [],
        }
    },
    computed: {
        roleHotelier: function () {
            return (this.$store.getters['user/user'].role === 'hotelier')
        },
        // Check if role user
        roleUser: function () {
            return (this.$store.getters['user/user'].role === 'user')
        },
    },
    created() {
        this.$store.dispatch('type/listTypes', this.$route.params.uuid)
            .then(() => {
                this.types = this.$store.getters['type/types']
            })
    },
    methods: {
        getSrc: function (amenity) {
            let images = require.context('../../assets/', false, /\.png$/)
            return images('./' + amenity + ".png")
        },
        deleteType: function (uuid) {
            this.$store.dispatch('type/resetStatus')
            this.$store.dispatch('type/deleteType', {hotelId: this.$route.params.uuid, typeId: uuid})
                .then(() => {
                    if (this.$store.getters['type/status'] === 'FAILED') {
                        // Alert for failed delete api
                        this.makeToast(this.$t('type.type.errors.title'), this.$t('type.type.errors.exceptionOccurred'))
                    } else {
                        window.location.reload()
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
.list-item {
    margin: 10px 0
}
.p-inline {
    display: inline-block;
}
.icon {
    height: 30px;
    width: 30px;
}
</style>