<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<script>
    $(document).ready(function() {
        $('#btn_translate').click(function() {
            translateHello();
        });

        $('#language_code').keypress(function(event) {
            if (event.which === 13) {
                translateHello();
            }
        });

        function translateHello() {
            var languageCode = $('#language_code').val();
            var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';

            $.getJSON(apiUrl + languageCode, function(data) {
                $('#hello').text(data.hello);
            });
        }
    });
</script>
