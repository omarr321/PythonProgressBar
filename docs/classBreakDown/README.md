# Class Break Down
---
## def \_\_init\_\_()
#### About
This is the constuctor for the class and sets up the progress bar for use

<style>
td, th {
   border: none!important;
}
</style>

<style>
td:nth-child(1) {
  width: 150px;
  }

/* the second */
td:nth-child(2) {
  width: 500px;
}

.niceTables thg {
background: grey;
word-wrap: break-word;
text-align: center;
}
.niceTables tr:nth-child(1) { background: #464444; }
.niceTables tr:nth-child(2) { background: #464444; }
.niceTables tr:nth-child(3) { background: #464444; }
.niceTables tr:nth-child(4) { background: #464444; }
.niceTables tr:nth-child(5) { background: #464444; }
.niceTables tr:nth-child(6) { background: #464444; }
.niceTables tr:nth-child(7) { background: #464444; }
.niceTables tr:nth-child(8) { background: #464444; }
.niceTables tr:nth-child(9) { background: #464444; }
</style>

#### Input Varables

<div class="niceTables">

Name | Description | Default Value
--- | --- | ---
blank | Sets the empty space of the progress bar | ' '
fill | Sets the full space of the progress bar | u"\u2588"
length | Sets the lenght of the progress bar | 20
steps | Sets how many incurments the bar needs to get to 100% | 20
doneMess | Sets the message displayed at the end of the progress bar when it is full | "-DONE!"
barEnd | Sets the ends for the progress bar | "|"
inclRet | If True, includes a '\r' char to the begianning of the progress bar | True
autoPrint | When you step the progress bar, it prints it out | False

</div>

---
## def step()
#### About
This is the definition that steps the progress bar. If the steps would increase the steps count to beyond the steps of the bar, it will set down to the max steps.
#### Input Varables

<div class="niceTables">

Name | Description | Default Value
--- | --- | ---
step | The number of units to progress the progress bar | 1

</div>

---
## def toString()
#### About
This will convert the progress bar to string and return it
#### Input Varables
NONE

---