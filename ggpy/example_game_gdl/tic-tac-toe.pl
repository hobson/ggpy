<- role(xplayer)
<- role oplayer
<- init (cell 1 1 blank)
<- init (cell 1 2 blank)
<- init (cell 1 3 blank)
<- init (cell 2 1 blank)
<- init (cell 2 2 blank)
<- init (cell 2 3 blank)
<- init (cell 3 1 blank)
<- init (cell 3 2 blank)
<- init (cell 3 3 blank)
<- init (control xplayer)
<- (legal ?player (mark ?m ?n))
<-     (true (cell ?m ?n blank))
<-     (true (control ?player))
<- (next (cell ?m ?n x))
<-     (does xplayer (mark ?m ?n))
<- (next (cell ?m ?n o))
<-     (does oplayer (mark ?m ?n))
<- terminal
<-     (line x)
<- terminal
<-     (line o)
<- terminal
<-     not boardopen
<- (goal xplayer 100)
<-     (line x)
<- (goal oplayer 0)
<-     (line x))