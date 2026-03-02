module Pangram (isPangram) where

import Data.Char (toLower)

isPangram :: String -> Bool
isPangram text = all (`elem` map toLower text) ['a'..'z']

-- How does this work?
-- > :t all
-- all :: Foldable t => (a -> Bool) -> t a -> Bool
--
-- So, all takes a unary function that returns a bool, and a Foldable (like list). It
-- then applies the function to every element in the Foldable and returns True if all
-- values returned by that unary function is True.
