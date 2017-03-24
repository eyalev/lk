
_lk_completion() {
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _LK_COMPLETE=complete $1 ) )
    return 0
}

complete -F _lk_completion -o default lk;
