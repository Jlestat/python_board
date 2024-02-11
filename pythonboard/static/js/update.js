document.getElementById('editPostButton').addEventListener('click', function() {
    document.getElementById('postContent').style.display = 'none';
    document.getElementById('editPostForm').style.display = 'block';
});

document.getElementById('editPostForm').addEventListener('submit', function(e) {
    e.preventDefault();

    var formData = new FormData(this);
    formData.append('csrfmiddlewaretoken', '{{ csrf_token }}');

    fetch('/path/to/edit/view/{{ post.id }}/', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('postContent').style.display = 'block';
        document.getElementById('editPostForm').style.display = 'none';
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

