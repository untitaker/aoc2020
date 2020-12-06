#!/usr/bin/env runhaskell
import System.IO
import Debug.Trace
import qualified Data.Set as Set

run setInit setFunc = run2 setInit
    where
    run2 curSet [] = Set.size curSet
    run2 curSet ("":rest) = (Set.size curSet) + (run2 setInit rest)
    run2 curSet (line:rest) = run2 (setFunc curSet $ Set.fromList line) rest

main = do
    contents <- readFile "day6.input.txt"

    let part1 = run Set.empty Set.union $ lines contents
    putStrLn $ "part 1: " ++ (show part1)

    let part2 = run (Set.fromList ['a'..'z']) Set.intersection $ lines contents
    putStrLn $ "part 2: " ++ (show part2)
