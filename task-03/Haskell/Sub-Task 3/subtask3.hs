import Control.Monad (forM_)
printDiamond :: Int -> IO ()
printDiamond n = do
    forM_ [0..n-1] $ \i -> putStrLn $ replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*'
    forM_ [n-2,n-3..0] $ \i -> putStrLn $ replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*'

main = do
    putStrLn "Enter a number: "
    n <- readLn
    printDiamond n