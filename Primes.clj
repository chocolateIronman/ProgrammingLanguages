(defn get-divisors [n]
  (range 2 (+ (Math/floor (Math/sqrt n)) 1))
)

;(println(get-divisors 101))
;(println(get-divisors 4))


(defn divides? [x n]
  (if (=(mod n x) 0)
    true
    false
  )
)

;(println (divides? 2 10))
;(println (divides? 4 10))

(defn swapper [x n]
  (divides? n x)
  )


(defn no-divisors? [n]
  (not (contains? (set (map (partial swapper n) (get-divisors n))) true))
)

;(println(no-divisors? 9))
;(println(no-divisors? 7))

(defn is-prime? [n]
  (if (= n 1)
    false
    (if (= n 2)
      true
      (no-divisors? n)
    )
  )
)

;(println(is-prime? 1))
;(println(is-prime? 2))
;(println (is-prime? 3))
;(println (is-prime? 4))
;(println (is-prime? 101))

(defn prime-seq [a b]
  ( filter is-prime? (range a (inc b)))
)

;(println(prime-seq 50 100))
;(println(prime-seq 7 11))

(defn print-top-primes [a b]
  (def primes (take-last 10 (prime-seq a b)))
  (run! println (reverse primes))
  (reduce + primes)
)

;(println "Total=" (print-top-primes 50 100))
;(println "Total=" (print-top-primes 7 11))
