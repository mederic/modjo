#import <Foundation/Foundation.h>
import "Place.h"
import "Person.h"

@interface Shop : NSObject {
	Place *place;
	Person *owner;
	NSArray *employees;
	NSArray *customers;
}

@property (nonatomic, strong) Place *place;
@property (nonatomic, strong) Person *owner;
@property (nonatomic, strong) NSArray *employees;
@property (nonatomic, strong) NSArray *customers;

@end

