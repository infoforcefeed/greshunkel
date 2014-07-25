from greshunkel.build import POSTS_DIR
from greshunkel.utils import parse_variable
from greshunkel.slimdown import Slimdown
from greshunkel.module_loader import make_module_from_file

from os import listdir, getcwd, path
from sys import exit

__all__ = ["config",]

PWD = getcwd()

DEFAULT_LANGUAGE = "en"
# Question: Hey qpfiffer, why is this indented all weird?
# Man I don't know leave me alone.
BASE_CONTEXT = {}
config = {}

def load_config():
    if path.isfile("{}/Greshunkelfile".format(PWD)):
        intrl_config = make_module_from_file(
            "config", "{}/Greshunkelfile".format(PWD))
        config["BASE_CONTEXT"] = intrl_config.BASE_CONTEXT
        if hasattr(intrl_config, "DEFAULT_LANGUAGE"):
            config["DEFAULT_LANGUAGE"] = intrl_config.DEFAULT_LANGUAGE
        else:
            config["DEFAULT_LANGUAGE"] = DEFAULT_LANGUAGE
        for thing in dir(intrl_config):
            if not hasattr(thing, "__call__"):
                config[thing] = getattr(intrl_config, thing)
    else:
        print("ERROR NO Greshunkelfile FOUND.")
        exit(1)

def build_blog_context(default_context):
    default_context['POSTS'] = []

    slimmin = Slimdown()
    for post in listdir(POSTS_DIR):
        if not post.endswith(".markdown"):
            continue

        new_post = {}
        dashes_seen = 0
        reading_meta = True
        muh_file = open(POSTS_DIR + post)
        all_text = ""
        for line in muh_file:
            stripped = line.strip()
            if stripped == '---':
                dashes_seen += 1
                if reading_meta and dashes_seen < 2:
                    continue
            elif reading_meta and dashes_seen >= 2:
                reading_meta = False
                continue

            if reading_meta and ':' in line:
                split_line = stripped.split(":")
                new_post[split_line[0]] = split_line[1]

            if not reading_meta:
                all_text += line

        new_post['content'] = slimmin.render(all_text)
        new_post['preview'] = new_post['content'][:300] + "&hellip;"
        new_post['link'] = "blog/{}".format(post.replace("markdown", "html"))
        new_post['filename'] = post
        new_post['built_filename'] = post.replace("markdown", "html")
        default_context['POSTS'].append(new_post)
        muh_file.close()
    default_context['POSTS'] = sorted(default_context['POSTS'], key=lambda x: x["date"], reverse=True)
    return default_context

load_config()
