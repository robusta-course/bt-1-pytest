Feature: Kiểm thử API cộng số

Scenario: Kiểm thử cộng số 2 và 3
    Given tôi truy cập vào API cộng số
    When tôi gửi yêu cầu GET tới '/add/2/3'
    Then tôi nhận được kết quả "5"
