
$(document).ready(function () {
    $(".content-markdown").each(function () {
        let content = $(this).text() // The markdown content
        trimmed_content = $.trim(
            content) // White spaces seemed to add <pre> tags. So removing whitespaces
        let markedContent = marked(
            trimmed_content) // converting to HTML using the marked JS lib function
        $(this).html(markedContent) // display the converted HTML
    })
})
