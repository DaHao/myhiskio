Stable Matching Problem

有 N 位男生，N 位女生，找到一個最穩定的配對狀態
何謂穩定配對？配對完後不存在一對男女喜歡對方更勝於目前配對

Perfect matching: 每個人都有配對，不一定是穩定配對

Stable Matching 演算法：
定義每個人有 3 種狀態：free(unmarried) 、engaged 、married
每個男/女有心中的好感排序名單
男生可對女生進行 proposed ，女生接受的話雙方進入 engaged


everyone status set to free
while ( man is free & 尚未對 woman proposed ) do
        woman = 最高好感 in man list & man 還沒 proposed
        if ( woman is free ) then
                ( man, woman ) set engaged
        else if ( woman is engaged but man rank high than current man ) then 
                current man set free
                ( man, woman ) set engaged
return result
