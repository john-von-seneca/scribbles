val orig = 36220; //362.2 in cents
var res = 0
val ITERS = args(0).toInt

def time[R](block: => R): R = {
  val t0 = System.nanoTime()
  val result = block    // call-by-name
  val t1 = System.nanoTime()
  val t_diff = t1 - t0
  println("Elapsed time: " + t_diff + " ns :: " + t_diff/1000.0/1000.0/1000.0 + " s" )
  result
}

                    // Now wrap your method calls, for example change this...
                    // val result = 1 to 1000 sum
                    // ... into this
                    // val result = time { 1 to 1000 sum }

val time_taken =
time {
    for ( i <- 1.to(ITERS) ) {
            val result = Math.round( orig * i )
                    if ( result != 543 ) res += 1    //compare with something
                        }
                        }

println("time elapsed: " + time_taken + " ms")


val orig_bd = BigDecimal(362.2)
val mult_bd = BigDecimal(0.015)
res = 0

val time_taken_bd =
time {
    for ( i <- 1.to(ITERS) ) {
            val result = orig_bd * mult_bd
            if ( result != 543 ) res += 1    //compare with something
    }
}

println("time elapsed: " + time_taken_bd+ " ms")
