
# Sample data of point 1.
v1 = c(0.8, 1.5, 1.7, 2.6, 3.9)
v2 = c(1.1, 2.2, 1.6, 2.6, 3.8)
plot(v1,v2, xlim=c(0,5), ylim=c(0,5))
abline(0,1)


# 3. Calculate the median of a vector

my.median <- function(v){
    v = sort(v)
    L = length(v)
    half = round(L/2)
    if (L %% 2 == 0){   # even length
        return( 0.5*(v[half]+v[half+1]) )
    } else {            # odd length
        return( v[half+1] )
    }
}


# 4. Normalize two vectors by quantiles

quantile.norm.2vec <- function(a,b){
    a.order = order(a)
    b.order = order(b)
    a.sorted = sort(a)
    b.sorted = sort(b)
    avg = 0.5 * (a.sorted + b.sorted)
    a.new = avg[a.order]
    b.new = avg[b.order]
    return(list(a.new,b.new))
}

# Test on sample data from point 1.
result = quantile.norm.2vec(v1,v2)
v1.norm = result[[1]]
v2.norm = result[[2]]
plot(v1.norm, v2.norm, xlim=c(0,5), ylim=c(0,5))
abline(0,1)


# 5. Check with longer random vectors

v1 = runif(2000)
v2 = runif(2000)
result = quantile.norm.2vec(v1,v2)
v1.norm = result[[1]]
v2.norm = result[[2]]
print(my.median(v1.norm) == my.median(v2.norm))


