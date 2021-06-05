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
        <b-list-group
            id="types-list"
            :current-page="currentPage"
            :per-page="perPage"
        >
            <b-list-group-item
                v-for="type in types.slice((currentPage-1)*perPage, (currentPage-1)*perPage+perPage)"
                :key="type.uuid"
                class="list-item"
            >
                <div>
                    <button
                        v-if="roleHotelier"
                        href="#"
                        style="right: 110px; width: 80px"
                        class="btn btn-sm btn-primary position-absolute"
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
                        size="sm"
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
                        button-size="sm"
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
                            {{ type.name }}
                        </span>
                    </h4>

                    <!--                    <p class="p-inline">-->
                    <!--                        <span class="font-weight-bolder">-->
                    <!--                            {{ $t('type.type.capacity') }}:-->
                    <!--                        </span>-->
                    <!--                        <span class="text-secondary">-->
                    <!--                            {{ type.capacity }}-->
                    <!--                        </span>-->
                    <!--                    </p>-->

                    <p class="p-inline">
                        <span class="font-weight-bolder">
                            {{ $t('type.type.adultNumber') }}:
                        </span>
                        <span class="text-secondary">
                            {{ type.adultNumber }}
                        </span>
                    </p>

                    <p
                        class="p-inline"
                        style="margin: 20px"
                    >
                        <span class="font-weight-bolder">
                            {{ $t('type.type.childrenNumber') }}:
                        </span>
                        <span class="text-secondary">
                            {{ type.childrenNumber }}
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
                            {{ formatPrice(type.price) }} VND
                        </span>
                    </p>

                    <p
                        class="p-inline"
                        style="margin: 20px"
                    >
                        <span class="font-weight-bolder">
                            {{ $t('type.type.area') }}:
                        </span>
                        <span class="text-secondary">
                            {{ type.area }} m2
                        </span>
                    </p>

                    <div>
                        <span class="font-weight-bolder">
                            {{ $t('hotel.hotel.amenities') }}
                        </span>
                        <div class="test">
                            <ul
                                style="padding: 0; list-style-type: none"
                            >
                                <li
                                    v-for="(amenity, index) in type.amenities"
                                    :key="`${type.uuid}-amenity-${index}`"
                                >
                                    <img
                                        :src="getSrc(amenity)"
                                        :alt="amenity"
                                        class="icon"
                                    >
                                    {{ amenity }}
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </b-list-group-item>
        </b-list-group>
        <br>
        <b-pagination
            v-if="types.length > perPage"
            v-model="currentPage"
            :per-page="perPage"
            :total-rows="rows"
            pills
            aria-controls="types-list"
        />
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

export default {
    name: "Type",
    components: {TypeForm},
    data: function () {
        return {
            types: [],
            currentPage: 1,
            perPage: 10,
            rows: 0,
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
                this.rows = this.types.length
                this.types.sort(function (a,b) {
                    return new Date(a.created) - new Date(b.created)
                })
            })
    },
    methods: {
        formatPrice(price) {
            let temp = price.toString()
            let result = ''
            for (let i=temp.length - 1; i>=0; i--) {
                result = temp.charAt(i) + result
                if ((temp.length - i) % 3 === 0) {
                    result = "." + result
                }
            }
            if (result.charAt(0) === ".") {
                result = result.substring(1)
            }
            return result
        },
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
    margin: 10px 0;
    border-radius: 10px;
}
.p-inline {
    display: inline-block;
}
.icon {
    height: 30px;
    width: 30px;
}

.test ul {
    display: flex;
    flex-wrap: wrap;
    padding-left: 0;
}
.test ul li {
    list-style: none;
    flex: 0 0 20%;
}
</style>