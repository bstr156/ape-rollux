from ape import plugins
from ape.api import NetworkAPI, create_network_type
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_geth import GethProvider
from ape_test import LocalProvider

from .ecosystem import NETWORKS, Rollux, RolluxConfig


@plugins.register(plugins.Config)
def config_class():
    return RolluxConfig


@plugins.register(plugins.EcosystemPlugin)
def ecosystems():
    yield Rollux


@plugins.register(plugins.NetworkPlugin)
def networks():
    for network_name, network_params in NETWORKS.items():
        yield "rollux", network_name, create_network_type(*network_params)
        yield "rollux", f"{network_name}-fork", NetworkAPI

    # NOTE: This works for local providers, as they get chain_id from themselves
    yield "rollux", LOCAL_NETWORK_NAME, NetworkAPI


@plugins.register(plugins.ProviderPlugin)
def providers():
    for network_name in NETWORKS:
        yield "rollux", network_name, GethProvider

    yield "rollux", LOCAL_NETWORK_NAME, LocalProvider
