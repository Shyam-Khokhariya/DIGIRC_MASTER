const formatGroup=(a,b)=>(c,d)=>{for(var e=c.length,f=[],h=0,k=a[0],l=0;0<e&&0<k&&(l+k+1>d&&(k=Math.max(1,d-l)),f.push(c.substring(e-=k,e+k)),!((l+=k+1)>d));)k=a[h=(h+1)%a.length];return f.reverse().join(b)};export default formatGroup;