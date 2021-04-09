$(function () {
        // Enables popover
        $("[data-toggle=popover]").popover({
          container: "body",
          html: true,
          placement: "auto",
          trigger: "hover",
          content: function () {
            // get the url for the full size img
            var url = $(this).data("full");
            return '<img src="' + url + '">';
          },
        });
      });