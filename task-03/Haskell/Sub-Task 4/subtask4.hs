import System.IO
import Control.Monad (forM_)

printDiamond :: Int -> String
printDiamond n = unlines $ map (\i -> replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*') [0..n-1] ++ map (\i -> replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*') [n-2,n-3..0]

main = do
    input <- readFile "input.txt"
    let n = read input :: Int
    writeFile "output.txt" (printDiamond n)