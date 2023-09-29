---
name: TimeInput
description: Use the TimeInput component to capture time input from user.
endpoint: /components/timeinput
package: dash_mantine_components
---

.. toc::

### Simple Example

This is a simple example of the TimeInput. You can enter a valid time string or use the date object from datetime 
library.

Use the  `withSeconds` prop to display seconds.

.. exec::docs.timeinput.simple

### Input Props

TimeInput supports all props from Input and InputWrapper components such as `radius`, `size`, `required`, etc.

.. exec::docs.timeinput.interactive
    :code: false

### Invalid State And Error

You can display an error with a red border and add an error message.

.. exec::docs.timeinput.error

### Styles API


### Keyword Arguments

#### TimeInput

.. kwargs::TimeInput
