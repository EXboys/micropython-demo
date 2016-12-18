# micropython-demo
micropython-demo

# microtpl
A template that likes jinja2 or smarty in PHP,it can works with miropython. I have test it in esp8266 witch's mem size is just 36k.
microtpl only spends 1000 bytes mem when you run it


```python
import mirotpl
args = {'var':'test','name':[1,2,3,4,5],'display':'1'}
html=microtpl.render('index.html',args)
print(html)
```
eg:
```html
<p>{var}{var|b}</p>
{for value in name}
	<p>{value}</p>
{/for}
{if display == 1}
	11111
{/if}
```
