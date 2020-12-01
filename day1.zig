const std = @import("std");
const math = std.math;
const maxInt = std.math.maxInt;
const binarySearch = std.sort.binarySearch;
const sort = std.sort;

// This is the same as std.sort.asc except std's seems to be broken on zig 0.7
// (at least the one in homebrew spews "unable to evaluate constant expression")
fn sort_u64(context: void, lhs: u64, rhs: u64) bool {
    return lhs < rhs;
}

// The previous function signature can only be used for sorting, not for binary search (lol)
fn order_u64(context: void, lhs: u64, rhs: u64) math.Order {
    return math.order(lhs, rhs);
}

pub fn main() !void {
    var integers = std.ArrayList(u64).init(std.heap.c_allocator);

    const stdin = std.io.getStdIn().inStream();
    const stdout = std.io.getStdOut().outStream();

    var buf: [10]u8 = undefined;

    while (try stdin.readUntilDelimiterOrEof(buf[0..], '\n')) |line| {
        try integers.append(try parseU64(line, 10));
    }

    sort.sort(u64, integers.items, {}, sort_u64);

    for (integers.items) |value| {
        var value2: u64 = 2020;

        if (@subWithOverflow(u64, value2, value, &value2)) {
            continue;
        }

        if (binarySearch(u64, value2, integers.items, {}, order_u64)) |_| {
            try stdout.print("{} * {} = {}\n", .{ value, value2, value * value2 });
        }
    }

    for (integers.items) |value| {
        for (integers.items) |value2| {
            var value3: u64 = 2020;

            if (@subWithOverflow(u64, value3, value, &value3)) {
                continue;
            }

            if (@subWithOverflow(u64, value3, value2, &value3)) {
                continue;
            }

            if (binarySearch(u64, value3, integers.items, {}, order_u64)) |_| {
                try stdout.print("{} * {} * {} = {}\n", .{ value, value2, value3, value * value2 * value3 });
            }
        }
    }
}

// no int parsing in stdlib (lol)
fn parseU64(buf: []const u8, radix: u8) !u64 {
    var x: u64 = 0;

    for (buf) |c| {
        const digit = charToDigit(c);

        if (digit >= radix) {
            return error.InvalidChar;
        }

        // x *= radix
        if (@mulWithOverflow(u64, x, radix, &x)) {
            return error.Overflow;
        }

        // x += digit
        if (@addWithOverflow(u64, x, digit, &x)) {
            return error.Overflow;
        }
    }

    return x;
}

fn charToDigit(c: u8) u8 {
    return switch (c) {
        '0'...'9' => c - '0',
        'A'...'Z' => c - 'A' + 10,
        'a'...'z' => c - 'a' + 10,
        else => maxInt(u8),
    };
}
