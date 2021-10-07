const copyBtn = document.querySelector('.copy_btn');
const facebookShare = document.querySelector('.facebook_share');
const intention = document.querySelector('.intention');
const feedback = document.querySelector('.feedback');

const kakaoShare = document.querySelector('.kakao_share');
Kakao.init('1f7a70ed2e9d63f3495e5f7206857c98');
// Kakao.isInitialized();
// kakao developer에서 플랫폼 등록해야함(도메인 필요)

function sendLink(){
    let result_url = window.location.href;
    Kakao.Link.sendDefault({
        objectType:'feed',
        content:{
            title:'군생활 강도 측정기',
            description:'내 군생활 강도는?',
            imageUrl:'https://mbit.weniv.co.kr/static/img/mbit_thumbnail.png',
            link:{
                mobileWebUrl:'https://sugarcontentcheck-tubcs.run.goorm.io',
                webUrl:'https://sugarcontentcheck-tubcs.run.goorm.io',
            },
        },
        social:{
            likeCount:286,
            commentCount:45,
            sharedCount:845,
        },
        buttons:[
        {
            title:'결과 보러가기',
            link:{
                webUrl:result_url,
                mobileWebUrl:result_url,
            },
        },
        {
            title:'테스트 하러가기',
            link:{
                webUrl:'https://sugarcontentcheck-tubcs.run.goorm.io',
                mobileWebUrl:'https://sugarcontentcheck-tubcs.run.goorm.io',
            },
        },
        ],
    });
}


$(function(){
    let url = window.location.href
    let img = $('.result_img img').attr('src');
    
    $("meta[property='og\\:url']").attr('content',url)
    $("meta[property='og\\:image']").attr('content',image)
});

function copyUrl(){
    let tmp = document.createElement('input');
    let url = location.href;
    
    document.body.appendChild(tmp);
    tmp.value = url;
    tmp.select();
    document.execCommand("copy");
    document.body.removeChild(tmp);
    
    alert("URL이 복사되었습니다.");
}

function sharefacebook(){
    let url = location.href;
    let facebook = 'http://www.facebook.com/sharer/sharer.php?u=';
    let link = facebook + url;
    window.open(link);
    
}

function intention_alert(){    
    alert("재미로 만들었습니다.\n이용 중에 불편하신 내용, 보완하면 좋겠는 점이 있으시다면\n 아래의 피드백 버튼으로 보내주시면 정말 감사하겠습니다.");
}

copyBtn.addEventListener('click', copyUrl);
facebookShare.addEventListener('click', sharefacebook);
kakaoShare.addEventListener('click', sendLink);
intention.addEventListener('click', intention_alert);

// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById('myBtn');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName('close')[0];

// When the user clicks on the button, open the modal
btn.onclick = function () {
    modal.style.display = 'block';
};

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = 'none';
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
};