/**
 * Tyr servers timestamp is recorded as 5 hours behind real time.
 * This is because at that point, we trusted syslog's given time
 * which ended up being a local time!
 */
var lastTime = null;
java.nio.file.Files.lines(
  java.nio.file.Paths.get("/dev/stdin")
).map(function (line) {
    var currentTime = java.time.Instant.parse(line.substring(0, line.indexOf("\t")));
    if ( line.contains("tyr") ) {
        if ( currentTime.plusSeconds(100 * 60).isBefore(lastTime) ) {
            currentTime = currentTime.plusSeconds(5 * 60 * 60);
        }
    }
    var result = [java.time.format.DateTimeFormatter.ISO_INSTANT.format(currentTime),
        line.substring(line.indexOf("\t"))
    ].join("");
    lastTime = currentTime;
    return result;
})
.forEach(print);