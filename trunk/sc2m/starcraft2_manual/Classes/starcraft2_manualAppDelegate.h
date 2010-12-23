//
//  starcraft2_manualAppDelegate.h
//  starcraft2 manual
//
//  Created by lich0079 on 10-8-4.
//  Copyright ibm 2010. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface starcraft2_manualAppDelegate : NSObject <UIApplicationDelegate, UITabBarControllerDelegate> {
    UIWindow *window;
    UITabBarController *tabBarController;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;
@property (nonatomic, retain) IBOutlet UITabBarController *tabBarController;

@end
