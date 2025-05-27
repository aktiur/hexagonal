#!/usr/bin/env bash

function deplacer_drom() {
  local -n _args=$1
  _args+=( -affine "where=code_departement =='971'" "shift=6556000,3230000" scale=3 )
  _args+=( -affine "where=code_departement =='972'" "shift=6780000,3405000" scale=4 )
  _args+=( -affine "where=code_departement =='973'" "shift=6150000,4620000" scale=0.6 )
  _args+=( -affine "where=code_departement =='974'" "shift=-5700000,7450000" scale=3 )
  _args+=( -affine "where=code_departement =='976'" "shift=-4310000,6500000" scale=3 )
}

function deplacer_idf() {
  # shellcheck disable=SC2178
  local -n _args=$1
  _args+=( -affine "where=['77','78','91','95'].includes(code_departement)" "shift=900000,200000" scale=2 )
  _args+=( -affine "where=['75','92','93','94'].includes(code_departement)" "shift=900000,-200000" scale=6 )
}
