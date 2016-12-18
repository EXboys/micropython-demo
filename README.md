# micropython-demo
micropython-demo

# microtpl
A template that likes jinja2 or smarty in PHP,it can works with miropython. 

```python
import mirotpl
args = {'var':'test','name':[1,2,3,4,5],'display':'1'}
html=microtpl.render('index.html',args)
print(html)
```

```html
<p>{var}{var|b}</p>
{for value in name}
	<p>{value}</p>
{/for}
{if display == 1}
	11111
{/if}
```
