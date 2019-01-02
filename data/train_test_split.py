
ROOT_DIR='ml-1m/ratings.dat'

OUTPUT_DIR_TRAIN='ml-1m/train.dat'
OUTPUT_DIR_TEST='ml-1m/test.dat'


NUM_USERS=6040
NUM_TEST_RATINGS=10


def _count_rating_per_user():
    
    rating_per_user={}
    user_counter=1
    rating_counter=0
    
    for line in open(ROOT_DIR):
        
        line=line.split('::')
        user_nr=int(line[0])
        
        if user_nr==user_counter and user_nr != NUM_USERS:
            rating_counter+=1
        else:
            rating_per_user[user_counter]=rating_counter
            user_counter+=1      
            rating_counter=1

    return rating_per_user
            
                 
def _train_test_split():
    
    user_rating=_count_rating_per_user()
    temp_user=0
    test_counter=0
    
    train_writer=open(OUTPUT_DIR_TRAIN, 'w')
    test_writer=open(OUTPUT_DIR_TEST, 'w')
    
    for line in open(ROOT_DIR):
        
        splitted_line=line.split('::')
        user_nr=int(splitted_line[0])
        
        try:   
            if temp_user!=user_nr:
                write_test_samples=True
                temp_user=user_nr
                
            if user_rating[user_nr]<=NUM_TEST_RATINGS*2:
                continue
            else:
                
                if write_test_samples==True:
                    test_writer.write(line)
                    test_counter+=1
                    if test_counter>=NUM_TEST_RATINGS:
                        test_counter=0
                        write_test_samples=False        
                elif write_test_samples==False:
                    train_writer.write(line)
        
        except KeyError:   
            print('Key not found')
            continue
_train_test_split()          
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                