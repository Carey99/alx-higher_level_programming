<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
    $(document).ready(function() {
        $('#btn_translate').click(function() {
            var languageCode = $('#language_code').val();
            var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode + '.json';

            $.getJSON(apiUrl, function(data) {
                var translation = data.hello;
                $('#hello').text(translation);
            });
        });
    });
</script>
