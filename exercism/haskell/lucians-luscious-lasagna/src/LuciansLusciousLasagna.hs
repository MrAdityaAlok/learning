module LuciansLusciousLasagna (elapsedTimeInMinutes, expectedMinutesInOven, preparationTimeInMinutes) where

expectedMinutesInOven :: Int
expectedMinutesInOven = 40

preparationTimeInMinutes :: Int -> Int
preparationTimeInMinutes numOfLayersToCook = numOfLayersToCook * 2 -- 2 minutes per layer

elapsedTimeInMinutes :: Int -> Int -> Int
elapsedTimeInMinutes numOfLayers minsLasganaInOven = minsLasganaInOven + preparationTimeInMinutes numOfLayers
