const imageBox = document.getElementById('image-box') //사진편집기 나올 div박스
const imageForm = document.getElementById('image-form') //폼테그
const confirmBtn = document.getElementById('confirm-btn') //등록버튼

/*
const nameInput = document.getElementById('id_file')
const speciesInput = document.getElementById('id_file')
const sexInput = document.getElementById('id_file')
const neutralInput = document.getElementById('id_file')
const alertInput = document.getElementById('id_file')
const characterInput = document.getElementById('id_file')
const latitudeInput = document.getElementById('id_file')
const longitudeInput = document.getElementById('id_file')
*/
var nameInput = $('input[name=name]').val();
var speciesInput = $('input[name=species]').val();
var sexInput = $('input[name=sex]').val();
var neutralInput = $('input[name=neutral]').val();
var alertInput = $('input[name=alert]').val();
var characterInput = $('input[name=character]').val();
var latitudeInput = $('input[name=latitude]').val();
var longitudeInput = $('input[name=longitude]').val();

const imageInput = document.getElementById('id_file') //사진 넣는 파일선택 버튼


const csrf = document.getElementsByName('csrfmiddlewaretoken')


imageInput.addEventListener('change', ()=>{ //만약 파일이 선택된다면~

    const img_data = imageInput.files[0] //입력된 이미지 파일 정보 받아옴
    const url = URL.createObjectURL(img_data) //이미지의 웹상 url 생성
    
    imageBox.innerHTML = `<img src="${url}" id="image" width="700px">` //이미지 박스에 이미지 표시
    var $image = $('#image') //$:jquary기호 , #:id 기호

    $(imageInput).attr("disabled", true);

    //image 변수에 선택된 영역 값을 담는 것 같음
    $image.cropper({
        aspectRatio: 1 / 1
    });
    
    var cropper = $image.data('cropper'); 
    confirmBtn.addEventListener('click', ()=>{ //만약 버튼이 클릭된다면~ 
        cropper.getCroppedCanvas().toBlob((blob) => {
            console.log('confirmed')

            nameInput = $('input[name=name]').val();
            speciesInput = $('input[name=species]').val();
            sexInput = $('input[name=sex]:checked').val();
            neutralInput = $('input[name=neutral]:checked').val();
            alertInput = $('input[name=alert]:checked').val();
            characterInput = $('input[name=character]').val();
            latitudeInput = $('input[name=latitude]').val();
            longitudeInput = $('input[name=longitude]').val();

            const fd = new FormData();
            fd.append('csrfmiddlewaretoken', csrf[0].value)
            fd.append('photo', blob, 'my-image.png'); //폼데이터 객체에 이미지 정보 추가
            fd.append('name', nameInput)
            fd.append('species', speciesInput)
            fd.append('sex', sexInput)
            fd.append('neutral', neutralInput)
            fd.append('alert', alertInput)
            fd.append('character', characterInput)
            fd.append('latitude', latitudeInput)
            fd.append('longitude', longitudeInput)

            $.ajax({
                type:'POST',
                url: imageForm.action,
                enctype: 'multipart/form-data',
                data: fd,
                success: function(response){
                    console.log('success')
                    location.replace('http://127.0.0.1:8000/'); 
                },
                error: function(error){
                    console.log('error', error)
                },
                cache: false,
                contentType: false,
                processData: false,
            })
        })
    })
})