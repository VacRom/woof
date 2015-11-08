module Box

import eq
import serialize

data Box t = mkBox t

unbox: Box t -> t
unbox (mkBox b) = b

instance (eq a) => eq (Box a) where
  eql b1 b2 = eql (unbox b1) (unbox b2)
  
instance (serialize a) => serialize (Box a) where
  toString (mkBox b) = "(" ++ (toString b) ++ ")"


--equivalently
--eql (mkBox v1) (mkBox v2) = eql v1 v2
