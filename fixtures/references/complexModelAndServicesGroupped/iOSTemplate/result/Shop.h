#import <Foundation/Foundation.h>
import "Location.h"
import "Person.h"

@interface Shop : NSObject {
	NSString *id;
	Location *location;
	Person *owner;
}

@property (nonatomic, strong) NSString *id;
@property (nonatomic, strong) Location *location;
@property (nonatomic, strong) Person *owner;

@end

