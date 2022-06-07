{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Designer Door Mat\n",
    "\n",
    "\n",
    "r, col = map(int,input().split())\n",
    "\n",
    "trace = '-'\n",
    "middle = '.|.'\n",
    "\n",
    "j = 1\n",
    "for i in range(int((r - 1)/2), 0, -1):\n",
    "    #print(i, j)\n",
    "    print(int(col/r * i) * trace + j*middle + int(col/r * i) * trace )\n",
    "    j +=2\n",
    "print(int((col-7)/ 2)*trace + 'WELCOME' + int((col-7)/ 2)*trace)\n",
    "j -= 2\n",
    "\n",
    "for i in range(1,int((r - 1)/2) + 1):\n",
    "    #print(i, j)\n",
    "    print(int(col/r * i) * trace + j*middle + int(col/r * i) * trace )\n",
    "    j -=2\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
