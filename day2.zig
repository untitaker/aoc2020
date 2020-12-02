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
    const stdin = std.io.getStdIn().inStream();
    const stdout = std.io.getStdOut().outStream();

    var buf: [10]u8 = undefined;

    var validPasswords1: u64 = 0;
    var validPasswords2: u64 = 0;

    while (true) {
        const lower = try parseU64((try stdin.readUntilDelimiterOrEof(buf[0..], '-')) orelse break, 10);
        const upper = try parseU64((try stdin.readUntilDelimiterOrEof(buf[0..], ' ')) orelse break, 10);
        const char = ((try stdin.readUntilDelimiterOrEof(buf[0..], ' ')) orelse break)[0];

        try stdout.print("{}-{} {c}:", .{ lower, upper, char });

        var charCount: u64 = 0;
        var hasCharacterAtOnePosition: bool = false;

        var i: u64 = 0;

        while (true) {
            i += 1;

            const passwordChar = stdin.readByte() catch break;
            try stdout.print("{c}", .{passwordChar});

            if (passwordChar == '\n') {
                break;
            }

            if (passwordChar == char) {
                charCount += 1;

                if (i == lower or i == upper) {
                    hasCharacterAtOnePosition = !hasCharacterAtOnePosition;
                }
            }
        }

        if (lower <= charCount and charCount <= upper) {
            validPasswords1 += 1;
        }

        if (hasCharacterAtOnePosition) {
            validPasswords2 += 1;
        }
    }

    try stdout.print("found {} valid passwords according to old policy (part 1)\n", .{validPasswords1});
    try stdout.print("found {} valid passwords according to new policy (part 2)\n", .{validPasswords2});
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
