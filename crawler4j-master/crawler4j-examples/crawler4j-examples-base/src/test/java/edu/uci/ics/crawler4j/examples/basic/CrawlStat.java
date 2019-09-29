package edu.uci.ics.crawler4j.examples.basic;

public class CrawlStat {
    private int totalProcessedPages;
    private long totalLinks;
    private long totalTextSize;

    public int getTotalProcessedPages() {
        return totalProcessedPages;
    }

    public void setTotalProcessedPages(int totalProcessedPages) {
        this.totalProcessedPages = totalProcessedPages;
    }

    public void incProcessedPages() {
        this.totalProcessedPages++;
    }

    public long getTotalLinks() {
        return totalLinks;
    }

    public void setTotalLinks(long totalLinks) {
        this.totalLinks = totalLinks;
    }

    public void incTotalLinks(int count) {
        this.totalLinks += count;
    }

//    public long getTotalTextSize() {
//        return totalTextSize;
//    }
//
//    public void setTotalTextSize(long totalTextSize) {
//        this.totalTextSize = totalTextSize;
//    }
//
//    public void incTotalTextSize(int count) {
//        this.totalTextSize += count;
//    }


}