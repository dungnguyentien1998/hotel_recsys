export default {
    // Hotel status and list
    status: state => state.status,
    hotels: state => state.hotels,
    notify_hotels: state => state.notify_hotels,
    count_hotelier: state => state.count_hotelier,
    old_count_hotelier: state => state.old_count_hotelier,
    count: state => state.count,
    name: state => state.name,
    city: state => state.city,
    district: state => state.district,
    ward: state => state.ward,
    star: state => state.star,
    amenities: state => state.amenities,
    page: state => state.page,
    is_search: state => state.is_search,
}