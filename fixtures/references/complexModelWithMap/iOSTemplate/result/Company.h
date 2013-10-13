#import <Foundation/Foundation.h>
import "Person.h"
import "Location.h"
import "Shop.h"

@interface Company : NSObject {
	Person *ceo;
	NSDictionary *shops;
}

@property (nonatomic, strong) Person *ceo;
@property (nonatomic, strong) NSDictionary *shops;

@end

