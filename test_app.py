"""
Test suite for the Pink Morsel Sales Visualiser Dash app.

This suite verifies that the key components of the app are present:
- Header
- Visualisation (chart)
- Region picker (radio items)
"""

import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def dash_app():
    """Fixture to import the Dash app for testing."""
    app = import_app("app")
    return app


def test_header_is_present(dash_app):
    """
    Test that the header is present in the app layout.
    
    The header should contain the title "Pink Morsel Sales Visualiser".
    """
    layout_str = str(dash_app.layout)
    
    # Check for the hero title text
    assert "Pink Morsel Sales Visualiser" in layout_str, \
        "Header title 'Pink Morsel Sales Visualiser' not found in layout"
    
    # Check for the hero class
    assert "hero-title" in layout_str, \
        "Header class 'hero-title' not found in layout"
    
    print("✓ Header is present")


def test_visualisation_is_present(dash_app):
    """
    Test that the visualisation (chart) is present in the app layout.
    
    The chart should be a dcc.Graph component with id='sales-chart'.
    """
    layout_str = str(dash_app.layout)
    
    # Check for the sales chart Graph component
    assert "sales-chart" in layout_str, \
        "Chart component with id='sales-chart' not found in layout"
    
    # Verify it's a Graph component (dcc.Graph renders with specific attributes)
    assert "Graph" in layout_str, \
        "Graph component not found in layout"
    
    print("✓ Visualisation is present")


def test_region_picker_is_present(dash_app):
    """
    Test that the region picker is present in the app layout.
    
    The region picker should be a dcc.RadioItems component with id='region-filter'
    and should contain options for all regions (all, east, north, south, west).
    """
    layout_str = str(dash_app.layout)
    
    # Check for the region filter RadioItems component
    assert "region-filter" in layout_str, \
        "Region picker with id='region-filter' not found in layout"
    
    # Check for RadioItems component
    assert "RadioItems" in layout_str, \
        "RadioItems component not found in layout"
    
    # Check that region options are present
    regions = ["all", "east", "north", "south", "west"]
    for region in regions:
        assert region in layout_str.lower(), \
            f"Region option '{region}' not found in layout"
    
    print("✓ Region picker is present with all expected options")


def test_callback_exists():
    """
    Bonus test: Verify that the callback connecting region filter to chart exists.
    Dash 4 stores callbacks in a global registry (GLOBAL_CALLBACK_MAP).
    """
    from dash._callback import GLOBAL_CALLBACK_MAP

    # The callback output key for the chart should be registered
    assert len(GLOBAL_CALLBACK_MAP) > 0, \
        "No callbacks registered in the Dash global callback map"

    assert "sales-chart.figure" in GLOBAL_CALLBACK_MAP, \
        "Callback output 'sales-chart.figure' not found in global callback map"

    print("✓ Callback connecting region filter to chart exists")


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])
