function countletter(harf, str){
    let count = 0 
   let a = str.split('')
   for (i=0 ; a.length>i ; i++){
    if(a[i]==harf){
        count++
    }
    
   }
   return count
}
console.log(countletter('g' , 'engeee'))
