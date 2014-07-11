#!/bin/bash
cd ./lwqq
git archive --format=tar.gz v$1 --prefix=lwqq-$1/ -o ../lwqq-$1.tar.gz
cd ../pidgin-lwqq
git archive --format=tar.gz v$1 --prefix=pidgin-lwqq-$1/ -o ../pidgin-lwqq-$1.tar.gz
cd ..
