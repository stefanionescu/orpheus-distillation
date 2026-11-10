"""Pytest setup for every suite, so the developer environment changes no result."""

from __future__ import annotations

from tests.harness.environment import SERVER_VARIABLES, CLEARED_VARIABLES, hide_variables, clear_variables

# Pytest imports this module before it collects a test. Hiding the server variables keeps unit and integration
# tests off a live server, and the e2e suite reads them back from their hidden names.
clear_variables(CLEARED_VARIABLES)
hide_variables(SERVER_VARIABLES)
