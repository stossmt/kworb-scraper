document.body.onload = initTable();

var header;
var tableData;
var isSortedAscending;

function initTable() {
    header = [
        'Pos', 
        'Pos+', 
        'Artist', 
        'Title', 
        'Spins', 
        'Spins+', 
        'Bullet', 
        'Bullet+', 
        'Aud', 
        'Aud+', 
        'Days', 
        'Pk'
    ];

    tableData = window.tableData
    isSortedAscending = new Array(header.length).fill(false);
    isSortedAscending[0] = true;

    renderTable();
}

function renderTable() {
    var table = document.createElement('table');
    table.setAttribute('id', 'kworb-table');

    for(var i=0 ; i<=tableData.length ; i++) {
        var row = table.insertRow(i);
        row.id = "row-" + i;

        for(var j=0 ; j<header.length ; j++) {
            var column = row.insertCell();
            column.id = "column-" + j;

            if(isHeaderCell(i)) {
                column.appendChild(document.createTextNode(header[j]));
                column.addEventListener('click', sortColumn);
            } else {
                column.appendChild(document.createTextNode(tableData[i-1][j+2]));
            }
            row.appendChild(column);
        }

        var div = document.querySelector('#kworb-table')
        if(div.firstChild) {
            div.removeChild(div.firstChild);
        }
        div.appendChild(table);
    }

    function isHeaderCell(i) {
        return i <= 0;
    }
}

function sortColumn(e) {
    var columnIndex = parseInt(e.target.id.split("-").pop()) + 2;
    tableData.sort(function(a,b) {
        if (a[columnIndex] === b[columnIndex]) {
            return 0;
        }
        else if(isSortedAscending[columnIndex-2] === false) {
            return (a[columnIndex] < b[columnIndex]) ? -1 : 1;
        }
        else {
            return (a[columnIndex] < b[columnIndex]) ? 1 : -1;            
        }
    });

    isSortedAscending[columnIndex-2] = !isSortedAscending[columnIndex-2];
    renderTable(); 
}