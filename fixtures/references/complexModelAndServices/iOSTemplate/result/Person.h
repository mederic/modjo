#import <Foundation/Foundation.h>

@interface Person : NSObject {
	NSString *id;
	NSString *firstname;
	NSString *lastname;
	NSDate *birthdate;
	BOOLisAMan;
}

@property (nonatomic, strong) NSString *id;
@property (nonatomic, strong) NSString *firstname;
@property (nonatomic, strong) NSString *lastname;
@property (nonatomic, strong) NSDate *birthdate;
@property (assign) BOOL isAMan;

@end

