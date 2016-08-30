


Installing IHaskell Notebook
==============================

using: https://github.com/gibiansky/IHaskell

Dependencies
---------------
1. zeromq
  1. **ubuntu**: ```sudo apt-fast -y install libzmq3-dev```
  1. **mac**: ```brew install zeromq```
  
1. libmagic
  1. **ubuntu**: ```sudo apt-fast -y install libmagic-dev```
  1. **mac**: ```brew install libmagic```
  
1. stack
  1. **ubuntu**: [Instructions](http://docs.haskellstack.org/en/stable/install_and_upgrade.html#ubuntu)
  1. **mac**: ```brew install haskell-stack```
  1. post installation
      ```
      stack setup
      ```

Finally
-------
```
git clone https://github.com/gibiansky/IHaskell
cd Ihaskell
stack install
ihaskell install
```

The notes are based on the edx course **DelftX: FP101x Introduction to Functional Programming**  
[edx](https://courses.edx.org/courses/course-v1:DelftX+FP101x+3T2015/info) 
[github](https://github.com/fptudelft/FP101x-Content-2015)
