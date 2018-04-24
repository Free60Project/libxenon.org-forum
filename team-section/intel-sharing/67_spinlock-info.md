# Spinlock info

## 2011-04-20 13:48:28, posted by: tuxuser

by cOz [quote] // from the libsmb implementation...  
 ```
 #elif defined(POWERPC_SPINLOCKS)  
   
 static inline int __spin_trylock(spinlock_t *lock)  
 {  
    unsigned int result;  
   
    __asm__ __volatile__(  
    "1: lwarx %0,0,%1n  
    cmpwi 0,%0,0n  
    li %0,0n  
    bne- 2fn  
    li %0,1n  
    stwcx. %0,0,%1n  
    bne- 1bn  
    isyncn  
    2:" : "=&r"(result)  
    : "r"(lock)  
    : "cr0", "memory");  
   
    return (result == 1) ? 0 : EBUSY;  
 }  
   
 static inline void __spin_unlock(spinlock_t *lock)  
 {  
    asm volatile("eieio":::"memory");  
    *lock = 0;  
 }  
   
 static inline void __spin_lock_init(spinlock_t *lock)  
 {  
    *lock = 0;  
 }  
   
 static inline int __spin_is_locked(spinlock_t *lock)  
 {  
    return (*lock != 0);  
 }
 ```