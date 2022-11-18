
var chart = c3.generate({
    bindto: '.tn_chrat',
    data: {
        columns: [
            ['이용자 평균점수', 30, 90, 30, 40, 10, 15], //차트명, 차트별 value
            ['진단결과', 50, 100, 40, 50, 20, 45],
        ],
        type: 'bar', //차트타입
        colors: {
            '이용자 평균점수': '#9a9a9a', //차트의 color
            '진단결과': '#f73718'
        }
    },
    grid: {
        y: {
            show: true // 선여부
        },
    },
    bar: {
        width: {
            ratio: 0.3
        }
    },
    axis: {
        x: {
            type: 'category', //그룹 막대일 때 지정
            categories: ['종합', '필요성', '태도', '신념', '심리상태', '기술'],
        },
        y: {
            max: 100, //최대값
            min: 0, //최소값
            padding: {
                top: 0,
                bottom: 0
            },
            tick: {
                count: 6
            }
        },

    },
    tooltip: { // 툴팁 여부
        show: false
    },
    legend: { //범례여부
        show: false
    },
    padding: {
        bottom: 20,
        top: 20
    }


});