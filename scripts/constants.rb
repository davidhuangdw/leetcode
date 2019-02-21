require_relative 'yaml_erb_loader'

DEFAULTS_CONFIG_FILE_PATH = File.expand_path('../defaults.yml.erb', __FILE__)
DEFAULTS_CONFIG = YamlErbLoader.load_yml(DEFAULTS_CONFIG_FILE_PATH)

