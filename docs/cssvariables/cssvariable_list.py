import dash_mantine_components as dmc


css_variables =  [
    {"--mantine-scale": "1"},
    {"--mantine-cursor-type": "default"},
    {"--mantine-color-scheme": "light dark"},
    {"--mantine-webkit-font-smoothing": "antialiased"},
    {"--mantine-moz-font-smoothing": "grayscale"},
    {"--mantine-color-white": "#fff"},
    {"--mantine-color-black": "#000"},
    {"--mantine-line-height": "1.55"},
    {"--mantine-font-family": "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji"},
    {"--mantine-font-family-monospace": "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace"},
    {"--mantine-font-family-headings": "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji"},
    {"--mantine-heading-font-weight": "700"},
    {"--mantine-heading-text-wrap": "wrap"},
    {"--mantine-radius-default": "0.25rem"},
    {"--mantine-primary-color-filled": "var(--mantine-color-blue-filled)"},
    {"--mantine-primary-color-filled-hover": "var(--mantine-color-blue-filled-hover)"},
    {"--mantine-primary-color-light": "var(--mantine-color-blue-light)"},
    {"--mantine-primary-color-light-hover": "var(--mantine-color-blue-light-hover)"},
    {"--mantine-primary-color-light-color": "var(--mantine-color-blue-light-color)"},
    {"--mantine-breakpoint-xs": "36em"},
    {"--mantine-breakpoint-sm": "48em"},
    {"--mantine-breakpoint-md": "62em"},
    {"--mantine-breakpoint-lg": "75em"},
    {"--mantine-breakpoint-xl": "88em"},
    {"--mantine-spacing-xs": "0.625rem"},
    {"--mantine-spacing-sm": "0.75rem"},
    {"--mantine-spacing-md": "1rem"},
    {"--mantine-spacing-lg": "1.25rem"},
    {"--mantine-spacing-xl": "2rem"},
    {"--mantine-font-size-xs": "0.75rem"},
    {"--mantine-font-size-sm": "0.875rem"},
    {"--mantine-font-size-md": "1rem"},
    {"--mantine-font-size-lg": "1.125rem"},
    {"--mantine-font-size-xl": "1.25rem"},
    {"--mantine-line-height-xs": "1.4"},
    {"--mantine-line-height-sm": "1.45"},
    {"--mantine-line-height-md": "1.55"},
    {"--mantine-line-height-lg": "1.6"},
    {"--mantine-line-height-xl": "1.65"},
    {"--mantine-shadow-xs": "0 0.0625rem 0.1875rem rgba(0, 0, 0, 0.05), 0 0.0625rem 0.125rem rgba(0, 0, 0, 0.1)"},
    {"--mantine-shadow-sm": "0 0.0625rem 0.1875rem rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 0 0.625rem 0.9375rem -0.3125rem, rgba(0, 0, 0, 0.04) 0 0.4375rem 0.4375rem -0.3125rem"},
    {"--mantine-shadow-md": "0 0.0625rem 0.1875rem rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 0 1.25rem 1.5625rem -0.3125rem, rgba(0, 0, 0, 0.04) 0 0.625rem 0.625rem -0.3125rem"},
    {"--mantine-shadow-lg": "0 0.0625rem 0.1875rem rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 0 1.75rem 1.4375rem -0.4375rem, rgba(0, 0, 0, 0.04) 0 0.75rem 0.75rem -0.4375rem"},
    {"--mantine-shadow-xl": "0 0.0625rem 0.1875rem rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 0 2.25rem 1.75rem -0.4375rem, rgba(0, 0, 0, 0.04) 0 1.0625rem 1.0625rem -0.4375rem"},
    {"--mantine-radius-xs": "0.125rem"},
    {"--mantine-radius-sm": "0.25rem"},
    {"--mantine-radius-md": "0.5rem"},
    {"--mantine-radius-lg": "1rem"},
    {"--mantine-radius-xl": "2rem"},
    {"--mantine-primary-color-0": "var(--mantine-color-blue-0)"},
    {"--mantine-primary-color-1": "var(--mantine-color-blue-1)"},
    {"--mantine-primary-color-2": "var(--mantine-color-blue-2)"},
    {"--mantine-primary-color-3": "var(--mantine-color-blue-3)"},
    {"--mantine-primary-color-4": "var(--mantine-color-blue-4)"},
    {"--mantine-primary-color-5": "var(--mantine-color-blue-5)"},
    {"--mantine-primary-color-6": "var(--mantine-color-blue-6)"},
    {"--mantine-primary-color-7": "var(--mantine-color-blue-7)"},
    {"--mantine-primary-color-8": "var(--mantine-color-blue-8)"},
    {"--mantine-primary-color-9": "var(--mantine-color-blue-9)"},
    {"--mantine-color-dark-0": "#C9C9C9"},
    {"--mantine-color-dark-1": "#b8b8b8"},
    {"--mantine-color-dark-2": "#828282"},
    {"--mantine-color-dark-3": "#696969"},
    {"--mantine-color-dark-4": "#424242"},
    {"--mantine-color-dark-5": "#3b3b3b"},
    {"--mantine-color-dark-6": "#2e2e2e"},
    {"--mantine-color-dark-7": "#242424"},
    {"--mantine-color-dark-8": "#1f1f1f"},
    {"--mantine-color-dark-9": "#141414"},
    {"--mantine-color-gray-0": "#f8f9fa"},
    {"--mantine-color-gray-1": "#f1f3f5"},
    {"--mantine-color-gray-2": "#e9ecef"},
    {"--mantine-color-gray-3": "#dee2e6"},
    {"--mantine-color-gray-4": "#ced4da"},
    {"--mantine-color-gray-5": "#adb5bd"},
    {"--mantine-color-gray-6": "#868e96"},
    {"--mantine-color-gray-7": "#495057"},
    {"--mantine-color-gray-8": "#343a40"},
    {"--mantine-color-gray-9": "#212529"},
    {"--mantine-color-red-0": "#fff5f5"},
    {"--mantine-color-red-1": "#ffe3e3"},
    {"--mantine-color-red-2": "#ffc9c9"},
    {"--mantine-color-red-3": "#ffa8a8"},
    {"--mantine-color-red-4": "#ff8787"},
    {"--mantine-color-red-5": "#ff6b6b"},
    {"--mantine-color-red-6": "#fa5252"},
    {"--mantine-color-red-7": "#f03e3e"},
    {"--mantine-color-red-8": "#e03131"},
    {"--mantine-color-red-9": "#c92a2a"},
    {"--mantine-color-pink-0": "#fff0f6"},
    {"--mantine-color-pink-1": "#ffdeeb"},
    {"--mantine-color-pink-2": "#fcc2d7"},
    {"--mantine-color-pink-3": "#faa2c1"},
    {"--mantine-color-pink-4": "#f783ac"},
    {"--mantine-color-pink-5": "#f06595"},
    {"--mantine-color-pink-6": "#e64980"},
    {"--mantine-color-pink-7": "#d6336c"},
    {"--mantine-color-pink-8": "#c2255c"},
    {"--mantine-color-pink-9": "#a61e4d"},
    {"--mantine-color-grape-0": "#f8f0fc"},
    {"--mantine-color-grape-1": "#f3d9fa"},
    {"--mantine-color-grape-2": "#eebefa"},
    {"--mantine-color-grape-3": "#e599f7"},
    {"--mantine-color-grape-4": "#da77f2"},
    {"--mantine-color-grape-5": "#cc5de8"},
    {"--mantine-color-grape-6": "#be4bdb"},
    {"--mantine-color-grape-7": "#ae3ec9"},
    {"--mantine-color-grape-8": "#9c36b5"},
    {"--mantine-color-grape-9": "#862e9c"},
    {"--mantine-color-violet-0": "#f3f0ff"},
    {"--mantine-color-violet-1": "#e5dbff"},
    {"--mantine-color-violet-2": "#d0bfff"},
    {"--mantine-color-violet-3": "#b197fc"},
    {"--mantine-color-violet-4": "#9775fa"},
    {"--mantine-color-violet-5": "#845ef7"},
    {"--mantine-color-violet-6": "#7950f2"},
    {"--mantine-color-violet-7": "#7048e8"},
    {"--mantine-color-violet-8": "#6741d9"},
    {"--mantine-color-violet-9": "#5f3dc4"},
    {"--mantine-color-indigo-0": "#edf2ff"},
    {"--mantine-color-indigo-1": "#dbe4ff"},
    {"--mantine-color-indigo-2": "#bac8ff"},
    {"--mantine-color-indigo-3": "#91a7ff"},
    {"--mantine-color-indigo-4": "#748ffc"},
    {"--mantine-color-indigo-5": "#5c7cfa"},
    {"--mantine-color-indigo-6": "#4c6ef5"},
    {"--mantine-color-indigo-7": "#4263eb"},
    {"--mantine-color-indigo-8": "#3b5bdb"},
    {"--mantine-color-indigo-9": "#364fc7"},
    {"--mantine-color-blue-0": "#e7f5ff"},
    {"--mantine-color-blue-1": "#d0ebff"},
    {"--mantine-color-blue-2": "#a5d8ff"},
    {"--mantine-color-blue-3": "#74c0fc"},
    {"--mantine-color-blue-4": "#4dabf7"},
    {"--mantine-color-blue-5": "#339af0"},
    {"--mantine-color-blue-6": "#228be6"},
    {"--mantine-color-blue-7": "#1c7ed6"},
    {"--mantine-color-blue-8": "#1971c2"},
    {"--mantine-color-blue-9": "#1864ab"},
    {"--mantine-color-cyan-0": "#e3fafc"},
    {"--mantine-color-cyan-1": "#c5f6fa"},
    {"--mantine-color-cyan-2": "#99e9f2"},
    {"--mantine-color-cyan-3": "#66d9e8"},
    {"--mantine-color-cyan-4": "#3bc9db"},
    {"--mantine-color-cyan-5": "#22b8cf"},
    {"--mantine-color-cyan-6": "#15aabf"},
    {"--mantine-color-cyan-7": "#1098ad"},
    {"--mantine-color-cyan-8": "#0c8599"},
    {"--mantine-color-cyan-9": "#0b7285"},
    {"--mantine-color-teal-0": "#e6fcf5"},
    {"--mantine-color-teal-1": "#c3fae8"},
    {"--mantine-color-teal-2": "#96f2d7"},
    {"--mantine-color-teal-3": "#63e6be"},
    {"--mantine-color-teal-4": "#38d9a9"},
    {"--mantine-color-teal-5": "#20c997"},
    {"--mantine-color-teal-6": "#12b886"},
    {"--mantine-color-teal-7": "#0ca678"},
    {"--mantine-color-teal-8": "#099268"},
    {"--mantine-color-teal-9": "#087f5b"},
    {"--mantine-color-green-0": "#ebfbee"},
    {"--mantine-color-green-1": "#d3f9d8"},
    {"--mantine-color-green-2": "#b2f2bb"},
    {"--mantine-color-green-3": "#8ce99a"},
    {"--mantine-color-green-4": "#69db7c"},
    {"--mantine-color-green-5": "#51cf66"},
    {"--mantine-color-green-6": "#40c057"},
    {"--mantine-color-green-7": "#37b24d"},
    {"--mantine-color-green-8": "#2f9e44"},
    {"--mantine-color-green-9": "#2b8a3e"},
    {"--mantine-color-lime-0": "#f4fce3"},
    {"--mantine-color-lime-1": "#e9fac8"},
    {"--mantine-color-lime-2": "#d8f5a2"},
    {"--mantine-color-lime-3": "#c0eb75"},
    {"--mantine-color-lime-4": "#a9e34b"},
    {"--mantine-color-lime-5": "#94d82d"},
    {"--mantine-color-lime-6": "#82c91e"},
    {"--mantine-color-lime-7": "#74b816"},
    {"--mantine-color-lime-8": "#66a80f"},
    {"--mantine-color-lime-9": "#5c940d"},
    {"--mantine-color-yellow-0": "#fff9db"},
    {"--mantine-color-yellow-1": "#fff3bf"},
    {"--mantine-color-yellow-2": "#ffec99"},
    {"--mantine-color-yellow-3": "#ffe066"},
    {"--mantine-color-yellow-4": "#ffd43b"},
    {"--mantine-color-yellow-5": "#fcc419"},
    {"--mantine-color-yellow-6": "#fab005"},
    {"--mantine-color-yellow-7": "#f59f00"},
    {"--mantine-color-yellow-8": "#f08c00"},
    {"--mantine-color-yellow-9": "#e67700"},
    {"--mantine-color-orange-0": "#fff4e6"},
    {"--mantine-color-orange-1": "#ffe8cc"},
    {"--mantine-color-orange-2": "#ffd8a8"},
    {"--mantine-color-orange-3": "#ffc078"},
    {"--mantine-color-orange-4": "#ffa94d"},
    {"--mantine-color-orange-5": "#ff922b"},
    {"--mantine-color-orange-6": "#fd7e14"},
    {"--mantine-color-orange-7": "#f76707"},
    {"--mantine-color-orange-8": "#e8590c"},
    {"--mantine-color-orange-9": "#d9480f"},
    {"--mantine-h1-font-size": "2.125rem"},
    {"--mantine-h1-line-height": "1.3"},
    {"--mantine-h1-font-weight": "700"},
    {"--mantine-h2-font-size": "1.625rem"},
    {"--mantine-h2-line-height": "1.35"},
    {"--mantine-h2-font-weight": "700"},
    {"--mantine-h3-font-size": "1.375rem"},
    {"--mantine-h3-line-height": "1.4"},
    {"--mantine-h3-font-weight": "700"},
    {"--mantine-h4-font-size": "1.125rem"},
    {"--mantine-h4-line-height": "1.45"},
    {"--mantine-h4-font-weight": "700"},
    {"--mantine-h5-font-size": "1rem"},
    {"--mantine-h5-line-height": "1.5"},
    {"--mantine-h5-font-weight": "700"},
    {"--mantine-h6-font-size": "0.875rem"},
    {"--mantine-h6-line-height": "1.5"},
    {"--mantine-h6-font-weight": "700"},
]

def make_rows(data):
    rows = [
        dmc.Grid([
            dmc.GridCol(dmc.Text(key), span=5),
            dmc.GridCol(dmc.Text(value), span=5),
            dmc.GridCol(dmc.Box(h=24, w=24, bg=value), span=2),
            dmc.GridCol(dmc.Divider(), span=12)
        ])
        for item in data
        for key, value in item.items()
    ]
    return rows


component =  dmc.Box(
    make_rows(css_variables)
)


