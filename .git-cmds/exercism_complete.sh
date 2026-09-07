#!/bin/bash

yellow() {
  echo -e "==> \033[1;33m${1}\033[0m"
}

green() {
  echo -e "==> \033[1;32m${1}\033[0m"
}

while IFS= read -r line; do
  status="${line:0:2}"
  file="${line:3}"

  IFS=/ read -r exercism track exercise <<<"$file"
  exercise="${exercise%%/*}"
  commit_msg="$exercism/$track: add $exercise"

  if [[ "$status" == "??" ]]; then
    yellow "found untracked: $file"
  else
    # assume I never added to cause 'A'
    yellow "found modified: $file"
    yellow "needs a commit message:"
    read -rp "$exercism/$track/$exercise: " msg </dev/tty
    commit_msg="$exercism/$track/$exercise: $msg"
  fi

  git add "$file"

  green "commiting: $commit_msg"

  git commit -sm "$commit_msg" >/dev/null
done < <(git status --porcelain -- exercism/)
