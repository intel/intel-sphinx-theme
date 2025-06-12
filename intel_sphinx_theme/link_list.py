from docutils import nodes
from docutils.parsers.rst import Directive, directives

class LinkList(Directive):
    has_content = True
    option_spec = {
        'position': directives.unchanged,  # optional: 'sidebar' or other positions
        'title': directives.unchanged_required  # required title
    }

    def run(self):
        # Ensure the title is present
        title = self.options.get('title')
        if not title:
            error = self.state_machine.reporter.error(
                'The "title" option is required for the "link-list" directive.',
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno
            )
            return [error]

        position = self.options.get('position', 'content')  # default to content

        # Create HTML content for the linked list
        content = ['<div class="link-list">']
        content.append(f'<div class="page-toc tocsection">{title}</div>')
        content.append('<ul>')

        for line in self.content:
            if line.strip():
                # Separate link text and URL
                text, url = line.rsplit(' ', 1)
                # Add external link icon if necessary
                external_icon = ''
                if url.startswith('http'):
                    external_icon = '<span aria-hidden="true" role="img" class="icon icon-external-link icon-regular"></span>'
                # Add list item
                content.append(f'<li><a href="{url}">{text}{external_icon}</a></li>')

        content.append('</ul></div>')

        # If position is 'sidebar', store the content in temp_data for this page
        if position == 'sidebar':
            sidebar_content = '\n'.join(content)
            print(f"Storing sidebar content for page {self.state.document.settings.env.docname}: {sidebar_content}")
            # Store the content in temp_data with a key specific to this page
            if 'custom_sidebar_content' not in self.state.document.settings.env.temp_data:
                self.state.document.settings.env.temp_data['custom_sidebar_content'] = {}
            self.state.document.settings.env.temp_data['custom_sidebar_content'][self.state.document.settings.env.docname] = sidebar_content
            return []

        # Otherwise, return the content as raw HTML for in-page rendering
        return [nodes.raw('', '\n'.join(content), format='html')]
