BEGIN {FS = ","}
{print $2,",",$3, $4, $5, $6}
