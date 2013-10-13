#import <Foundation/Foundation.h>
import "Location.h"

@interface Trip : NSObject {
	NSDate *from;
	NSDate *to;
	Location *location;
}

@property (nonatomic, strong) NSDate *from;
@property (nonatomic, strong) NSDate *to;
@property (nonatomic, strong) Location *location;

@end

