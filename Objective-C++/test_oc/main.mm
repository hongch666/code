// main.mm
#import <Foundation/Foundation.h>
#include <iostream>

int main(int argc, const char * argv[]) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    NSLog(@"Hello, Objective-C++ World!");
    std::cout << "Hello, C++ World!" << std::endl;
    [pool drain];
    return 0;
}
