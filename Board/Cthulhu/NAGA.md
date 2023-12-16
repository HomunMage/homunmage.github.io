---
layout: default
---

# NAGA

<head>
    <title>My Chart</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>

<body>
  <div><canvas id="myChart"></canvas></div>
  <br>
  <div><table id="csvTable"></table></div>
</body>

<style>
#myChart {
    width: 100%;   /* This will make the chart take up the full width of its container */
    height: 300px; /* This will make the chart 300 pixels high */
}
</style>

<script>
// Function to parse CSV data
function parseCSV(data) {
    const rows = data.split('\n');
    let dates = [];
    let matchRates = [];
    let similarity = [];
    let badHandRates = [];
    let Rs = [];

    // Skip the first row (headers)
    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].split(',');

        dates.push(cells[0]);
        matchRates.push(parseFloat(cells[1]));
        similarity.push(parseFloat(cells[2]));
        badHandRates.push(parseFloat(cells[3]));
        Rs.push(parseInt(cells[4]));
    }

    return {dates, matchRates, similarity, badHandRates, Rs};
}

// Function to parse CSV data and create an HTML table
function createTable(data) {
    const table = document.getElementById('csvTable');

    // Create header row
    const headerRow = document.createElement('tr');
    const headers = ['日期', '一致率', '類似度', '惡手率', 'R'];
    for (const header of headers) {
        const th = document.createElement('th');
        th.textContent = header;
        headerRow.appendChild(th);
    }
    table.appendChild(headerRow);

    // Create data rows
    for (let i = 0; i < data.dates.length; i++) {
        const row = document.createElement('tr');

        let dateCell = document.createElement('td');
        let matchRateCell = document.createElement('td');
        let similarityCell = document.createElement('td');
        let badHandRateCell = document.createElement('td');
        let RCell = document.createElement('td');

        dateCell.textContent = data.dates[i];
        matchRateCell.textContent = data.matchRates[i];
        similarityCell.textContent = data.similarity[i];
        badHandRateCell.textContent = data.badHandRates[i];
        RCell.textContent = data.Rs[i];

        row.appendChild(dateCell);
        row.appendChild(matchRateCell);
        row.appendChild(similarityCell);
        row.appendChild(badHandRateCell);
        row.appendChild(RCell);

        table.appendChild(row);
    }
}

// Function to load the CSV file using XMLHttpRequest
function loadCSV(file) {
    const xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            const data = parseCSV(xhr.responseText);
            // Reverse the data for the chart, but use the original data for the table
            const reversedData = {
                dates: [...data.dates].reverse(),
                matchRates: [...data.matchRates].reverse(),
                similarity: [...data.similarity].reverse(),
                badHandRates: [...data.badHandRates].reverse(),
                Rs: [...data.Rs].reverse()
            };
            drawChart(reversedData);
            createTable(data);
        }
    };

    xhr.open('GET', file, true);
    xhr.send();
}

function drawChart(data) {
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        maintainAspectRatio: false,
        type: 'line',
        data: {
            labels: data.dates,
            datasets: [
                {
                    label: '一致率',
                    data: data.matchRates,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1,
                    yAxisID: 'y-axis-1',
                    tension: 0.4  // This line added
                },
                {
                    label: '類似度',
                    data: data.similarity,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    yAxisID: 'y-axis-1',
                    tension: 0.4  // This line added
                },
                {
                    label: '惡手率',
                    data: data.badHandRates,
                    borderColor: 'rgba(255, 206, 86, 1)',
                    borderWidth: 1,
                    yAxisID: 'y-axis-1',
                    tension: 0.4  // This line added
                },
                {
                    label: 'R',
                    data: data.Rs,
                    borderColor: 'rgba(153, 102, 255, 1)',
                    borderWidth: 1,
                    yAxisID: 'y-axis-2',
                    tension: 0.4  // This line added
                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    id: 'y-axis-1',
                    type: 'linear',
                    position: 'left',
                    beginAtZero: true
                }, {
                    id: 'y-axis-2',
                    type: 'linear',
                    position: 'right',
                    beginAtZero: true,
                    grid: {
                        drawOnChartArea: false
                    },
                }]
            }
        }
    });
}

// Call the loadCSV function with the path to your CSV file
loadCSV('./NAGA.csv');
</script>
