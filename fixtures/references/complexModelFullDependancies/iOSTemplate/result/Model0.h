#import <Foundation/Foundation.h>
import "Model1.h"
import "Model2.h"
import "Model4.h"
import "Model3.h"

@interface Model0 : NSObject {
	Model1 *test1;
	NSArray *test2;
	NSDictionary *test3;
}

@property (nonatomic, strong) Model1 *test1;
@property (nonatomic, strong) NSArray *test2;
@property (nonatomic, strong) NSDictionary *test3;

@end

