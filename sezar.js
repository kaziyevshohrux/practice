
//console.log(a)
let c = [];
function sezar(num, word){
    for (i =0; word.length>i;i++){
        let a = ((word.charCodeAt(i))+num)
        c.push(String.fromCharCode(a))
        for (j=0;c.length>j;j++){
            if(c[j]=='$'){
                c[j]=' '
            }
        }
        
    }
    return c.join('')
    
}
console.log(sezar(4,'Abcm kjkz'))
//harf boradi index boyicha va 4+ qadam qoshilgach shu indexdagi harfdi oladi