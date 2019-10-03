1. Data Structures
    ~~a. Items/Events/??? term - Description*, Status*, Scheduled*, Start Date/Time, End Date/Time, Est Duration, Queue/Bucket (foreign key w/ default)~~
    b. [Delay!] Buckets - Pending/Queue (is this a bucket or a binary status between scheduled?), Custom Lists, establish Item property as foreign key
    c. Function to initialize data (create default queue bucket, ???)
    d. Schedule structure
        i. Daily instances, maybe a dictionary?  Check to see if something exists you can leverage
        ii. For now, plan on 5PM -> 1 AM window; pre-segmented into 15min maybe?  Or could it be defined in raw minutes?
2. Functions
    ~~a. Add Item~~
        ...to Queue
        ...to Schedule
    b. ~~Schedule~~/Unschedule Item
    c. Change Item Status
    d. [!] Print Daily Schedule
    e. Assign to Bucket
3. Validations
    a. Item times do not overlap
    b. Duration matches start/end period (or offer to update)
    c. Handling for uncompleted items in the past (delay for some time to allow updates, then move back to queue)
    d. Scheduled item has start/end, queued item has duration