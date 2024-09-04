document.addEventListener("DOMContentLoaded", function() {
    fetch('data/douban_movies.json')
        .then(response => response.json())
        .then(data => {
            const labels = data.map(item => item.title);
            const ratings = data.map(item => item.rating);

            const ctx = document.getElementById('barChart').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: '评分',
                        data: ratings,
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error:', error));
});