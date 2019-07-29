module Main where

mod3or5 :: Int -> Int
mod3or5 number =
  if number `mod` 3 == 0 || number `mod` 5 == 0
    then number
  else
    0

-- with map
sumMap :: Int -> Int
sumMap number = sum (map mod3or5 [1..number])

-- with list comprehension
sumComp :: Int -> Int
sumComp number =
  sum [mod3or5 x | x <- [1..number]]

-- pattern matching & recursion
sumPattern :: [Int] -> Int
sumPattern [] = 0
sumPattern (x:xs) = mod3or5 x + sumPattern xs


main :: IO ()
main = do
  let sum = sumComp 999
  putStrLn (show (sum == 233168))

  let sum2 = sumPattern [1..999]
  putStrLn (show (sum2 == 233168))

  let sum3 = sumMap 999
  putStrLn (show (sum3 == 233168))
