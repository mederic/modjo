#import <Foundation/Foundation.h>

@interface Person : NSObject {
	NSString *firstname;
	NSString *lastname;
	NSDate *birthdate;
}

@property (nonatomic, strong) NSString *firstname;
@property (nonatomic, strong) NSString *lastname;
@property (nonatomic, strong) NSDate *birthdate;

@end

