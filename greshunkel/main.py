from build import main as build_main
from context import BASE_CONTEXT, build_blog_context


def main():
    context = build_blog_context(BASE_CONTEXT)
    build_main(context)
