module days

data days = monday | tuesday | wednesday | thursday | friday | saturday | sunday

nextDay: days -> days
nextDay monday = tuesday
nextDay tuesday = wednesday
nextDay wednesday = thursday
nextDay thursday = friday
nextDay friday = saturday
nextDay saturday = sunday
nextDay _ = monday

nextWeekday: days -> days
nextWeekday monday = tuesday
nextWeekday tuesday = wednesday
nextWeekday wednesday = thursday
nextWeekday thursday = friday
nextWeekday _ = monday
