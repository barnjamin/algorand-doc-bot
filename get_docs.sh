#!/bin/bash


CORPUS_DIR="source_data"
SPEC_DIR="$CORPUS_DIR/specs"
DEVDOC_DIR="$CORPUS_DIR/docs"
JS_DIR="$CORPUS_DIR/jssdk"
PY_DIR="$CORPUS_DIR/pysdk"
GO_DIR="$CORPUS_DIR/gosdk"
JAVA_DIR="$CORPUS_DIR/javasdk"
PYTEAL_DIR="$CORPUS_DIR/pyteal"

#TODO: args to fire off fns when we want to refresh some doc 

reset(){
    [ -d $CORPUS_DIR ] && rm -rf $CORPUS_DIR
    mkdir $CORPUS_DIR 
    mkdir $SPEC_DIR
    mkdir $DEVDOC_DIR
    mkdir $JS_DIR
    mkdir $PY_DIR 
    mkdir $GO_DIR
    mkdir $JAVA_DIR 
    mkdir $PYTEAL_DIR
}


specs(){
    echo "Getting specs"
    [ -d $SPEC_DIR ] && rm -rf $SPEC_DIR
    git clone https://github.com/algorandfoundation/specs.git
    cp -R specs/dev/* $SPEC_DIR
    rm -rf specs
}



devdocs(){
    echo "Getting docs"
    [ -d $DEVDOC_DIR ] && rm -rf $DEVDOC_DIR
    git clone https://github.com/algorand/docs.git 
    cp -R docs/docs/* $DEVDOC_DIR
    rm -rf docs
}

pysdk(){
    echo "Getting pysdk"
    [ -d $PY_DIR ] && rm -rf $PY_DIR
    git clone https://github.com/algorand/py-algorand-sdk.git
    cd py-algorand-sdk
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    cd docs
    pip install -r requirements.txt
    make text
    cd ../..
    cp -R py-algorand-sdk/docs/_build/text/* $PY_DIR 
    rm -rf py-algorand-sdk
}

jssdk(){
    echo "Getting jssdk"
    [ -d $JS_DIR ] && rm -rf $JS_DIR
    git clone https://github.com/algorand/js-algorand-sdk.git
    cd js-algorand-sdk
    npm install
    npm install typedoc-plugin-markdown
    npx typedoc --plugin typedoc-plugin-markdown --options typedoc.config.json
    cd ..
    cp -R js-algorand-sdk/docs/* source_data/jssdk/
    rm -rf js-algorand-sdk
}


gosdk(){

}

javasdk(){

}

pyteal(){

}

