module Main where

fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib(n - 1) + fib(n - 2)

sumEven :: Int -> Int
sumEven maximum = sum (takeWhile (<maximum) (filter even (map (fib) [1..])))

main :: IO ()
main = do
  let sum = sumEven 4000000
  putStrLn (show (sum == 4613732))
