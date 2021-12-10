## daftar isi
* [perbedaan dasar](#perbedaan-yang-paling-mendasar-dan-sering-dilupakan)
* [perbedaan class](#perbedaan-pembuatan-class)
* [perbedaan function](#perbedaan-pembuatan-function)

## perbedaan yang paling mendasar dan sering dilupakan

| php  | python |
| ------------- | ------------- |
| `null`  | `None`  |
| `false`  | `False`  |
| `true`  | `True`  |
| `!==`  | `!=`  |
| `(int)'000'`<br>converting only  | `int('000')`<br>convert/checking  |
| `(bool)'true/false'`<br>converting only  | `bool('000')`<br>checking only  |
| `(str)'000'`<br>converting only  | `str('000')`<br>convert/checking  |
| `(float)'000'`<br>converting only  | `float('000')`<br>convert/checking  |
| `(double)'000'`<br>converting only  | pakai `float(x)`  |
| `in_something()/false`  | `not in`  |
| `in_something()/true`  | `in`  |
| `isset()`  | `is not None`  |
| `something;`  | `something`  |
| `$syntax = 'any val';`  | `syntax = 'any val'`  |
| `{} code bracket`  | `{} dict object`  |
| `[] array`<br>visible index  | `[] list`<br>invisible index  |
| `array[] = 'val'/['val'=>'val']`  | `list += ['list']`  |
| `$object = (object)['object'=>'val']`<br>membuat object  | `object = {'object':'val'}`<br>membuat object  |
| `function name()`  | `def name()`  |

<br><br>
## perbedaan pembuatan class
```php
/* PHP */
class name(){
  private $var;
  
  function __construct($var){
    $this->var = $var;
  }
  
  function anything(){
    return $this->var;
  }
}

/* penggunaanya */
$obj = new name('var');
$obj->anything()
```
```python
# python
class name:
  def __init__(self,var):
    self.val = var
    
  def anything(self):
    return self.var
    
# penggunaanya
obj = name('var')
obj.anything()
```


<br><br>
## perbedaan pembuatan function
```php
/* PHP */
function name($var=''){
  return $var;
}

/* penggunaan */
name('something');
```
```python
# python
def name(var=''):
  return var
  
# penggunaan
name('someting')
```

