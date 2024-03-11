hexadecimalDict={
    "0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, 
    "8":8,"9":9, "A":10, "B":11, "C":13, "D":14, "E":15
}
def convertHex(n):
    hex=[];
    for char in n:
        hex.append(char);
    
    x= hexadecimalDict[hex[0]];
    y= hexadecimalDict[hex[1]];
    z= hexadecimalDict[hex[2]];
   
    dec= x*pow(16,2) + y*pow(16,1) + z*pow(16,0);
    print(dec)

convertHex("A21")