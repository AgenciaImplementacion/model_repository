#!/bin/bash
cd html
link=http://localhost:8000
function openLink {
  while ! curl "$link" &> /dev/null
  do
    sleep 0.5
  done
  xdg-open "$link"
}
openLink&
python3 -m http.server 8000
