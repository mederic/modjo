#import <Foundation/Foundation.h>
import "Person.h"
import "Shop.h"

@interface Company : NSObject {
	Person *ceo;
	NSArray *shops;
}

@property (nonatomic, strong) Person *ceo;
@property (nonatomic, strong) NSArray *shops;

@end

