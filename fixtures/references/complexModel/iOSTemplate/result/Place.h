#import <Foundation/Foundation.h>
import "Location.h"

@interface Place : NSObject {
	Location *location;
	NSString *name;
}

@property (nonatomic, strong) Location *location;
@property (nonatomic, strong) NSString *name;

@end

