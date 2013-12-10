BEGIN{FS="|"}
{
if($0~/^>/)
{i++;
gsub(" PREDICTED:","",$5);
split($5,a," ");
gsub(">","",$0);gsub(" ","|",$0);
print ">"i"|"substr(a[1],1,5)"|"substr(a[2],1,6)"|"$0
}
else{print}
} 

