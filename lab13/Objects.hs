module Objects  
( Object(..)
, volume 
, area
) where  

data Object = Sphere Float
                | Cube Float
                | Cuboid Float Float Float

volume :: Object -> Float  
volume (Sphere r) = (4/3)*pi*r^3
volume (Cube x) = x^3
volume (Cuboid a b c) =  a * b * c


area :: Object -> Float  
area (Sphere r) = 4 * pi * r^2
area (Cube x) = 6 * x^2
area (Cuboid a b c) = (a * b * 2) + (a * c * 2) + (b * c * 2)