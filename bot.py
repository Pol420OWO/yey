import socket
import subprocess
import platform
import os
import sysconfig
import base64

from github import Github
from github import InputGitTreeElement

user = "Pol420OWO"
password = "V0l02022"

g = Github(user,password)
g = Github("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")

repo = g.get_user().get_repo('yey')

file_list = ["C:/Users/polmernie/OneDrive - Centre d'Estudis Monlau/Desktop"]
file_names = ["pene.bat"]

commit_message = 'python update 2'
master_ref = repo.get_git_ref('heads/master')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)
element_list = list()
for i, entry in enumerate(file_list):
  with open(entry) as input_file:
    data = input_file.read()
  if entry.endswith('.png'):
    data = base64.b64encode(data)
  element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
  element_list.append(element)
tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)
