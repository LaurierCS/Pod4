# Components

All classes with tag `base` are required for the component to look right.\
Classes with the `utility` tag are add-ons to the `base` classes, i.e: adds animation or makes them look even better.

Content Table
- [Components](#components)
  - [Button](#button)
  - [Input](#input)
    - [Input Component Context](#input-component-context)
  - [Filter](#filter)
    - [Filter Object For Context](#filter-object-for-context)
  - [Icon](#icon)
    - [Available Icon Templates](#available-icon-templates)
    - [Preview of the icons (in the same order as the table above)](#preview-of-the-icons-in-the-same-order-as-the-table-above)
  - [Tech Tag](#tech-tag)
    - [Available variants of Tech Tag](#available-variants-of-tech-tag)
    - [Preview](#preview-of-tech-tag)
  - [Marker](#marker) 


## Button

```html
<!-- Using button tag -->
<button class="bg-primary-gradient button button-transition" type="button">Click Me!</button>

<!-- Using anchon tag -->
<a href="#" class="bg-primary-gradient button button-transition">Click Me!</a>

<!-- Using input tag -->
<input type="submit" value="Click Me!" class="bg-primary-gradient button button-transition"/>
```

Since the component is actually just made with css, the actual element that it is used depends on the developer.\
This allow much more flexibility when trying to style a button.\

| Class | Description | Tag |
| :---- | :---------- | :-- |
| `button` | Base class of a button. | `base` |
| `button-sm` | A smaller version of the base class. | `base` |
| `button-lg` | A slightly bigger version of the base class. | `base` |
| `button-xl` | Largest version of a button. | `base` |
| `button-transition` | This is a utility class that adds animation to a button. | `utility` |

## Input

```python
# views.py

def some_view(request):
  # some code
  context = {
    "input": {
      "attributes": {
        "name": "username",
        "type": "text",
        "required": "true",
        "placeholder": "Enter Username"
      },
      "label": "Username:"
      # here we can decide its look after some input validation
      "state": "valid" if data_is_valid else "invalid" if data_is_invalid else None
    }
  }
  # some more code
  return render(request, template, context)
```

```html
<!-- html file where the input component is neede. -->
<!-- Should just be included with some context -->
{% include 'components/input.html' with input_context=input %}

<!-- 
  If there is only one input in the entire html, then having
  a key "input_context" in the main context is good enough.
  Get rid of the need to pass a specific context for the input.
-->
{% include 'components/input.html' %}
```

### Input Component Context

| Key | Value | Description |
| :-- | :---- | :---------- |
| `attributes` | `dictionary` | This should be a dictionary with the keys being an attribute of an input tag and its value being the correct value the attribute needs.|
| `label` | `string` | This is the label text that is above the input box. |
| `state` | `"valid"`, `"invalid"`, `None` | This decides the look of the input box. `valid` for a green look, and `invalid` for a red look. If neither look is desired then do not defined this in the context.|

The input component is built to be able to handle simple validation that the element tag originally supports. Since the `invalid` style uses the pseudo-selector `:invalid`.

## Icon
```html
<div>
  {% include 'icons/icon_template.html' with class="w-6 h-6 text-black" %}
</div>
```
The class context directly passed to the `<svg>` tag in the template. It serves the same purpose of the normal `class` attribute in any HTML tag.

### Available Icon Templates
| Template Name | 
|:------------- |
| `bookmark_fill.html` |
| `bookmark_outline.html` |
| `check.html` |
| `cross_circle_outline.html` |
| `cross_circle_fill.html` |
| `facebook.html` |
| `github.html` |
| `openbook.html` |
| `settings.html` |
| `terminal.html` |

### Preview of the icons (in the same order as the table above)

![image](https://user-images.githubusercontent.com/46619361/164488267-7a25a000-2f5b-404c-b921-7f2080430775.png)

## Tech Tag

```html
<!-- Pre-defined colors -->
<span class="tech-tag-1 tech-tag-blue">Tech</span>
<span class="tech-tag-1 tech-tag-orange">Tech</span>
<span class="tech-tag-1 tech-tag-green">Tech</span>

<!-- tech-tag-2 is a bigger version of tech-tag-1 -->
<span class="tech-tag-2 tech-tag-blue">Tech</span>
<span class="tech-tag-2 tech-tag-orange">Tech</span>
<span class="tech-tag-2 tech-tag-green">Tech</span>

<!-- Custom color -->
<span class="tech-tag-2 border-rice-white text-rice-white hover:bg-rice-white hover:text-black">Tech</span>
```

It is also possible to use a `<div>` tag to do the job.

### Available variants of Tech Tag

| Class Name | Description | Tag |
| :--------- | :---------- | :-- |
| `tech-tag-1` | Default size of a tech tag. | `base` |
| `tech-tag-2` | Slightly bigger tech tag. | `base` |
| `tech-tag-blue` | Pre-defined `sky-400` color theme with hover effect. | `utility` |
| `tech-tag-orange` | Pre-defined `orange-400` color theme with hover effect. | `utility` |
| `tech-tag-green` | Pre-defined `green-400` color theme with hover effect. | `utility` |
A list of all the colors is available [here](https://tailwindcss.com/docs/customizing-colors).

### Preview of Tech Tag

![Preview](https://user-images.githubusercontent.com/46619361/164512195-fc435539-db22-4067-9612-0568ebf33899.gif)

## Marker
```html
{% include 'components/marker.html' with marker_name="HTML" marker_color="bg-red-700" %}
```
The color context must be a valid color class. Failing to provide a valid color class will default to `white`.
Valid color classes include [tailwind official colors](https://tailwindcss.com/docs/customizing-colors) and [customized colors](https://github.com/LaurierCS/Pod4/blob/main/docs/tailwind-quick-start.md#colors).

| Attribute | Description |
| :-------- | :---------- |
| `marker_name` | The text beside the circle. |
| `marker_color` | The color of the circel. |

## Input

```python
# views.py

def some_view(request):
  # some code
  context = {
    "input": {
      "attributes": {
        "name": "username",
        "type": "text",
        "required": "true",
        "placeholder": "Enter Username"
      },
      "label": "Username:"
    }
  }
  # some more code
  return render(request, template, context)
```

```html
<!-- html file where the input component is neede. -->
<!-- Should just be included with some context -->
{% include 'components/input.html' with input_context=input %}

<!-- 
  If there is only one input in the entire html, then having
  a key "input_context" in the main context is good enough.
  Get rid of the need to pass a specific context for the input.
-->
{% include 'components/input.html' %}
```

### Input Component Context Tale

| Key | Value | Description |
| :-- | :---- | :---------- |
| `attributes` | `dictionary` | This should be a dictionary with the keys being an attribute of an input tag and its value being the correct value the attribute needs.|
| `label` | `string` | This is the label text that is above the input box. |

The input component is built to be able to handle simple validation that the element tag originally supports. Since the `invalid` style uses the pseudo-selector `:invalid`.

## Filter

```html
{% include 'components/filter.html' with filter=filter_object %}
<!-- or with context = { "filter": { ... } " -->
{% include 'components/filter.html' %}
```

```python
# views.py

def view_with_filter(request):
  template = "app/template.html"
  endpoint = "/api/filter"
  # create a list of selections
  ...
  context = {
    "filter": {
      "selections": selections, # list
      "endpoint": endpoint
    }
  }
  if request.method == "POST":
    # handle filter query
    # get filter query value
    filter_query = request.POST.get("filter-query")
    # search in database
    ...
    # make context
    ...
    return render(request, template, context) # return a view with filtered content

  return render(request, template, context) # return a view with all content
```

### Filter Object For Context
| Field | Description |
| :---- | :---------- |
| `selections` | A list of strings with the available filtering selections. This values should match the category that we can actually query or compare with what it is in the database. |
| `endpoint` | The endpoint url. It is going to send a `POST` request with a form. Get the value of the query with `request.POST.get("filter-query")`. |
