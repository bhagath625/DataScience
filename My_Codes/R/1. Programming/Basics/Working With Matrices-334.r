## 2. Combining Vectors into Matrices ##

harvard <- c(1,1,1,1,3)
stanford <- c(2,9,3,4,10)
MIT <- c(3,3,2,2,1)
cambridge <- c(4,2,6,13,48)
oxford <- c(5,7,12,9,15)
columbia <- c(6,13,13,12,4)
uni_matrix <- rbind(harvard, stanford, MIT, cambridge, oxford, columbia)

## 3. Naming Matrix Rows and Columns ##

uni_matrix <- rbind(harvard, stanford, MIT, cambridge, oxford, columbia)
categories <- c("world_rank", "quality_of_education", "influence", "broad_impact" ,"patents")
colnames(uni_matrix) <- categories

## 4. Finding Matrix Dimensions ##

tuition <- c(43280,45000,45016,49350,28450,55161)
dim(uni_matrix)[1] == length(tuition)

## 5. Adding Columns to Matrices ##

tuition <- c(43280, 45000, 45016, 49350, 28450, 55161)
complete_matrix <- cbind(uni_matrix, tuition)

## 6. Indexing Matrices By Element ##

complete_matrix <- cbind(uni_matrix, tuition)
oxford_influence <- complete_matrix["oxford", "influence"]
cam_stan_patents <- complete_matrix[c("cambridge", "stanford"), "patents"]

## 7. Subsetting Matrices by Rows and Columns ##

oxford_rank <- complete_matrix["oxford",]
influence <- complete_matrix[,"influence"]
harv_mit_rank <- complete_matrix[c("harvard", "MIT"),]
influence_patents <- complete_matrix[,c("influence", "patents")]

## 8. Ranking Universites ##

world_rank_rank <- rank(complete_matrix[,"world_rank"])
quality_of_education_rank <- rank(complete_matrix[,"quality_of_education"])
influence_rank <- rank(complete_matrix[,"influence"])
broad_impact_rank <- rank(complete_matrix[,"broad_impact"])
patents_rank <- rank(complete_matrix[,"patents"])
tuition_rank <- rank(complete_matrix[,"tuition"])

## 9. Scoring and Ranking Universities ##

ranks_matrix <- rbind(world_rank_rank, quality_of_education_rank, influence_rank, broad_impact_rank, patents_rank, tuition_rank)
sum(ranks_matrix[,"harvard"])
sum(ranks_matrix[,"stanford"])
sum(ranks_matrix[,"MIT"])
sum(ranks_matrix[,"cambridge"])
sum(ranks_matrix[,"oxford"])
sum(ranks_matrix[,"columbia"])