#!/usr/bin/env runhaskell
import System.IO
import Control.Monad
import Data.List (foldl', find, sort)
import Data.Maybe (fromJust)

bin 'F' = 0
bin 'L' = 0
bin 'R' = 1
bin 'B' = 1

seatId :: String -> Int
seatId = foldl' (\acc x -> acc * 2 + bin x) 0

pairs (x:xs) = zip (x:xs) xs

main = do
    contents <- readFile "day5.input.txt"
    let seatIds = sort $ map seatId $ words contents

    let part1 = maximum seatIds
    putStrLn ("part 1: " ++ (show part1))

    let (a, _) = fromJust $ find (\(a, b) -> a == b - 2) $ pairs seatIds
    let part2 = a + 1
    putStrLn ("part 2: " ++ (show part2))
