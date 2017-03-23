<%inherit file="base.mako"/>
<%def name="title()">Development</%def>

<p>chiplibrary is open-source, and is licensed under the MIT License.  You are free to download the code, and do with it as you please.</p>

<h2>Getting the code</h2>
<p>If you're just a nerd and want to see how the development process goes for the site and for the actual chip database, <a href="http://github.com/chrisrsantiago/chiplibrary" title="chiplibrary - GitHub">check out the project on GitHub</a>.  If you have git installed, getting the source code for both chiplibrary and chiplibrary-data is as simple as:</p>

<blockquote>git clone https://github.com/chrisrsantiago/chiplibrary.git</blockquote>
<blockquote>git clone https://github.com/chrisrsantiago/chiplibrary-data.git</blockquote>

<p>All relevant development reference is included in each project's respective README files, and around the source code.</p>

<h2>Which one do I download?</h2>

<p><strong>chiplibrary</strong> is the codebase for the official website, which is written in Python atop the Pyramid web framework.  All of the code used to power all of the sections on the website is present, including but not limited to: chips, folders, articles and the user system</p>

<p><strong>chiplibrary-data</strong> is the codebase for the actual battlechip data, including a web scraper written in Python atop Scrapy.  If you are not interested in the website's code but are interested in the data only, then this is what you want.  The <em>dumps</em> folder contains a pre-generated Scrapy XML dump of all the battlechips from every game compiled into one, including CSV files supplied by Tterajj42 and cheeseandcereal.</p>
