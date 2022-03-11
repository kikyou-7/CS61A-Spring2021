(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
    (if (null? (cdr s))
        null 
        (car (cdr s))
    )
)

(define (caddr s) 
    (if (null? (cddr s))
        null 
        (car (cddr s))
    )
)

(define (sign val) 
    (cond((= 0 val) 0)
         ((> 0 val) -1)
         (#t 1)
    )
)

(define (square x) (* x x))
;qucik pow by recusive
(define (pow base exp) 
    (cond ((= 0 exp) 1)
          ((odd? exp) (* base (pow (square base) (quotient exp 2))))
          ( (even? exp) ( pow (square base) (quotient exp 2) ) )
    )

)
