{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ">8.21\n",
      "= 8 + 0.21\n"
     ]
    }
   ],
   "source": [
    "a=float(input(\">\"))\n",
    "b='0.'+str(int(a*100)%100)\n",
    "print('=',int(a),'+',b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ">2\n",
      "222222\n",
      "    22\n",
      "222222\n",
      "22\n",
      "222222\n",
      "\n"
     ]
    }
   ],
   "source": [
    "m=int(input(\">\"))\n",
    "a='2'*(m*3)+\"\\n\"\n",
    "b=\" \"*(m*2)+'2'*(m*1)+'\\n'\n",
    "c='2'*(m)+\"\\n\"\n",
    "print(a+b+a+c+a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
