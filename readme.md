# Marketo API
### Note:
- Hiện tại Swagger dùng Swagger UI 2.x, vẫn chưa update lên UI 3.x
- JWT Token không dùng được với Swagger vì nó ko include token đó vào header giống như DRF Token
- Viewset của DRF không hiện được FileField/ImageField(chưa tìm ra cách), nên hiện tại dùng APIView cho các API có FileField
- Reset sequence postgres:
`ALTER SEQUENCE store_id_seq RESTART WITH 3;`
- https://stackoverflow.com/questions/119312/urls-dash-vs-underscore
- Nên dùng thử django_cleanup để delete mấy tấm hình đi kèm vs instance
- Null has no effect on manytomany field
