# Components

All classes with tag `base` are required for the component to look right.\
Classes with the `utility` tag are add-ons to the `base` classes, i.e: adds animation or makes them look even better.

Content Table
- [Components](#components)
  - [Button](#button)
    - [Available Icon Templates](#available-icon-templates)
    - [Preview of the icons (in the same order as the table above)](#preview-of-the-icons-in-the-same-order-as-the-table-above)
  - [Tech Tag](#tech-tag)
    - [Available variants of Tech Tag](#available-variants-of-tech-tag)
  - [Marker](#marker)
  - [Input](#input)


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
 render(request, template, context)
```

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
Please use the template below as a guide to make an input witht the same style in figma.
```html
<div
  class="relative w-fit p-4 mt-4 mb-2 mx-2"
>
  <input 
  {% for k, v in attributes.items %}
    {{ k }}="{{ v }}"
  {% endfor %}
  class="peer p-2 bg-transparent outline-none 
  border-white rounded-xl border-solid border-2 
  transition-colors duration-150
  focus-visible:placeholder:text-gray-500
  focus-visible:border-active 
  text-white w-full placeholder:text-white 
  required:not-focus-visible:border-white
  required:not-focus-visible:invalid:border-error
  valid:focus-visible:border-success" 
  />
  <label 
    for="{{ attributes.name }}" 
    class="absolute left-5 -top-[15%] text-white"
  >
    {{ label }}
  </label>
</div>
```
