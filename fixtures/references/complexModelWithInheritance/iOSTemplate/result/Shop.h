#import <Foundation/Foundation.h>
import "Person.h"

@interface Shop : NSObject {
	Person *owner;
	NSArray *employees;
	NSArray *customers;
}

@property (nonatomic, strong) Person *owner;
@property (nonatomic, strong) NSArray *employees;
@property (nonatomic, strong) NSArray *customers;

@end

