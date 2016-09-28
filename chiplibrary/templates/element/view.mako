<%inherit file="../base.mako"/>

<%def name="title()">${element.name | str.title} &mdash; Elements</%def>
<%def name="title_breadcrumb()">${element.name | str.title}</%def>
<%def name="title_header()">Element: ${element.name | str.title}</%def>

<p>Placeholder page for now.</p>
