const std = @import("std");
 
// 如果 `main` 不是 `pub` (public)，此代码将无法编译
pub fn main() void {
    const user = User{
        .power = 9001,
        .name = "Goku",
    };
 
    std.debug.print("{s}'s power is {d}\n", .{user.name, user.power});
}
 
pub const User = struct {
    power: u64,
    name: []const u8,
};