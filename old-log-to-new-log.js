java.nio.file.Files.lines(
  java.nio.file.Paths.get("/dev/stdin")
).map(function (line) {
    var time = line.substring(0, line.indexOf(" "))
    var payload = line.substring(line.indexOf(" ") + 1);
    var instant = java.time.LocalDateTime.parse(time).atZone(java.time.ZoneId.of("Europe/Paris")).toInstant()
    var newTimeStr = java.time.format.DateTimeFormatter.ISO_INSTANT.format(instant);
    return [newTimeStr, "aura.woop.ac:10000", payload].join("\t");
})
.forEach(print);
