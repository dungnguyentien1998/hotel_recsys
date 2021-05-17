from app.views import *
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('login', Login.as_view(), name='user.login'),
    path('register', Register.as_view(), name='user.register'),
    # path('activate', ActivateAccount.as_view(), name='user.activate'),
    path('forgot-password', ForgotPassword.as_view(), name='user.forgot'),
    path('users/account', Account.as_view(), name='user.account'),
    path('users/change-password', ChangePassword.as_view(), name='user.change_password'),
    path('users/<user_id>', UserDetail.as_view(), name='user.detail'),
    path('admin/users', User.as_view(), name='user.manage'),
    path('admin/hotels/<hotel_id>', HotelActive.as_view(), name='hotel.manage'),
    path('hotels', Hotel.as_view(), name='hotel'),
    path('hotels/<hotel_id>', HotelDetail.as_view(), name='hotel.detail'),
    path('hotels/<hotel_id>/types', Type.as_view(), name='type'),
    path('hotels/<hotel_id>/types/<type_id>', TypeDetail.as_view(), name='type.detail'),
    path('hotels/<hotel_id>/rooms', Room.as_view(), name='room'),
    path('hotels/<hotel_id>/rooms/<room_id>', RoomDetail.as_view(), name='room.detail'),
    path('hotels/<hotel_id>/reviews', Review.as_view(), name='review'),
    path('hotels/<hotel_id>/reviews/<review_id>', ReviewDetail.as_view(), name='review.detail'),
    path('hotels/<hotel_id>/complaints', Complaint.as_view(), name='complaint'),
    path('hotels/<hotel_id>/complaints/<complaint_id>', ComplaintDetail.as_view(), name='complaint.detail'),
    path('bookings', Booking.as_view(), name='booking'),
    path('bookings/<booking_id>', BookingDetail.as_view(), name='booking.detail'),
    path('favorites', Favorite.as_view(), name='favorites.get'),
    path('favorites/<favorite_id>', Favorite.as_view(), name='favorites.delete'),
    path('hotels/<hotel_id>/favorites', Favorite.as_view(), name='favorite.create'),
    path('hotels/<hotel_id>/favorites/<favorite_id>', FavoriteDetail.as_view(), name='favorite.delete'),
    path('recommendations', Recommendation.as_view(), name='recommendations'),
    path('hotels/<hotel_id>/recommendations', RecommendationDetail.as_view(), name='hotel.recommendations'),
    # path('hotels/<hotel_id>/bookings', HotelierBooking.as_view(), name='hotel.bookings'),
    path('new_bookings', NewBooking.as_view(), name='new_booking'),
    path('new_bookings/<booking_id>', NewBookingDetail.as_view(), name='new_booking.detail'),
    path('hotels/<hotel_id>/new_bookings', NewHotelierBooking.as_view(), name='hotel.new_bookings'),
    path('hotels/<hotel_id>/new_bookings/<booking_id>', NewHotelierBookingDetail.as_view(), name='hotel.new_booking'),
]
