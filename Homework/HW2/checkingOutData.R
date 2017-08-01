setwd("/Users/erinrossiter/Dropbox/Summer2016/PythonCourse2016/Homework/HW2/")

## reading in each data set
fin_disclosures <- read.csv("judicialWatch.csv",
                            header = TRUE,
                            stringsAsFactors = FALSE)
fin_disclosures <- fin_disclosures[ ,1:4]

fed_judges <- read.csv("federalJudges.csv",
                        header = TRUE,
                        stringsAsFactors = FALSE)

## how many judges?
num_judges = length(unique(fin_disclosures$Name))

## avg.. how many reports per judge?
nrow(fin_disclosures) / num_judges

## reports for years 2003 - 2012
sort(unique(fin_disclosures$Year))

## I don't know the year of only 2
length(which(fin_disclosures$Year == 0))

## How many reports per year?
reports_yearly <- sapply(unique(fin_disclosures$Year), function(x){
  length(which(fin_disclosures$Year == x))
})
names(reports_yearly) <- unique(fin_disclosures$Year)





#####################
library("tabulizer")
library(plyr)
library(pdftools)
library(qpcR)
library(doMC)

links <- fin_disclosures$LinktoDoc


find_table <- function(x){
  # out <- tryCatch(
  #   {
      rand_num = sample(1:1000, 1)
      file_name = paste0("tempPDF", rand_num, ".pdf")
      download.file(x, file_name, quiet = T)
      txt = pdf_text(file_name)
      unlink(file_name)
      
      # page_nums <- c()
      # if(length(txt) != 0){
      #   for(i in 1:length(txt)){
      #     if(grepl(pattern = "INVESTMENTS and TRUSTS", ignore.case = TRUE, txt[i])){
      #       page_nums = append(page_nums, i)
      #     }
      #   }
      # }
      # return(page_nums)
      
      return(txt)
      
      
  #   },
  #   error = function(cond) {
  #     message("Here's the original error message:")
  #     message(cond)
  #     return(NULL)
  #   },
  #   warning = function(cond) {
  #     message("Here's the original warning message:")
  #     message(cond)
  #     return(NULL)
  #   },
  #   finally = {
  #     message(paste("Processed Link:", x))
  #   }
  # )
  # return(out)
}


xx <- find_table(links[1])
xx[1]

#registerDoMC(5)
table_pages <- alply(links[1:50], 1, .fun = find_table, .parallel = FALSE)

## How many are null/didn't find "INVESTMENTS AND TRUSTS"
sum(laply(table_pages, is.null))





