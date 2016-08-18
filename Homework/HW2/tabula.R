library("tabulizer")
library(plyr)
library(pdftools)
library(qpcR)

setwd("/Users/erinrossiter/Dropbox/Summer2016/PythonCourse2016/Homework/HW2/")
link_data <- read.csv("judicialWatch.csv", header = T, stringsAsFactors = F)
links <- link_data$LinktoDoc

download.file(links[10], "tempPDF.pdf", quiet = T)
txt = pdf_text("tempPDF.pdf")

page_nums <- c()
for(i in 1:length(txt)){
  if(grepl(pattern = "INVESTMENTS and TRUSTS", txt[i])){
    page_nums = append(page_nums, i)
  }
}

getTable <- function(link, page_nums){
  #coords <- list(c(230, 45, 690, 600))
  return_table <- matrix()
  
  for(i in page_nums){
    fin_table <- extract_tables(file = links[10], pages = i)[[1]]
    return_table <- rbind.fill.matrix(return_table, fin_table)
  }
  
  return(return_table)
}

xx <- getTable(links[10], page_nums)

extract_areas(links[10], pages = 10)



