1. Data Structures

   1. ~~Items/Events/??? term - Description*, Status*, Scheduled*, Start Date/Time, End Date/Time, Est Duration, Queue/Bucket (foreign key w/ default)~~
   2. [Delay!] Buckets - Pending/Queue (is this a bucket or a binary status between scheduled?), Custom Lists, establish Item property as foreign key
   3. Function to initialize data (create default queue bucket, ???)
   4. Schedule structure
   
      1. Daily instances, maybe a dictionary?  Check to see if something exists you can leverage
      2. For now, plan on 5PM -> 1 AM window; pre-segmented into 15min maybe?  Or could it be defined in raw minutes?
2. Functions
   1. ~~Add Item~~
        ...to Queue
        ...to Schedule
   2. ~~Schedule~~/Unschedule Item
   3. Change Item Status
   4. [!] Print Daily Schedule
   5. Assign to Bucket
3. Validations
   0. Item times do not overlap
   0. Duration matches start/end period (or offer to update)
   0. Handling for uncompleted items in the past (delay for some time to allow updates, then move back to queue)
   0. Scheduled item has start/end, queued item has duration