#import <Foundation/Foundation.h>
import "Location.h"

@interface Country : NSObject {
	NSDictionary *cities;
}

@property (nonatomic, strong) NSDictionary *cities;

@end

