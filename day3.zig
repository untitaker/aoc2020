const std = @import("std");
const math = std.math;
const maxInt = std.math.maxInt;
const binarySearch = std.sort.binarySearch;
const sort = std.sort;

pub fn main() !void {
    const stdout = std.io.getStdOut().outStream();
    try stdout.print("Part 1: {} trees\n", .{try run(3, 1)});
    try stdout.print("Part 2: {}\n", .{(try run(1, 1)) * (try run(3, 1)) * (try run(5, 1)) * (try run(7, 1)) * (try run(1, 2))});
}

fn run(skipColumns: u64, skipLines: u64) !u64 {
    const input = (try std.fs.cwd().openFile("day3.input.txt", .{})).reader();

    var xOffset: u64 = 0;
    var trees: u64 = 0;

    while (true) {
        var lineLength: u64 = 0;
        while (lineLength < xOffset) {
            _ = input.readByte() catch break;
            lineLength += 1;
        }

        const pos = input.readByte() catch break;
        lineLength += 1;
        if (pos == '#') {
            trees += 1;
        }

        // read to end of line
        while ((input.readByte() catch break) != '\n') {
            lineLength += 1;
        }

        var i: u64 = 1;
        while (i < skipLines) {
            while ((input.readByte() catch break) != '\n') {}
            i += 1;
        }

        xOffset = (xOffset + skipColumns) % lineLength;
    }

    return trees;
}
